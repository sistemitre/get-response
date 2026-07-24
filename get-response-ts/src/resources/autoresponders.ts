/** Operations tagged 'Autoresponders' in the GetResponse API. */

import type { Core } from '../core.js';
import type * as M from '../models.js';

export class AutorespondersResource {
  constructor(private readonly core: Core) {}

  /** > **The action-based autoresponder feature has been migrated over to marketing automation. Your existing autoresponders are now converted into workflows. You can no longer create and update action-based autoresponders using our API.** This request allows you to create an autoresponder. Remember to select the proper `sendSettings` - depending on `type` you need to fill corresponding setting (eg. if you selected type `delay`, then you MUST fill `delayInHours` field). */
  readonly createAutoresponder = async (
    body: M.NewAutoresponder,
    signal?: AbortSignal,
  ): Promise<M.AutoresponderDetails> => {
    return this.core.request<M.AutoresponderDetails>('POST', '/autoresponders', {
      body,
      signal,
    });
  };

  /** Delete autoresponder. */
  readonly deleteAutoresponder = async (
    autoresponderId: string,
    signal?: AbortSignal,
  ): Promise<void> => {
    return this.core.request<void>('DELETE', '/autoresponders/{autoresponderId}', {
      pathParams: { autoresponderId: autoresponderId },
      signal,
    });
  };

  /** Get a single autoresponder by its ID */
  readonly getAutoresponder = async (
    autoresponderId: string,
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
    },
    signal?: AbortSignal,
  ): Promise<M.AutoresponderDetails> => {
    return this.core.request<M.AutoresponderDetails>('GET', '/autoresponders/{autoresponderId}', {
      pathParams: { autoresponderId: autoresponderId },
      query: params ? { fields: params.fields } : undefined,
      signal,
    });
  };

  /** You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by. */
  readonly getAutoresponderList = async (
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
      /** Page number */
      page?: number;
      /** Requested number of results per page */
      perPage?: number;
      /** Search autoresponder by campaign ID */
      queryCampaignId?: string;
      /** Search autoresponder created from this date (GetResponse date format: yyyy-MM-ddTHH:mm:ss+HHMM, e.g. 2024-01-15T10:30:00+0000 -- no colon in the offset, no sub-second precision (unlike Date.prototype.toISOString())) */
      queryCreatedOnFrom?: string;
      /** Search autoresponder created to this date (GetResponse date format: yyyy-MM-ddTHH:mm:ss+HHMM, e.g. 2024-01-15T10:30:00+0000 -- no colon in the offset, no sub-second precision (unlike Date.prototype.toISOString())) */
      queryCreatedOnTo?: string;
      /** Search autoresponder by name */
      queryName?: string;
      /** Search autoresponder by status */
      queryStatus?: M.GetAutoresponderListQueryStatus;
      /** Search autoresponder by subject */
      querySubject?: string;
      /** Sort by click rate */
      sortClickRate?: M.SortOrderEnum;
      /** Sort by date */
      sortCreatedOn?: M.SortOrderEnum;
      /** Sort by cycle day */
      sortDayOfCycle?: M.SortOrderEnum;
      /** Sort by delivered */
      sortDelivered?: M.SortOrderEnum;
      /** Sort by name */
      sortName?: M.SortOrderEnum;
      /** Sort by open rate */
      sortOpenRate?: M.SortOrderEnum;
      /** Sort by subject */
      sortSubject?: M.SortOrderEnum;
    },
    signal?: AbortSignal,
  ): Promise<Record<string, unknown>[]> => {
    return this.core.request<Record<string, unknown>[]>('GET', '/autoresponders', {
      query: params
        ? {
            'query[subject]': params.querySubject,
            'query[name]': params.queryName,
            'query[status]': params.queryStatus,
            'query[createdOn][from]': params.queryCreatedOnFrom,
            'query[createdOn][to]': params.queryCreatedOnTo,
            'query[campaignId]': params.queryCampaignId,
            'sort[name]': params.sortName,
            'sort[subject]': params.sortSubject,
            'sort[dayOfCycle]': params.sortDayOfCycle,
            'sort[delivered]': params.sortDelivered,
            'sort[openRate]': params.sortOpenRate,
            'sort[clickRate]': params.sortClickRate,
            'sort[createdOn]': params.sortCreatedOn,
            fields: params.fields,
            perPage: params.perPage,
            page: params.page,
          }
        : undefined,
      signal,
    });
  };

  /** > This returns the statistics summary for selected autoresponders. You can select them by specifying the autoresponder or campaign IDs. As in all statistics, you can change the date and time range (hourly daily monthly or total). Keep in mind that all statistics date ranges are given in standard UTC period type objects. ([See ISO 8601 standard](http://en.wikipedia.org/wiki/ISO_8601#Time_intervals)) (https://app.getresponse.com/statistics.html?t=followup#total). You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by. */
  readonly getAutoresponderStatisticsCollection = async (
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
      /** Page number */
      page?: number;
      /** Requested number of results per page */
      perPage?: number;
      /** The list of autoresponder resource IDs (string separated with '') */
      queryAutoreponderId?: string;
      /** The list of campaign resource IDs (string separated with '') */
      queryCampaignId?: string;
      /** Count data from this date (GetResponse date format: yyyy-MM-ddTHH:mm:ss+HHMM, e.g. 2024-01-15T10:30:00+0000 -- no colon in the offset, no sub-second precision (unlike Date.prototype.toISOString())) */
      queryCreatedOnFrom?: string;
      /** Count data to this date (GetResponse date format: yyyy-MM-ddTHH:mm:ss+HHMM, e.g. 2024-01-15T10:30:00+0000 -- no colon in the offset, no sub-second precision (unlike Date.prototype.toISOString())) */
      queryCreatedOnTo?: string;
      /** Group results by time interval */
      queryGroupBy?: M.GetAutoresponderStatisticsCollectionQueryGroupBy;
    },
    signal?: AbortSignal,
  ): Promise<M.MessageStatisticsListElement[]> => {
    return this.core.request<M.MessageStatisticsListElement[]>(
      'GET',
      '/autoresponders/statistics',
      {
        query: params
          ? {
              'query[groupBy]': params.queryGroupBy,
              'query[autoreponderId]': params.queryAutoreponderId,
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

  /** Get the autoresponder thumbnail */
  readonly getAutoresponderThumbnail = async (
    autoresponderId: string,
    params?: {
      /** The size of the autoresponder thumbnail */
      size?: M.GetAutoresponderThumbnailSize;
    },
    signal?: AbortSignal,
  ): Promise<void> => {
    return this.core.request<void>('GET', '/autoresponders/{autoresponderId}/thumbnail', {
      pathParams: { autoresponderId: autoresponderId },
      query: params ? { size: params.size } : undefined,
      signal,
    });
  };

  /** > This requst returns the statistics summary for a single given autoresponder. As in all statistics, you can change the date and time range (hourly daily monthly or total). Keep in mind that all statistics date ranges are given in standard UTC period type objects. ([See ISO 8601 standard](http://en.wikipedia.org/wiki/ISO_8601#Time_intervals)) (https://app.getresponse.com/statistics.html?t=followup#total). You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by. */
  readonly getSingleAutoresponderStatistics = async (
    autoresponderId: string,
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
      queryGroupBy?: M.GetSingleAutoresponderStatisticsQueryGroupBy;
    },
    signal?: AbortSignal,
  ): Promise<M.MessageStatisticsListElement[]> => {
    return this.core.request<M.MessageStatisticsListElement[]>(
      'GET',
      '/autoresponders/{autoresponderId}/statistics',
      {
        pathParams: { autoresponderId: autoresponderId },
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

  /** > **The action-based autoresponder feature has been migrated over to marketing automation. Your existing autoresponders are now converted into workflows. You can no longer create and update action-based autoresponders using our API.** This method allows you to update an autoresponder. The same rules as in creating an autoresponder apply. */
  readonly updateAutoresponder = async (
    autoresponderId: string,
    body: M.UpdateAutoresponder,
    signal?: AbortSignal,
  ): Promise<M.AutoresponderDetails> => {
    return this.core.request<M.AutoresponderDetails>('POST', '/autoresponders/{autoresponderId}', {
      pathParams: { autoresponderId: autoresponderId },
      body,
      signal,
    });
  };
}
