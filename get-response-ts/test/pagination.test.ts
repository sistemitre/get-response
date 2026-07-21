/** `GetResponseClient.paginate` walks full pages and stops on a short/empty one. */

import { describe, expect, it } from 'vitest';
import { jsonResponse } from './helpers.js';
import { makeClient } from './helpers.js';

function contact(i: number) {
  return { contactId: `id${i}`, email: `${i}@example.com`, href: 'h' };
}

describe('pagination', () => {
  it('walks full pages then stops on a short page', async () => {
    const pages = [
      Array.from({ length: 50 }, (_, i) => contact(i)),
      Array.from({ length: 50 }, (_, i) => contact(i + 50)),
      [contact(100)],
    ];
    let calls = 0;

    const client = makeClient(async (url) => {
      const page = Number(new URL(url instanceof Request ? url.url : url.toString()).searchParams.get('page'));
      calls += 1;
      return jsonResponse(pages[page - 1]);
    });

    const seen = [];
    for await (const item of client.paginate(client.contacts.getContactList, { perPage: 50 })) {
      seen.push(item);
    }

    expect(seen).toHaveLength(101);
    expect(calls).toBe(3);
  });
});
