/** Operations tagged 'Forms' in the GetResponse API. */

import type { Core } from '../core.js';
import type * as M from '../models.js';

export class FormsResource {
  constructor(private readonly core: Core) {}

  /** Get form by ID */
  readonly getForm = async (
    formId: string,
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
    },
    signal?: AbortSignal,
  ): Promise<M.FormDetails> => {
    return this.core.request<M.FormDetails>('GET', '/forms/{formId}', {
      pathParams: { formId: formId },
      query: params ? { fields: params.fields } : undefined,
      signal,
    });
  };

  /** You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by. */
  readonly getFormList = async (
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
      /** Page number */
      page?: number;
      /** Requested number of results per page */
      perPage?: number;
      /** Search forms assigned to this list (campaign). You can pass multiple comma-separated values, eg. `Xd1P,sC7r` */
      queryCampaignId?: string;
      /** Search forms created from this date (GetResponse date format: yyyy-MM-ddTHH:mm:ss+HHMM, e.g. 2024-01-15T10:30:00+0000 -- no colon in the offset, no sub-second precision (unlike Date.prototype.toISOString())) */
      queryCreatedOnFrom?: string;
      /** Search forms created to this date (GetResponse date format: yyyy-MM-ddTHH:mm:ss+HHMM, e.g. 2024-01-15T10:30:00+0000 -- no colon in the offset, no sub-second precision (unlike Date.prototype.toISOString())) */
      queryCreatedOnTo?: string;
      /** Search forms by name */
      queryName?: string;
      /** Search by status. **Note:** `disabled` includes both `unpublished` and `draft` and `enabled` equals `published` */
      queryStatus?: M.GetFormListQueryStatus;
      sortCreatedOn?: M.SortOrderEnum;
      sortName?: M.SortOrderEnum;
      sortSubscribed?: M.SortOrderEnum;
      sortSubscriptionRate?: M.SortOrderEnum;
      sortUniqueVisitors?: M.SortOrderEnum;
      sortVisitors?: M.SortOrderEnum;
    },
    signal?: AbortSignal,
  ): Promise<M.Form[]> => {
    return this.core.request<M.Form[]>('GET', '/forms', {
      query: params
        ? {
            'query[name]': params.queryName,
            'query[createdOn][from]': params.queryCreatedOnFrom,
            'query[createdOn][to]': params.queryCreatedOnTo,
            'query[campaignId]': params.queryCampaignId,
            'query[status]': params.queryStatus,
            'sort[createdOn]': params.sortCreatedOn,
            'sort[name]': params.sortName,
            'sort[visitors]': params.sortVisitors,
            'sort[uniqueVisitors]': params.sortUniqueVisitors,
            'sort[subscribed]': params.sortSubscribed,
            'sort[subscriptionRate]': params.sortSubscriptionRate,
            fields: params.fields,
            perPage: params.perPage,
            page: params.page,
          }
        : undefined,
      signal,
    });
  };

  /** Get the list of form variants (A/B tests) */
  readonly getFormVariantList = async (
    formId: string,
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
    },
    signal?: AbortSignal,
  ): Promise<M.FormVariantDetails[]> => {
    return this.core.request<M.FormVariantDetails[]>('GET', '/forms/{formId}/variants', {
      pathParams: { formId: formId },
      query: params ? { fields: params.fields } : undefined,
      signal,
    });
  };
}
