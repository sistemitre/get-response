/** Operations tagged 'Products' in the GetResponse API. */

import type { Core } from '../core.js';
import type * as M from '../models.js';

export class ProductsResource {
  constructor(private readonly core: Core) {}

  /** Sending a **POST** request to this URL will create a new product resource. In order to create a new product, you need to send the product resource in the body of the request (remember that you need to serialize the body into a JSON string) You don't need a separate endpoint for each element (e.g. variant, category, meta-field). You can create them all with this method. Please note that categories aren't required, but if a product has at least one category, then one of those categories must be marked as default. This can be set by field `isDefault`. If none of the elements contains isDefault=true, then the system picks the first one from the collection by default. */
  readonly createProduct = async (
    shopId: string,
    body: M.NewProduct,
    signal?: AbortSignal,
  ): Promise<M.Product> => {
    return this.core.request<M.Product>('POST', '/shops/{shopId}/products', {
      pathParams: { shopId: shopId },
      body,
      signal,
    });
  };

  /** Delete product */
  readonly deleteProduct = async (
    shopId: string,
    productId: string,
    signal?: AbortSignal,
  ): Promise<void> => {
    return this.core.request<void>('DELETE', '/shops/{shopId}/products/{productId}', {
      pathParams: { shopId: shopId, productId: productId },
      signal,
    });
  };

  /** This method returns product according to the given `productId` in the context of a given `shopId`. */
  readonly getProductById = async (
    shopId: string,
    productId: string,
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
    },
    signal?: AbortSignal,
  ): Promise<M.Product> => {
    return this.core.request<M.Product>('GET', '/shops/{shopId}/products/{productId}', {
      pathParams: { shopId: shopId, productId: productId },
      query: params ? { fields: params.fields } : undefined,
      signal,
    });
  };

  /** Sending a **GET** request to this URL returns a collection of product resources that belong to the given shop. You can narrow down the list of resources by passing proper query parameters (the list of which you can find below in the request params section). You can basically search by: * name * vendor * category * categoryId * externalId * variantName * metaFieldNames * metaFieldValues * createdOn The `metaFieldNames` and `metaFieldValues` fields can be a list of values separated by a comma [,]. You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by. */
  readonly getProductList = async (
    shopId: string,
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
      /** Page number */
      page?: number;
      /** Requested number of results per page */
      perPage?: number;
      /** Search products by category ID */
      queryCategoryId?: string;
      /** Search products by category name */
      queryCategory?: string;
      /** Search products created from this date */
      queryCreatedOnFrom?: Record<string, unknown>;
      /** Search products created to this date */
      queryCreatedOnTo?: Record<string, unknown>;
      /** Search products by external ID */
      queryExternalId?: string;
      /** Search products by meta field name (the list of names must be separated by a comma [,]) */
      queryMetaFieldNames?: string;
      /** Search products by meta field value (the list of values must be separated by a comma [,]) */
      queryMetaFieldValues?: string;
      /** Search products by name */
      queryName?: string;
      /** Search products by product variant name */
      queryVariantName?: string;
      /** Search products by vendor */
      queryVendor?: string;
      /** Sort by date */
      sortCreatedOn?: M.SortOrderEnum;
      /** Sort by name */
      sortName?: M.SortOrderEnum;
    },
    signal?: AbortSignal,
  ): Promise<M.Product[]> => {
    return this.core.request<M.Product[]>('GET', '/shops/{shopId}/products', {
      pathParams: { shopId: shopId },
      query: params
        ? {
            'query[name]': params.queryName,
            'query[vendor]': params.queryVendor,
            'query[category]': params.queryCategory,
            'query[categoryId]': params.queryCategoryId,
            'query[externalId]': params.queryExternalId,
            'query[variantName]': params.queryVariantName,
            'query[metaFieldNames]': params.queryMetaFieldNames,
            'query[metaFieldValues]': params.queryMetaFieldValues,
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

  /** Update the properties of a shop's product. You should only send those fields that need to be changed. The remaining properties will stay the same. However, when updating variants, categories, and meta fields, you need to send entire collections. Individual fields can't be updated. If you want to update particular fields, you can do so using their specific endpoints, i.e.: * categories - `POST /v3/shops/{shopId}/categories/{categoryId}` * variants - POST `/v3/shops/{shopId}/products/{productId}/variants/{variantId}` * metaFields - `POST /v3/shops/{shopId}/meta-fields/{metaFieldId}` */
  readonly updateProduct = async (
    shopId: string,
    productId: string,
    body: M.UpdateProduct,
    signal?: AbortSignal,
  ): Promise<M.Product> => {
    return this.core.request<M.Product>('POST', '/shops/{shopId}/products/{productId}', {
      pathParams: { shopId: shopId, productId: productId },
      body,
      signal,
    });
  };

  /** This method makes it possible to assign meta fields. It doesn't remove or unassign meta fields. It returns a list of product meta fields. */
  readonly upsertMetaFields = async (
    shopId: string,
    productId: string,
    body: M.UpsertMetaField,
    signal?: AbortSignal,
  ): Promise<M.MetaField[]> => {
    return this.core.request<M.MetaField[]>(
      'POST',
      '/shops/{shopId}/products/{productId}/meta-fields',
      {
        pathParams: { shopId: shopId, productId: productId },
        body,
        signal,
      },
    );
  };

  /** This method makes it possible to assign product categories, and to set a default product category. This method doesn't remove or unassign product categories. It returns a list of product categories. Please note that if you assign only one category to a given product, that category is marked as default. If you try to remove the default mark, your change won't be executed. */
  readonly upsertProductCategories = async (
    shopId: string,
    productId: string,
    body: M.UpsertProductCategory,
    signal?: AbortSignal,
  ): Promise<M.BaseCategory[]> => {
    return this.core.request<M.BaseCategory[]>(
      'POST',
      '/shops/{shopId}/products/{productId}/categories',
      {
        pathParams: { shopId: shopId, productId: productId },
        body,
        signal,
      },
    );
  };
}
