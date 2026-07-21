/** Operations tagged 'GDPR Fields' in the GetResponse API. */

import type { Core } from '../core.js';
import type * as M from '../models.js';

export class GdprFieldsResource {
  constructor(private readonly core: Core) {}

  /** Get GDPR Field details */
  readonly getGDPRField = async (
    gdprFieldId: string,
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
    },
    signal?: AbortSignal,
  ): Promise<M.GDPRFieldDetails> => {
    return this.core.request<M.GDPRFieldDetails>('GET', '/gdpr-fields/{gdprFieldId}', {
      pathParams: { gdprFieldId: gdprFieldId },
      query: params ? { fields: params.fields } : undefined,
      signal,
    });
  };

  /** Get the GDPR fields list */
  readonly getGDPRFieldList = async (
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
      /** Page number */
      page?: number;
      /** Requested number of results per page */
      perPage?: number;
      /** Sort fields by creation date */
      sortCreatedOn?: M.SortOrderEnum;
      /** Sort fields by name */
      sortName?: M.SortOrderEnum;
    },
    signal?: AbortSignal,
  ): Promise<M.GDPRField[]> => {
    return this.core.request<M.GDPRField[]>('GET', '/gdpr-fields', {
      query: params
        ? {
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
}
