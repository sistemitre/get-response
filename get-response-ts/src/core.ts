/** HTTP transport: request building, auth-agnostic call plumbing, and error mapping. */

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
  const url = new URL(resolvedPath, `${baseUrl.replace(/\/$/, '')}/`);
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
