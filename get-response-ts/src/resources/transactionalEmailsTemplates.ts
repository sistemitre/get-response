/** Operations tagged 'Transactional Emails Templates' in the GetResponse API. */

import type { Core } from '../core.js';
import type * as M from '../models.js';

export class TransactionalEmailsTemplatesResource {
  constructor(private readonly core: Core) {}

  /** This method creates a new transactional email template */
  readonly createTransactionalEmailTemplate = async (
    body: M.CreateTransactionalEmailTemplate,
    signal?: AbortSignal,
  ): Promise<M.TransactionalEmailsTemplateDetails> => {
    return this.core.request<M.TransactionalEmailsTemplateDetails>(
      'POST',
      '/transactional-emails/templates',
      {
        body,
        signal,
      },
    );
  };

  /** Delete transactional email template */
  readonly deleteTransactionalEmailsTemplate = async (
    transactionalEmailTemplateId: string,
    signal?: AbortSignal,
  ): Promise<void> => {
    return this.core.request<void>(
      'DELETE',
      '/transactional-emails/templates/{transactionalEmailTemplateId}',
      {
        pathParams: { transactionalEmailTemplateId: transactionalEmailTemplateId },
        signal,
      },
    );
  };

  /** Get a single template by ID */
  readonly getTransactionalEmailsTemplatesById = async (
    transactionalEmailTemplateId: string,
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
    },
    signal?: AbortSignal,
  ): Promise<M.TransactionalEmailsTemplateDetails> => {
    return this.core.request<M.TransactionalEmailsTemplateDetails>(
      'GET',
      '/transactional-emails/templates/{transactionalEmailTemplateId}',
      {
        pathParams: { transactionalEmailTemplateId: transactionalEmailTemplateId },
        query: params ? { fields: params.fields } : undefined,
        signal,
      },
    );
  };

  /** You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by. */
  readonly getTransactionalEmailsTemplatesList = async (
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
      /** Page number */
      page?: number;
      /** Requested number of results per page */
      perPage?: number;
      /** Search templates by subject */
      querySubject?: string;
      /** Sort by creation date */
      sortCreatedOn?: M.SortOrderEnum;
      /** Sort by template subject */
      sortSubject?: M.SortOrderEnum;
    },
    signal?: AbortSignal,
  ): Promise<M.TransactionalEmailsTemplateListElement[]> => {
    return this.core.request<M.TransactionalEmailsTemplateListElement[]>(
      'GET',
      '/transactional-emails/templates',
      {
        query: params
          ? {
              'query[subject]': params.querySubject,
              'sort[createdOn]': params.sortCreatedOn,
              'sort[subject]': params.sortSubject,
              fields: params.fields,
              perPage: params.perPage,
              page: params.page,
            }
          : undefined,
        signal,
      },
    );
  };

  /** This method allows you to update transactional email template */
  readonly updateTransactionalEmailsTemplate = async (
    transactionalEmailTemplateId: string,
    body: Record<string, unknown>,
    signal?: AbortSignal,
  ): Promise<M.TransactionalEmailsTemplateDetails> => {
    return this.core.request<M.TransactionalEmailsTemplateDetails>(
      'POST',
      '/transactional-emails/templates/{transactionalEmailTemplateId}',
      {
        pathParams: { transactionalEmailTemplateId: transactionalEmailTemplateId },
        body,
        signal,
      },
    );
  };
}
