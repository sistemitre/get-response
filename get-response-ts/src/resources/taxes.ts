/** Operations tagged 'Taxes' in the GetResponse API. */

import type { Core } from '../core.js';
import type * as M from '../models.js';

export class TaxesResource {
  constructor(private readonly core: Core) {}

  /** Sending a **POST** request to this URL will create a new tax resource. In order to create a new tax, you need to send a tax resource in the body of the request (remember that you need to serialize the body into a JSON string) */
  readonly createTax = async (
    shopId: string,
    body: M.NewTax,
    signal?: AbortSignal,
  ): Promise<M.Tax> => {
    return this.core.request<M.Tax>('POST', '/shops/{shopId}/taxes', {
      pathParams: { shopId: shopId },
      body,
      signal,
    });
  };

  /** Delete tax by ID */
  readonly deleteTax = async (
    shopId: string,
    taxId: string,
    signal?: AbortSignal,
  ): Promise<void> => {
    return this.core.request<void>('DELETE', '/shops/{shopId}/taxes/{taxId}', {
      pathParams: { shopId: shopId, taxId: taxId },
      signal,
    });
  };

  /** This method returns tax with a given `taxId` in the context of a given `shopId` */
  readonly getTaxById = async (
    shopId: string,
    taxId: string,
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
    },
    signal?: AbortSignal,
  ): Promise<M.Tax> => {
    return this.core.request<M.Tax>('GET', '/shops/{shopId}/taxes/{taxId}', {
      pathParams: { shopId: shopId, taxId: taxId },
      query: params ? { fields: params.fields } : undefined,
      signal,
    });
  };

  /** Sending **GET** request to this URL returns a collection of tax resources that belong to the given shop. You can narrow down the list of resources by passing proper query parameters (the list of which you can find below, in the request params section). You can basically search by: * name * createdOn You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by. */
  readonly getTaxList = async (
    shopId: string,
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
      /** Page number */
      page?: number;
      /** Requested number of results per page */
      perPage?: number;
      /** Search tax created from this date */
      queryCreatedOnFrom?: string;
      /** Search tax created to this date */
      queryCreatedOnTo?: string;
      /** Search tax by name */
      queryName?: string;
      /** Sort by date */
      sortCreatedOn?: M.SortOrderEnum;
    },
    signal?: AbortSignal,
  ): Promise<M.Tax[]> => {
    return this.core.request<M.Tax[]>('GET', '/shops/{shopId}/taxes', {
      pathParams: { shopId: shopId },
      query: params
        ? {
            'query[name]': params.queryName,
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

  /** Update the properties of the shop tax. You should only send the fields that need to be changed. The rest of the properties will stay the same. */
  readonly updateTax = async (
    shopId: string,
    taxId: string,
    body: M.UpdateTax,
    signal?: AbortSignal,
  ): Promise<M.Tax> => {
    return this.core.request<M.Tax>('POST', '/shops/{shopId}/taxes/{taxId}', {
      pathParams: { shopId: shopId, taxId: taxId },
      body,
      signal,
    });
  };
}
