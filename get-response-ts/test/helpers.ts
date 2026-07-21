/** Shared test helper: build a `GetResponseClient` over an injected fetch implementation. */

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
