/** Operations tagged 'Legacy Landing Pages' in the GetResponse API. */

import type { Core } from '../core.js';
import type * as M from '../models.js';

export class LegacyLandingPagesResource {
  constructor(private readonly core: Core) {}

  /** Get single landing page by ID */
  readonly getLandingPageById = async (
    landingPageId: string,
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
    },
    signal?: AbortSignal,
  ): Promise<M.LandingPage[]> => {
    return this.core.request<M.LandingPage[]>('GET', '/landing-pages/{landingPageId}', {
      pathParams: { landingPageId: landingPageId },
      query: params ? { fields: params.fields } : undefined,
      signal,
    });
  };

  /** You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by. */
  readonly getLandingPageList = async (
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
      /** Page number */
      page?: number;
      /** Requested number of results per page */
      perPage?: number;
      /** Search landing pages by ID of the assigned campaign. Campaign ID must be encoded! You can get the campaign list with encoded IDs by calling the `/v3/campaigns` endpoint. You can search by multiple comma separated values eg. `o5lx,34er`. */
      queryCampaignId?: string;
      /** Show landing pages created from this date */
      queryCreatedOnFrom?: Record<string, unknown>;
      /** Show landing pages created to this date */
      queryCreatedOnTo?: Record<string, unknown>;
      /** Search landing pages by domain */
      queryDomain?: string;
      /** Search landing pages by metaTitle field */
      queryMetaTitle?: string;
      /** Search landing pages by status */
      queryStatus?: M.StatusEnum;
      /** Search landing pages by subdomain */
      querySubdomain?: string;
      /** Search landing pages by user provided domain */
      queryUserDomain?: string;
      /** Sort by campaign */
      sortCampaignId?: M.SortOrderEnum;
      /** Sort by date */
      sortCreatedOn?: M.SortOrderEnum;
      /** Sort by domain */
      sortDomain?: M.SortOrderEnum;
      /** Sort by metaTitle */
      sortMetaTitle?: M.SortOrderEnum;
    },
    signal?: AbortSignal,
  ): Promise<M.BaseLandingPage[]> => {
    return this.core.request<M.BaseLandingPage[]>('GET', '/landing-pages', {
      query: params
        ? {
            'query[domain]': params.queryDomain,
            'query[status]': params.queryStatus,
            'query[subdomain]': params.querySubdomain,
            'query[metaTitle]': params.queryMetaTitle,
            'query[userDomain]': params.queryUserDomain,
            'query[campaignId]': params.queryCampaignId,
            'query[createdOn][from]': params.queryCreatedOnFrom,
            'query[createdOn][to]': params.queryCreatedOnTo,
            'sort[createdOn]': params.sortCreatedOn,
            'sort[domain]': params.sortDomain,
            'sort[campaignId]': params.sortCampaignId,
            'sort[metaTitle]': params.sortMetaTitle,
            fields: params.fields,
            perPage: params.perPage,
            page: params.page,
          }
        : undefined,
      signal,
    });
  };
}
