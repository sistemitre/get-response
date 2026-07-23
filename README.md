# get-response

Three fully-typed, async client libraries for the [GetResponse v3 API](https://apireference.getresponse.com/) —
Python, C#, and TypeScript/Node — generated from GetResponse's official OpenAPI spec by a
single generator in this repo. Covers all 220 operations across 43 resource groups
(contacts, campaigns, newsletters, autoresponders, e-commerce, marketing automation, and
more), with an opt-in client-side rate limiter shared across all three.

No official GetResponse SDK exists for any of these languages, and the community Python
packages we found were either narrow or unmaintained — this repo exists to fill that gap
with something complete and kept in sync with the spec by construction, not by hand.

## The three packages

| Language | Package | Install |
|---|---|---|
| Python | [`get-response-py/`](get-response-py/) — `getresponse` on PyPI | `pip install getresponse` |
| C# | [`get-response-cs/GetResponse.Api/`](get-response-cs/GetResponse.Api/) — `GetResponse.Api` on NuGet | `dotnet add package GetResponse.Api` |
| TypeScript/Node | [`get-response-ts/`](get-response-ts/) — `getresponse` on npm | `npm install getresponse` |

Each has its own README with a full quickstart, pagination, error handling, and rate
limiting — read those to actually use a client. This README is about the repo as a whole.

```python
# Python
async with GetResponseClient(api_key="...") as client:
    contacts = await client.contacts.get_contact_list(query_email="jane@example.com")
```
```csharp
// C#
var client = new GetResponseClient("...");
var contacts = await client.Contacts.GetContactListAsync(queryEmail: "jane@example.com");
```
```typescript
// TypeScript
const client = new GetResponseClient({ apiKey: "..." });
const contacts = await client.contacts.getContactList({ queryEmail: "jane@example.com" });
```

## How this repo is put together

`codegen/` is a spec-driven generator and the single source of truth. It reads the vendored
OpenAPI spec (`openapi/open-api.json`) and emits all three packages — models, enums, and
one typed method per operation. Nothing under `get-response-py/getresponse/`,
`get-response-cs/GetResponse.Api/`, or `get-response-ts/src/` is hand-edited; each package
also has a small hand-written core (HTTP transport, auth, pagination, error mapping, the
rate limiter) that the generator doesn't touch. See [`codegen/README.md`](codegen/README.md)
for how the generator itself works.

To pick up an API change: re-vendor the spec, then regenerate everything with one command:

```
./.venv/Scripts/python.exe -m codegen.generate --python --csharp --typescript
```

```
get-response/
├─ openapi/open-api.json     # vendored spec — the actual source of truth
├─ codegen/                  # the generator (Python) — see codegen/README.md
├─ get-response-py/          # Python package (async, httpx + pydantic v2)
├─ get-response-cs/          # C# solution (net8.0;net9.0, System.Text.Json only)
└─ get-response-ts/          # TypeScript package (ESM, zero runtime deps)
```

## Development

Each package can be built/linted/tested independently once generated:

- **Python**: `./.venv/Scripts/python.exe -m pytest get-response-py/tests -q` (also `ruff`, `mypy`)
- **C#**: `dotnet build get-response-cs/GetResponse.sln`, `dotnet test`, `dotnet format --verify-no-changes`
- **TypeScript**: `npm run build && npm run lint && npm test` (from `get-response-ts/`)

All test suites run offline against a mocked HTTP layer — no GetResponse API key is needed
to build or test any of the three packages; you only need one to actually call the API.

If you're changing behavior, **fix the generator, not the generated output** — anything
under the three package directories gets overwritten on the next regenerate.

## CI/CD

GitHub Actions workflows live in [`.github/workflows/`](.github/workflows/): `ci.yml` runs on
every push and PR to `main` (build/lint/test + a check that regenerating produces no drift),
and `release.yml` publishes all three packages to their public registries (nuget.org, PyPI,
npm) when a `vX.Y.Z` tag is pushed. `main` is protected — merges require `ci.yml` to pass.

## License

MIT.
