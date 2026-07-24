/** Operations tagged 'Orders' in the GetResponse API. */

import type { Core } from '../core.js';
import type * as M from '../models.js';

export class OrdersResource {
  constructor(private readonly core: Core) {}

  /** Sending a **POST** request to this URL will create a new order resource. In order to create a new order, you need to send the order resource in the body of the request (remember that you need to serialize the body into a JSON string). */
  readonly createOrder = async (
    shopId: string,
    body: M.NewOrder,
    params?: {
      /** The additional flags parameter with the value `skipAutomation` will skip the triggering `Make a purchase` element in an automated workflow */
      additionalFlags?: string;
    },
    signal?: AbortSignal,
  ): Promise<M.OrderResponse> => {
    return this.core.request<M.OrderResponse>('POST', '/shops/{shopId}/orders', {
      pathParams: { shopId: shopId },
      query: params ? { additionalFlags: params.additionalFlags } : undefined,
      body,
      signal,
    });
  };

  /** Delete order */
  readonly deleteOrder = async (
    shopId: string,
    orderId: string,
    signal?: AbortSignal,
  ): Promise<void> => {
    return this.core.request<void>('DELETE', '/shops/{shopId}/orders/{orderId}', {
      pathParams: { shopId: shopId, orderId: orderId },
      signal,
    });
  };

  /** This method returns the order according to the given `orderId`. */
  readonly getOrderById = async (
    shopId: string,
    orderId: string,
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
    },
    signal?: AbortSignal,
  ): Promise<M.OrderResponse> => {
    return this.core.request<M.OrderResponse>('GET', '/shops/{shopId}/orders/{orderId}', {
      pathParams: { shopId: shopId, orderId: orderId },
      query: params ? { fields: params.fields } : undefined,
      signal,
    });
  };

  /** Sending a **GET** request to this URL returns a collection of order resources that belong to the given shop. You can narrow down the list of resources by passing proper query parameters (the list of which you can find below in the request params section). You can basically search by: * description * status * externalId * processedAt The `description` fields can be a pattern and we'll try to match this phrase. You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by. */
  readonly getOrderList = async (
    shopId: string,
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
      /** Page number */
      page?: number;
      /** Requested number of results per page */
      perPage?: number;
      /** Search order by description */
      queryDescription?: string;
      /** Search order by external ID */
      queryExternalId?: string;
      /** Show orders processed from this date (GetResponse date format: yyyy-MM-ddTHH:mm:ss+HHMM, e.g. 2024-01-15T10:30:00+0000 -- no colon in the offset, no sub-second precision (unlike Date.prototype.toISOString())) */
      queryProcessedAtFrom?: string;
      /** Show orders processed to this date (GetResponse date format: yyyy-MM-ddTHH:mm:ss+HHMM, e.g. 2024-01-15T10:30:00+0000 -- no colon in the offset, no sub-second precision (unlike Date.prototype.toISOString())) */
      queryProcessedAtTo?: string;
      /** Search order by status */
      queryStatus?: string;
      /** Sort by date */
      sortCreatedOn?: M.SortOrderEnum;
    },
    signal?: AbortSignal,
  ): Promise<M.Order[]> => {
    return this.core.request<M.Order[]>('GET', '/shops/{shopId}/orders', {
      pathParams: { shopId: shopId },
      query: params
        ? {
            'query[description]': params.queryDescription,
            'query[status]': params.queryStatus,
            'query[externalId]': params.queryExternalId,
            'query[processedAt][from]': params.queryProcessedAtFrom,
            'query[processedAt][to]': params.queryProcessedAtTo,
            'sort[createdOn]': params.sortCreatedOn,
            fields: params.fields,
            perPage: params.perPage,
            page: params.page,
          }
        : undefined,
      signal,
    });
  };

  /** Update the properties of a shop's order. You should send only those fields that need to be changed. The rest of the properties will stay the same. However, in case of `billingAddress` and `shippingAddress`, you must send the entire representation. Individual fields can't be updated. If you want to update individual fields of an address, you can do so using `POST /v3/addresses/{addressId}`. In case of `selectedVariants`, when the collection is updated, the old collection is completely removed. The same goes for meta fields. Individual fields can't be updated either. The full representations of `selectedVariants` and `metaFields` must be sent instead. */
  readonly updateOrder = async (
    shopId: string,
    orderId: string,
    body: M.UpdateOrder,
    params?: {
      /** The additional flags parameter with the value `skipAutomation` will skip the triggering `Make a purchase` element in an automated workflow */
      additionalFlags?: string;
    },
    signal?: AbortSignal,
  ): Promise<M.OrderResponse> => {
    return this.core.request<M.OrderResponse>('POST', '/shops/{shopId}/orders/{orderId}', {
      pathParams: { shopId: shopId, orderId: orderId },
      query: params ? { additionalFlags: params.additionalFlags } : undefined,
      body,
      signal,
    });
  };
}
