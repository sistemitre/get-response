/** Operations tagged 'A/B tests' in the GetResponse API. */

import type { Core } from '../core.js';
import type * as M from '../models.js';

export class AbTestsResource {
  constructor(private readonly core: Core) {}

  /** Get a single A/B test by ID. */
  readonly getSplittest = async (
    splittestId: string,
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
    },
    signal?: AbortSignal,
  ): Promise<M.Splittest> => {
    return this.core.request<M.Splittest>('GET', '/splittests/{splittestId}', {
      pathParams: { splittestId: splittestId },
      query: params ? { fields: params.fields } : undefined,
      signal,
    });
  };

  /** The list of A/B tests. You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by. */
  readonly getSplittestList = async (
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
      /** Page number */
      page?: number;
      /** Requested number of results per page */
      perPage?: number;
      /** Search A/B tests created from this date */
      queryCreatedOnFrom?: Record<string, unknown>;
      /** Search A/B tests created to this date */
      queryCreatedOnTo?: Record<string, unknown>;
      /** Search A/B tests by name */
      queryName?: string;
      /** Search A/B tests by status */
      queryStatus?: M.GetSplittestListQueryStatus;
      /** Search A/B tests by type */
      queryType?: string;
      /** Sort by creation date */
      sortCreatedOn?: M.SortOrderEnum;
      /** Sort by name */
      sortName?: M.SortOrderEnum;
    },
    signal?: AbortSignal,
  ): Promise<M.Splittest[]> => {
    return this.core.request<M.Splittest[]>('GET', '/splittests', {
      query: params
        ? {
            'query[name]': params.queryName,
            'query[type]': params.queryType,
            'query[status]': params.queryStatus,
            'query[createdOn][from]': params.queryCreatedOnFrom,
            'query[createdOn][to]': params.queryCreatedOnTo,
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
}
