/** Non-2xx responses raise `GetResponseApiError` with `ErrorResponse` fields populated. */

import { describe, expect, it } from 'vitest';
import { GetResponseApiError } from '../src/index.js';
import { jsonResponse } from './helpers.js';
import { makeClient } from './helpers.js';

describe('errors', () => {
  it('maps a 400 ErrorResponse body to a typed exception', async () => {
    const body = {
      httpStatus: 400,
      code: 1010,
      codeDescription: 'Invalid value',
      message: 'Email is invalid',
      moreInfo: 'https://apidocs.getresponse.com/errors/1010',
      context: { field: 'email' },
      uuid: 'abc-123',
    };
    const client = makeClient(async () => jsonResponse(body, { status: 400 }));

    await expect(client.contacts.getContactList()).rejects.toMatchObject({
      statusCode: 400,
      code: 1010,
      message: 'Email is invalid',
      context: { field: 'email' },
      uuid: 'abc-123',
    });
    await expect(client.contacts.getContactList()).rejects.toBeInstanceOf(GetResponseApiError);
  });
});
