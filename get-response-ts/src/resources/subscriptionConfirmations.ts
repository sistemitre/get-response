/** Operations tagged 'Subscription Confirmations' in the GetResponse API. */

import type { Core } from '../core.js';
import type * as M from '../models.js';

export class SubscriptionConfirmationsResource {
  constructor(private readonly core: Core) {}

  /** Sending **GET** request to this url, returns collection of **SUBSCRIPTION CONFIRMATIONS** bodies. Language code used in url must be in ISO 639-1 Language Code Standard. */
  readonly getSubscriptionConfirmationBodyList = async (
    languageCode: string,
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
    },
    signal?: AbortSignal,
  ): Promise<M.SubscriptionConfirmationBody[]> => {
    return this.core.request<M.SubscriptionConfirmationBody[]>(
      'GET',
      '/subscription-confirmations/body/{languageCode}',
      {
        pathParams: { languageCode: languageCode },
        query: params ? { fields: params.fields } : undefined,
        signal,
      },
    );
  };

  /** Sending **GET** request to this url, returns collection of **SUBSCRIPTION CONFIRMATIONS** subjects. Language code used in url must be in ISO 639-1 Language Code Standard. */
  readonly getSubscriptionConfirmationSubjectList = async (
    languageCode: string,
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
    },
    signal?: AbortSignal,
  ): Promise<M.SubscriptionConfirmationSubject[]> => {
    return this.core.request<M.SubscriptionConfirmationSubject[]>(
      'GET',
      '/subscription-confirmations/subject/{languageCode}',
      {
        pathParams: { languageCode: languageCode },
        query: params ? { fields: params.fields } : undefined,
        signal,
      },
    );
  };
}
