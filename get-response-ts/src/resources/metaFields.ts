/** Operations tagged 'Meta Fields' in the GetResponse API. */

import type { Core } from '../core.js';
import type * as M from '../models.js';

export class MetaFieldsResource {
  constructor(private readonly core: Core) {}

  /** Sending a **POST** request to this URL will create a new meta field resource. In order to create a new meta field, you need to send a meta field resource in the body of the request (remember that you need to serialize the body into a JSON string) */
  readonly createMetaField = async (
    shopId: string,
    body: M.NewMetaField,
    signal?: AbortSignal,
  ): Promise<M.MetaField> => {
    return this.core.request<M.MetaField>('POST', '/shops/{shopId}/meta-fields', {
      pathParams: { shopId: shopId },
      body,
      signal,
    });
  };

  /** Delete meta field */
  readonly deleteMetaField = async (
    shopId: string,
    metaFieldId: string,
    signal?: AbortSignal,
  ): Promise<void> => {
    return this.core.request<void>('DELETE', '/shops/{shopId}/meta-fields/{metaFieldId}', {
      pathParams: { shopId: shopId, metaFieldId: metaFieldId },
      signal,
    });
  };

  /** This method returns meta field with a given `metaFieldId` in the context of a given `shopId` */
  readonly getMetaField = async (
    shopId: string,
    metaFieldId: string,
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
    },
    signal?: AbortSignal,
  ): Promise<M.MetaField> => {
    return this.core.request<M.MetaField>('GET', '/shops/{shopId}/meta-fields/{metaFieldId}', {
      pathParams: { shopId: shopId, metaFieldId: metaFieldId },
      query: params ? { fields: params.fields } : undefined,
      signal,
    });
  };

  /** Sending a **GET** request to this URL returns a collection of meta field resources that belong to the given shop. You can narrow down the list of resources by passing proper query parameters (the list of which you can find below in the request params section). You can basically search by: * name * value * description * createdOn You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by. */
  readonly getMetaFields = async (
    shopId: string,
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
      /** Page number */
      page?: number;
      /** Requested number of results per page */
      perPage?: number;
      /** Search meta fields created from this date (GetResponse date format: yyyy-MM-ddTHH:mm:ss+HHMM, e.g. 2024-01-15T10:30:00+0000 -- no colon in the offset, no sub-second precision (unlike Date.prototype.toISOString())) */
      queryCreatedOnFrom?: string;
      /** Search meta fields created to this date (GetResponse date format: yyyy-MM-ddTHH:mm:ss+HHMM, e.g. 2024-01-15T10:30:00+0000 -- no colon in the offset, no sub-second precision (unlike Date.prototype.toISOString())) */
      queryCreatedOnTo?: string;
      /** Search meta fields by description */
      queryDescription?: string;
      /** Search meta fields by name */
      queryName?: string;
      /** Search meta fields by value */
      queryValue?: string;
      /** Sort by date */
      sortCreatedOn?: M.SortOrderEnum;
    },
    signal?: AbortSignal,
  ): Promise<M.MetaField[]> => {
    return this.core.request<M.MetaField[]>('GET', '/shops/{shopId}/meta-fields', {
      pathParams: { shopId: shopId },
      query: params
        ? {
            'query[name]': params.queryName,
            'query[description]': params.queryDescription,
            'query[value]': params.queryValue,
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

  /** Update the properties of a shop's meta field. You should send only those fields that need to be changed. The rest of the properties will stay the same. */
  readonly updateMetaField = async (
    shopId: string,
    metaFieldId: string,
    body: M.UpdateMetaField,
    signal?: AbortSignal,
  ): Promise<M.MetaField> => {
    return this.core.request<M.MetaField>('POST', '/shops/{shopId}/meta-fields/{metaFieldId}', {
      pathParams: { shopId: shopId, metaFieldId: metaFieldId },
      body,
      signal,
    });
  };
}
