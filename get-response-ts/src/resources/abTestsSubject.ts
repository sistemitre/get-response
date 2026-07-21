/** Operations tagged 'A/B tests - subject' in the GetResponse API. */

import type { Core } from '../core.js';
import type * as M from '../models.js';

export class AbTestsSubjectResource {
  constructor(private readonly core: Core) {}

  /** You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by. */
  readonly getAbTestSubjectList = async (
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
      /** Page number */
      page?: number;
      /** Requested number of results per page */
      perPage?: number;
      /** Search A/B tests by ID. You can search for multiple A/B tests using comma-separated values, for example, `pgIH, CNXF` */
      queryAbTestId?: string;
      /** Search A/B tests by list ID. You can search for multiple A/B tests using comma-separated list IDs, for example, `pgIH, CNXF` */
      queryCampaignId?: string;
      /** Search A/B tests by name */
      queryName?: string;
      /** Search A/B tests by stage */
      queryStage?: M.GetAbTestSubjectListQueryStage;
      /** Sort by name */
      sortName?: M.SortOrderEnum;
      /** Sort by send date */
      sortSendOn?: M.SortOrderEnum;
      /** Sort by stage */
      sortStage?: M.SortOrderEnum;
      /** Sort by total delivered */
      sortTotalDelivered?: M.SortOrderEnum;
    },
    signal?: AbortSignal,
  ): Promise<M.AbtestsSubjectListItem[]> => {
    return this.core.request<M.AbtestsSubjectListItem[]>('GET', '/ab-tests/subject', {
      query: params
        ? {
            'query[name]': params.queryName,
            'query[stage]': params.queryStage,
            'query[abTestId]': params.queryAbTestId,
            'query[campaignId]': params.queryCampaignId,
            'sort[name]': params.sortName,
            'sort[stage]': params.sortStage,
            'sort[sendOn]': params.sortSendOn,
            'sort[totalDelivered]': params.sortTotalDelivered,
            fields: params.fields,
            perPage: params.perPage,
            page: params.page,
          }
        : undefined,
      signal,
    });
  };

  /** This method allows you to schedule the cancellation of an A/B test. Cancelling an A/B test is an asynchronous operation. */
  readonly cancelAbTest = async (abTestId: string, signal?: AbortSignal): Promise<void> => {
    return this.core.request<void>('POST', '/ab-tests/{abTestId}/cancel', {
      pathParams: { abTestId: abTestId },
      signal,
    });
  };

  /** Create a new A/B test */
  readonly createSubjectAbTest = async (
    body: M.NewAbtestsSubject,
    signal?: AbortSignal,
  ): Promise<M.AbtestsSubjectDetails> => {
    return this.core.request<M.AbtestsSubjectDetails>('POST', '/ab-tests/subject', {
      body,
      signal,
    });
  };

  /** This method allows you to delete an A/B test. Deletion is only permitted when the test is in one of the following states: `draft`, `cancelled`, `finished`, or `completed`. */
  readonly deleteAbTest = async (abTestId: string, signal?: AbortSignal): Promise<void> => {
    return this.core.request<void>('DELETE', '/ab-tests/{abTestId}', {
      pathParams: { abTestId: abTestId },
      signal,
    });
  };

  /** Get a single A/B test by ID */
  readonly getAbTestSubjectById = async (
    abTestId: string,
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
    },
    signal?: AbortSignal,
  ): Promise<M.AbtestsSubjectDetails> => {
    return this.core.request<M.AbtestsSubjectDetails>('GET', '/ab-tests/subject/{abTestId}', {
      pathParams: { abTestId: abTestId },
      query: params ? { fields: params.fields } : undefined,
      signal,
    });
  };

  /** Choose A/B test winner */
  readonly postAbtestsSubjectByIdWinner = async (
    abTestId: string,
    body: M.ChooseWinnerAbtestsSubject,
    signal?: AbortSignal,
  ): Promise<void> => {
    return this.core.request<void>('POST', '/ab-tests/subject/{abTestId}/winner', {
      pathParams: { abTestId: abTestId },
      body,
      signal,
    });
  };
}
