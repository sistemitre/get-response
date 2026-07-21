/** Bracket-notation query parameter building. */

import { describe, expect, it } from 'vitest';
import { jsonResponse } from './helpers.js';
import { makeClient } from './helpers.js';

describe('query building', () => {
  it('uses bracket notation and skips undefined params', async () => {
    let capturedUrl: URL | undefined;
    const client = makeClient(async (url) => {
      capturedUrl = new URL(url instanceof Request ? url.url : url.toString());
      return jsonResponse([]);
    });

    await client.contacts.getContactList({
      queryEmail: 'a@b.com',
      sortName: 'ASC',
      page: 2,
      perPage: 50,
    });

    const params = capturedUrl!.searchParams;
    expect(params.get('query[email]')).toBe('a@b.com');
    expect(params.get('sort[name]')).toBe('ASC');
    expect(params.get('page')).toBe('2');
    expect(params.get('perPage')).toBe('50');
    expect(params.has('query[name]')).toBe(false);
  });
});
