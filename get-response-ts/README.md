# @sistemitre/getresponse

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

