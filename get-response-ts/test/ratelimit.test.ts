/** Rate limiter: disabled-by-default passthrough, reactive retry, cap, and concurrency. */

import { describe, expect, it, vi } from 'vitest';
import { RateLimitError } from '../src/index.js';
import { jsonResponse } from './helpers.js';
import { makeClient } from './helpers.js';

describe('rate limiter', () => {
  it('is a no-op when rateLimit is not provided', async () => {
    let calls = 0;
    const client = makeClient(async () => {
      calls += 1;
      return jsonResponse([]);
    });

    await client.contacts.getContactList();

    expect(calls).toBe(1);
  });

  it('retries a 429 after sleeping for X-RateLimit-Reset, using an injected sleep', async () => {
    const sleep = vi.fn(async (_ms: number) => {});
    let calls = 0;
    const client = makeClient(
      async () => {
        calls += 1;
        if (calls === 1) {
          return new Response(null, {
            status: 429,
            headers: { 'X-RateLimit-Reset': '1 seconds' },
          });
        }
        return jsonResponse([]);
      },
      { rateLimit: { sleep, maxWaitSeconds: 60 } },
    );

    const result = await client.contacts.getContactList();

    expect(result).toEqual([]);
    expect(calls).toBe(2);
    expect(sleep).toHaveBeenCalledWith(1000);
  });

  it('throws RateLimitError without a long sleep when the reset exceeds maxWaitSeconds', async () => {
    const sleep = vi.fn(async (_ms: number) => {});
    const client = makeClient(
      async () =>
        new Response(null, {
          status: 429,
          headers: { 'X-RateLimit-Reset': '9999 seconds' },
        }),
      { rateLimit: { sleep, maxWaitSeconds: 60 } },
    );

    await expect(client.contacts.getContactList()).rejects.toBeInstanceOf(RateLimitError);
    expect(sleep).not.toHaveBeenCalled();
  });

  it('never exceeds maxConcurrency in-flight requests', async () => {
    let active = 0;
    let maxActive = 0;
    const client = makeClient(
      async () => {
        active += 1;
        maxActive = Math.max(maxActive, active);
        await new Promise((resolve) => setTimeout(resolve, 5));
        active -= 1;
        return jsonResponse([]);
      },
      { rateLimit: { maxConcurrency: 3, requestsPerSecond: 1000, requestsPerWindow: 1_000_000 } },
    );

    await Promise.all(Array.from({ length: 10 }, () => client.contacts.getContactList()));

    expect(maxActive).toBeLessThanOrEqual(3);
  });
});
