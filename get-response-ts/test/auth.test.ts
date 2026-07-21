/** Auth header selection: `X-Auth-Token` for API keys, `Bearer` for OAuth2 tokens. */

import { describe, expect, it } from 'vitest';
import { GetResponseClient } from '../src/index.js';
import { jsonResponse } from './helpers.js';

describe('auth', () => {
  it('sends X-Auth-Token for an apiKey', async () => {
    let captured: Headers | undefined;
    const client = new GetResponseClient({
      apiKey: 'my-key',
      fetch: async (_url, init) => {
        captured = new Headers(init?.headers);
        return jsonResponse([]);
      },
    });

    await client.contacts.getContactList();

    expect(captured?.get('X-Auth-Token')).toBe('api-key my-key');
  });

  it('sends Bearer for an accessToken', async () => {
    let captured: Headers | undefined;
    const client = new GetResponseClient({
      accessToken: 'my-token',
      fetch: async (_url, init) => {
        captured = new Headers(init?.headers);
        return jsonResponse([]);
      },
    });

    await client.contacts.getContactList();

    expect(captured?.get('Authorization')).toBe('Bearer my-token');
  });

  it('requires exactly one credential', () => {
    expect(() => new GetResponseClient()).toThrow();
    expect(() => new GetResponseClient({ apiKey: 'a', accessToken: 'b' })).toThrow();
  });
});
