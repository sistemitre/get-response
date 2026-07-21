/** Operations tagged 'Legacy Forms' in the GetResponse API. */

import type { Core } from '../core.js';
import type * as M from '../models.js';

export class LegacyFormsResource {
  constructor(private readonly core: Core) {}

  /** Get Legacy Form by ID. */
  readonly getLegacyFormById = async (
    webformId: string,
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
    },
    signal?: AbortSignal,
  ): Promise<M.LegacyForm> => {
    return this.core.request<M.LegacyForm>('GET', '/webforms/{webformId}', {
      pathParams: { webformId: webformId },
      query: params ? { fields: params.fields } : undefined,
      signal,
    });
  };

  /** Get the list of Legacy Forms. You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by. */
  readonly getLegacyFormList = async (
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
      /** Page number */
      page?: number;
      /** Requested number of results per page */
      perPage?: number;
      /** Search Legacy Forms by campaignId. Accepts multiple IDs separated with a comma */
      queryCampaignId?: string;
      /** Search Legacy Forms modified from this date */
      queryModifiedOnFrom?: string;
      /** Search Legacy Forms modified to this date */
      queryModifiedOnTo?: string;
      /** Search Legacy Forms by name */
      queryName?: string;
      /** Sort Legacy Forms by modification date */
      sortModifiedOn?: M.SortOrderEnum;
    },
    signal?: AbortSignal,
  ): Promise<M.LegacyForm[]> => {
    return this.core.request<M.LegacyForm[]>('GET', '/webforms', {
      query: params
        ? {
            'query[name]': params.queryName,
            'query[modifiedOn][from]': params.queryModifiedOnFrom,
            'query[modifiedOn][to]': params.queryModifiedOnTo,
            'query[campaignId]': params.queryCampaignId,
            'sort[modifiedOn]': params.sortModifiedOn,
            fields: params.fields,
            perPage: params.perPage,
            page: params.page,
          }
        : undefined,
      signal,
    });
  };
}
