"""TypeScript emitter: renders the `Api` IR (see `codegen/ir.py`) into a complete, typed,
async, zero-runtime-dependency ESM client for Node under `get-response-ts/`.

Two buckets, per `emit()`:
  - Always generated (spec-derived, wiped + rewritten every run): `src/models.ts`,
    `src/resources/*.ts` (per-tag resource classes), `src/resourceGroups.ts` (the glue
    that attaches one resource-group property per tag to `GetResponseClient` via TS
    declaration merging).
  - Scaffold-once (written only if missing via `_write_once`, then permanently
    hand-maintained): project/build config, `src/core.ts`/`errors.ts`/`ratelimit.ts`,
    `src/client.ts`, `src/index.ts`, `README.md`, and the `test/` suite. Safe to hand-edit
    once created -- regenerating never touches them again.

Regenerate via `python -m codegen.generate --typescript`. Never hand-edit the
always-generated bucket; fix this emitter and re-run instead. `emit()` finishes by running
`prettier --write` and `eslint --fix` over the output (skipped with a warning if
`node_modules` isn't installed yet -- run `npm install` once, then regenerate).
"""

from __future__ import annotations

import json
import shutil
import subprocess
from pathlib import Path

from codegen.ir import Api, EnumType, Field, Model, Operation, Param, TypeRef

# -- name helpers ---------------------------------------------------------------------

_WORD_RE = __import__("re").compile(r"[0-9a-zA-Z]+")

# Reserved words that can't be used as a bare identifier (function parameter / variable
# name) in JS/TS. Property and method names are unaffected -- reserved words are legal
# there -- so this only guards path-parameter identifiers.
_JS_RESERVED = {
    "break", "case", "catch", "class", "const", "continue", "debugger", "default",
    "delete", "do", "else", "enum", "export", "extends", "false", "finally", "for",
    "function", "if", "implements", "import", "in", "instanceof", "interface", "let",
    "new", "null", "package", "private", "protected", "public", "return", "static",
    "super", "switch", "this", "throw", "true", "try", "typeof", "var", "void", "while",
    "with", "yield", "await", "arguments", "eval",
}


def _safe_ts_ident(name: str) -> str:
    """Append a trailing underscore if `name` collides with a JS reserved word."""
    return f"{name}_" if name in _JS_RESERVED else name


def _tag_words(tag: str) -> list[str]:
    """Split a tag into word tokens, treating `/` as a non-boundary (`A/B` -> `AB`)."""
    return _WORD_RE.findall(tag.replace("/", ""))


def _tag_pascal(tag: str) -> str:
    """`'A/B tests - subject'` -> `'AbTestsSubject'`, `'SMS Messages'` -> `'SmsMessages'`."""
    return "".join(w[:1].upper() + w[1:].lower() for w in _tag_words(tag))


def _tag_camel(tag: str) -> str:
    """`'Campaigns (Lists)'` -> `'campaignsLists'` (used for the client property + filename)."""
    pascal = _tag_pascal(tag)
    return pascal[:1].lower() + pascal[1:] if pascal else pascal


def _lit(value: str) -> str:
    """Render `value` as a safe, JSON-compatible (and therefore valid JS/TS) string literal."""
    return json.dumps(value)


def _doc(text: str) -> str:
    """Render a one-line JSDoc comment, or `''` if there's no text."""
    text = (text or "").replace("*/", "*\\/").strip()
    return f"/** {text} */" if text else ""


def _dedupe_by_wire_name(params: list[Param]) -> list[Param]:
    """Drop duplicate params sharing a wire name (the spec occasionally repeats a path

    parameter both at the path-item level and the operation level).
    """
    seen: set[str] = set()
    out = []
    for p in params:
        if p.wire_name not in seen:
            seen.add(p.wire_name)
            out.append(p)
    return out


def _ts_type(t: TypeRef, prefix: str = "") -> str:
    """Map a `TypeRef` to its TypeScript type annotation.

    `prefix` is prepended to `model`/`enum` type names -- `''` when rendering `models.ts`
    itself (same-file references), `'M.'` when rendering a resource file that imports
    `models.ts` as `import type * as M from '../models.js'`.
    """
    if t.kind == "string":
        return "string"
    if t.kind in ("int", "number"):
        return "number"
    if t.kind == "bool":
        return "boolean"
    if t.kind == "datetime":
        return "string"
    if t.kind == "object":
        return "Record<string, unknown>"
    if t.kind == "any":
        return "unknown"
    if t.kind == "array":
        assert t.item is not None
        return f"{_ts_type(t.item, prefix)}[]"
    if t.kind in ("model", "enum"):
        assert t.model is not None
        return f"{prefix}{t.model}"
    raise ValueError(f"unhandled TypeRef kind: {t.kind!r}")


def _references_models(ops: list[Operation]) -> bool:
    """Whether any operation in `ops` needs a type from `models.ts` (decides the import)."""

    def refs(t: TypeRef | None) -> bool:
        if t is None:
            return False
        if t.kind == "array":
            return refs(t.item)
        return t.kind in ("model", "enum")

    for op in ops:
        if any(refs(p.type) for p in (*op.path_params, *op.query_params)):
            return True
        if refs(op.body_type) or refs(op.return_type):
            return True
    return False


# -- models.ts -------------------------------------------------------------------------


def _render_enum_ts(e: EnumType) -> str:
    doc = _doc(e.doc or f"{e.name} enum.")
    values = " | ".join(_lit(v) for v in e.values) if e.values else "never"
    return f"{doc}\nexport type {e.name} = {values};"


def _render_field_ts(f: Field) -> str:
    doc_text = f.doc
    if f.type.kind == "datetime":
        doc_text = f"{doc_text} (ISO 8601 date-time string)" if doc_text else "ISO 8601 date-time string."
    lines = []
    doc = _doc(doc_text)
    if doc:
        lines.append(f"  {doc}")
    opt = "" if f.required else "?"
    lines.append(f"  {_lit(f.wire_name)}{opt}: {_ts_type(f.type)};")
    return "\n".join(lines)


def _render_model_ts(m: Model) -> str:
    doc = _doc(m.doc or f"{m.name} model.")
    lines = [doc, f"export interface {m.name} {{"]
    lines.extend(_render_field_ts(f) for f in m.fields)
    lines.append("}")
    return "\n".join(lines)


def _render_models_ts(api: Api) -> str:
    enums_sorted = sorted(api.enums, key=lambda e: e.name)
    models_sorted = sorted(api.models, key=lambda m: m.name)

    parts = [
        "/**\n"
        " * Generated data models: every schema in the GetResponse OpenAPI spec.\n"
        " *\n"
        " * Enums are string-literal union types (simpler and tree-shakeable vs. a real\n"
        " * `enum`); models are plain interfaces keyed by the raw JSON wire name, so\n"
        " * (de)serialization is the identity function -- `response.json()` already\n"
        " * produces objects matching these shapes, and `JSON.stringify` on a value typed\n"
        " * as one of these interfaces produces valid wire JSON directly.\n"
        " *\n"
        " * This file is generated -- do not edit it directly.\n"
        " */\n",
    ]
    for e in enums_sorted:
        parts.append(_render_enum_ts(e))
        parts.append("")
    for m in models_sorted:
        parts.append(_render_model_ts(m))
        parts.append("")
    return "\n".join(parts).rstrip() + "\n"


# -- resources/*.ts ----------------------------------------------------------------


def _render_multipart_method_ts(op: Operation) -> str:
    return_ann = _ts_type(op.return_type, "M.") if op.return_type is not None else "void"
    method_name = _safe_ts_ident(op.cs_name[0].lower() + op.cs_name[1:]).removesuffix("Async")
    doc = _doc(f"{op.doc or op.summary or op.operation_id} Sends `file` as multipart/form-data.")
    return (
        f"  {doc}\n"
        f"  readonly {method_name} = async (\n"
        f"    file: Blob | ArrayBuffer | Uint8Array,\n"
        f'    filename = "upload",\n'
        f"    signal?: AbortSignal,\n"
        f"  ): Promise<{return_ann}> => {{\n"
        f"    const blob = file instanceof Blob ? file : new Blob([file as unknown as BlobPart]);\n"
        f"    const form = new FormData();\n"
        f'    form.append("file", blob, filename);\n'
        f"    return this.core.request<{return_ann}>({_lit(op.http_method)}, {_lit(op.path)}, {{\n"
        f"      body: form,\n"
        f"      signal,\n"
        f"    }});\n"
        f"  }};"
    )


def _ts_method_name(operation_id: str) -> str:
    """camelCase method name from an operationId (already camelCase in the spec)."""
    name = operation_id[0].lower() + operation_id[1:] if operation_id else operation_id
    return _safe_ts_ident(name)


def _render_method_ts(op: Operation) -> str:
    if op.is_multipart:
        return _render_multipart_method_ts(op)

    path_params = _dedupe_by_wire_name(op.path_params)
    query_params = _dedupe_by_wire_name(op.query_params)
    method_name = _ts_method_name(op.operation_id)
    return_ann = _ts_type(op.return_type, "M.") if op.return_type is not None else "void"
    doc = _doc(op.doc or op.summary or op.operation_id)

    sig_lines: list[str] = []
    for p in path_params:
        pname = _safe_ts_ident(p.cs_name)
        sig_lines.append(f"    {pname}: string,")
    if op.body_type is not None:
        sig_lines.append(f"    body: {_ts_type(op.body_type, 'M.')},")
    if query_params:
        sig_lines.append("    params?: {")
        for p in sorted(query_params, key=lambda p: (not p.required, p.wire_name)):
            doc_text = p.doc
            if p.type.kind == "datetime":
                note = (
                    "GetResponse date format: yyyy-MM-ddTHH:mm:ss+HHMM, e.g. "
                    "2024-01-15T10:30:00+0000 -- no colon in the offset, no sub-second "
                    "precision (unlike Date.prototype.toISOString())"
                )
                doc_text = f"{doc_text} ({note})" if doc_text else note[0].upper() + note[1:]
            field_doc = _doc(doc_text)
            if field_doc:
                sig_lines.append(f"      {field_doc}")
            opt = "" if p.required else "?"
            sig_lines.append(f"      {p.cs_name}{opt}: {_ts_type(p.type, 'M.')};")
        sig_lines.append("    },")
    sig_lines.append("    signal?: AbortSignal,")

    opt_lines: list[str] = []
    if path_params:
        entries = ", ".join(f"{_lit(p.wire_name)}: {_safe_ts_ident(p.cs_name)}" for p in path_params)
        opt_lines.append(f"      pathParams: {{ {entries} }},")
    if query_params:
        entries = ", ".join(f"{_lit(p.wire_name)}: params.{p.cs_name}" for p in query_params)
        opt_lines.append(f"      query: params ? {{ {entries} }} : undefined,")
    if op.body_type is not None:
        opt_lines.append("      body,")
    opt_lines.append("      signal,")

    lines = []
    if doc:
        lines.append(f"  {doc}")
    lines.append(f"  readonly {method_name} = async (")
    lines.extend(sig_lines)
    lines.append(f"  ): Promise<{return_ann}> => {{")
    lines.append(f"    return this.core.request<{return_ann}>({_lit(op.http_method)}, {_lit(op.path)}, {{")
    lines.extend(opt_lines)
    lines.append("    });")
    lines.append("  };")
    return "\n".join(lines)


def _render_resource_file(tag: str, ops: list[Operation]) -> str:
    class_name = f"{_tag_pascal(tag)}Resource"
    doc = f"Operations tagged {tag!r} in the GetResponse API."

    parts = [
        f"/** {doc} */",
        "",
        "import type { Core } from '../core.js';",
    ]
    if _references_models(ops):
        parts.append("import type * as M from '../models.js';")
    parts.append("")
    parts.append(f"export class {class_name} {{")
    parts.append("  constructor(private readonly core: Core) {}")
    for op in sorted(ops, key=lambda o: o.operation_id):
        parts.append("")
        parts.append(_render_method_ts(op))
    parts.append("}")
    return "\n".join(parts) + "\n"


def _render_resources_index(tags: list[str]) -> str:
    lines = ["/** Barrel export: one resource class per API tag. */", ""]
    for tag in tags:
        lines.append(f"export {{ {_tag_pascal(tag)}Resource }} from './{_tag_camel(tag)}.js';")
    return "\n".join(lines) + "\n"


# -- resourceGroups.ts (always generated) / client.ts (scaffold-once) -------------------


def _render_resource_groups_ts(tags: list[str]) -> str:
    """Render `src/resourceGroups.ts`: one readonly property + one constructor call per tag.

    `GetResponseClient` (scaffold-once, hand-maintained) picks this up via TS declaration
    merging (`export interface GetResponseClient extends GeneratedResourceGroups {}`) plus
    `Object.assign(this, createResourceGroups(this.core))` in its constructor, so a new tag
    shows up on the client without ever touching the hand-written file.
    """
    lines = [
        "/** Resource-group properties attached to GetResponseClient. Generated from the spec's tags. */",
        "",
        "import type { Core } from './core.js';",
        "import {",
    ]
    for tag in tags:
        lines.append(f"  {_tag_pascal(tag)}Resource,")
    lines.append("} from './resources/index.js';")
    lines.append("")
    lines.append("/** One readonly resource-group property per API tag. */")
    lines.append("export interface GeneratedResourceGroups {")
    for tag in tags:
        lines.append(f"  readonly {_tag_camel(tag)}: {_tag_pascal(tag)}Resource;")
    lines.append("}")
    lines.append("")
    lines.append("/** Constructs one resource-group instance per tag, keyed by property name. */")
    lines.append("export function createResourceGroups(core: Core): GeneratedResourceGroups {")
    lines.append("  return {")
    for tag in tags:
        lines.append(f"    {_tag_camel(tag)}: new {_tag_pascal(tag)}Resource(core),")
    lines.append("  };")
    lines.append("}")
    return "\n".join(lines) + "\n"


_CLIENT_TS = """/** Root client: auth, resource-group properties (via declaration merging), and pagination. */

import { Core, DEFAULT_BASE_URL, type FetchFn } from './core.js';
import type { RateLimitOptions } from './ratelimit.js';
import { createResourceGroups, type GeneratedResourceGroups } from './resourceGroups.js';

/** Constructor options for {@link GetResponseClient}. */
export interface GetResponseClientOptions {
  /** API key: sent as `X-Auth-Token: api-key <apiKey>`. Mutually exclusive with `accessToken`. */
  apiKey?: string;
  /** OAuth2 bearer token: sent as `Authorization: Bearer <accessToken>`. */
  accessToken?: string;
  /** API base URL. Defaults to the standard GetResponse endpoint (see also the MAX US/PL constants in `core.ts`). */
  baseUrl?: string;
  /** Per-request timeout in milliseconds. Defaults to 30000. */
  timeoutMs?: number;
  /** Inject a custom `fetch` implementation (used by the test suite). Defaults to the global `fetch`. */
  fetch?: FetchFn;
  /** Opt-in client-side rate limiting; disabled unless provided. */
  rateLimit?: RateLimitOptions;
}

// Declaration merging: `GeneratedResourceGroups` (regenerated from the spec's tags) supplies
// one readonly resource-group property per tag; the runtime assignment happens in the
// constructor below via `Object.assign`. Safe despite eslint's static check -- the merged
// interface only ever adds readonly properties that `Object.assign` populates at construction.
// eslint-disable-next-line @typescript-eslint/no-unsafe-declaration-merging, @typescript-eslint/no-empty-object-type
export interface GetResponseClient extends GeneratedResourceGroups {}

/** Async, fully-typed GetResponse v3 API client; one property per resource-group tag. */
// eslint-disable-next-line @typescript-eslint/no-unsafe-declaration-merging
export class GetResponseClient {
  private readonly core: Core;

  constructor(options: GetResponseClientOptions = {}) {
    const { apiKey, accessToken, baseUrl = DEFAULT_BASE_URL, timeoutMs = 30_000, fetch: fetchImpl, rateLimit } = options;
    if ((apiKey === undefined) === (accessToken === undefined)) {
      throw new Error('Provide exactly one of `apiKey` or `accessToken`.');
    }
    const authHeader: Record<string, string> = apiKey !== undefined
      ? { 'X-Auth-Token': `api-key ${apiKey}` }
      : { Authorization: `Bearer ${accessToken}` };
    this.core = new Core({ baseUrl, authHeader, timeoutMs, fetch: fetchImpl, rateLimit });
    Object.assign(this, createResourceGroups(this.core));
  }

  /**
   * Walk every page of a `list`/`get*List` resource method, yielding items one by one.
   *
   * GetResponse also reports `TotalCount`/`CurrentPage`/`TotalPages` response headers, but
   * resource methods only return typed bodies (no header access), so this walks by page
   * length instead: it stops once a page comes back empty or shorter than `perPage`.
   */
  async *paginate<T>(
    listMethod: (
      params: Record<string, unknown> & { page?: number; perPage?: number },
      signal?: AbortSignal,
    ) => Promise<T[]>,
    options: { perPage?: number; params?: Record<string, unknown>; signal?: AbortSignal } = {},
  ): AsyncGenerator<T, void, void> {
    const perPage = options.perPage ?? 100;
    let page = 1;
    for (;;) {
      const items = await listMethod({ ...options.params, page, perPage }, options.signal);
      if (items.length === 0) return;
      yield* items;
      if (items.length < perPage) return;
      page += 1;
    }
  }
}
"""


_INDEX_TS = """/** Async, fully-typed GetResponse v3 API client. */

export { GetResponseClient } from './client.js';
export type { GetResponseClientOptions } from './client.js';
export { GetResponseApiError, RateLimitError } from './errors.js';
export type { RateLimitOptions } from './ratelimit.js';
export * as models from './models.js';
"""


# -- core.ts / errors.ts / ratelimit.ts (hand-written once, not per-IR) ------------------

_CORE_TS = """/** HTTP transport: request building, auth-agnostic call plumbing, and error mapping. */

import { GetResponseApiError } from './errors.js';
import { RateLimiter, type RateLimitOptions } from './ratelimit.js';

export const DEFAULT_BASE_URL = 'https://api.getresponse.com/v3';
export const MAX_US_BASE_URL = 'https://api3.getresponse360.com/v3';
export const MAX_PL_BASE_URL = 'https://api3.getresponse360.pl/v3';

export type FetchFn = typeof fetch;

export interface CoreOptions {
  baseUrl: string;
  authHeader: Record<string, string>;
  timeoutMs: number;
  fetch?: FetchFn;
  rateLimit?: RateLimitOptions;
}

export interface RequestOptions {
  pathParams?: Record<string, string>;
  // Almost always string/number/boolean; a handful of spec params (e.g. the `query[x][from]`
  // date-range filters) are typed as free-form objects, so this stays `unknown` and
  // `buildUrl` below falls back to JSON-encoding anything that isn't already a primitive.
  query?: Record<string, unknown>;
  body?: unknown;
  signal?: AbortSignal;
}

function buildUrl(
  baseUrl: string,
  path: string,
  pathParams?: Record<string, string>,
  query?: Record<string, unknown>,
): string {
  let resolvedPath = path;
  for (const [key, value] of Object.entries(pathParams ?? {})) {
    resolvedPath = resolvedPath.replace(`{${key}}`, encodeURIComponent(value));
  }
  const url = new URL(resolvedPath, `${baseUrl.replace(/\\/$/, '')}/`);
  for (const [key, value] of Object.entries(query ?? {})) {
    if (value === undefined || value === null) continue;
    const stringValue = typeof value === 'object' ? JSON.stringify(value) : String(value);
    url.searchParams.set(key, stringValue);
  }
  return url.toString();
}

async function parseBody<T>(response: Response): Promise<T> {
  if (response.status === 204) return undefined as T;
  const text = await response.text();
  if (!text) return undefined as T;
  return JSON.parse(text) as T;
}

/** Thin wrapper around `fetch`: one call site for every generated resource method. */
export class Core {
  private readonly baseUrl: string;
  private readonly authHeader: Record<string, string>;
  private readonly timeoutMs: number;
  private readonly fetchImpl: FetchFn;
  private readonly rateLimiter?: RateLimiter;

  constructor(options: CoreOptions) {
    this.baseUrl = options.baseUrl;
    this.authHeader = options.authHeader;
    this.timeoutMs = options.timeoutMs;
    this.fetchImpl = options.fetch ?? fetch;
    this.rateLimiter = options.rateLimit ? new RateLimiter(options.rateLimit) : undefined;
  }

  /** Send one API call and decode the JSON response into `T` (or `undefined` for a void return). */
  async request<T>(method: string, path: string, options: RequestOptions = {}): Promise<T> {
    let attempt = 0;
    for (;;) {
      if (this.rateLimiter) await this.rateLimiter.acquire();
      let response: Response;
      try {
        response = await this.send(method, path, options);
      } finally {
        if (this.rateLimiter) this.rateLimiter.release();
      }
      if (this.rateLimiter) this.rateLimiter.observe(response);

      if (response.status === 429 && this.rateLimiter) {
        await this.rateLimiter.handle429(response, attempt);
        attempt += 1;
        continue;
      }
      if (!response.ok) {
        throw await GetResponseApiError.fromResponse(response);
      }
      return parseBody<T>(response);
    }
  }

  private async send(method: string, path: string, options: RequestOptions): Promise<Response> {
    const url = buildUrl(this.baseUrl, path, options.pathParams, options.query);
    const headers: Record<string, string> = { ...this.authHeader, Accept: 'application/json' };
    let body: BodyInit | undefined;
    if (options.body instanceof FormData) {
      body = options.body;
    } else if (options.body !== undefined) {
      headers['Content-Type'] = 'application/json';
      body = JSON.stringify(options.body);
    }

    const controller = new AbortController();
    const timeout = setTimeout(() => controller.abort(), this.timeoutMs);
    const onAbort = () => controller.abort();
    options.signal?.addEventListener('abort', onAbort, { once: true });
    try {
      return await this.fetchImpl(url, { method, headers, body, signal: controller.signal });
    } finally {
      clearTimeout(timeout);
      options.signal?.removeEventListener('abort', onAbort);
    }
  }
}
"""

_ERRORS_TS = """/** Typed errors: every non-2xx response maps to one of these. */

import type { ErrorResponse } from './models.js';

/** Extra fields accepted by the {@link GetResponseApiError} constructor. */
export interface GetResponseApiErrorOptions {
  code?: number;
  codeDescription?: string;
  message?: string;
  moreInfo?: string;
  context?: Record<string, unknown>;
  uuid?: string;
}

/** Raised for any non-2xx response; carries the parsed `ErrorResponse` fields. */
export class GetResponseApiError extends Error {
  readonly statusCode: number;
  readonly code?: number;
  readonly codeDescription?: string;
  readonly moreInfo?: string;
  readonly context?: Record<string, unknown>;
  readonly uuid?: string;

  constructor(statusCode: number, options: GetResponseApiErrorOptions = {}) {
    super(options.message ?? options.codeDescription ?? `GetResponse API error ${statusCode}`);
    this.name = 'GetResponseApiError';
    this.statusCode = statusCode;
    this.code = options.code;
    this.codeDescription = options.codeDescription;
    this.moreInfo = options.moreInfo;
    this.context = options.context;
    this.uuid = options.uuid;
    Object.setPrototypeOf(this, new.target.prototype);
  }

  /** Build from an HTTP error response, tolerating a body that isn't an `ErrorResponse`. */
  static async fromResponse(response: Response): Promise<GetResponseApiError> {
    try {
      const body = (await response.json()) as Partial<ErrorResponse>;
      return new GetResponseApiError(response.status, {
        code: body.code,
        codeDescription: body.codeDescription,
        message: body.message,
        moreInfo: body.moreInfo,
        context: body.context,
        uuid: body.uuid,
      });
    } catch {
      return new GetResponseApiError(response.status);
    }
  }
}

/** Extra fields accepted by the {@link RateLimitError} constructor. */
export interface RateLimitErrorOptions extends GetResponseApiErrorOptions {
  resetSeconds?: number;
  limit?: number;
  remaining?: number;
}

/** Raised by the opt-in rate limiter when a wait would exceed `maxWaitSeconds` or retries are exhausted. */
export class RateLimitError extends GetResponseApiError {
  readonly resetSeconds?: number;
  readonly limit?: number;
  readonly remaining?: number;

  constructor(statusCode: number, options: RateLimitErrorOptions = {}) {
    super(statusCode, {
      ...options,
      message: options.message ?? 'Rate limit exceeded and the wait/retry budget is exhausted.',
    });
    this.name = 'RateLimitError';
    this.resetSeconds = options.resetSeconds;
    this.limit = options.limit;
    this.remaining = options.remaining;
    Object.setPrototypeOf(this, new.target.prototype);
  }
}
"""

_RATELIMIT_TS = """/**
 * Opt-in client-side rate limiting, shared in behavior with the Python/C# clients.
 *
 * Disabled unless {@link RateLimitOptions} is passed to `GetResponseClient`. Three layers:
 *  - proactive: before each attempt, acquire a concurrency slot plus a per-second and a
 *    per-window token; if the wait needed would exceed `maxWaitSeconds`, throw before ever
 *    sending the request.
 *  - reactive: on a 429, read `X-RateLimit-Reset` (falling back to the `ErrorResponse`
 *    body's `context.timeToReset`); retry after sleeping if a retry budget remains and the
 *    reset is within `maxWaitSeconds`, otherwise throw.
 *  - adaptive: read `X-RateLimit-Remaining`/`X-RateLimit-Limit` on every response; once
 *    remaining hits 0, block subsequent acquires until the reported reset.
 */

import { RateLimitError } from './errors.js';

/** Options for `GetResponseClient({ rateLimit })`. Omitting the whole object disables the limiter. */
export interface RateLimitOptions {
  /** Master on/off switch (default true once this options object is provided). */
  enabled?: boolean;
  /** Max in-flight requests. Default 10. */
  maxConcurrency?: number;
  /** Requests allowed per rolling second. Default 80. */
  requestsPerSecond?: number;
  /** Requests allowed per rolling window. Default 30000. */
  requestsPerWindow?: number;
  /** Length of the rolling window, in seconds. Default 600. */
  windowSeconds?: number;
  /** Multiplier applied to `requestsPerSecond`/`requestsPerWindow` (concurrency is not scaled). Default 1.0. */
  safetyMargin?: number;
  /** Max reactive retries on 429 before giving up. Default 5. */
  maxRetries?: number;
  /** Max seconds this limiter will ever wait/sleep before throwing {@link RateLimitError}. Default 60. */
  maxWaitSeconds?: number;
  /** Injectable delay function, for deterministic tests. Defaults to a `setTimeout`-based sleep. */
  sleep?: (ms: number) => Promise<void>;
}

const defaultSleep = (ms: number): Promise<void> => new Promise((resolve) => setTimeout(resolve, ms));

/** A tiny FIFO counting semaphore bounding concurrent requests. */
class Semaphore {
  private active = 0;
  private readonly queue: Array<() => void> = [];

  constructor(private readonly max: number) {}

  async acquire(): Promise<void> {
    if (this.active < this.max) {
      this.active += 1;
      return;
    }
    await new Promise<void>((resolve) => this.queue.push(resolve));
    this.active += 1;
  }

  release(): void {
    this.active -= 1;
    const next = this.queue.shift();
    if (next) next();
  }
}

/** A sliding-window token bucket: `limit` grants per `windowMs`. */
class TokenBucket {
  private timestamps: number[] = [];

  constructor(
    private readonly limit: number,
    private readonly windowMs: number,
  ) {}

  /** Milliseconds to wait right now before a token would be available (0 if one already is). */
  waitMs(now: number): number {
    this.prune(now);
    if (this.timestamps.length < this.limit) return 0;
    return Math.max(0, this.timestamps[0] + this.windowMs - now);
  }

  consume(now: number): void {
    this.prune(now);
    this.timestamps.push(now);
  }

  private prune(now: number): void {
    while (this.timestamps.length > 0 && this.timestamps[0] <= now - this.windowMs) {
      this.timestamps.shift();
    }
  }
}

function parseResetSeconds(header: string | null): number | undefined {
  if (!header) return undefined;
  const match = /^\\s*(\\d+)/.exec(header);
  return match ? Number(match[1]) : undefined;
}

/** Proactive + reactive + adaptive rate limiting for one `GetResponseClient` instance. */
export class RateLimiter {
  private readonly enabled: boolean;
  private readonly maxWaitMs: number;
  private readonly maxRetries: number;
  private readonly sleepFn: (ms: number) => Promise<void>;
  private readonly concurrency: Semaphore;
  private readonly perSecond: TokenBucket;
  private readonly perWindow: TokenBucket;
  private blockedUntil = 0;

  constructor(options: RateLimitOptions) {
    this.enabled = options.enabled ?? true;
    const margin = options.safetyMargin ?? 1.0;
    const rps = Math.max(1, Math.floor((options.requestsPerSecond ?? 80) * margin));
    const rpw = Math.max(1, Math.floor((options.requestsPerWindow ?? 30_000) * margin));
    const windowSeconds = options.windowSeconds ?? 600;
    this.maxWaitMs = (options.maxWaitSeconds ?? 60) * 1000;
    this.maxRetries = options.maxRetries ?? 5;
    this.sleepFn = options.sleep ?? defaultSleep;
    this.concurrency = new Semaphore(options.maxConcurrency ?? 10);
    this.perSecond = new TokenBucket(rps, 1000);
    this.perWindow = new TokenBucket(rpw, windowSeconds * 1000);
  }

  /** Acquire a concurrency slot and a rate-limit token before sending a request. */
  async acquire(): Promise<void> {
    if (!this.enabled) return;
    await this.concurrency.acquire();
    const now = Date.now();
    const wait = Math.max(Math.max(0, this.blockedUntil - now), this.perSecond.waitMs(now), this.perWindow.waitMs(now));
    if (wait > this.maxWaitMs) {
      this.concurrency.release();
      throw new RateLimitError(429, {
        resetSeconds: wait / 1000,
        message: 'Proactive rate-limit wait would exceed maxWaitSeconds.',
      });
    }
    if (wait > 0) await this.sleepFn(wait);
    const consumedAt = Date.now();
    this.perSecond.consume(consumedAt);
    this.perWindow.consume(consumedAt);
  }

  /** Release the concurrency slot acquired by {@link acquire}. */
  release(): void {
    if (!this.enabled) return;
    this.concurrency.release();
  }

  /** Adaptive layer: track `X-RateLimit-Remaining`/`-Reset` so the next `acquire` can block. */
  observe(response: Response): void {
    if (!this.enabled) return;
    const remaining = response.headers.get('X-RateLimit-Remaining');
    if (remaining !== null && Number(remaining) <= 0) {
      const resetSeconds = parseResetSeconds(response.headers.get('X-RateLimit-Reset')) ?? 1;
      this.blockedUntil = Date.now() + resetSeconds * 1000;
    }
  }

  /** Reactive layer: sleep and return to retry a 429, or throw {@link RateLimitError} to give up. */
  async handle429(response: Response, attempt: number): Promise<void> {
    const limitHeader = response.headers.get('X-RateLimit-Limit');
    const remainingHeader = response.headers.get('X-RateLimit-Remaining');
    const limit = limitHeader ? Number(limitHeader) : undefined;
    const remaining = remainingHeader ? Number(remainingHeader) : undefined;

    let resetSeconds = parseResetSeconds(response.headers.get('X-RateLimit-Reset'));
    if (resetSeconds === undefined) {
      resetSeconds = await this.contextResetSeconds(response);
    }

    const canRetry =
      resetSeconds !== undefined && attempt < this.maxRetries && resetSeconds * 1000 <= this.maxWaitMs;
    if (!canRetry) {
      throw new RateLimitError(429, { resetSeconds, limit, remaining });
    }
    await this.sleepFn(resetSeconds! * 1000);
  }

  private async contextResetSeconds(response: Response): Promise<number | undefined> {
    try {
      const body = (await response.json()) as { context?: { timeToReset?: number } };
      return body?.context?.timeToReset;
    } catch {
      return undefined;
    }
  }
}
"""


# -- package.json / tsconfig / lint+format config / README ------------------------------

_PACKAGE_JSON = """{
  "name": "@sistemitre/getresponse",
  "version": "0.1.0",
  "description": "Async, fully-typed Node.js client for the GetResponse v3 API.",
  "license": "MIT",
  "author": "Sistemi Tre",
  "repository": { "type": "git", "url": "git+https://github.com/sistemitre/get-response.git" },
  "homepage": "https://github.com/sistemitre/get-response",
  "bugs": "https://github.com/sistemitre/get-response/issues",
  "type": "module",
  "engines": { "node": ">=18" },
  "main": "dist/index.js",
  "module": "dist/index.js",
  "types": "dist/index.d.ts",
  "exports": {
    ".": {
      "types": "./dist/index.d.ts",
      "import": "./dist/index.js"
    }
  },
  "files": ["dist"],
  "scripts": {
    "build": "tsc",
    "lint": "eslint src",
    "format": "prettier --write src",
    "test": "vitest run"
  },
  "devDependencies": {
    "@eslint/js": "^9.9.0",
    "@types/node": "^22.0.0",
    "eslint": "^9.9.0",
    "eslint-config-prettier": "^9.1.0",
    "prettier": "^3.3.0",
    "typescript": "^5.5.0",
    "typescript-eslint": "^8.0.0",
    "vitest": "^2.0.0"
  }
}
"""

_TSCONFIG_JSON = """{
  "compilerOptions": {
    "target": "ES2022",
    "lib": ["ES2022", "DOM"],
    "module": "NodeNext",
    "moduleResolution": "NodeNext",
    "strict": true,
    "declaration": true,
    "outDir": "dist",
    "rootDir": "src",
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true
  },
  "include": ["src/**/*.ts"],
  "exclude": ["**/*.test.ts", "dist", "node_modules"]
}
"""

_ESLINT_CONFIG = """import js from '@eslint/js';
import tseslint from 'typescript-eslint';
import prettier from 'eslint-config-prettier';

export default tseslint.config(
  { ignores: ['dist/**', 'node_modules/**', 'coverage/**'] },
  js.configs.recommended,
  ...tseslint.configs.recommended,
  {
    rules: {
      '@typescript-eslint/no-unused-vars': ['warn', { argsIgnorePattern: '^_' }],
      '@typescript-eslint/no-non-null-assertion': 'off',
    },
  },
  prettier,
);
"""

_PRETTIERRC = """{
  "singleQuote": true,
  "semi": true,
  "tabWidth": 2,
  "printWidth": 100,
  "trailingComma": "all"
}
"""

_PRETTIERIGNORE = "dist\nnode_modules\ncoverage\n"

_README_MD = """# @sistemitre/getresponse

An async, fully-typed Node.js client for the [GetResponse v3 API](https://apireference.getresponse.com/),
generated from the official OpenAPI spec. ESM only, zero runtime dependencies -- built on
the global `fetch`.

## Install

```bash
npm install @sistemitre/getresponse
```

## Quickstart

```ts
import { GetResponseClient } from '@sistemitre/getresponse';

const client = new GetResponseClient({ apiKey: 'YOUR_API_KEY' });

const contacts = await client.contacts.getContactList({ queryEmail: 'jane@example.com' });
for (const contact of contacts) {
  console.log(contact.contactId, contact.email);
}
```

Pass `accessToken` instead of `apiKey` to authenticate with an OAuth2 bearer token.

A real API key (or access token) is required for live use; the test suite injects a fake
`fetch` and needs neither.

## Pagination

`list`/`get*List` resource methods return one page at a time. `GetResponseClient.paginate`
walks every page for you:

```ts
for await (const contact of client.paginate(client.contacts.getContactList, { perPage: 100 })) {
  console.log(contact.email);
}
```

It stops once a page comes back empty or shorter than `perPage` -- simpler and more
transport-agnostic than reading the `TotalPages`/`CurrentPage` response headers.

## Rate limiting

Client-side rate limiting is opt-in and disabled by default:

```ts
const client = new GetResponseClient({
  apiKey: 'YOUR_API_KEY',
  rateLimit: {
    maxConcurrency: 10,
    requestsPerSecond: 80,
    requestsPerWindow: 30_000,
    windowSeconds: 600,
    maxRetries: 5,
    maxWaitSeconds: 60,
  },
});
```

When enabled it combines three layers: **proactive** concurrency + token-bucket throttling
before a request is sent, **reactive** retry-after-sleep on HTTP 429 (honoring
`X-RateLimit-Reset`), and **adaptive** blocking once `X-RateLimit-Remaining` hits 0. Any wait
that would exceed `maxWaitSeconds` throws `RateLimitError` instead of blocking indefinitely.

## Models

Every model is a plain `interface` keyed by the raw JSON wire name (e.g. `contactId`, not
`contact_id`), so (de)serialization is the identity function. Enums are string-literal union
types (`'ASC' | 'DESC'`), not runtime `enum`s. All `date-time` fields are typed `string` --
GetResponse uses ISO 8601.

"""

_GITIGNORE = "node_modules/\ndist/\ncoverage/\n*.tsbuildinfo\nnpm-debug.log*\n"

_VITEST_CONFIG = """import { defineConfig } from 'vitest/config';

export default defineConfig({
  test: {
    include: ['test/**/*.test.ts'],
  },
});
"""

# -- tests --------------------------------------------------------------------------

_TEST_HELPERS = """/** Shared test helper: build a `GetResponseClient` over an injected fetch implementation. */

import { GetResponseClient, type GetResponseClientOptions } from '../src/index.js';

export function makeClient(
  fetchImpl: typeof fetch,
  options: Partial<GetResponseClientOptions> = {},
): GetResponseClient {
  return new GetResponseClient({ apiKey: 'test-key', fetch: fetchImpl, ...options });
}

export function jsonResponse(body: unknown, init: ResponseInit = {}): Response {
  return new Response(JSON.stringify(body), {
    status: 200,
    headers: { 'Content-Type': 'application/json' },
    ...init,
  });
}
"""

_TEST_AUTH = """/** Auth header selection: `X-Auth-Token` for API keys, `Bearer` for OAuth2 tokens. */

import { describe, expect, it } from 'vitest';
import { GetResponseClient } from '../src/index.js';
import { jsonResponse } from './helpers.js';

describe('auth', () => {
  it('sends X-Auth-Token for an apiKey', async () => {
    let captured: Headers | undefined;
    const client = new GetResponseClient({
      apiKey: 'my-key',
      fetch: async (_url, init) => {
        captured = new Headers(init?.headers);
        return jsonResponse([]);
      },
    });

    await client.contacts.getContactList();

    expect(captured?.get('X-Auth-Token')).toBe('api-key my-key');
  });

  it('sends Bearer for an accessToken', async () => {
    let captured: Headers | undefined;
    const client = new GetResponseClient({
      accessToken: 'my-token',
      fetch: async (_url, init) => {
        captured = new Headers(init?.headers);
        return jsonResponse([]);
      },
    });

    await client.contacts.getContactList();

    expect(captured?.get('Authorization')).toBe('Bearer my-token');
  });

  it('requires exactly one credential', () => {
    expect(() => new GetResponseClient()).toThrow();
    expect(() => new GetResponseClient({ apiKey: 'a', accessToken: 'b' })).toThrow();
  });
});
"""

_TEST_QUERY_BUILDING = """/** Bracket-notation query parameter building. */

import { describe, expect, it } from 'vitest';
import { jsonResponse } from './helpers.js';
import { makeClient } from './helpers.js';

describe('query building', () => {
  it('uses bracket notation and skips undefined params', async () => {
    let capturedUrl: URL | undefined;
    const client = makeClient(async (url) => {
      capturedUrl = new URL(url instanceof Request ? url.url : url.toString());
      return jsonResponse([]);
    });

    await client.contacts.getContactList({
      queryEmail: 'a@b.com',
      sortName: 'ASC',
      page: 2,
      perPage: 50,
    });

    const params = capturedUrl!.searchParams;
    expect(params.get('query[email]')).toBe('a@b.com');
    expect(params.get('sort[name]')).toBe('ASC');
    expect(params.get('page')).toBe('2');
    expect(params.get('perPage')).toBe('50');
    expect(params.has('query[name]')).toBe(false);
  });
});
"""

_TEST_MODELS = """/**
 * Model (de)serialization: a realistic Contact payload parses as-is (identity); a NewContact
 * value serializes to wire JSON with no undefined keys, keyed by the raw camelCase wire names.
 */

import { describe, expect, it } from 'vitest';
import type { Contact, NewContact } from '../src/models.js';

describe('models', () => {
  it('a Contact payload parses with wire-name keys intact', () => {
    const payload: Contact = {
      contactId: 'abc123',
      name: 'Jane Doe',
      origin: 'api',
      createdOn: '2024-01-01T00:00:00+00:00',
      campaign: { campaignId: 'c1', name: 'My Campaign' },
      email: 'jane@example.com',
      href: 'https://api.getresponse.com/v3/contacts/abc123',
    };

    const contact: Contact = JSON.parse(JSON.stringify(payload));

    expect(contact.contactId).toBe('abc123');
    expect(contact.email).toBe('jane@example.com');
    expect(contact.origin).toBe('api');
    expect(contact.campaign?.campaignId).toBe('c1');
  });

  it('a NewContact value serializes to camelCase wire JSON with no undefined keys', () => {
    const newContact: NewContact = {
      contactId: '',
      href: '',
      email: 'jane@example.com',
      campaign: { campaignId: 'c1' },
      name: 'Jane Doe',
    };

    const dumped = JSON.parse(JSON.stringify(newContact));

    expect(dumped.email).toBe('jane@example.com');
    expect(dumped.campaign.campaignId).toBe('c1');
    expect(dumped.contactId).toBe('');
    expect('contact_id' in dumped).toBe(false);
    expect(Object.values(dumped).every((v) => v !== undefined)).toBe(true);
  });
});
"""

_TEST_PAGINATION = """/** `GetResponseClient.paginate` walks full pages and stops on a short/empty one. */

import { describe, expect, it } from 'vitest';
import { jsonResponse } from './helpers.js';
import { makeClient } from './helpers.js';

function contact(i: number) {
  return { contactId: `id${i}`, email: `${i}@example.com`, href: 'h' };
}

describe('pagination', () => {
  it('walks full pages then stops on a short page', async () => {
    const pages = [
      Array.from({ length: 50 }, (_, i) => contact(i)),
      Array.from({ length: 50 }, (_, i) => contact(i + 50)),
      [contact(100)],
    ];
    let calls = 0;

    const client = makeClient(async (url) => {
      const page = Number(new URL(url instanceof Request ? url.url : url.toString()).searchParams.get('page'));
      calls += 1;
      return jsonResponse(pages[page - 1]);
    });

    const seen = [];
    for await (const item of client.paginate(client.contacts.getContactList, { perPage: 50 })) {
      seen.push(item);
    }

    expect(seen).toHaveLength(101);
    expect(calls).toBe(3);
  });
});
"""

_TEST_ERRORS = """/** Non-2xx responses raise `GetResponseApiError` with `ErrorResponse` fields populated. */

import { describe, expect, it } from 'vitest';
import { GetResponseApiError } from '../src/index.js';
import { jsonResponse } from './helpers.js';
import { makeClient } from './helpers.js';

describe('errors', () => {
  it('maps a 400 ErrorResponse body to a typed exception', async () => {
    const body = {
      httpStatus: 400,
      code: 1010,
      codeDescription: 'Invalid value',
      message: 'Email is invalid',
      moreInfo: 'https://apidocs.getresponse.com/errors/1010',
      context: { field: 'email' },
      uuid: 'abc-123',
    };
    const client = makeClient(async () => jsonResponse(body, { status: 400 }));

    await expect(client.contacts.getContactList()).rejects.toMatchObject({
      statusCode: 400,
      code: 1010,
      message: 'Email is invalid',
      context: { field: 'email' },
      uuid: 'abc-123',
    });
    await expect(client.contacts.getContactList()).rejects.toBeInstanceOf(GetResponseApiError);
  });
});
"""

_TEST_RATELIMIT = """/** Rate limiter: disabled-by-default passthrough, reactive retry, cap, and concurrency. */

import { describe, expect, it, vi } from 'vitest';
import { RateLimitError } from '../src/index.js';
import { jsonResponse } from './helpers.js';
import { makeClient } from './helpers.js';

describe('rate limiter', () => {
  it('is a no-op when rateLimit is not provided', async () => {
    let calls = 0;
    const client = makeClient(async () => {
      calls += 1;
      return jsonResponse([]);
    });

    await client.contacts.getContactList();

    expect(calls).toBe(1);
  });

  it('retries a 429 after sleeping for X-RateLimit-Reset, using an injected sleep', async () => {
    const sleep = vi.fn(async (_ms: number) => {});
    let calls = 0;
    const client = makeClient(
      async () => {
        calls += 1;
        if (calls === 1) {
          return new Response(null, {
            status: 429,
            headers: { 'X-RateLimit-Reset': '1 seconds' },
          });
        }
        return jsonResponse([]);
      },
      { rateLimit: { sleep, maxWaitSeconds: 60 } },
    );

    const result = await client.contacts.getContactList();

    expect(result).toEqual([]);
    expect(calls).toBe(2);
    expect(sleep).toHaveBeenCalledWith(1000);
  });

  it('throws RateLimitError without a long sleep when the reset exceeds maxWaitSeconds', async () => {
    const sleep = vi.fn(async (_ms: number) => {});
    const client = makeClient(
      async () =>
        new Response(null, {
          status: 429,
          headers: { 'X-RateLimit-Reset': '9999 seconds' },
        }),
      { rateLimit: { sleep, maxWaitSeconds: 60 } },
    );

    await expect(client.contacts.getContactList()).rejects.toBeInstanceOf(RateLimitError);
    expect(sleep).not.toHaveBeenCalled();
  });

  it('never exceeds maxConcurrency in-flight requests', async () => {
    let active = 0;
    let maxActive = 0;
    const client = makeClient(
      async () => {
        active += 1;
        maxActive = Math.max(maxActive, active);
        await new Promise((resolve) => setTimeout(resolve, 5));
        active -= 1;
        return jsonResponse([]);
      },
      { rateLimit: { maxConcurrency: 3, requestsPerSecond: 1000, requestsPerWindow: 1_000_000 } },
    );

    await Promise.all(Array.from({ length: 10 }, () => client.contacts.getContactList()));

    expect(maxActive).toBeLessThanOrEqual(3);
  });
});
"""


# -- orchestration --------------------------------------------------------------------


def _write_once(path: Path, content: str) -> None:
    """Write `content` to `path` only if it doesn't already exist.

    Used for every scaffold-bucket file (project/build config, the hand-written core
    runtime, `client.ts`, `index.ts`, tests): written once on first generate, then left
    alone forever so it can be hand-maintained without a later regenerate clobbering it.
    """
    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8", newline="\n")


def _run_formatters(root: Path) -> None:
    """Run prettier --write + eslint --fix over `root/src`, if the toolchain is installed."""
    bin_dir = root / "node_modules" / ".bin"
    is_windows = shutil.os.name == "nt"
    prettier = bin_dir / ("prettier.cmd" if is_windows else "prettier")
    eslint = bin_dir / ("eslint.cmd" if is_windows else "eslint")
    if not prettier.exists():
        print(
            f"note: {bin_dir} has no prettier/eslint yet -- run `npm install` in {root}, "
            "then regenerate to auto-format."
        )
        return
    # Paths passed to the subprocess are relative to `cwd=root`, and `.cmd` shims need a
    # shell on Windows to resolve/execute correctly.
    prettier_rel = str(Path("node_modules") / ".bin" / prettier.name)
    eslint_rel = str(Path("node_modules") / ".bin" / eslint.name)
    subprocess.run([prettier_rel, "--write", "src"], cwd=root, check=True, shell=is_windows)
    subprocess.run([eslint_rel, "--fix", "src"], cwd=root, check=True, shell=is_windows)


def emit(api: Api, out_dir: str = "get-response-ts") -> None:
    """Render `get-response-ts`, then format it via prettier/eslint.

    Two buckets:
      - Always generated (spec-derived, wiped + rewritten every run): `src/models.ts`,
        `src/resources/` (whole dir), `src/resourceGroups.ts`.
      - Scaffold-once (written only if missing, then permanently hand-maintained):
        everything else -- project/build config, the hand-written core runtime
        (`core.ts`/`errors.ts`/`ratelimit.ts`), `client.ts`, `index.ts`, `README.md`, and
        the whole `test/` suite. Once created these are never touched again, so they can
        be hand-edited safely.
    """
    root = Path(out_dir)
    src = root / "src"
    resources_dir = src / "resources"
    test_dir = root / "test"

    # Narrow wipe: only the generated-only subtrees get deleted + recreated. Everything
    # else in `src/`/`test/`, plus `node_modules`/the npm lockfile, is left alone.
    if resources_dir.exists():
        shutil.rmtree(resources_dir)
    src.mkdir(parents=True, exist_ok=True)
    resources_dir.mkdir(parents=True, exist_ok=True)
    test_dir.mkdir(parents=True, exist_ok=True)

    (src / "models.ts").write_text(_render_models_ts(api), encoding="utf-8", newline="\n")

    tags = sorted({op.tag for op in api.operations})
    by_tag: dict[str, list[Operation]] = {tag: [] for tag in tags}
    for op in api.operations:
        by_tag[op.tag].append(op)

    for tag in tags:
        (resources_dir / f"{_tag_camel(tag)}.ts").write_text(
            _render_resource_file(tag, by_tag[tag]), encoding="utf-8", newline="\n"
        )
    (resources_dir / "index.ts").write_text(
        _render_resources_index(tags), encoding="utf-8", newline="\n"
    )

    (src / "resourceGroups.ts").write_text(
        _render_resource_groups_ts(tags), encoding="utf-8", newline="\n"
    )

    # Scaffold-once: written only on first generate, then hand-maintained forever.
    _write_once(root / "package.json", _PACKAGE_JSON)
    _write_once(root / "tsconfig.json", _TSCONFIG_JSON)
    _write_once(root / "eslint.config.js", _ESLINT_CONFIG)
    _write_once(root / ".prettierrc", _PRETTIERRC)
    _write_once(root / ".prettierignore", _PRETTIERIGNORE)
    _write_once(root / ".gitignore", _GITIGNORE)
    _write_once(root / "vitest.config.ts", _VITEST_CONFIG)
    _write_once(root / "README.md", _README_MD)

    _write_once(src / "errors.ts", _ERRORS_TS)
    _write_once(src / "ratelimit.ts", _RATELIMIT_TS)
    _write_once(src / "core.ts", _CORE_TS)
    _write_once(src / "index.ts", _INDEX_TS)
    _write_once(src / "client.ts", _CLIENT_TS)

    _write_once(test_dir / "helpers.ts", _TEST_HELPERS)
    _write_once(test_dir / "auth.test.ts", _TEST_AUTH)
    _write_once(test_dir / "query-building.test.ts", _TEST_QUERY_BUILDING)
    _write_once(test_dir / "models.test.ts", _TEST_MODELS)
    _write_once(test_dir / "pagination.test.ts", _TEST_PAGINATION)
    _write_once(test_dir / "errors.test.ts", _TEST_ERRORS)
    _write_once(test_dir / "ratelimit.test.ts", _TEST_RATELIMIT)

    print(f"wrote {len(tags)} resource modules, models.ts, resourceGroups.ts -> {root}")

    _run_formatters(root)
