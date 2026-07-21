/** Operations tagged 'Predefined Fields' in the GetResponse API. */

import type { Core } from '../core.js';
import type * as M from '../models.js';

export class PredefinedFieldsResource {
  constructor(private readonly core: Core) {}

  /** Makes it possible to create a new predefined field. */
  readonly createPredefinedField = async (
    body: M.NewPredefinedField,
    signal?: AbortSignal,
  ): Promise<M.PredefinedField> => {
    return this.core.request<M.PredefinedField>('POST', '/predefined-fields', {
      body,
      signal,
    });
  };

  /** Delete a predefined field */
  readonly deletePredefinedField = async (
    predefinedFieldId: string,
    signal?: AbortSignal,
  ): Promise<void> => {
    return this.core.request<void>('DELETE', '/predefined-fields/{predefinedFieldId}', {
      pathParams: { predefinedFieldId: predefinedFieldId },
      signal,
    });
  };

  /** Get detailed information about a specified predefined field. */
  readonly getPredefinedFieldById = async (
    predefinedFieldId: string,
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
    },
    signal?: AbortSignal,
  ): Promise<M.PredefinedField> => {
    return this.core.request<M.PredefinedField>('GET', '/predefined-fields/{predefinedFieldId}', {
      pathParams: { predefinedFieldId: predefinedFieldId },
      query: params ? { fields: params.fields } : undefined,
      signal,
    });
  };

  /** You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by. */
  readonly getPredefinedFieldList = async (
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
      /** Page number */
      page?: number;
      /** Requested number of results per page */
      perPage?: number;
      /** Search by campaign ID */
      queryCampaignId?: string;
      /** Search by name */
      queryName?: string;
      /** Sort by name */
      sortName?: M.SortOrderEnum;
    },
    signal?: AbortSignal,
  ): Promise<M.PredefinedField[]> => {
    return this.core.request<M.PredefinedField[]>('GET', '/predefined-fields', {
      query: params
        ? {
            'sort[name]': params.sortName,
            'query[name]': params.queryName,
            'query[campaignId]': params.queryCampaignId,
            fields: params.fields,
            perPage: params.perPage,
            page: params.page,
          }
        : undefined,
      signal,
    });
  };

  /** Update a predefined field */
  readonly updatePredefinedField = async (
    predefinedFieldId: string,
    body: M.UpdatePredefinedField,
    signal?: AbortSignal,
  ): Promise<M.PredefinedField> => {
    return this.core.request<M.PredefinedField>('POST', '/predefined-fields/{predefinedFieldId}', {
      pathParams: { predefinedFieldId: predefinedFieldId },
      body,
      signal,
    });
  };
}
