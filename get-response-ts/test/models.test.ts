/**
 * Model (de)serialization: a realistic Contact payload parses as-is (identity); a NewContact
 * value serializes to wire JSON with no undefined keys, keyed by the raw camelCase wire names.
 */

import { describe, expect, it } from 'vitest';
import type { Contact, NewContact } from '../src/models.js';

describe('models', () => {
  it('a Contact payload parses with wire-name keys intact', () => {
    const payload: Contact = {
      contactId: 'abc123',
      name: 'Jane Doe',
      origin: 'api',
      createdOn: '2024-01-01T00:00:00+00:00',
      campaign: { campaignId: 'c1', name: 'My Campaign' },
      email: 'jane@example.com',
      href: 'https://api.getresponse.com/v3/contacts/abc123',
    };

    const contact: Contact = JSON.parse(JSON.stringify(payload));

    expect(contact.contactId).toBe('abc123');
    expect(contact.email).toBe('jane@example.com');
    expect(contact.origin).toBe('api');
    expect(contact.campaign?.campaignId).toBe('c1');
  });

  it('a NewContact value serializes to camelCase wire JSON with no undefined keys', () => {
    const newContact: NewContact = {
      contactId: '',
      href: '',
      email: 'jane@example.com',
      campaign: { campaignId: 'c1' },
      name: 'Jane Doe',
    };

    const dumped = JSON.parse(JSON.stringify(newContact));

    expect(dumped.email).toBe('jane@example.com');
    expect(dumped.campaign.campaignId).toBe('c1');
    expect(dumped.contactId).toBe('');
    expect('contact_id' in dumped).toBe(false);
    expect(Object.values(dumped).every((v) => v !== undefined)).toBe(true);
  });
});
