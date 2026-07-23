/** Operations tagged 'Transactional Emails' in the GetResponse API. */

import type { Core } from '../core.js';
import type * as M from '../models.js';

export class TransactionalEmailsResource {
  constructor(private readonly core: Core) {}

  /** Send transactional email */
  readonly createTransactionalEmail = async (
    body: M.CreateTransactionalEmail,
    signal?: AbortSignal,
  ): Promise<M.TransactionalEmail> => {
    return this.core.request<M.TransactionalEmail>('POST', '/transactional-emails', {
      body,
      signal,
    });
  };

  /** Get transactional email details by transactional email ID */
  readonly getTransactionalEmailsById = async (
    transactionalEmailId: string,
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
    },
    signal?: AbortSignal,
  ): Promise<M.TransactionalEmailDetails> => {
    return this.core.request<M.TransactionalEmailDetails>(
      'GET',
      '/transactional-emails/{transactionalEmailId}',
      {
        pathParams: { transactionalEmailId: transactionalEmailId },
        query: params ? { fields: params.fields } : undefined,
        signal,
      },
    );
  };

  /** You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by. */
  readonly getTransactionalEmailsList = async (
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
      /** Page number */
      page?: number;
      /** Requested number of results per page */
      perPage?: number;
      /** Search transactional emails sent from this date */
      querySentOnFrom?: string;
      /** Search transactional emails sent to this date */
      querySentOnTo?: string;
      /** Search transactional emails with a specific tag ID */
      queryTagId?: string;
      /** Search tagged/untagged transactional emails */
      queryTagged?: M.StringBooleanEnum;
    },
    signal?: AbortSignal,
  ): Promise<M.TransactionalEmailListElement[]> => {
    return this.core.request<M.TransactionalEmailListElement[]>('GET', '/transactional-emails', {
      query: params
        ? {
            'query[sentOn][from]': params.querySentOnFrom,
            'query[sentOn][to]': params.querySentOnTo,
            'query[tagged]': params.queryTagged,
            'query[tagId]': params.queryTagId,
            fields: params.fields,
            perPage: params.perPage,
            page: params.page,
          }
        : undefined,
      signal,
    });
  };

  /** Get the overall statistics of transactional emails */
  readonly getTransactionalEmailsStatistics = async (
    params?: {
      /** Group results by time interval */
      queryGroupBy: M.GetTransactionalEmailsStatisticsQueryGroupBy;
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
      /** Search transactional emails with a specific tag ID */
      queryTagId?: string;
      /** Search tagged/untagged transactional emails */
      queryTagged?: M.StringBooleanEnum;
      /** Count data from this date */
      queryTimeFrameFrom?: string;
      /** Count data to this date */
      queryTimeFrameTo?: string;
    },
    signal?: AbortSignal,
  ): Promise<M.TransactionalEmailStatistics[]> => {
    return this.core.request<M.TransactionalEmailStatistics[]>(
      'GET',
      '/transactional-emails/statistics',
      {
        query: params
          ? {
              'query[groupBy]': params.queryGroupBy,
              'query[timeFrame][from]': params.queryTimeFrameFrom,
              'query[timeFrame][to]': params.queryTimeFrameTo,
              'query[tagged]': params.queryTagged,
              'query[tagId]': params.queryTagId,
              fields: params.fields,
            }
          : undefined,
        signal,
      },
    );
  };
}
