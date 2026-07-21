# getresponse

An async, fully-typed Python client for the [GetResponse v3 API](https://apireference.getresponse.com/),
generated from the official OpenAPI spec.

## Install

```bash
pip install -e .
```

## Quickstart

```python
import asyncio

from getresponse import GetResponseClient


async def main() -> None:
    async with GetResponseClient(api_key="YOUR_API_KEY") as client:
        contacts = await client.contacts.get_contact_list(query_email="jane@example.com")
        for contact in contacts:
            print(contact.contact_id, contact.email)


asyncio.run(main())
```

Use `access_token=` instead of `api_key=` to authenticate with an OAuth2 bearer token.

A real API key (or access token) is required for live use; the test suite mocks the
network entirely and needs neither.

## Pagination

Resource `list_*`/`get_*_list` methods return one page at a time. `GetResponseClient.paginate`
walks every page for you:

```python
async for contact in client.paginate(client.contacts.get_contact_list, per_page=100):
    print(contact.email)
```

It stops once a page comes back empty or shorter than `per_page` -- simpler and more
transport-agnostic than reading the `TotalPages`/`CurrentPage` response headers.

## Rate limiting

The client can throttle itself to stay under GetResponse's API limits. It's **opt-in** --
pass `rate_limit=` and it's off by default:

```python
from getresponse import GetResponseClient, RateLimitOptions

client = GetResponseClient(
    api_key="YOUR_API_KEY",
    rate_limit=RateLimitOptions(safety_margin=0.9),
)
```

When enabled, every request goes through:

- **Proactive throttling**: a concurrency cap (`max_concurrency`, default 10) plus per-second
  and per-window token buckets (`requests_per_second`/`requests_per_window`, default 80 and
  30000 over `window_seconds`, default 600). `safety_margin` (default `1.0`) scales the rps/
  window caps down before use; concurrency is never scaled.
- **Reactive retries**: on an HTTP 429, the reset time is read from the `X-RateLimit-Reset`
  header (falling back to the error body's `context.timeToReset`) and the request is retried
  after sleeping that long, up to `max_retries` (default 5).
- **Adaptive best-effort throttling**: `X-RateLimit-Remaining`/`X-RateLimit-Limit` response
  headers are tracked, and new requests are blocked once a response reports zero remaining.

Every wait -- proactive or reactive -- is capped by `max_wait` (default 60s). If satisfying a
request would require waiting longer than that, the client raises `RateLimitError` (a
`GetResponseApiError` subclass with `reset_seconds`/`limit`/`remaining`) instead of sleeping
indefinitely.

Note: GetResponse's limits are enforced per account/API key on their side. If the same key is
shared across multiple client instances or processes, each instance only tracks its own
requests, so the actual server-side limit can still be hit -- this limiter is a best-effort,
client-local approximation, not a substitute for a shared/coordinated limiter.

