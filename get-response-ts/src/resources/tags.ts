/** Operations tagged 'Tags' in the GetResponse API. */

import type { Core } from '../core.js';
import type * as M from '../models.js';

export class TagsResource {
  constructor(private readonly core: Core) {}

  /** Add a new tag */
  readonly createTag = async (body: M.NewTag, signal?: AbortSignal): Promise<M.TagDetails> => {
    return this.core.request<M.TagDetails>('POST', '/tags', {
      body,
      signal,
    });
  };

  /** Delete tag by ID */
  readonly deleteTag = async (tagId: string, signal?: AbortSignal): Promise<void> => {
    return this.core.request<void>('DELETE', '/tags/{tagId}', {
      pathParams: { tagId: tagId },
      signal,
    });
  };

  /** Retrieve a specific tag by its ID */
  readonly getTagById = async (
    tagId: string,
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
    },
    signal?: AbortSignal,
  ): Promise<M.TagDetails> => {
    return this.core.request<M.TagDetails>('GET', '/tags/{tagId}', {
      pathParams: { tagId: tagId },
      query: params ? { fields: params.fields } : undefined,
      signal,
    });
  };

  /** Provides a list of tags. You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by. */
  readonly getTagsList = async (
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
      /** Page number */
      page?: number;
      /** Requested number of results per page */
      perPage?: number;
      /** Search tags created from this date */
      queryCreatedAtFrom?: string;
      /** Search tags created to this date */
      queryCreatedAtTo?: string;
      /** Search tags by name */
      queryName?: string;
      /** Sort tags by creation date */
      sortCreatedAt?: M.SortOrderEnum;
      /** Sort by name */
      sortName?: M.SortOrderEnum;
    },
    signal?: AbortSignal,
  ): Promise<M.Tag[]> => {
    return this.core.request<M.Tag[]>('GET', '/tags', {
      query: params
        ? {
            'query[name]': params.queryName,
            'query[createdAt][from]': params.queryCreatedAtFrom,
            'query[createdAt][to]': params.queryCreatedAtTo,
            'sort[createdAt]': params.sortCreatedAt,
            'sort[name]': params.sortName,
            fields: params.fields,
            perPage: params.perPage,
            page: params.page,
          }
        : undefined,
      signal,
    });
  };

  /** Updating the tag is not allowed. The method currently performs no update actions and only returns the current tag details. */
  readonly updateTag = async (
    tagId: string,
    body: M.UpdateTag,
    signal?: AbortSignal,
  ): Promise<M.TagDetails> => {
    return this.core.request<M.TagDetails>('POST', '/tags/{tagId}', {
      pathParams: { tagId: tagId },
      body,
      signal,
    });
  };
}
