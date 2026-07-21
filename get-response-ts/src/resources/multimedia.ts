/** Operations tagged 'Multimedia' in the GetResponse API. */

import type { Core } from '../core.js';
import type * as M from '../models.js';

export class MultimediaResource {
  constructor(private readonly core: Core) {}

  /** Get images list */
  readonly getImageList = async (
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
      /** Page number */
      page?: number;
      /** Requested number of results per page */
      perPage?: number;
    },
    signal?: AbortSignal,
  ): Promise<M.ImageDetails[]> => {
    return this.core.request<M.ImageDetails[]>('GET', '/multimedia', {
      query: params
        ? { fields: params.fields, perPage: params.perPage, page: params.page }
        : undefined,
      signal,
    });
  };

  /** Upload image Sends `file` as multipart/form-data. */
  readonly uploadImage = async (
    file: Blob | ArrayBuffer | Uint8Array,
    filename = 'upload',
    signal?: AbortSignal,
  ): Promise<M.ImageDetails> => {
    const blob = file instanceof Blob ? file : new Blob([file as unknown as BlobPart]);
    const form = new FormData();
    form.append('file', blob, filename);
    return this.core.request<M.ImageDetails>('POST', '/multimedia', {
      body: form,
      signal,
    });
  };
}
