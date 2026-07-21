/** Operations tagged 'File Library' in the GetResponse API. */

import type { Core } from '../core.js';
import type * as M from '../models.js';

export class FileLibraryResource {
  constructor(private readonly core: Core) {}

  /** Create a file */
  readonly createFile = async (body: M.NewFile, signal?: AbortSignal): Promise<M.File> => {
    return this.core.request<M.File>('POST', '/file-library/files', {
      body,
      signal,
    });
  };

  /** Create a folder */
  readonly createFolder = async (body: M.NewFolder, signal?: AbortSignal): Promise<M.Folder[]> => {
    return this.core.request<M.Folder[]>('POST', '/file-library/folders', {
      body,
      signal,
    });
  };

  /** Delete file by file ID */
  readonly deleteFile = async (fileId: string, signal?: AbortSignal): Promise<void> => {
    return this.core.request<void>('DELETE', '/file-library/files/{fileId}', {
      pathParams: { fileId: fileId },
      signal,
    });
  };

  /** Delete folder by folder ID */
  readonly deleteFolder = async (folderId: string, signal?: AbortSignal): Promise<void> => {
    return this.core.request<void>('DELETE', '/file-library/folders/{folderId}', {
      pathParams: { folderId: folderId },
      signal,
    });
  };

  /** Get file by ID */
  readonly getFileById = async (
    fileId: string,
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
    },
    signal?: AbortSignal,
  ): Promise<M.File> => {
    return this.core.request<M.File>('GET', '/file-library/files/{fileId}', {
      pathParams: { fileId: fileId },
      query: params ? { fields: params.fields } : undefined,
      signal,
    });
  };

  /** By default, you can only search files in the root directory. To search for files in all folders, use the parameter `query[allFolders]=true`. To search for files in a specified folder, use the parameter `query[folderId]=<folderId>`. **Note: these two parameters can't be used together**. You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by. */
  readonly getFileList = async (
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
      /** Page number */
      page?: number;
      /** Requested number of results per page */
      perPage?: number;
      /** Return files from all folders, including the root folder. **This parameter can't be used together with ** `query[folderId]` */
      queryAllFolders?: M.StringBooleanEnum;
      /** Search for files in a specific folder. **This parameter can't be used together with ** `query[allFolders]` */
      queryFolderId?: string;
      /** Search for files by group */
      queryGroup?: M.FileGroup;
      /** Search for files by name */
      queryName?: string;
      /** Sort files by group */
      sortGroup?: M.SortOrderEnum;
      /** Sort by name */
      sortName?: M.SortOrderEnum;
      /** Sort files by size */
      sortSize?: M.SortOrderEnum;
    },
    signal?: AbortSignal,
  ): Promise<M.File[]> => {
    return this.core.request<M.File[]>('GET', '/file-library/files', {
      query: params
        ? {
            'query[allFolders]': params.queryAllFolders,
            'query[folderId]': params.queryFolderId,
            'query[name]': params.queryName,
            'query[group]': params.queryGroup,
            'sort[name]': params.sortName,
            'sort[group]': params.sortGroup,
            'sort[size]': params.sortSize,
            fields: params.fields,
            perPage: params.perPage,
            page: params.page,
          }
        : undefined,
      signal,
    });
  };

  /** You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by. */
  readonly getFolderList = async (
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
      /** Page number */
      page?: number;
      /** Requested number of results per page */
      perPage?: number;
      /** Search folders by name */
      queryName?: string;
      /** Sort folders by creation date */
      sortCreatedOn?: M.SortOrderEnum;
      /** Sort folders by name */
      sortName?: M.SortOrderEnum;
      /** Sort folders by size */
      sortSize?: M.SortOrderEnum;
    },
    signal?: AbortSignal,
  ): Promise<M.Folder[]> => {
    return this.core.request<M.Folder[]>('GET', '/file-library/folders', {
      query: params
        ? {
            'query[name]': params.queryName,
            'sort[name]': params.sortName,
            'sort[size]': params.sortSize,
            'sort[createdOn]': params.sortCreatedOn,
            fields: params.fields,
            perPage: params.perPage,
            page: params.page,
          }
        : undefined,
      signal,
    });
  };

  /** Get storage space information */
  readonly quota = async (signal?: AbortSignal): Promise<M.Quota> => {
    return this.core.request<M.Quota>('GET', '/file-library/quota', {
      signal,
    });
  };
}
