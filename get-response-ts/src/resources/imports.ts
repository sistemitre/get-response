/** Operations tagged 'Imports' in the GetResponse API. */

import type { Core } from '../core.js';
import type * as M from '../models.js';

export class ImportsResource {
  constructor(private readonly core: Core) {}

  /** This endpoint lets you schedule a contact import. That way, you can add and update your contacts using a single API call. Since API imports are asynchronous, you should check periodically for updates while your original API request is being processed. To keep track of your import status, use [GET import](https://apireference.getresponse.com/#operation/getImportById) (provide the importId from the response), or subscribe to an [import finished](https://apidocs.getresponse.com/v3/payloads#contacts-import-finished) webhook. Please note, that this endpoint has **specific rate limits** - for details please refer to [Create Import Limits](https://apidocs.getresponse.com/v3/case-study/create-import#limits). For more information on imports, check our [API Docs](https://apidocs.getresponse.com/v3/case-study/create-import) or [Help Center](https://www.getresponse.com/help/how-do-i-prepare-a-file-for-import.html) */
  readonly createImport = async (body: M.NewImport, signal?: AbortSignal): Promise<M.Import> => {
    return this.core.request<M.Import>('POST', '/imports', {
      body,
      signal,
    });
  };

  /** Get import details by ID. */
  readonly getImportById = async (
    importId: string,
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
    },
    signal?: AbortSignal,
  ): Promise<M.Import> => {
    return this.core.request<M.Import>('GET', '/imports/{importId}', {
      pathParams: { importId: importId },
      query: params ? { fields: params.fields } : undefined,
      signal,
    });
  };

  /** You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by. */
  readonly getImportList = async (
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
      /** Page number */
      page?: number;
      /** Requested number of results per page */
      perPage?: number;
      /** Search imports by campaignId */
      queryCampaignId?: string;
      /** Search imports created from this date */
      queryCreatedOnFrom?: string;
      /** Search imports created to this date */
      queryCreatedOnTo?: string;
      /** Sort imports by inserted contact count */
      sortAddedContacts?: M.SortOrderEnum;
      /** Sort imports by campaign name */
      sortCampaignName?: M.SortOrderEnum;
      /** Sort imports by creation date */
      sortCreatedOn?: M.SortOrderEnum;
      /** Sort imports by finish date */
      sortFinishedOn?: M.SortOrderEnum;
      /** Sort imports by invalid contact count */
      sortInvalidContacts?: M.SortOrderEnum;
      /** Sort imports by status (uploaded, to_review, approved, finished, rejected, canceled) */
      sortStatus?: M.SortOrderEnum;
      /** Sort imports by updated contact count */
      sortUpdatedContacts?: M.SortOrderEnum;
      /** Sort imports by uploaded contact count */
      sortUploadedContacts?: M.SortOrderEnum;
    },
    signal?: AbortSignal,
  ): Promise<M.Import[]> => {
    return this.core.request<M.Import[]>('GET', '/imports', {
      query: params
        ? {
            'query[campaignId]': params.queryCampaignId,
            'query[createdOn][from]': params.queryCreatedOnFrom,
            'query[createdOn][to]': params.queryCreatedOnTo,
            'sort[createdOn]': params.sortCreatedOn,
            'sort[finishedOn]': params.sortFinishedOn,
            'sort[campaignName]': params.sortCampaignName,
            'sort[uploadedContacts]': params.sortUploadedContacts,
            'sort[updatedContacts]': params.sortUpdatedContacts,
            'sort[addedContacts]': params.sortAddedContacts,
            'sort[invalidContacts]': params.sortInvalidContacts,
            'sort[status]': params.sortStatus,
            fields: params.fields,
            perPage: params.perPage,
            page: params.page,
          }
        : undefined,
      signal,
    });
  };
}
