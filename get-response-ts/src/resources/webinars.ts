/** Operations tagged 'Webinars' in the GetResponse API. */

import type { Core } from '../core.js';
import type * as M from '../models.js';

export class WebinarsResource {
  constructor(private readonly core: Core) {}

  /** Get a webinar by ID */
  readonly getWebinarById = async (
    webinarId: string,
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
    },
    signal?: AbortSignal,
  ): Promise<M.Webinar> => {
    return this.core.request<M.Webinar>('GET', '/webinars/{webinarId}', {
      pathParams: { webinarId: webinarId },
      query: params ? { fields: params.fields } : undefined,
      signal,
    });
  };

  /** You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by. */
  readonly getWebinarList = async (
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
      /** Page number */
      page?: number;
      /** Requested number of results per page */
      perPage?: number;
      /** The list of campaign resource IDs (string separated with ',') */
      queryCampaignId?: string;
      /** Search webinars by name */
      queryName?: string;
      /** Search webinars by status */
      queryStatus?: M.GetWebinarListQueryStatus;
      /** Search webinars by type */
      queryType?: M.GetWebinarListQueryType;
      /** Sort webinars by creation date */
      sortCreatedOn?: M.SortOrderEnum;
      /** Sort webinars by name */
      sortName?: M.SortOrderEnum;
      /** Sort webinars by update date */
      sortStartsOn?: M.SortOrderEnum;
    },
    signal?: AbortSignal,
  ): Promise<M.Webinar[]> => {
    return this.core.request<M.Webinar[]>('GET', '/webinars', {
      query: params
        ? {
            'query[name]': params.queryName,
            'query[campaignId]': params.queryCampaignId,
            'query[status]': params.queryStatus,
            'sort[name]': params.sortName,
            'sort[createdOn]': params.sortCreatedOn,
            'sort[startsOn]': params.sortStartsOn,
            'query[type]': params.queryType,
            fields: params.fields,
            perPage: params.perPage,
            page: params.page,
          }
        : undefined,
      signal,
    });
  };
}
