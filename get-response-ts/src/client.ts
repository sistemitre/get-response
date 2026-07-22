/** Root client: auth, resource-group properties (via declaration merging), and pagination. */

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
    const {
      apiKey,
      accessToken,
      baseUrl = DEFAULT_BASE_URL,
      timeoutMs = 30_000,
      fetch: fetchImpl,
      rateLimit,
    } = options;
    if ((apiKey === undefined) === (accessToken === undefined)) {
      throw new Error('Provide exactly one of `apiKey` or `accessToken`.');
    }
    const authHeader: Record<string, string> =
      apiKey !== undefined
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
