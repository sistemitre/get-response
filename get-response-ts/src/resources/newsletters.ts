/** Operations tagged 'Newsletters' in the GetResponse API. */

import type { Core } from '../core.js';
import type * as M from '../models.js';

export class NewslettersResource {
  constructor(private readonly core: Core) {}

  /** > Using this method, you can cancel the sending of the newsletter. It will also turn the newsletter into a **draft**. */
  readonly cancelMessageSend = async (
    newsletterId: string,
    signal?: AbortSignal,
  ): Promise<M.NewsletterDetails> => {
    return this.core.request<M.NewsletterDetails>('POST', '/newsletters/{newsletterId}/cancel', {
      pathParams: { newsletterId: newsletterId },
      signal,
    });
  };

  /** > This method creates a new newsletter and puts it in a queue to send. **NOTE: This method has a limit of 256 calls per day.** */
  readonly createNewsletter = async (
    body: M.NewNewsletter,
    signal?: AbortSignal,
  ): Promise<M.NewsletterDetails> => {
    return this.core.request<M.NewsletterDetails>('POST', '/newsletters', {
      body,
      signal,
    });
  };

  /** Delete newsletter */
  readonly deleteNewsletter = async (newsletterId: string, signal?: AbortSignal): Promise<void> => {
    return this.core.request<void>('DELETE', '/newsletters/{newsletterId}', {
      pathParams: { newsletterId: newsletterId },
      signal,
    });
  };

  /** Get a single newsletter by its ID. */
  readonly getNewsletter = async (
    newsletterId: string,
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
    },
    signal?: AbortSignal,
  ): Promise<M.NewsletterDetails> => {
    return this.core.request<M.NewsletterDetails>('GET', '/newsletters/{newsletterId}', {
      pathParams: { newsletterId: newsletterId },
      query: params ? { fields: params.fields } : undefined,
      signal,
    });
  };

  /** **DEPRECATED**: This method is deprecated and scheduled for removal. To synchronise newsletter activities please use [custom reports](https://apireference.getresponse.com/#operation/createCustomReport) with type `message_activity_reports`. This is the preferred approach due to better performance. By default, activities from the **last 14 days** are listed only. You can get activities for last 30 days only. You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by. */
  readonly getNewsletterActivities = async (
    newsletterId: string,
    params?: {
      /** Page number */
      page?: number;
      /** Requested number of results per page */
      perPage?: number;
      /** Search newsletter activities by activity type */
      queryActivity?: M.GetNewsletterActivitiesQueryActivity;
      /** Search newsletter activities from this date. Default value is 14 days earlier. You can get activities for last 30 days only. (GetResponse date format: yyyy-MM-ddTHH:mm:ss+HHMM, e.g. 2024-01-15T10:30:00+0000 -- no colon in the offset, no sub-second precision (unlike Date.prototype.toISOString())) */
      queryCreatedOnFrom?: string;
      /** Search newsletter activities to this date. Default value is now (GetResponse date format: yyyy-MM-ddTHH:mm:ss+HHMM, e.g. 2024-01-15T10:30:00+0000 -- no colon in the offset, no sub-second precision (unlike Date.prototype.toISOString())) */
      queryCreatedOnTo?: string;
      /** Sort by date */
      sortCreatedOn?: M.SortOrderEnum;
    },
    signal?: AbortSignal,
  ): Promise<M.NewsletterActivity[]> => {
    return this.core.request<M.NewsletterActivity[]>(
      'GET',
      '/newsletters/{newsletterId}/activities',
      {
        pathParams: { newsletterId: newsletterId },
        query: params
          ? {
              'query[activity]': params.queryActivity,
              'query[createdOn][from]': params.queryCreatedOnFrom,
              'query[createdOn][to]': params.queryCreatedOnTo,
              'sort[createdOn]': params.sortCreatedOn,
              perPage: params.perPage,
              page: params.page,
            }
          : undefined,
        signal,
      },
    );
  };

  /** You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by. */
  readonly getNewsletterList = async (
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
      /** Page number */
      page?: number;
      /** Requested number of results per page */
      perPage?: number;
      /** Search newsletters by campaign ID */
      queryCampaignId?: string;
      /** Search newsletters created from this date (GetResponse date format: yyyy-MM-ddTHH:mm:ss+HHMM, e.g. 2024-01-15T10:30:00+0000 -- no colon in the offset, no sub-second precision (unlike Date.prototype.toISOString())) */
      queryCreatedOnFrom?: string;
      /** Search newsletters created to this date (GetResponse date format: yyyy-MM-ddTHH:mm:ss+HHMM, e.g. 2024-01-15T10:30:00+0000 -- no colon in the offset, no sub-second precision (unlike Date.prototype.toISOString())) */
      queryCreatedOnTo?: string;
      /** Search newsletters by name */
      queryName?: string;
      /** Search for newsletters sent from this date (GetResponse date format: yyyy-MM-ddTHH:mm:ss+HHMM, e.g. 2024-01-15T10:30:00+0000 -- no colon in the offset, no sub-second precision (unlike Date.prototype.toISOString())) */
      querySendOnFrom?: string;
      /** Search for newsletters sent to this date (GetResponse date format: yyyy-MM-ddTHH:mm:ss+HHMM, e.g. 2024-01-15T10:30:00+0000 -- no colon in the offset, no sub-second precision (unlike Date.prototype.toISOString())) */
      querySendOnTo?: string;
      /** Search newsletters by status */
      queryStatus?: M.GetNewsletterListQueryStatus;
      /** Search newsletters by subject */
      querySubject?: string;
      /** Search newsletters by type */
      queryType?: M.GetNewsletterListQueryType;
      /** Sort by date */
      sortCreatedOn?: M.SortOrderEnum;
      /** Sort by send on date */
      sortSendOn?: M.SortOrderEnum;
    },
    signal?: AbortSignal,
  ): Promise<M.NewsletterListElement[]> => {
    return this.core.request<M.NewsletterListElement[]>('GET', '/newsletters', {
      query: params
        ? {
            'query[subject]': params.querySubject,
            'query[name]': params.queryName,
            'query[status]': params.queryStatus,
            'query[createdOn][from]': params.queryCreatedOnFrom,
            'query[createdOn][to]': params.queryCreatedOnTo,
            'query[sendOn][from]': params.querySendOnFrom,
            'query[sendOn][to]': params.querySendOnTo,
            'query[type]': params.queryType,
            'query[campaignId]': params.queryCampaignId,
            'sort[createdOn]': params.sortCreatedOn,
            'sort[sendOn]': params.sortSendOn,
            fields: params.fields,
            perPage: params.perPage,
            page: params.page,
          }
        : undefined,
      signal,
    });
  };

  /** >This makes it possible to fetch newsletter statistics based on the list of campaign or newsletter IDs (you can pass them in the query parameter - see the description below). Remember that all the statistics date ranges are returned in standard UTC period type objects. ([See ISO 8601 standard](http://en.wikipedia.org/wiki/ISO_8601#Time_intervals)). You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by. */
  readonly getNewsletterStatisticsCollection = async (
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
      /** Page number */
      page?: number;
      /** Requested number of results per page */
      perPage?: number;
      /** The list of campaign resource IDs (string separated with '') */
      queryCampaignId?: string;
      /** Count data from this date (GetResponse date format: yyyy-MM-ddTHH:mm:ss+HHMM, e.g. 2024-01-15T10:30:00+0000 -- no colon in the offset, no sub-second precision (unlike Date.prototype.toISOString())) */
      queryCreatedOnFrom?: string;
      /** Count data to this date (GetResponse date format: yyyy-MM-ddTHH:mm:ss+HHMM, e.g. 2024-01-15T10:30:00+0000 -- no colon in the offset, no sub-second precision (unlike Date.prototype.toISOString())) */
      queryCreatedOnTo?: string;
      /** Group results by time interval */
      queryGroupBy?: M.GetNewsletterStatisticsCollectionQueryGroupBy;
      /** The list of newsletter resource IDs (string separated with '') */
      queryNewsletterId?: string;
    },
    signal?: AbortSignal,
  ): Promise<M.MessageStatisticsListElement[]> => {
    return this.core.request<M.MessageStatisticsListElement[]>('GET', '/newsletters/statistics', {
      query: params
        ? {
            'query[groupBy]': params.queryGroupBy,
            'query[newsletterId]': params.queryNewsletterId,
            'query[campaignId]': params.queryCampaignId,
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

  /** Get newsletter thumbnail */
  readonly getNewsletterThumbnail = async (
    newsletterId: string,
    params?: {
      /** The size of the thumbnail */
      size?: M.GetNewsletterThumbnailSize;
    },
    signal?: AbortSignal,
  ): Promise<void> => {
    return this.core.request<void>('GET', '/newsletters/{newsletterId}/thumbnail', {
      pathParams: { newsletterId: newsletterId },
      query: params ? { size: params.size } : undefined,
      signal,
    });
  };

  /** > This makes it possible to easily fetch statistics for a single newsletter. You can group the data hourly, daily, monthly and as a total sum. Remember that all statistics date ranges are given in standard UTC period type objects. ([See ISO 8601 standard](http://en.wikipedia.org/wiki/ISO_8601#Time_intervals)). You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by. */
  readonly getSingleNewsletterStatistics = async (
    newsletterId: string,
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
      queryGroupBy?: M.GetSingleNewsletterStatisticsQueryGroupBy;
    },
    signal?: AbortSignal,
  ): Promise<M.MessageStatisticsListElement[]> => {
    return this.core.request<M.MessageStatisticsListElement[]>(
      'GET',
      '/newsletters/{newsletterId}/statistics',
      {
        pathParams: { newsletterId: newsletterId },
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

  /** Send the newsletter draft */
  readonly sendDraft = async (
    body: M.SendNewsletterDraft,
    signal?: AbortSignal,
  ): Promise<M.NewsletterDetails> => {
    return this.core.request<M.NewsletterDetails>('POST', '/newsletters/send-draft', {
      body,
      signal,
    });
  };
}
