/** Operations tagged 'Contacts' in the GetResponse API. */

import type { Core } from '../core.js';
import type * as M from '../models.js';

export class ContactsResource {
  constructor(private readonly core: Core) {}

  /** This endpoint lets you create multiple contacts in one request. **Note** This endpoint is subject to special limits and throttling. You can make 80 calls per time frame (10 minutes) and only 1 call per second. The allowed batch size is 1000 contacts. For more information, check our [API Docs](https://apidocs.getresponse.com/v3/case-study/adding-batch-contacts). */
  readonly createBatchContacts = async (
    body: Record<string, unknown>,
    signal?: AbortSignal,
  ): Promise<void> => {
    return this.core.request<void>('POST', '/contacts/batch', {
      body,
      signal,
    });
  };

  /** Create a new contact */
  readonly createContact = async (body: M.NewContact, signal?: AbortSignal): Promise<void> => {
    return this.core.request<void>('POST', '/contacts', {
      body,
      signal,
    });
  };

  /** Delete a contact by contact ID */
  readonly deleteContact = async (
    contactId: string,
    params?: {
      /** This makes it possible to pass the IP from which the contact unsubscribed. Used only if the `messageId` was send. */
      ipAddress?: string;
      /** > The ID of a message (such as a newsletter, an autoresponder, or an RSS-newsletter). When passed, this method will simulate the unsubscribe process, as if the contact clicked the unsubscribe link in a given message. */
      messageId?: string;
    },
    signal?: AbortSignal,
  ): Promise<void> => {
    return this.core.request<void>('DELETE', '/contacts/{contactId}', {
      pathParams: { contactId: contactId },
      query: params ? { messageId: params.messageId, ipAddress: params.ipAddress } : undefined,
      signal,
    });
  };

  /** By default, only activities from the last 14 days are returned. To get earlier data, use `query[createdOn]` parameter. You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by. */
  readonly getActivities = async (
    contactId: string,
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
      /** Page number */
      page?: number;
      /** Requested number of results per page */
      perPage?: number;
      queryCreatedOnFrom?: string;
      queryCreatedOnTo?: string;
    },
    signal?: AbortSignal,
  ): Promise<M.ContactActivity[]> => {
    return this.core.request<M.ContactActivity[]>('GET', '/contacts/{contactId}/activities', {
      pathParams: { contactId: contactId },
      query: params
        ? {
            'query[createdOn][from]': params.queryCreatedOnFrom,
            'query[createdOn][to]': params.queryCreatedOnTo,
            fields: params.fields,
            perPage: params.perPage,
            page: params.page,
          }
        : undefined,
      signal,
    });
  };

  /** Returns all available information about an active (non-deleted) contact identified by `contactId`. The response includes basic contact data, associated tags, and values of custom fields */
  readonly getContactById = async (
    contactId: string,
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
    },
    signal?: AbortSignal,
  ): Promise<M.ContactDetails> => {
    return this.core.request<M.ContactDetails>('GET', '/contacts/{contactId}', {
      pathParams: { contactId: contactId },
      query: params ? { fields: params.fields } : undefined,
      signal,
    });
  };

  /** Returns a list of all consent fields assigned to the contact, including their current status and history of changes. */
  readonly getContactConsentsById = async (
    contactId: string,
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
    },
    signal?: AbortSignal,
  ): Promise<M.ContactConsent[]> => {
    return this.core.request<M.ContactConsent[]>('GET', '/contacts/{contactId}/consents', {
      pathParams: { contactId: contactId },
      query: params ? { fields: params.fields } : undefined,
      signal,
    });
  };

  /** You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by. */
  readonly getContactList = async (
    params?: {
      /** The additional flags parameter with the value 'exactMatch' will search for contacts with the exact value of the email and name provided in the query string. Without this flag, matching is done via a standard 'like' comparison, which may sometimes be slow. */
      additionalFlags?: string;
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
      /** Page number */
      page?: number;
      /** Requested number of results per page */
      perPage?: number;
      /** Search contacts by campaign ID */
      queryCampaignId?: string;
      /** Return only contacts whose data was changed on or after the given date. Use ISO 8601 format */
      queryChangedOnFrom?: string;
      /** Return only contacts whose data was changed on or before the given date. Use ISO 8601 format */
      queryChangedOnTo?: string;
      /** Return only contacts created on or after the given date. Use ISO 8601 format */
      queryCreatedOnFrom?: string;
      /** Return only contacts created on or before the given date. Use ISO 8601 format */
      queryCreatedOnTo?: string;
      /** Search contacts by email */
      queryEmail?: string;
      /** Search contacts by name */
      queryName?: string;
      /** Search contacts by origin */
      queryOrigin?: M.GetContactListQueryOrigin;
      /** Sort by campaign ID */
      sortCampaignId?: M.SortOrderEnum;
      /** Sort by change date */
      sortChangedOn?: M.SortOrderEnum;
      /** Sort contacts by subscription date */
      sortCreatedOn?: M.SortOrderEnum;
      /** Sort by email */
      sortEmail?: M.SortOrderEnum;
      /** Sort by name */
      sortName?: M.SortOrderEnum;
    },
    signal?: AbortSignal,
  ): Promise<M.ContactListElement[]> => {
    return this.core.request<M.ContactListElement[]>('GET', '/contacts', {
      query: params
        ? {
            'query[email]': params.queryEmail,
            'query[name]': params.queryName,
            'query[campaignId]': params.queryCampaignId,
            'query[origin]': params.queryOrigin,
            'query[createdOn][from]': params.queryCreatedOnFrom,
            'query[createdOn][to]': params.queryCreatedOnTo,
            'query[changedOn][from]': params.queryChangedOnFrom,
            'query[changedOn][to]': params.queryChangedOnTo,
            'sort[email]': params.sortEmail,
            'sort[name]': params.sortName,
            'sort[createdOn]': params.sortCreatedOn,
            'sort[changedOn]': params.sortChangedOn,
            'sort[campaignId]': params.sortCampaignId,
            additionalFlags: params.additionalFlags,
            fields: params.fields,
            perPage: params.perPage,
            page: params.page,
          }
        : undefined,
      signal,
    });
  };

  /** Provides all contacts from a single campaign. You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by. */
  readonly getContactsFromCampaign = async (
    campaignId: string,
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
      /** Page number */
      page?: number;
      /** Requested number of results per page */
      perPage?: number;
      /** Return only contacts created on or after the given date. Use ISO 8601 format */
      queryCreatedOnFrom?: string;
      /** Return only contacts created on or before the given date. Use ISO 8601 format */
      queryCreatedOnTo?: string;
      /** Search contacts by email */
      queryEmail?: string;
      /** Search contacts by name */
      queryName?: string;
      /** Sort contacts by creation date */
      sortCreatedOn?: M.SortOrderEnum;
      /** Sort contacts by email */
      sortEmail?: M.SortOrderEnum;
      /** Sort contacts by name */
      sortName?: M.SortOrderEnum;
    },
    signal?: AbortSignal,
  ): Promise<M.ContactListElement[]> => {
    return this.core.request<M.ContactListElement[]>('GET', '/campaigns/{campaignId}/contacts', {
      pathParams: { campaignId: campaignId },
      query: params
        ? {
            'query[email]': params.queryEmail,
            'query[name]': params.queryName,
            'query[createdOn][from]': params.queryCreatedOnFrom,
            'query[createdOn][to]': params.queryCreatedOnTo,
            'sort[email]': params.sortEmail,
            'sort[name]': params.sortName,
            'sort[createdOn]': params.sortCreatedOn,
            fields: params.fields,
            perPage: params.perPage,
            page: params.page,
          }
        : undefined,
      signal,
    });
  };

  /** Skip the fields you don't want to update. If tags and custom fields are provided, they'll be **replaced** with the values sent in this request. If the `campaignId` changes, the contact will be moved from the original campaign (list) to the new campaign (list). Their activity history and statistics will also be moved. */
  readonly updateContact = async (
    contactId: string,
    body: M.UpdateContact,
    signal?: AbortSignal,
  ): Promise<M.ContactDetails> => {
    return this.core.request<M.ContactDetails>('POST', '/contacts/{contactId}', {
      pathParams: { contactId: contactId },
      body,
      signal,
    });
  };

  /** Upsert (add or update) the custom fields of a contact. This method doesn't remove (unassign) custom fields. */
  readonly upsertContactCustoms = async (
    contactId: string,
    body: M.UpsertContactCustomFields,
    signal?: AbortSignal,
  ): Promise<M.ContactCustomField[]> => {
    return this.core.request<M.ContactCustomField[]>(
      'POST',
      '/contacts/{contactId}/custom-fields',
      {
        pathParams: { contactId: contactId },
        body,
        signal,
      },
    );
  };

  /** Upsert (add or update) the tags of a contact. This method doesn't remove (unassign) tags. */
  readonly upsertTags = async (
    contactId: string,
    body: M.UpsertContactTags,
    signal?: AbortSignal,
  ): Promise<Record<string, unknown>[]> => {
    return this.core.request<Record<string, unknown>[]>('POST', '/contacts/{contactId}/tags', {
      pathParams: { contactId: contactId },
      body,
      signal,
    });
  };
}
