/** Operations tagged 'Suppressions' in the GetResponse API. */

import type { Core } from '../core.js';
import type * as M from '../models.js';

export class SuppressionsResource {
  constructor(private readonly core: Core) {}

  /** Creates a new suppression list */
  readonly createSuppression = async (
    body: M.NewSuppression,
    signal?: AbortSignal,
  ): Promise<M.SuppressionDetails> => {
    return this.core.request<M.SuppressionDetails>('POST', '/suppressions', {
      body,
      signal,
    });
  };

  /** Deletes a given suppression list by ID */
  readonly deleteSuppression = async (
    suppressionId: string,
    signal?: AbortSignal,
  ): Promise<void> => {
    return this.core.request<void>('DELETE', '/suppressions/{suppressionId}', {
      pathParams: { suppressionId: suppressionId },
      signal,
    });
  };

  /** Get a suppression list by ID */
  readonly getSuppressionById = async (
    suppressionId: string,
    signal?: AbortSignal,
  ): Promise<M.SuppressionDetails> => {
    return this.core.request<M.SuppressionDetails>('GET', '/suppressions/{suppressionId}', {
      pathParams: { suppressionId: suppressionId },
      signal,
    });
  };

  /** Get suppression lists */
  readonly getSuppressionsList = async (
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
      /** Page number */
      page?: number;
      /** Requested number of results per page */
      perPage?: number;
      /** Search suppressions created from this date (GetResponse date format: yyyy-MM-ddTHH:mm:ss+HHMM, e.g. 2024-01-15T10:30:00+0000 -- no colon in the offset, no sub-second precision (unlike Date.prototype.toISOString())) */
      queryCreatedOnFrom?: string;
      /** Search suppressions created to this date (GetResponse date format: yyyy-MM-ddTHH:mm:ss+HHMM, e.g. 2024-01-15T10:30:00+0000 -- no colon in the offset, no sub-second precision (unlike Date.prototype.toISOString())) */
      queryCreatedOnTo?: string;
      /** Search suppressions by name */
      queryName?: string;
      /** Sort by the createdOn date */
      sortCreatedOn?: M.SortOrderEnum;
      /** Sort by name */
      sortName?: M.SortOrderEnum;
    },
    signal?: AbortSignal,
  ): Promise<M.Suppression[]> => {
    return this.core.request<M.Suppression[]>('GET', '/suppressions', {
      query: params
        ? {
            'query[name]': params.queryName,
            'query[createdOn][from]': params.queryCreatedOnFrom,
            'query[createdOn][to]': params.queryCreatedOnTo,
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

  /** Update a suppression list by ID */
  readonly updateSuppression = async (
    suppressionId: string,
    body: M.UpdateSuppression,
    signal?: AbortSignal,
  ): Promise<M.SuppressionDetails> => {
    return this.core.request<M.SuppressionDetails>('POST', '/suppressions/{suppressionId}', {
      pathParams: { suppressionId: suppressionId },
      body,
      signal,
    });
  };
}
