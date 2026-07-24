/** Operations tagged 'Categories' in the GetResponse API. */

import type { Core } from '../core.js';
import type * as M from '../models.js';

export class CategoriesResource {
  constructor(private readonly core: Core) {}

  /** Create shop category. You can pass the `parentId` parameter to create a sub-category of a given parent. Unlike most **POST** methods, this call is idempotent, that is: sending the same request 10 times will not create 10 new categories. Only one category will be created. */
  readonly createCategory = async (
    shopId: string,
    body: M.NewCategory,
    signal?: AbortSignal,
  ): Promise<M.Category> => {
    return this.core.request<M.Category>('POST', '/shops/{shopId}/categories', {
      pathParams: { shopId: shopId },
      body,
      signal,
    });
  };

  /** Delete category */
  readonly deleteCategory = async (
    shopId: string,
    categoryId: string,
    signal?: AbortSignal,
  ): Promise<void> => {
    return this.core.request<void>('DELETE', '/shops/{shopId}/categories/{categoryId}', {
      pathParams: { shopId: shopId, categoryId: categoryId },
      signal,
    });
  };

  /** Sending a **GET** request to this URL returns a collection of category resources that belong to the given shop. You can narrow down the list of resources by passing proper query parameters (the list of which you can find below in the request params section). You can basically search by: *name * createdOn * parentId The `name` fields can be a pattern and we'll try to match this phrase. The `parentId` will search for sub-categories of a given parent category. You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by. */
  readonly getCategories = async (
    shopId: string,
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
      /** Page number */
      page?: number;
      /** Requested number of results per page */
      perPage?: number;
      /** Search categories by external ID */
      queryExternalId?: string;
      /** Search category by name */
      queryName?: string;
      /** Search categories by their parent */
      queryParentId?: string;
      /** Show categories starting from this date (GetResponse date format: yyyy-MM-ddTHH:mm:ss+HHMM, e.g. 2024-01-15T10:30:00+0000 -- no colon in the offset, no sub-second precision (unlike Date.prototype.toISOString())) */
      searchCreatedAtFrom?: string;
      /** Show categories starting to this date (GetResponse date format: yyyy-MM-ddTHH:mm:ss+HHMM, e.g. 2024-01-15T10:30:00+0000 -- no colon in the offset, no sub-second precision (unlike Date.prototype.toISOString())) */
      searchCreatedAtTo?: string;
      /** Sort by date */
      sortCreatedAt?: M.SortOrderEnum;
      /** Sort by name */
      sortName?: M.SortOrderEnum;
    },
    signal?: AbortSignal,
  ): Promise<M.Category[]> => {
    return this.core.request<M.Category[]>('GET', '/shops/{shopId}/categories', {
      pathParams: { shopId: shopId },
      query: params
        ? {
            'query[name]': params.queryName,
            'query[parentId]': params.queryParentId,
            'query[externalId]': params.queryExternalId,
            'search[createdAt][from]': params.searchCreatedAtFrom,
            'search[createdAt][to]': params.searchCreatedAtTo,
            'sort[name]': params.sortName,
            'sort[createdAt]': params.sortCreatedAt,
            fields: params.fields,
            perPage: params.perPage,
            page: params.page,
          }
        : undefined,
      signal,
    });
  };

  /** This method returns a category according to the given `categoryId`. */
  readonly getCategory = async (
    shopId: string,
    categoryId: string,
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
    },
    signal?: AbortSignal,
  ): Promise<M.Category> => {
    return this.core.request<M.Category>('GET', '/shops/{shopId}/categories/{categoryId}', {
      pathParams: { shopId: shopId, categoryId: categoryId },
      query: params ? { fields: params.fields } : undefined,
      signal,
    });
  };

  /** Update the properties of the shop category. You can specify a `parentId` to assign a category as sub-category for an existing category. You should send only those fields that need to be changed. The rest of the properties will stay the same. */
  readonly updateCategory = async (
    shopId: string,
    categoryId: string,
    body: M.Category,
    signal?: AbortSignal,
  ): Promise<M.Category> => {
    return this.core.request<M.Category>('POST', '/shops/{shopId}/categories/{categoryId}', {
      pathParams: { shopId: shopId, categoryId: categoryId },
      body,
      signal,
    });
  };
}
