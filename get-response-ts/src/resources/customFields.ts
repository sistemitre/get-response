/** Operations tagged 'Custom Fields' in the GetResponse API. */

import type { Core } from '../core.js';
import type * as M from '../models.js';

export class CustomFieldsResource {
  constructor(private readonly core: Core) {}

  /** Create a custom field */
  readonly createCustomField = async (
    body: M.NewCustomField,
    signal?: AbortSignal,
  ): Promise<M.CustomFieldResponse> => {
    return this.core.request<M.CustomFieldResponse>('POST', '/custom-fields', {
      body,
      signal,
    });
  };

  /** Delete a single custom field definition */
  readonly deleteCustomField = async (
    customFieldId: string,
    signal?: AbortSignal,
  ): Promise<void> => {
    return this.core.request<void>('DELETE', '/custom-fields/{customFieldId}', {
      pathParams: { customFieldId: customFieldId },
      signal,
    });
  };

  /** Returns a list of custom fields */
  readonly getCustomFieldById = async (
    customFieldId: string,
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
    },
    signal?: AbortSignal,
  ): Promise<M.CustomFieldResponse> => {
    return this.core.request<M.CustomFieldResponse>('GET', '/custom-fields/{customFieldId}', {
      pathParams: { customFieldId: customFieldId },
      query: params ? { fields: params.fields } : undefined,
      signal,
    });
  };

  /** You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by. */
  readonly getCustomFieldList = async (
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
      /** Page number */
      page?: number;
      /** Requested number of results per page */
      perPage?: number;
      /** Search custom fields by name */
      queryName?: string;
      /** Sort by name */
      sortName?: M.SortOrderEnum;
    },
    signal?: AbortSignal,
  ): Promise<M.CustomField[]> => {
    return this.core.request<M.CustomField[]>('GET', '/custom-fields', {
      query: params
        ? {
            'query[name]': params.queryName,
            'sort[name]': params.sortName,
            fields: params.fields,
            perPage: params.perPage,
            page: params.page,
          }
        : undefined,
      signal,
    });
  };

  /** Update the custom field definition */
  readonly updateCustomField = async (
    customFieldId: string,
    body: M.UpdateCustomField,
    signal?: AbortSignal,
  ): Promise<M.CustomFieldResponse> => {
    return this.core.request<M.CustomFieldResponse>('POST', '/custom-fields/{customFieldId}', {
      pathParams: { customFieldId: customFieldId },
      body,
      signal,
    });
  };
}
