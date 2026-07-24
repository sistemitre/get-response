/** Operations tagged 'RSS Newsletters' in the GetResponse API. */

import type { Core } from '../core.js';
import type * as M from '../models.js';

export class RssNewslettersResource {
  constructor(private readonly core: Core) {}

  /** Create RSS newsletter */
  readonly createRssNewsletter = async (
    body: M.NewRssNewsletter,
    signal?: AbortSignal,
  ): Promise<M.RssNewsletterDetails> => {
    return this.core.request<M.RssNewsletterDetails>('POST', '/rss-newsletters', {
      body,
      signal,
    });
  };

  /** Delete RSS newsletter */
  readonly deleteRssNewsletter = async (
    rssNewsletterId: string,
    signal?: AbortSignal,
  ): Promise<void> => {
    return this.core.request<void>('DELETE', '/rss-newsletters/{rssNewsletterId}', {
      pathParams: { rssNewsletterId: rssNewsletterId },
      signal,
    });
  };

  /** Get RSS newsletter by ID */
  readonly getRssNewsletterById = async (
    rssNewsletterId: string,
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
    },
    signal?: AbortSignal,
  ): Promise<M.RssNewsletterDetails> => {
    return this.core.request<M.RssNewsletterDetails>('GET', '/rss-newsletters/{rssNewsletterId}', {
      pathParams: { rssNewsletterId: rssNewsletterId },
      query: params ? { fields: params.fields } : undefined,
      signal,
    });
  };

  /** You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by. */
  readonly getRssNewsletterStatisticsCollection = async (
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
      /** Page number */
      page?: number;
      /** Requested number of results per page */
      perPage?: number;
      /** The list of campaign resource IDs (string separated with ',') */
      queryCampaignId?: string;
      /** Count data from this date (GetResponse date format: yyyy-MM-ddTHH:mm:ss+HHMM, e.g. 2024-01-15T10:30:00+0000 -- no colon in the offset, no sub-second precision (unlike Date.prototype.toISOString())) */
      queryCreatedOnFrom?: string;
      /** Count data to this date (GetResponse date format: yyyy-MM-ddTHH:mm:ss+HHMM, e.g. 2024-01-15T10:30:00+0000 -- no colon in the offset, no sub-second precision (unlike Date.prototype.toISOString())) */
      queryCreatedOnTo?: string;
      /** Group results by time interval */
      queryGroupBy?: M.GetRssNewsletterStatisticsCollectionQueryGroupBy;
      /** The list of RSS newsletter resource IDs (string separated with ',') */
      queryRssNewsletterId?: string;
    },
    signal?: AbortSignal,
  ): Promise<M.MessageStatisticsListElement[]> => {
    return this.core.request<M.MessageStatisticsListElement[]>(
      'GET',
      '/rss-newsletters/statistics',
      {
        query: params
          ? {
              'query[groupBy]': params.queryGroupBy,
              'query[rssNewsletterId]': params.queryRssNewsletterId,
              'query[campaignId]': params.queryCampaignId,
              'query[createdOn][from]': params.queryCreatedOnFrom,
              'query[createdOn][to]': params.queryCreatedOnTo,
              fields: params.fields,
              perPage: params.perPage,
              page: params.page,
            }
          : undefined,
        signal,
      },
    );
  };

  /** You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by. */
  readonly getRssNewslettersList = async (
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
      /** Page number */
      page?: number;
      /** Requested number of results per page */
      perPage?: number;
      /** Search RSS newsletters by campaign ID */
      queryCampaignId?: string;
      /** Search RSS newsletters created from this date (GetResponse date format: yyyy-MM-ddTHH:mm:ss+HHMM, e.g. 2024-01-15T10:30:00+0000 -- no colon in the offset, no sub-second precision (unlike Date.prototype.toISOString())) */
      queryCreatedOnFrom?: string;
      /** Search RSS newsletters created to this date (GetResponse date format: yyyy-MM-ddTHH:mm:ss+HHMM, e.g. 2024-01-15T10:30:00+0000 -- no colon in the offset, no sub-second precision (unlike Date.prototype.toISOString())) */
      queryCreatedOnTo?: string;
      /** Search RSS newsletters by status */
      queryStatus?: M.GetRssNewslettersListQueryStatus;
      /** Search RSS newsletters by subject */
      querySubject?: string;
      /** Sort by date */
      sortCreatedOn?: M.SortOrderEnum;
    },
    signal?: AbortSignal,
  ): Promise<M.RssNewsletterListItem[]> => {
    return this.core.request<M.RssNewsletterListItem[]>('GET', '/rss-newsletters', {
      query: params
        ? {
            'query[subject]': params.querySubject,
            'query[status]': params.queryStatus,
            'query[createdOn][from]': params.queryCreatedOnFrom,
            'query[createdOn][to]': params.queryCreatedOnTo,
            'query[campaignId]': params.queryCampaignId,
            'sort[createdOn]': params.sortCreatedOn,
            fields: params.fields,
            perPage: params.perPage,
            page: params.page,
          }
        : undefined,
      signal,
    });
  };

  /** You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by. */
  readonly getSingleRssNewsletterStatisticsCollection = async (
    rssNewsletterId: string,
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
      /** Page number */
      page?: number;
      /** Requested number of results per page */
      perPage?: number;
      /** Count data from this date (GetResponse date format: yyyy-MM-ddTHH:mm:ss+HHMM, e.g. 2024-01-15T10:30:00+0000 -- no colon in the offset, no sub-second precision (unlike Date.prototype.toISOString())) */
      queryCreatedOnFrom?: string;
      /** Count data to this date (GetResponse date format: yyyy-MM-ddTHH:mm:ss+HHMM, e.g. 2024-01-15T10:30:00+0000 -- no colon in the offset, no sub-second precision (unlike Date.prototype.toISOString())) */
      queryCreatedOnTo?: string;
      /** Group results by time interval */
      queryGroupBy?: M.GetSingleRssNewsletterStatisticsCollectionQueryGroupBy;
    },
    signal?: AbortSignal,
  ): Promise<M.MessageStatisticsListElement[]> => {
    return this.core.request<M.MessageStatisticsListElement[]>(
      'GET',
      '/rss-newsletters/{rssNewsletterId}/statistics',
      {
        pathParams: { rssNewsletterId: rssNewsletterId },
        query: params
          ? {
              'query[groupBy]': params.queryGroupBy,
              'query[createdOn][from]': params.queryCreatedOnFrom,
              'query[createdOn][to]': params.queryCreatedOnTo,
              fields: params.fields,
              perPage: params.perPage,
              page: params.page,
            }
          : undefined,
        signal,
      },
    );
  };

  /** Update RSS newsletter */
  readonly updateRssNewsletter = async (
    rssNewsletterId: string,
    body: M.UpdateRssNewsletter,
    signal?: AbortSignal,
  ): Promise<M.RssNewsletterDetails> => {
    return this.core.request<M.RssNewsletterDetails>('POST', '/rss-newsletters/{rssNewsletterId}', {
      pathParams: { rssNewsletterId: rssNewsletterId },
      body,
      signal,
    });
  };
}
