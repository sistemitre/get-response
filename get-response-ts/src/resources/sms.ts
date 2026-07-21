/** Operations tagged 'Sms' in the GetResponse API. */

import type { Core } from '../core.js';
import type * as M from '../models.js';

export class SmsResource {
  constructor(private readonly core: Core) {}

  /** Get details for the SMS message statistics */
  readonly getSmsStats = async (
    smsId: string,
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
      /** Get statistics for a single SMS from this date */
      queryCreatedOnFrom?: string;
      /** Get statistics for a single SMS to this date */
      queryCreatedOnTo?: string;
    },
    signal?: AbortSignal,
  ): Promise<M.SmsStats> => {
    return this.core.request<M.SmsStats>('GET', '/statistics/sms/{smsId}', {
      pathParams: { smsId: smsId },
      query: params
        ? {
            'query[createdOn][from]': params.queryCreatedOnFrom,
            'query[createdOn][to]': params.queryCreatedOnTo,
            fields: params.fields,
          }
        : undefined,
      signal,
    });
  };
}
