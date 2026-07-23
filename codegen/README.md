# codegen — the GetResponse client generator

This package is the **single source of truth** for what's actually derived from the
OpenAPI spec in every GetResponse API client in this repo (Python, C#, TypeScript):
models, enums, and per-tag resource/operation methods. Everything else in
`get-response-py/`, `get-response-cs/`, and `get-response-ts/` — build/project files, the
hand-written core runtime (HTTP transport, auth, pagination, error mapping, the rate
limiter), READMEs, and test suites — is **scaffolded once** and then genuinely
hand-maintained; regenerating never touches it again. See "Two buckets" below.

Audience: maintainers of this repo, not consumers of the generated libraries. If you just
want to *use* a client, see that library's own README (`get-response-py/README.md`,
`get-response-cs/GetResponse.Api/README.md`, `get-response-ts/README.md`).

## Pipeline

```
openapi/open-api.json ─▶ spec.py (load, $ref-resolve, allOf-flatten, type-map) ─▶ Api (ir.py)
                                                                                     │
                                              ┌──────────────────┬───────────────────┼───────────────────┐
                                              ▼                  ▼                                       ▼
                                       emit_python.py      emit_csharp.py                        emit_typescript.py
                                              │                  │                                       │
                                              ▼                  ▼                                       ▼
                                     get-response-py/  get-response-cs/GetResponse.Api/          get-response-ts/
```

1. **`spec.py`** loads the vendored spec, resolves every `$ref`, flattens `allOf`
   compositions into flat property sets, collapses `oneOf`/`anyOf` to a permissive
   `object` type (only a handful of schemas use them — not worth modeling as unions),
   and maps JSON Schema types to the language-neutral `TypeRef` kinds used by the IR.
   `build_api(spec) -> Api` is the entry point.
2. **`ir.py`** defines the IR dataclasses (`Api`, `Model`, `Field`, `EnumType`, `Operation`,
   `Param`, `TypeRef`) that `spec.py` produces and every emitter consumes. **This is the
   contract** — field names and shapes here must not change without updating every emitter
   that reads them. Both `py_name`/`cs_name` (and the TS emitter's own camelCase/PascalCase
   conversion) are precomputed per `Field`/`Param`/`Operation` so emitters don't duplicate
   naming logic for each other's target casing.
3. **`naming.py`** — pure string-case helpers (`snake_case`, `pascal_case`, `camel_case`)
   plus reserved-word-safe identifier helpers (`safe_py_ident`, `safe_cs_ident`). Shared by
   `spec.py` when precomputing names and by emitters for anything not already on the IR
   (e.g. resource-group class names derived from tags).
4. **`emit_python.py` / `emit_csharp.py` / `emit_typescript.py`** each render the same `Api`
   IR into a complete, idiomatic package for their language, split across two buckets (see
   below). Each emitter also runs its language's formatter/linter as the last step of
   `emit()`, so generated output is always already-clean — `git diff` after a regenerate
   should only ever show real content changes to the always-generated bucket.

## Two buckets: what's regenerated vs. scaffolded once

Every `emit()` writes two kinds of files, and treats them completely differently:

- **Always generated** — models, enums, and one resource-group class per API tag, fully
  wiped and rewritten on *every* run: `getresponse/models.py` + `getresponse/resources/`
  (Python), `Models/`/`Resources/` (C#), `src/models.ts` + `src/resources/` (TypeScript).
  These are the only things actually derived from the spec.
- **Scaffold-once** — everything else: build/project files (`pyproject.toml`,
  `package.json`, `GetResponse.sln`, both `.csproj` files, lint/format configs), the
  hand-written core runtime (HTTP transport, auth, pagination, error mapping, the opt-in
  rate limiter, Python's `_compat.py`, C#'s `Internal/EnumWireValues.cs`), the root
  client's constructors/lifecycle, READMEs, and test suites. Each is written **only if it
  doesn't already exist** — a fresh checkout gets them scaffolded once; every later
  regenerate leaves them untouched. **Hand-editing these is expected and safe** — that's
  the whole point.
  - The C# `.sln` and both `.csproj` files are scaffolded via the real `dotnet` CLI
    (`dotnet new sln`/`classlib`/`xunit`, `dotnet sln add`, `dotnet add package`/
    `reference`) rather than a Python string template, gated by the same exists-check —
    see `_scaffold_solution_and_projects`/`_patch_api_csproj`/`_patch_tests_csproj` in
    `emit_csharp.py`. A few properties (`TargetFrameworks` multi-targeting, NuGet package
    metadata) have no CLI flag and get a one-time XML patch right after scaffolding, same
    as a human setting this up by hand would do.

**Unrecognized enum wire values**: GetResponse occasionally sends a wire value a generated
enum doesn't have a member for — either literally `""` instead of omitting an optional
field with no value, or a genuinely new value added to the live API after this client was
generated. Python and C# each get an `Unknown`/`UNKNOWN` sentinel member instead of raising:
- **Python**: every generated enum subclasses `_UnknownFallbackEnum` (in `_compat.py`,
  scaffold-once), which overrides `_missing_` to resolve any unrecognized value to
  `UNKNOWN`. Optional fields stay `Optional[...]`, so a genuinely absent field or explicit
  JSON `null` still resolves to Python `None` — `UNKNOWN` and `None` mean two different
  things (API sent something we don't recognize vs. field wasn't there at all).
- **C#**: `EnumMemberJsonConverter<T>` (non-nullable enum properties) keeps its existing
  fallback to the enum's `Unknown = 0` member. A separate `NullableEnumMemberJsonConverter<T>`
  (nullable enum properties) maps unrecognized values to C# `null` instead — deliberately
  *not* unified into "always non-nullable with `Unknown` as the null substitute," because
  the generator also emits write-only DTOs (e.g. `UpdateContact`) that get serialized back
  out as PATCH-style request bodies, relying on `JsonIgnoreCondition.WhenWritingNull` to
  omit fields the caller didn't set. A non-nullable property can never be `null`, so that
  omission would silently break and every unset enum field would be serialized as the
  literal string `"Unknown"` on every write.
- **TypeScript**: no equivalent exists or is needed — models are plain interfaces with zero
  runtime validation (`JSON.parse(...) as T`), so an unrecognized wire value simply flows
  through untouched; nothing throws.

**Keeping the root client in sync despite being scaffold-once**: `GetResponseClient` needs
one property per resource tag, but the tag list can change when the spec does. Each
language solves this with its own idiom for extending a type's public surface from two
places while keeping full static typing:
- **Python**: a generated mixin class `_ResourceGroups` (in `_resource_groups.py`, always
  regenerated) declares one typed attribute per tag plus an `_attach_resource_groups`
  method; the scaffold-once `GetResponseClient` inherits from it.
- **C#**: `GetResponseClient` is a `partial class`. The generated half
  (`GetResponseClient.Resources.cs`) declares the per-tag properties (`{ get; private
  set; }`, since C# forbids assigning a getter-only auto-property from outside the type's
  own constructor) plus an `InitializeResourceGroups` method; the scaffold-once half calls
  it from each constructor.
- **TypeScript**: a generated `resourceGroups.ts` exports an interface
  `GeneratedResourceGroups` plus a `createResourceGroups(core)` factory; the scaffold-once
  `client.ts` declaration-merges (`interface GetResponseClient extends
  GeneratedResourceGroups {}`) and calls `Object.assign(this, createResourceGroups(...))`
  in its constructor.

**To force a scaffold file back to its generated default** (rare — e.g. you want to
discard local hand-edits and start over): delete the file and regenerate; it'll be
recreated fresh. There's no flag for this — deleting the file *is* the mechanism.

## Regenerating

```
./.venv/Scripts/python.exe -m codegen.generate --python --csharp --typescript
```

Flags are independent — pass any subset to regenerate only those libraries. Add
`--dump-ir` to print IR summary stats (model/enum/operation counts, per-tag operation
distribution) and write a full IR JSON dump to `codegen/_ir_dump.json` — the fastest way
to inspect what a given schema or operation resolved to without re-reading the raw spec.

To pick up an API change: re-vendor `openapi/open-api.json` (re-download from
`https://apireference.getresponse.com/open-api.json`), then regenerate. This only ever
touches the always-generated bucket (models/enums/resources) — your hand-edits to the core
runtime, build files, README, or tests are never at risk.

## Testing the generator itself

`codegen/tests/` unit-tests the transform layer directly (naming edge cases, `allOf`
flattening, enum extraction, and a full `build_api()` pass over the real vendored spec
asserting the expected operation/model counts and that every `operationId` is unique).
Run with:

```
./.venv/Scripts/python.exe -m pytest codegen/tests -q
```

These are the guardrails for the one thing every emitter depends on — prefer adding a
case here over debugging the same IR quirk independently in three emitters.

## Extending

**Adding a field to the IR** (e.g. a new `Param` attribute): update `ir.py`, populate it in
`spec.py`, then update every emitter that needs it. Regenerate all three libraries and rerun
each one's full test suite before committing — a change here fans out everywhere.

**Adding a fourth target language**: write `emit_<language>.py` exposing
`emit(api: Api, out_dir: str) -> None`, following the shape of the existing emitters (each
is self-contained: it owns its output directory, its own lint/format/test wiring, and the
same two-bucket split — always-generated models/resources plus a scaffold-once core,
build files, README, and tests, with a generated resource-groups mixin/partial/interface
so the root client stays in sync without itself being regenerated). Wire a new
`--<language>` flag into `generate.py`'s lazy-import branches — the pattern there is
deliberately copy-paste-friendly. You should not need to touch `spec.py`, `ir.py`, or
another language's emitter.

## Design notes / known simplifications

- **`oneOf`/`anyOf`** (a small minority of schemas) collapse to a permissive object/`any`
  type rather than a modeled union — pragmatic given how few schemas use them.
- **`requestBody.required`** is never set in the spec itself; emitters treat "has a body"
  as "body is a required argument," which matches real usage even though the IR's
  `body_required` flag is always `False`.
- **Tag names** aren't a clean namespace (e.g. `"Forms"` vs `"Forms and Popups"`, `"Sms"`
  vs `"SMS Messages"`) — each emitter sanitizes/deduplicates tag names into resource-group
  class names independently rather than the IR pre-normalizing them, since the "nicest"
  identifier shape differs slightly per language convention.
- **Rate limiting** is implemented independently per emitter (each language has its own
  idiomatic concurrency/async primitives — `asyncio` locks/semaphores, .NET
  `System.Threading.RateLimiting`, JS promise queues) but all three follow the *same*
  documented contract (config field names/defaults, proactive + reactive + adaptive
  behavior, cap-then-raise on excessive waits) — see the "Rate limiting" section in each
  library's own README for the user-facing behavior.
