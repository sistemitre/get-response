/** Operations tagged 'Campaigns (Lists)' in the GetResponse API. */

import type { Core } from '../core.js';
import type * as M from '../models.js';

export class CampaignsListsResource {
  constructor(private readonly core: Core) {}

  /** This endpoint allows you to create a campaign (contact list). You can create up to 1000 campaigns (contact lists). */
  readonly createCampaign = async (
    body: M.NewCampaign,
    signal?: AbortSignal,
  ): Promise<M.Campaign> => {
    return this.core.request<M.Campaign>('POST', '/campaigns', {
      body,
      signal,
    });
  };

  /** Retrieve detailed information about a single campaign (contact list) by its unique campaignId. The response includes additional campaign settings such as postal address, subscription notification and confirmation settings, opt-in type, and profile information. */
  readonly getCampaign = async (
    campaignId: string,
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
    },
    signal?: AbortSignal,
  ): Promise<M.Campaign> => {
    return this.core.request<M.Campaign>('GET', '/campaigns/{campaignId}', {
      pathParams: { campaignId: campaignId },
      query: params ? { fields: params.fields } : undefined,
      signal,
    });
  };

  /** Returns campaign blocklist masks */
  readonly getCampaignBlocklist = async (
    campaignId: string,
    params?: {
      /** Blocklist mask to search for */
      queryMask?: string;
    },
    signal?: AbortSignal,
  ): Promise<M.Blocklist> => {
    return this.core.request<M.Blocklist>('GET', '/campaigns/{campaignId}/blocklists', {
      pathParams: { campaignId: campaignId },
      query: params ? { 'query[mask]': params.queryMask } : undefined,
      signal,
    });
  };

  /** Returns a list of campaigns (contact lists). You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by. */
  readonly getCampaignList = async (
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
      /** Page number */
      page?: number;
      /** Requested number of results per page */
      perPage?: number;
      /** Retrieve campaigns (contact lists) depending on whether they are marked as default (`isDefault` = `true`) */
      queryIsDefault?: boolean;
      /** Retrieve campaigns (contact lists) filtered by name */
      queryName?: string;
      /** Sort campaigns (contact lists) by creation date */
      sortCreatedOn?: M.SortOrderEnum;
      /** Sort by name */
      sortName?: M.SortOrderEnum;
    },
    signal?: AbortSignal,
  ): Promise<M.CampaignListElement[]> => {
    return this.core.request<M.CampaignListElement[]>('GET', '/campaigns', {
      query: params
        ? {
            'query[name]': params.queryName,
            'query[isDefault]': params.queryIsDefault,
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

  /** Returns the balance of subscriptions. Dates in the YYYY-MM-DD format are used as keys in the response. */
  readonly getCampaignStatisticsBalance = async (
    params?: {
      queryCampaignId: string;
      queryCreatedOnFrom?: Record<string, unknown>;
      queryCreatedOnTo?: Record<string, unknown>;
      queryGroupBy?: M.GetCampaignStatisticsBalanceQueryGroupBy;
    },
    signal?: AbortSignal,
  ): Promise<Record<string, unknown>[]> => {
    return this.core.request<Record<string, unknown>[]>('GET', '/campaigns/statistics/balance', {
      query: params
        ? {
            'query[campaignId]': params.queryCampaignId,
            'query[groupBy]': params.queryGroupBy,
            'query[createdOn][from]': params.queryCreatedOnFrom,
            'query[createdOn][to]': params.queryCreatedOnTo,
          }
        : undefined,
      signal,
    });
  };

  /** Returns the number of the total added and removed subscribers, grouped by default or by time period. */
  readonly getCampaignStatisticsListSize = async (
    params?: {
      queryCampaignId: string;
      queryCreatedOnFrom?: Record<string, unknown>;
      queryCreatedOnTo?: Record<string, unknown>;
      queryGroupBy?: M.GetCampaignStatisticsListSizeQueryGroupBy;
    },
    signal?: AbortSignal,
  ): Promise<M.CampaignListSizesStatisticsElement[]> => {
    return this.core.request<M.CampaignListSizesStatisticsElement[]>(
      'GET',
      '/campaigns/statistics/list-size',
      {
        query: params
          ? {
              'query[campaignId]': params.queryCampaignId,
              'query[groupBy]': params.queryGroupBy,
              'query[createdOn][from]': params.queryCreatedOnFrom,
              'query[createdOn][to]': params.queryCreatedOnTo,
            }
          : undefined,
        signal,
      },
    );
  };

  /** The results are indexed with the location name (PL, EN, etc.). */
  readonly getCampaignStatisticsLocations = async (
    params?: {
      queryCampaignId: string;
      queryCreatedOnFrom?: Record<string, unknown>;
      queryCreatedOnTo?: Record<string, unknown>;
      queryGroupBy?: M.GetCampaignStatisticsLocationsQueryGroupBy;
    },
    signal?: AbortSignal,
  ): Promise<Record<string, unknown>[]> => {
    return this.core.request<Record<string, unknown>[]>('GET', '/campaigns/statistics/locations', {
      query: params
        ? {
            'query[campaignId]': params.queryCampaignId,
            'query[groupBy]': params.queryGroupBy,
            'query[createdOn][from]': params.queryCreatedOnFrom,
            'query[createdOn][to]': params.queryCreatedOnTo,
          }
        : undefined,
      signal,
    });
  };

  /** The results are indexed with the campaign ID. */
  readonly getCampaignStatisticsOrigins = async (
    params?: {
      queryCampaignId: string;
      queryCreatedOnFrom?: Record<string, unknown>;
      queryCreatedOnTo?: Record<string, unknown>;
      queryGroupBy?: M.GetCampaignStatisticsOriginsQueryGroupBy;
    },
    signal?: AbortSignal,
  ): Promise<Record<string, unknown>[]> => {
    return this.core.request<Record<string, unknown>[]>('GET', '/campaigns/statistics/origins', {
      query: params
        ? {
            'query[campaignId]': params.queryCampaignId,
            'query[groupBy]': params.queryGroupBy,
            'query[createdOn][from]': params.queryCreatedOnFrom,
            'query[createdOn][to]': params.queryCreatedOnTo,
          }
        : undefined,
      signal,
    });
  };

  /** Returns the number and reason for removed contacts. Dates in the YYYY-MM-DD format are used as keys in the response. */
  readonly getCampaignStatisticsRemovals = async (
    params?: {
      queryCampaignId: string;
      queryCreatedOnFrom?: Record<string, unknown>;
      queryCreatedOnTo?: Record<string, unknown>;
      queryGroupBy?: M.GetCampaignStatisticsRemovalsQueryGroupBy;
    },
    signal?: AbortSignal,
  ): Promise<Record<string, unknown>[]> => {
    return this.core.request<Record<string, unknown>[]>('GET', '/campaigns/statistics/removals', {
      query: params
        ? {
            'query[campaignId]': params.queryCampaignId,
            'query[groupBy]': params.queryGroupBy,
            'query[createdOn][from]': params.queryCreatedOnFrom,
            'query[createdOn][to]': params.queryCreatedOnTo,
          }
        : undefined,
      signal,
    });
  };

  /** Returns the number and origin of subscriptions, grouped by a specified campaigns for each day on which any changes were made. Dates in the YYYY-MM-DD format are used as keys in the response. */
  readonly getCampaignStatisticsSubscriptions = async (
    params?: {
      queryCampaignId: string;
      queryCreatedOnFrom?: Record<string, unknown>;
      queryCreatedOnTo?: Record<string, unknown>;
      queryGroupBy?: M.GetCampaignStatisticsSubscriptionsQueryGroupBy;
    },
    signal?: AbortSignal,
  ): Promise<Record<string, unknown>[]> => {
    return this.core.request<Record<string, unknown>[]>(
      'GET',
      '/campaigns/statistics/subscriptions',
      {
        query: params
          ? {
              'query[campaignId]': params.queryCampaignId,
              'query[groupBy]': params.queryGroupBy,
              'query[createdOn][from]': params.queryCreatedOnFrom,
              'query[createdOn][to]': params.queryCreatedOnTo,
            }
          : undefined,
        signal,
      },
    );
  };

  /** The results are indexed with the campaign ID. */
  readonly getCampaignStatisticsSummary = async (
    params?: {
      queryCampaignId?: string;
    },
    signal?: AbortSignal,
  ): Promise<Record<string, unknown>[]> => {
    return this.core.request<Record<string, unknown>[]>('GET', '/campaigns/statistics/summary', {
      query: params ? { 'query[campaignId]': params.queryCampaignId } : undefined,
      signal,
    });
  };

  /** Update a campaign */
  readonly updateCampaign = async (
    campaignId: string,
    body: M.UpdateCampaign,
    signal?: AbortSignal,
  ): Promise<M.Campaign> => {
    return this.core.request<M.Campaign>('POST', '/campaigns/{campaignId}', {
      pathParams: { campaignId: campaignId },
      body,
      signal,
    });
  };

  /** Updates campaign blocklist masks */
  readonly updateCampaignBlocklist = async (
    campaignId: string,
    body: M.UpdateBlocklist,
    params?: {
      /** The flag value `add` adds the masks provided in the request body to your blocklist. The flag value `delete` deletes the masks. The masks are replaced if there are no flag values in the request body. For better performance, use the flag value `noResponse`. It removes the response body and can be used alone or combined with other flags. If multiple flags are used, separate them by a comma, like this: `additionalFlags=noResponse` or `additionalFlags=add,noResponse`. */
      additionalFlags?: M.UpdateCampaignBlocklistAdditionalFlags;
    },
    signal?: AbortSignal,
  ): Promise<M.Blocklist> => {
    return this.core.request<M.Blocklist>('POST', '/campaigns/{campaignId}/blocklists', {
      pathParams: { campaignId: campaignId },
      query: params ? { additionalFlags: params.additionalFlags } : undefined,
      body,
      signal,
    });
  };
}
