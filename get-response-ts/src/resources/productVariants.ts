/** Operations tagged 'Product Variants' in the GetResponse API. */

import type { Core } from '../core.js';
import type * as M from '../models.js';

export class ProductVariantsResource {
  constructor(private readonly core: Core) {}

  /** Sending a **POST** request to this URL will create a new product variant resource. In order to create a new product variant, you need to send a product variant resource in the body of the request (remember that you need to serialize the body into a JSON string) There is no need to create every element (like: image, meta field, tax) one by one by their own endpoints. All these elements can be created during this method. */
  readonly createProductVariant = async (
    shopId: string,
    productId: string,
    body: M.NewProductVariant,
    signal?: AbortSignal,
  ): Promise<M.ProductVariant> => {
    return this.core.request<M.ProductVariant>(
      'POST',
      '/shops/{shopId}/products/{productId}/variants',
      {
        pathParams: { shopId: shopId, productId: productId },
        body,
        signal,
      },
    );
  };

  /** Delete product variant */
  readonly deleteProductVariant = async (
    shopId: string,
    productId: string,
    variantId: string,
    signal?: AbortSignal,
  ): Promise<void> => {
    return this.core.request<void>(
      'DELETE',
      '/shops/{shopId}/products/{productId}/variants/{variantId}',
      {
        pathParams: { shopId: shopId, productId: productId, variantId: variantId },
        signal,
      },
    );
  };

  /** This method returns product variant according to the given `variantId` in the context of a given `shopId` and `productId` */
  readonly getProductVariantById = async (
    shopId: string,
    productId: string,
    variantId: string,
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
    },
    signal?: AbortSignal,
  ): Promise<M.ProductVariant> => {
    return this.core.request<M.ProductVariant>(
      'GET',
      '/shops/{shopId}/products/{productId}/variants/{variantId}',
      {
        pathParams: { shopId: shopId, productId: productId, variantId: variantId },
        query: params ? { fields: params.fields } : undefined,
        signal,
      },
    );
  };

  /** Sending a **GET** request to this URL returns a collection of product variant resources that belong to the given shop and product. You can narrow down the list of resources by passing proper query parameters (the list of which you can find below in the request params section). You can basically search by: * name * sku * description The `description` fields can be a pattern and we'll try to match this phrase. */
  readonly getProductVariantList = async (
    shopId: string,
    productId: string,
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
      /** Page number */
      page?: number;
      /** Requested number of results per page */
      perPage?: number;
      /** Show variants starting from this date (GetResponse date format: yyyy-MM-ddTHH:mm:ss+HHMM, e.g. 2024-01-15T10:30:00+0000 -- no colon in the offset, no sub-second precision (unlike Date.prototype.toISOString())) */
      queryCreatedAtFrom?: string;
      /** Show variants starting to this date (GetResponse date format: yyyy-MM-ddTHH:mm:ss+HHMM, e.g. 2024-01-15T10:30:00+0000 -- no colon in the offset, no sub-second precision (unlike Date.prototype.toISOString())) */
      queryCreatedAtTo?: string;
      /** Search variant by description */
      queryDescription?: string;
      /** Search variant by external ID */
      queryExternalId?: string;
      /** Search variant by name */
      queryName?: string;
      /** Search variant by SKU */
      querySku?: string;
      /** Sort by date */
      sortCreatedOn?: M.SortOrderEnum;
    },
    signal?: AbortSignal,
  ): Promise<M.ProductVariant[]> => {
    return this.core.request<M.ProductVariant[]>(
      'GET',
      '/shops/{shopId}/products/{productId}/variants',
      {
        pathParams: { shopId: shopId, productId: productId },
        query: params
          ? {
              'query[name]': params.queryName,
              'query[sku]': params.querySku,
              'query[description]': params.queryDescription,
              'query[externalId]': params.queryExternalId,
              'query[createdAt][from]': params.queryCreatedAtFrom,
              'query[createdAt][to]': params.queryCreatedAtTo,
              'sort[createdOn]': params.sortCreatedOn,
              fields: params.fields,
              perPage: params.perPage,
              page: params.page,
            }
          : undefined,
        signal,
      },
    );
  };

  /** Update properties of a product variant. You should send only those fields that need to be changed. The remaining properties will stay the same. However, when updating metafields, images, and taxes, you need to send entire collections. Individual fields can't be updated. If you want to update particular metafields or tax resources, you can do so using their particular endpoints, i.e: * taxes - `POST /v3/shops/{shopId}/taxes/{taxId}` * metaFields - `POST /v3/shops/{shopId}/meta-fields/{metaFieldId}` */
  readonly updateProductVariant = async (
    shopId: string,
    productId: string,
    variantId: string,
    body: M.UpdateProductVariant,
    signal?: AbortSignal,
  ): Promise<M.ProductVariant> => {
    return this.core.request<M.ProductVariant>(
      'POST',
      '/shops/{shopId}/products/{productId}/variants/{variantId}',
      {
        pathParams: { shopId: shopId, productId: productId, variantId: variantId },
        body,
        signal,
      },
    );
  };
}
