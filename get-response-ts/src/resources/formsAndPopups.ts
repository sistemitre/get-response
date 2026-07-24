/** Operations tagged 'Forms and Popups' in the GetResponse API. */

import type { Core } from '../core.js';
import type * as M from '../models.js';

export class FormsAndPopupsResource {
  constructor(private readonly core: Core) {}

  /** Get a single form or popup by ID */
  readonly getPopupDetails = async (
    popupId: string,
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
    },
    signal?: AbortSignal,
  ): Promise<M.PopupDetails> => {
    return this.core.request<M.PopupDetails>('GET', '/popups/{popupId}', {
      pathParams: { popupId: popupId },
      query: params ? { fields: params.fields } : undefined,
      signal,
    });
  };

  /** You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by. */
  readonly getPopupsList = async (
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
      /** Page number */
      page?: number;
      /** Requested number of results per page */
      perPage?: number;
      /** Search forms and popups by name */
      queryName?: string;
      /** Search forms and popups by status */
      queryStatus?: M.GetPopupsListQueryStatus;
      /** Sort forms and popups by creation date */
      sortCreatedAt?: M.SortOrderEnum;
      /** Sort by CTR (click-through rate) */
      sortCtr?: M.SortOrderEnum;
      /** Sort by number of leads */
      sortLeads?: M.SortOrderEnum;
      /** Sort forms and popups by name */
      sortName?: M.SortOrderEnum;
      /** Sort forms and popups by status */
      sortStatus?: M.SortOrderEnum;
      /** Sort by number of unique visitors */
      sortUniqueVisitors?: M.SortOrderEnum;
      /** Sort forms and popups by modification date */
      sortUpdatedAt?: M.SortOrderEnum;
      /** Sort by number of views */
      sortViews?: M.SortOrderEnum;
      /** Show statistics from this date (GetResponse date format: yyyy-MM-ddTHH:mm:ss+HHMM, e.g. 2024-01-15T10:30:00+0000 -- no colon in the offset, no sub-second precision (unlike Date.prototype.toISOString())) */
      statsFrom?: string;
      /** Show statistics to this date (GetResponse date format: yyyy-MM-ddTHH:mm:ss+HHMM, e.g. 2024-01-15T10:30:00+0000 -- no colon in the offset, no sub-second precision (unlike Date.prototype.toISOString())) */
      statsTo?: string;
    },
    signal?: AbortSignal,
  ): Promise<M.PopupListItem[]> => {
    return this.core.request<M.PopupListItem[]>('GET', '/popups', {
      query: params
        ? {
            'query[name]': params.queryName,
            'query[status]': params.queryStatus,
            'stats[from]': params.statsFrom,
            'stats[to]': params.statsTo,
            'sort[name]': params.sortName,
            'sort[status]': params.sortStatus,
            'sort[createdAt]': params.sortCreatedAt,
            'sort[updatedAt]': params.sortUpdatedAt,
            'sort[views]': params.sortViews,
            'sort[uniqueVisitors]': params.sortUniqueVisitors,
            'sort[leads]': params.sortLeads,
            'sort[ctr]': params.sortCtr,
            fields: params.fields,
            perPage: params.perPage,
            page: params.page,
          }
        : undefined,
      signal,
    });
  };
}
