# GetResponse API Client Generator

## Original instructions

Interact completely with the GetResponse v3 API. Three deliverables:

- **Python package** in `get-response-py/`
- **C# .NET solution** in `get-response-cs/` (solution) with project `get-response-cs/GetResponse.Api/` (NuGet package)
- **TypeScript/Node package** in `get-response-ts/` (npm package `@sistemitre/getresponse`)

Both are built from the official OpenAPI spec:
`https://apireference.getresponse.com/open-api.json` — vendored at `openapi/open-api.json`.

Rules: **DRY** and **KISS**. Meaningful doc comments on every method/class. Do not
over-explain — the reader is an experienced programmer.

## Architecture

A spec-driven code generator in `codegen/` is the **single source of truth** for what's
actually derived from the spec: models, enums, and per-tag resource/operation methods.
Regenerating **fully wipes and rewrites only those** — everything else (build/project files,
the hand-written core runtime, READMEs, tests) is **scaffolded once** (written only if
missing) and safe to hand-edit forever after. See `codegen/README.md`'s "Two buckets"
section for the full breakdown and how each language keeps the root client's resource-group
properties in sync with the spec's tags without the client itself being regenerated
(a generated mixin/partial-class/declaration-merging, one idiom per language). To pick up
API changes: re-vendor the spec, then regenerate — this only ever touches the
always-generated bucket.

To regenerate all three libraries:

```
./.venv/Scripts/python.exe -m codegen.generate --python --csharp --typescript
```

Flags `--python` / `--csharp` / `--typescript` can be passed independently to regenerate
only one library. `--dump-ir` prints IR summary stats and writes a full IR JSON dump to
`codegen/_ir_dump.json` for inspection.

## API facts

- Base URL: `https://api.getresponse.com/v3`
  (+ MAX US `api3.getresponse360.com/v3`, MAX PL `api3.getresponse360.pl/v3`)
- Auth: header `X-Auth-Token: api-key <KEY>` **or** OAuth2 `Authorization: Bearer <token>`
- 220 operations / 43 tags / 435 schemas
- Query params use bracket notation: `query[email]`, `query[createdOn][from]`, `sort[name]`,
  plus plain `page`, `perPage`, `fields`
- Pagination via response headers: `TotalCount`, `CurrentPage`, `TotalPages`, `PerPage`
- Errors return an `ErrorResponse` body: `httpStatus`, `code`, `codeDescription`, `message`,
  `moreInfo`, `context`, `uuid`

## Language choices

**Python** (`get-response-py/`): async only, `httpx` + `pydantic` v2, lint/format via `ruff`,
types via `mypy`.

**C#** (`get-response-cs/GetResponse.Api/`): `net8.0;net9.0;net10.0`, `System.Text.Json` only
(no external serialization deps), xUnit tests, `.editorconfig` + `dotnet format`.

**TypeScript** (`get-response-ts/`): ESM only, Node >=18, zero runtime deps (built on the
global `fetch`), models are plain interfaces keyed by wire name (identity (de)serialization)
with enums as string-literal union types, lint/format via `eslint` + `prettier`, tests via
`vitest`.

## Build environment note

The corporate NuGet feed returns 401 and aborts restore on this machine. A repo-local
`get-response-cs/nuget.config` (`<clear/>` + nuget.org only) isolates the C# build to nuget.org
so `dotnet restore`/`build`/`test`/`pack` work regardless of the machine's configured feeds.

## CI & Publishing

GitHub Actions workflows live in `.github/workflows/` in this repo:

- **CI** (`ci.yml`) runs on every push to `main` and on pull requests. It regenerates all
  three packages and fails if that produces any diff against what's committed here — the
  guard against someone editing the emitter or the vendored spec and forgetting to
  regenerate — then lints/builds/tests all three.
- **Release** (`release.yml`) triggers only on a version tag (`vX.Y.Z`) pushed to this repo.
  All three packages share one version, taken from the tag, and publish to their public
  registries. All three publish via **Trusted Publishing** (OIDC, no stored secret — see the
  workflow's top comment for the one-time pending-publisher/policy setup on each registry).
  npm's Trusted Publisher could only be configured after `@sistemitre/getresponse`'s first
  publish, which was done manually once to bootstrap the package name. To cut a release:

```
git tag v1.2.0
git push origin v1.2.0
```

`main` is protected on GitHub: merges require a pull request with a passing `ci.yml` check,
enforced for everyone including admins — no direct pushes.
