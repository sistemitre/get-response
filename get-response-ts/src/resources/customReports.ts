/** Operations tagged 'Custom Reports' in the GetResponse API. */

import type { Core } from '../core.js';
import type * as M from '../models.js';

export class CustomReportsResource {
  constructor(private readonly core: Core) {}

  /** The endpoint allows scheduling a custom report of a specific type for a given time period. Depending on the report type, you can also narrow down the data using appropriate filters. <strong>Important:</strong> The reports you can generate depend on your pricing plan. More information about using the endpoint, along with examples, can be found in the Case Study section of the [API documentation](http://apidocs.getresponse.com/v3/case-study/custom-reports-scheduling). */
  readonly createCustomReport = async (
    body: M.BaseCreateCustomReport,
    signal?: AbortSignal,
  ): Promise<M.CustomReportDetails> => {
    return this.core.request<M.CustomReportDetails>('POST', '/custom-reports', {
      body,
      signal,
    });
  };

  /** The endpoint allows retrieving detailed information about a custom report based on the provided `customReportId`. It returns report data, including: * details about the report, * generation statuses of the report files, * URLs from which the report files can be downloaded. More information on using custom reports can be found in the Case Study section of the [API documentation](http://apidocs.getresponse.com/v3/case-study/custom-reports). */
  readonly getCustomReportDetails = async (
    customReportId: string,
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
    },
    signal?: AbortSignal,
  ): Promise<M.CustomReportDetails> => {
    return this.core.request<M.CustomReportDetails>('GET', '/custom-reports/{customReportId}', {
      pathParams: { customReportId: customReportId },
      query: params ? { fields: params.fields } : undefined,
      signal,
    });
  };

  /** You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by. */
  readonly getCustomReportList = async (
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
      /** Page number */
      page?: number;
      /** Requested number of results per page */
      perPage?: number;
      /** Search custom reports by name */
      queryName?: string;
      /** Sort custom reports by frequency */
      sortFrequency?: M.SortOrderEnum;
      /** Sort custom reports by generation date */
      sortGeneratedAt?: M.SortOrderEnum;
      /** Sort custom reports by name */
      sortName?: M.SortOrderEnum;
    },
    signal?: AbortSignal,
  ): Promise<M.CustomReport[]> => {
    return this.core.request<M.CustomReport[]>('GET', '/custom-reports', {
      query: params
        ? {
            'query[name]': params.queryName,
            'sort[name]': params.sortName,
            'sort[frequency]': params.sortFrequency,
            'sort[generatedAt]': params.sortGeneratedAt,
            fields: params.fields,
            perPage: params.perPage,
            page: params.page,
          }
        : undefined,
      signal,
    });
  };
}
