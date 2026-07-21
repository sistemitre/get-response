# codegen — the GetResponse client generator

This package is the **single source of truth** for every GetResponse API client in this
repo (Python, C#, TypeScript). Nothing in `get-response-py/`, `get-response-cs/GetResponse.Api/`,
or `get-response-ts/` is hand-edited beyond the small hand-written runtime core each
language needs — everything else (models, enums, per-tag resource methods) is generated
from `openapi/open-api.json`.

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
   IR into a complete, idiomatic package for their language: models, enums, one class per
   resource tag, a hand-written-quality core (HTTP transport, auth, pagination, error
   mapping, opt-in rate limiter), and a test suite. Each emitter also runs its language's
   formatter/linter as the last step of `emit()`, so generated output is always
   already-clean — `git diff` after a regenerate should only ever show real content changes.

## Regenerating

```
./.venv/Scripts/python.exe -m codegen.generate --python --csharp --typescript
```

Flags are independent — pass any subset to regenerate only those libraries. Add
`--dump-ir` to print IR summary stats (model/enum/operation counts, per-tag operation
distribution) and write a full IR JSON dump to `codegen/_ir_dump.json` — the fastest way
to inspect what a given schema or operation resolved to without re-reading the raw spec.

To pick up an API change: re-vendor `openapi/open-api.json` (re-download from
`https://apireference.getresponse.com/open-api.json`), then regenerate.

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
is self-contained: it owns its output directory, its hand-written core templates, and its
own lint/format/test wiring). Wire a new `--<language>` flag into `generate.py`'s
lazy-import branches — the pattern there is deliberately copy-paste-friendly. You should
not need to touch `spec.py`, `ir.py`, or another language's emitter.

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
