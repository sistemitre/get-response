/** Operations tagged 'Websites' in the GetResponse API. */

import type { Core } from '../core.js';
import type * as M from '../models.js';

export class WebsitesResource {
  constructor(private readonly core: Core) {}

  /** Get a single Website by ID */
  readonly getWebsiteById = async (
    websiteId: string,
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
    },
    signal?: AbortSignal,
  ): Promise<M.WebsiteDetails> => {
    return this.core.request<M.WebsiteDetails>('GET', '/websites/{websiteId}', {
      pathParams: { websiteId: websiteId },
      query: params ? { fields: params.fields } : undefined,
      signal,
    });
  };

  /** You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by. */
  readonly getWebsitesList = async (
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
      /** Page number */
      page?: number;
      /** Requested number of results per page */
      perPage?: number;
      /** Search websites by name */
      queryName?: string;
      /** Search websites by status */
      queryStatus?: M.GetWebsitesListQueryStatus;
      /** Sort websites by creation date */
      sortCreatedAt?: M.SortOrderEnum;
      /** Sort websites by name */
      sortName?: M.SortOrderEnum;
      /** Sort websites by page views */
      sortPageViews?: M.SortOrderEnum;
      /** Sort by number of unique visitors */
      sortUniqueVisitors?: M.SortOrderEnum;
      /** Sort websites by modification date */
      sortUpdatedAt?: M.SortOrderEnum;
      /** Sort by number of site visits */
      sortVisits?: M.SortOrderEnum;
      /** Show statistics for websites from this date */
      statsFrom?: string;
      /** Show statistics for websites to this date */
      statsTo?: string;
    },
    signal?: AbortSignal,
  ): Promise<M.Website[]> => {
    return this.core.request<M.Website[]>('GET', '/websites', {
      query: params
        ? {
            'query[name]': params.queryName,
            'query[status]': params.queryStatus,
            'stats[from]': params.statsFrom,
            'stats[to]': params.statsTo,
            'sort[name]': params.sortName,
            'sort[createdAt]': params.sortCreatedAt,
            'sort[updatedAt]': params.sortUpdatedAt,
            'sort[pageViews]': params.sortPageViews,
            'sort[visits]': params.sortVisits,
            'sort[uniqueVisitors]': params.sortUniqueVisitors,
            fields: params.fields,
            perPage: params.perPage,
            page: params.page,
          }
        : undefined,
      signal,
    });
  };
}
