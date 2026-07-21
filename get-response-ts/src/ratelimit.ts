/**
 * Opt-in client-side rate limiting, shared in behavior with the Python/C# clients.
 *
 * Disabled unless {@link RateLimitOptions} is passed to `GetResponseClient`. Three layers:
 *  - proactive: before each attempt, acquire a concurrency slot plus a per-second and a
 *    per-window token; if the wait needed would exceed `maxWaitSeconds`, throw before ever
 *    sending the request.
 *  - reactive: on a 429, read `X-RateLimit-Reset` (falling back to the `ErrorResponse`
 *    body's `context.timeToReset`); retry after sleeping if a retry budget remains and the
 *    reset is within `maxWaitSeconds`, otherwise throw.
 *  - adaptive: read `X-RateLimit-Remaining`/`X-RateLimit-Limit` on every response; once
 *    remaining hits 0, block subsequent acquires until the reported reset.
 */

import { RateLimitError } from './errors.js';

/** Options for `GetResponseClient({ rateLimit })`. Omitting the whole object disables the limiter. */
export interface RateLimitOptions {
  /** Master on/off switch (default true once this options object is provided). */
  enabled?: boolean;
  /** Max in-flight requests. Default 10. */
  maxConcurrency?: number;
  /** Requests allowed per rolling second. Default 80. */
  requestsPerSecond?: number;
  /** Requests allowed per rolling window. Default 30000. */
  requestsPerWindow?: number;
  /** Length of the rolling window, in seconds. Default 600. */
  windowSeconds?: number;
  /** Multiplier applied to `requestsPerSecond`/`requestsPerWindow` (concurrency is not scaled). Default 1.0. */
  safetyMargin?: number;
  /** Max reactive retries on 429 before giving up. Default 5. */
  maxRetries?: number;
  /** Max seconds this limiter will ever wait/sleep before throwing {@link RateLimitError}. Default 60. */
  maxWaitSeconds?: number;
  /** Injectable delay function, for deterministic tests. Defaults to a `setTimeout`-based sleep. */
  sleep?: (ms: number) => Promise<void>;
}

const defaultSleep = (ms: number): Promise<void> =>
  new Promise((resolve) => setTimeout(resolve, ms));

/** A tiny FIFO counting semaphore bounding concurrent requests. */
class Semaphore {
  private active = 0;
  private readonly queue: Array<() => void> = [];

  constructor(private readonly max: number) {}

  async acquire(): Promise<void> {
    if (this.active < this.max) {
      this.active += 1;
      return;
    }
    await new Promise<void>((resolve) => this.queue.push(resolve));
    this.active += 1;
  }

  release(): void {
    this.active -= 1;
    const next = this.queue.shift();
    if (next) next();
  }
}

/** A sliding-window token bucket: `limit` grants per `windowMs`. */
class TokenBucket {
  private timestamps: number[] = [];

  constructor(
    private readonly limit: number,
    private readonly windowMs: number,
  ) {}

  /** Milliseconds to wait right now before a token would be available (0 if one already is). */
  waitMs(now: number): number {
    this.prune(now);
    if (this.timestamps.length < this.limit) return 0;
    return Math.max(0, this.timestamps[0] + this.windowMs - now);
  }

  consume(now: number): void {
    this.prune(now);
    this.timestamps.push(now);
  }

  private prune(now: number): void {
    while (this.timestamps.length > 0 && this.timestamps[0] <= now - this.windowMs) {
      this.timestamps.shift();
    }
  }
}

function parseResetSeconds(header: string | null): number | undefined {
  if (!header) return undefined;
  const match = /^\s*(\d+)/.exec(header);
  return match ? Number(match[1]) : undefined;
}

/** Proactive + reactive + adaptive rate limiting for one `GetResponseClient` instance. */
export class RateLimiter {
  private readonly enabled: boolean;
  private readonly maxWaitMs: number;
  private readonly maxRetries: number;
  private readonly sleepFn: (ms: number) => Promise<void>;
  private readonly concurrency: Semaphore;
  private readonly perSecond: TokenBucket;
  private readonly perWindow: TokenBucket;
  private blockedUntil = 0;

  constructor(options: RateLimitOptions) {
    this.enabled = options.enabled ?? true;
    const margin = options.safetyMargin ?? 1.0;
    const rps = Math.max(1, Math.floor((options.requestsPerSecond ?? 80) * margin));
    const rpw = Math.max(1, Math.floor((options.requestsPerWindow ?? 30_000) * margin));
    const windowSeconds = options.windowSeconds ?? 600;
    this.maxWaitMs = (options.maxWaitSeconds ?? 60) * 1000;
    this.maxRetries = options.maxRetries ?? 5;
    this.sleepFn = options.sleep ?? defaultSleep;
    this.concurrency = new Semaphore(options.maxConcurrency ?? 10);
    this.perSecond = new TokenBucket(rps, 1000);
    this.perWindow = new TokenBucket(rpw, windowSeconds * 1000);
  }

  /** Acquire a concurrency slot and a rate-limit token before sending a request. */
  async acquire(): Promise<void> {
    if (!this.enabled) return;
    await this.concurrency.acquire();
    const now = Date.now();
    const wait = Math.max(
      Math.max(0, this.blockedUntil - now),
      this.perSecond.waitMs(now),
      this.perWindow.waitMs(now),
    );
    if (wait > this.maxWaitMs) {
      this.concurrency.release();
      throw new RateLimitError(429, {
        resetSeconds: wait / 1000,
        message: 'Proactive rate-limit wait would exceed maxWaitSeconds.',
      });
    }
    if (wait > 0) await this.sleepFn(wait);
    const consumedAt = Date.now();
    this.perSecond.consume(consumedAt);
    this.perWindow.consume(consumedAt);
  }

  /** Release the concurrency slot acquired by {@link acquire}. */
  release(): void {
    if (!this.enabled) return;
    this.concurrency.release();
  }

  /** Adaptive layer: track `X-RateLimit-Remaining`/`-Reset` so the next `acquire` can block. */
  observe(response: Response): void {
    if (!this.enabled) return;
    const remaining = response.headers.get('X-RateLimit-Remaining');
    if (remaining !== null && Number(remaining) <= 0) {
      const resetSeconds = parseResetSeconds(response.headers.get('X-RateLimit-Reset')) ?? 1;
      this.blockedUntil = Date.now() + resetSeconds * 1000;
    }
  }

  /** Reactive layer: sleep and return to retry a 429, or throw {@link RateLimitError} to give up. */
  async handle429(response: Response, attempt: number): Promise<void> {
    const limitHeader = response.headers.get('X-RateLimit-Limit');
    const remainingHeader = response.headers.get('X-RateLimit-Remaining');
    const limit = limitHeader ? Number(limitHeader) : undefined;
    const remaining = remainingHeader ? Number(remainingHeader) : undefined;

    let resetSeconds = parseResetSeconds(response.headers.get('X-RateLimit-Reset'));
    if (resetSeconds === undefined) {
      resetSeconds = await this.contextResetSeconds(response);
    }

    const canRetry =
      resetSeconds !== undefined &&
      attempt < this.maxRetries &&
      resetSeconds * 1000 <= this.maxWaitMs;
    if (!canRetry) {
      throw new RateLimitError(429, { resetSeconds, limit, remaining });
    }
    await this.sleepFn(resetSeconds! * 1000);
  }

  private async contextResetSeconds(response: Response): Promise<number | undefined> {
    try {
      const body = (await response.json()) as { context?: { timeToReset?: number } };
      return body?.context?.timeToReset;
    } catch {
      return undefined;
    }
  }
}
