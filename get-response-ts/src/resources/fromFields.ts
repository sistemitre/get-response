/** Operations tagged 'From Fields' in the GetResponse API. */

import type { Core } from '../core.js';
import type * as M from '../models.js';

export class FromFieldsResource {
  constructor(private readonly core: Core) {}

  /** Create 'From' address */
  readonly createFromField = async (
    body: M.NewFromField,
    signal?: AbortSignal,
  ): Promise<M.FromField> => {
    return this.core.request<M.FromField>('POST', '/from-fields', {
      body,
      signal,
    });
  };

  /** Delete 'From' address */
  readonly deleteFromField = async (
    fromFieldId: string,
    params?: {
      /** The 'From' address ID that should replace the deleted 'From' address */
      fromFieldIdToReplaceWith?: string;
    },
    signal?: AbortSignal,
  ): Promise<void> => {
    return this.core.request<void>('DELETE', '/from-fields/{fromFieldId}', {
      pathParams: { fromFieldId: fromFieldId },
      query: params ? { fromFieldIdToReplaceWith: params.fromFieldIdToReplaceWith } : undefined,
      signal,
    });
  };

  /** Get a single 'From' address by ID */
  readonly getFromFieldById = async (
    fromFieldId: string,
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
    },
    signal?: AbortSignal,
  ): Promise<M.FromField> => {
    return this.core.request<M.FromField>('GET', '/from-fields/{fromFieldId}', {
      pathParams: { fromFieldId: fromFieldId },
      query: params ? { fields: params.fields } : undefined,
      signal,
    });
  };

  /** You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by. */
  readonly getFromFieldList = async (
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
      /** Page number */
      page?: number;
      /** Requested number of results per page */
      perPage?: number;
      /** Search 'From' address by email */
      queryEmail?: string;
      /** Search only active 'From' addresses */
      queryIsActive?: boolean;
      /** Search only default 'From' address */
      queryIsDefault?: boolean;
      /** Search 'From' address by name (GetResponse date format: yyyy-MM-ddTHH:mm:ss+HHMM, e.g. 2024-01-15T10:30:00+0000 -- no colon in the offset, no sub-second precision (unlike Date.prototype.toISOString())) */
      queryName?: string;
      /** Sort 'From' address by date */
      sortCreatedOn?: M.SortOrderEnum;
    },
    signal?: AbortSignal,
  ): Promise<M.FromField[]> => {
    return this.core.request<M.FromField[]>('GET', '/from-fields', {
      query: params
        ? {
            'query[email]': params.queryEmail,
            'query[name]': params.queryName,
            'query[isDefault]': params.queryIsDefault,
            'query[isActive]': params.queryIsActive,
            'sort[createdOn]': params.sortCreatedOn,
            fields: params.fields,
            perPage: params.perPage,
            page: params.page,
          }
        : undefined,
      signal,
    });
  };

  /** Set a 'From' address as default */
  readonly setFromFieldAsDefault = async (
    fromFieldId: string,
    signal?: AbortSignal,
  ): Promise<void> => {
    return this.core.request<void>('POST', '/from-fields/{fromFieldId}/default', {
      pathParams: { fromFieldId: fromFieldId },
      signal,
    });
  };
}
