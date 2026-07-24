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
      /** Get statistics for a single SMS from this date (GetResponse date format: yyyy-MM-ddTHH:mm:ss+HHMM, e.g. 2024-01-15T10:30:00+0000 -- no colon in the offset, no sub-second precision (unlike Date.prototype.toISOString())) */
      queryCreatedOnFrom?: string;
      /** Get statistics for a single SMS to this date (GetResponse date format: yyyy-MM-ddTHH:mm:ss+HHMM, e.g. 2024-01-15T10:30:00+0000 -- no colon in the offset, no sub-second precision (unlike Date.prototype.toISOString())) */
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
