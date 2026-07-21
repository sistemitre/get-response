/** Operations tagged 'Search Contacts' in the GetResponse API. */

import type { Core } from '../core.js';
import type * as M from '../models.js';

export class SearchContactsResource {
  constructor(private readonly core: Core) {}

  /** Delete search contacts */
  readonly deleteSearchContacts = async (
    searchContactId: string,
    signal?: AbortSignal,
  ): Promise<void> => {
    return this.core.request<void>('DELETE', '/search-contacts/{searchContactId}', {
      pathParams: { searchContactId: searchContactId },
      signal,
    });
  };

  /** Get contacts from saved search contacts by ID. */
  readonly getContactsByIdSearchContacts = async (
    searchContactId: string,
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
      /** Page number */
      page?: number;
      /** Requested number of results per page */
      perPage?: number;
      /** Sort by creation date */
      sortCreatedOn?: M.SortOrderEnum;
      /** Sort by email */
      sortEmail?: M.SortOrderEnum;
      /** Sort by name */
      sortName?: M.SortOrderEnum;
    },
    signal?: AbortSignal,
  ): Promise<M.SearchedContactDetails[]> => {
    return this.core.request<M.SearchedContactDetails[]>(
      'GET',
      '/search-contacts/{searchContactId}/contacts',
      {
        pathParams: { searchContactId: searchContactId },
        query: params
          ? {
              'sort[name]': params.sortName,
              'sort[email]': params.sortEmail,
              'sort[createdOn]': params.sortCreatedOn,
              fields: params.fields,
              perPage: params.perPage,
              page: params.page,
            }
          : undefined,
        signal,
      },
    );
  };

  /** Makes it possible to get a collection of contacts according to a given condition. Please refer to [Segments (search contacts) reference manual](https://apidocs.getresponse.com/v3/case-study/segments-manual) */
  readonly getContactsFromSearchContactsConditions = async (
    body: M.SearchContactsBySearchForm,
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
      /** Page number */
      page?: number;
      /** Requested number of results per page */
      perPage?: number;
      /** Sort by creation date */
      sortCreatedOn?: M.SortOrderEnum;
      /** Sort by email */
      sortEmail?: M.SortOrderEnum;
      /** Sort by name */
      sortName?: M.SortOrderEnum;
    },
    signal?: AbortSignal,
  ): Promise<M.SearchedContactDetails[]> => {
    return this.core.request<M.SearchedContactDetails[]>('POST', '/search-contacts/contacts', {
      query: params
        ? {
            'sort[name]': params.sortName,
            'sort[email]': params.sortEmail,
            'sort[createdOn]': params.sortCreatedOn,
            fields: params.fields,
            perPage: params.perPage,
            page: params.page,
          }
        : undefined,
      body,
      signal,
    });
  };

  /** Get the definition of a specific contact-search filter. */
  readonly getSearchContactsById = async (
    searchContactId: string,
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
    },
    signal?: AbortSignal,
  ): Promise<M.SearchContactsDetails> => {
    return this.core.request<M.SearchContactsDetails>('GET', '/search-contacts/{searchContactId}', {
      pathParams: { searchContactId: searchContactId },
      query: params ? { fields: params.fields } : undefined,
      signal,
    });
  };

  /** Makes it possible to retrieve a collection of short representations of search-contact (known as custom filters in the panel). Every item represents a basic filter object. You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by. */
  readonly getSearchContactsList = async (
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
      /** Page number */
      page?: number;
      /** Requested number of results per page */
      perPage?: number;
      /** Count data from this date */
      queryCreatedOnFrom?: Record<string, unknown>;
      /** Count data to this date */
      queryCreatedOnTo?: Record<string, unknown>;
      /** Search by name */
      queryName?: string;
      /** Sort by creation date */
      sortCreatedOn?: M.SortOrderEnum;
      /** Sort by name */
      sortName?: M.SortOrderEnum;
    },
    signal?: AbortSignal,
  ): Promise<M.BaseSearchContactsDetails[]> => {
    return this.core.request<M.BaseSearchContactsDetails[]>('GET', '/search-contacts', {
      query: params
        ? {
            'sort[name]': params.sortName,
            'sort[createdOn]': params.sortCreatedOn,
            'query[name]': params.queryName,
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

  /** Makes it possible to create a new search-contact. Please refer to [Segments (search contacts) reference manual](https://apidocs.getresponse.com/v3/case-study/segments-manual) */
  readonly newSearchContacts = async (
    body: M.NewSearchContacts,
    signal?: AbortSignal,
  ): Promise<M.SearchContactsDetails> => {
    return this.core.request<M.SearchContactsDetails>('POST', '/search-contacts', {
      body,
      signal,
    });
  };

  /** Update specified search contacts. */
  readonly updateSearchContacts = async (
    searchContactId: string,
    body: M.UpdateSearchContacts,
    signal?: AbortSignal,
  ): Promise<M.SearchContactsDetails> => {
    return this.core.request<M.SearchContactsDetails>(
      'POST',
      '/search-contacts/{searchContactId}',
      {
        pathParams: { searchContactId: searchContactId },
        body,
        signal,
      },
    );
  };

  /** Makes it possible to add and update custom field values for all contacts that meet the search criteria. This method doesn't remove or overwrite custom fields with the values from the request. */
  readonly upsertCustomFieldsBySearchContactId = async (
    searchContactId: string,
    body: M.UpsertContactCustomFields,
    signal?: AbortSignal,
  ): Promise<void> => {
    return this.core.request<void>('POST', '/search-contacts/{searchContactId}/custom-fields', {
      pathParams: { searchContactId: searchContactId },
      body,
      signal,
    });
  };
}
