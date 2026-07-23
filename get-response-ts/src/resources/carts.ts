/** Operations tagged 'Carts' in the GetResponse API. */

import type { Core } from '../core.js';
import type * as M from '../models.js';

export class CartsResource {
  constructor(private readonly core: Core) {}

  /** Sending a **POST** request to this URL will create a new cart resource. In order to create a new cart, you need to send the cart resource in the body of the request (remember that you need to serialize the body into a JSON string) */
  readonly createCart = async (
    shopId: string,
    body: M.NewCart,
    signal?: AbortSignal,
  ): Promise<M.Cart> => {
    return this.core.request<M.Cart>('POST', '/shops/{shopId}/carts', {
      pathParams: { shopId: shopId },
      body,
      signal,
    });
  };

  /** Delete cart */
  readonly deleteCart = async (
    shopId: string,
    cartId: string,
    signal?: AbortSignal,
  ): Promise<void> => {
    return this.core.request<void>('DELETE', '/shops/{shopId}/carts/{cartId}', {
      pathParams: { shopId: shopId, cartId: cartId },
      signal,
    });
  };

  /** This method returns cart with the given `cartId` in the context of a given `shopId` */
  readonly getCart = async (
    shopId: string,
    cartId: string,
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
    },
    signal?: AbortSignal,
  ): Promise<M.Cart> => {
    return this.core.request<M.Cart>('GET', '/shops/{shopId}/carts/{cartId}', {
      pathParams: { shopId: shopId, cartId: cartId },
      query: params ? { fields: params.fields } : undefined,
      signal,
    });
  };

  /** Sending a **GET** request to this URL returns a collection of cart resources that belong to the given shop. You can narrow down the list of resources by passing proper query parameters (the list of which you can find below in the request params section). You can basically search by: * externalId * createdOn You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by. */
  readonly getCarts = async (
    shopId: string,
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
      /** Page number */
      page?: number;
      /** Requested number of results per page */
      perPage?: number;
      /** Search carts created from this date */
      queryCreatedOnFrom?: string;
      /** Search carts created to this date */
      queryCreatedOnTo?: string;
      /** Search cart by external ID */
      queryExternalId?: string;
      /** Sort by date */
      sortCreatedOn?: M.SortOrderEnum;
    },
    signal?: AbortSignal,
  ): Promise<M.Cart[]> => {
    return this.core.request<M.Cart[]>('GET', '/shops/{shopId}/carts', {
      pathParams: { shopId: shopId },
      query: params
        ? {
            'query[createdOn][from]': params.queryCreatedOnFrom,
            'query[createdOn][to]': params.queryCreatedOnTo,
            'query[externalId]': params.queryExternalId,
            'sort[createdOn]': params.sortCreatedOn,
            fields: params.fields,
            perPage: params.perPage,
            page: params.page,
          }
        : undefined,
      signal,
    });
  };

  /** Update properties of the shop cart. You should send only those fields that need to be changed. The rest of the properties will stay the same. In case of selectedVariants, when the collection is updated, the old one is completely removed. */
  readonly updateCart = async (
    shopId: string,
    cartId: string,
    body: M.UpdateCart,
    signal?: AbortSignal,
  ): Promise<M.Cart> => {
    return this.core.request<M.Cart>('POST', '/shops/{shopId}/carts/{cartId}', {
      pathParams: { shopId: shopId, cartId: cartId },
      body,
      signal,
    });
  };
}
