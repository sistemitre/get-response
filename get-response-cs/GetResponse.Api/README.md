# GetResponse.Api

A complete, typed, async C# client for the [GetResponse v3 API](https://apireference.getresponse.com/),
generated from the official OpenAPI spec. Targets `net8.0`, `net9.0`, and `net10.0`, uses
`System.Text.Json` for all serialization, and has no dependency beyond
`System.Threading.RateLimiting` (used only by the optional rate limiter below).

- 220 operations across 49 resource groups (Contacts, Campaigns, Newsletters, Autoresponders,
  e-commerce, Automations, and more) as strongly-typed `Task`-returning methods.
- 372 models as `record` types and 317 enums, all documented from the spec.
- Works against an API key or an OAuth2 bearer token.
- Optional, opt-in client-side rate limiting for the API's documented request budgets.

## Install

```
dotnet add package GetResponse.Api
```

## Quickstart

```csharp
using GetResponse.Api;

var client = new GetResponseClient("YOUR_API_KEY");

var contacts = await client.Contacts.GetContactListAsync(queryEmail: "jane@example.com");

await client.Contacts.CreateContactAsync(new NewContact
{
    Email = "new.contact@example.com",
    CampaignId = "campaign-id",
});
```

Authenticate with an OAuth2 bearer token instead of an API key via the static factory:

```csharp
var client = GetResponseClient.CreateWithBearerToken("YOUR_ACCESS_TOKEN");
```

`GetResponseClient` is `IDisposable` — dispose it (or wrap it in a `using`) when you're done with it,
unless you constructed it around an `HttpClient` you own and manage yourself.

## Pagination

List endpoints return one page at a time. `Pagination.PaginateAsync` turns any list method into an
`IAsyncEnumerable<T>` that walks every page lazily:

```csharp
await foreach (var contact in Pagination.PaginateAsync(
    (page, perPage, ct) => client.Contacts.GetContactListAsync(page: page, perPage: perPage, ct: ct)))
{
    Console.WriteLine(contact.Email);
}
```

It stops as soon as a page comes back shorter than the requested page size — no need to inspect the
`TotalCount`/`CurrentPage`/`TotalPages` response headers yourself.

## Errors

Every non-2xx response throws `GetResponseApiException`, carrying the API's structured error body:
`StatusCode`, `Code`, `CodeDescription`, `Message`, `MoreInfo`, `Context`, and `Uuid`.

```csharp
try
{
    await client.Contacts.CreateContactAsync(new NewContact { Email = "bad" });
}
catch (GetResponseApiException ex)
{
    Console.WriteLine($"{ex.StatusCode} {ex.Code}: {ex.Message}");
}
```

## Rate limiting

GetResponse enforces 30,000 requests per 10-minute window, 80 requests/second, and up to 10
simultaneous requests per account, returning HTTP 429 (error code 1015) once a limit is hit. The
client can enforce these limits itself so you don't have to catch 429s in every call site — it's
**opt-in**, off by default:

```csharp
var client = new GetResponseClient("YOUR_API_KEY", new GetResponseClientOptions
{
    RateLimit = new RateLimitOptions
    {
        SafetyMargin = 0.9, // stay at 90% of the documented limits to leave headroom
    },
});
```

When configured, every request:

1. **Proactively** waits for a concurrency slot and a per-second/per-window budget slot before it is
   even sent, pacing requests to stay under the limits.
2. **Reactively** retries automatically on a 429, honoring the server's `X-RateLimit-Reset` header,
   up to `MaxRetries` (default 5).
3. **Adaptively** watches `X-RateLimit-Remaining` on every response and backs off pre-emptively once
   it nears zero.

If a required wait would exceed `MaxWaitSeconds` (default 60) — either before sending or after a
429 — the call throws `RateLimitException` (a `GetResponseApiException` subclass exposing
`ResetSeconds`, `Limit`, and `Remaining`) instead of blocking indefinitely.

**Caveat**: the 30,000/window budget is per API key, shared across every process using that key.
The limiter only sees traffic from its own `GetResponseClient` instance, so proactive pacing is
best-effort when multiple processes (or machines) share one key — the reactive 429 handling is the
reliable backstop in that case.

## Testing

`GetResponse.Api.Tests` runs entirely offline against a stub `HttpMessageHandler` — no API key
needed to build or test this project.
