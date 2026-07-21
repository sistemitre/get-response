/** Operations tagged 'Landing Pages' in the GetResponse API. */

import type { Core } from '../core.js';
import type * as M from '../models.js';

export class LandingPagesResource {
  constructor(private readonly core: Core) {}

  /** Get a single landing page by ID */
  readonly getLpsById = async (
    lpsId: string,
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
    },
    signal?: AbortSignal,
  ): Promise<M.LpsDetails> => {
    return this.core.request<M.LpsDetails>('GET', '/lps/{lpsId}', {
      pathParams: { lpsId: lpsId },
      query: params ? { fields: params.fields } : undefined,
      signal,
    });
  };

  /** You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by. */
  readonly getLpsList = async (
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
      /** Page number */
      page?: number;
      /** Requested number of results per page */
      perPage?: number;
      /** Search landing pages by name */
      queryName?: string;
      /** Search landing pages by status */
      queryStatus?: M.GetLpsListQueryStatus;
      /** Sort landing pages by creation date */
      sortCreatedAt?: M.SortOrderEnum;
      /** Sort landing pages by number of leads */
      sortLeads?: M.SortOrderEnum;
      /** Sort landing pages by name */
      sortName?: M.SortOrderEnum;
      /** Sort by subscription rate */
      sortSubscriptionRate?: M.SortOrderEnum;
      /** Sort landing pages by modification date */
      sortUpdatedAt?: M.SortOrderEnum;
      /** Sort by number of page visits */
      sortVisits?: M.SortOrderEnum;
      /** Show statistics for landing pages from this date */
      statsFrom?: string;
      /** Show statistics for landing pages to this date */
      statsTo?: string;
    },
    signal?: AbortSignal,
  ): Promise<M.Lps[]> => {
    return this.core.request<M.Lps[]>('GET', '/lps', {
      query: params
        ? {
            'query[name]': params.queryName,
            'query[status]': params.queryStatus,
            'stats[from]': params.statsFrom,
            'stats[to]': params.statsTo,
            'sort[name]': params.sortName,
            'sort[createdAt]': params.sortCreatedAt,
            'sort[updatedAt]': params.sortUpdatedAt,
            'sort[visits]': params.sortVisits,
            'sort[leads]': params.sortLeads,
            'sort[subscriptionRate]': params.sortSubscriptionRate,
            fields: params.fields,
            perPage: params.perPage,
            page: params.page,
          }
        : undefined,
      signal,
    });
  };
}
