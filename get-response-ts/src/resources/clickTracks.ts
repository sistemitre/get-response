/** Operations tagged 'Click Tracks' in the GetResponse API. */

import type { Core } from '../core.js';
import type * as M from '../models.js';

export class ClickTracksResource {
  constructor(private readonly core: Core) {}

  /** Get click tracked link details by click track ID */
  readonly getClickTrackById = async (
    clickTrackId: string,
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
    },
    signal?: AbortSignal,
  ): Promise<M.ClickTrackResource> => {
    return this.core.request<M.ClickTrackResource>('GET', '/click-tracks/{clickTrackId}', {
      pathParams: { clickTrackId: clickTrackId },
      query: params ? { fields: params.fields } : undefined,
      signal,
    });
  };

  /** You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by. */
  readonly getClickTrackList = async (
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
      /** Page number */
      page?: number;
      /** Requested number of results per page */
      perPage?: number;
      /** Search click tracks from messages created from this date (GetResponse date format: yyyy-MM-ddTHH:mm:ss+HHMM, e.g. 2024-01-15T10:30:00+0000 -- no colon in the offset, no sub-second precision (unlike Date.prototype.toISOString())) */
      queryCreatedOnFrom?: string;
      /** Search click tracks from messages created to this date (GetResponse date format: yyyy-MM-ddTHH:mm:ss+HHMM, e.g. 2024-01-15T10:30:00+0000 -- no colon in the offset, no sub-second precision (unlike Date.prototype.toISOString())) */
      queryCreatedOnTo?: string;
      /** Sort by message date */
      sortCreatedOn?: M.SortOrderEnum;
    },
    signal?: AbortSignal,
  ): Promise<M.ClickTrackResource[]> => {
    return this.core.request<M.ClickTrackResource[]>('GET', '/click-tracks', {
      query: params
        ? {
            'query[createdOn][from]': params.queryCreatedOnFrom,
            'query[createdOn][to]': params.queryCreatedOnTo,
            'sort[createdOn]': params.sortCreatedOn,
            fields: params.fields,
            perPage: params.perPage,
            page: params.page,
          }
        : undefined,
      signal,
    });
  };
}
