/** Operations tagged 'Shops' in the GetResponse API. */

import type { Core } from '../core.js';
import type * as M from '../models.js';

export class ShopsResource {
  constructor(private readonly core: Core) {}

  /** This method makes it possible to create a new shop. */
  readonly createShop = async (body: M.NewShop, signal?: AbortSignal): Promise<M.ShopDetails> => {
    return this.core.request<M.ShopDetails>('POST', '/shops', {
      body,
      signal,
    });
  };

  /** This method deletes a shop. */
  readonly deleteShop = async (shopId: string, signal?: AbortSignal): Promise<void> => {
    return this.core.request<void>('DELETE', '/shops/{shopId}', {
      pathParams: { shopId: shopId },
      signal,
    });
  };

  /** This method returns the shop according to the given `shopId` */
  readonly getShopById = async (
    shopId: string,
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
    },
    signal?: AbortSignal,
  ): Promise<M.ShopDetails> => {
    return this.core.request<M.ShopDetails>('GET', '/shops/{shopId}', {
      pathParams: { shopId: shopId },
      query: params ? { fields: params.fields } : undefined,
      signal,
    });
  };

  /** Sending a **GET** request to this URL returns a collection of shop resources. You can narrow down the list of resources by passing proper query parameters (the list of which you can find below in the request params section). You can basically search by: * name The `name` fields can be a pattern and we'll try to match this phrase. You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by. */
  readonly getShopList = async (
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
      /** Page number */
      page?: number;
      /** Requested number of results per page */
      perPage?: number;
      /** Search shop by name */
      queryName?: string;
      /** Sort by date */
      sortCreatedOn?: M.SortOrderEnum;
      /** Sort by name */
      sortName?: M.SortOrderEnum;
    },
    signal?: AbortSignal,
  ): Promise<Record<string, unknown>[]> => {
    return this.core.request<Record<string, unknown>[]>('GET', '/shops', {
      query: params
        ? {
            'query[name]': params.queryName,
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

  /** This makes it possible to update shop preferences. You should send only those fields that need to be changed. The rest of the properties remain the same. */
  readonly updateShop = async (
    shopId: string,
    body: M.UpdateShop,
    signal?: AbortSignal,
  ): Promise<M.ShopDetails> => {
    return this.core.request<M.ShopDetails>('POST', '/shops/{shopId}', {
      pathParams: { shopId: shopId },
      body,
      signal,
    });
  };
}
