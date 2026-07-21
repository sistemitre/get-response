/** Operations tagged 'Website' in the GetResponse API. */

import type { Core } from '../core.js';
import type * as M from '../models.js';

export class WebsiteResource {
  constructor(private readonly core: Core) {}

  /** Get details for website statistics */
  readonly getWbeGeneralPerformanceStats = async (
    websiteId: string,
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
      /** Show a single website statistics from this date */
      queryDateFrom?: Record<string, unknown>;
      /** Show a single website statistics to this date */
      queryDateTo?: Record<string, unknown>;
      /** Website statistics by device */
      queryDevice?: M.GetWbeGeneralPerformanceStatsQueryDevice;
      /** Website statistics by location */
      queryLocation?: string;
      /** Website statistics by a page UUID */
      queryPage?: string;
    },
    signal?: AbortSignal,
  ): Promise<M.WebsiteStats> => {
    return this.core.request<M.WebsiteStats>('GET', '/statistics/wbe/{websiteId}/performance', {
      pathParams: { websiteId: websiteId },
      query: params
        ? {
            'query[date][from]': params.queryDateFrom,
            'query[date][to]': params.queryDateTo,
            'query[location]': params.queryLocation,
            'query[device]': params.queryDevice,
            'query[page]': params.queryPage,
            fields: params.fields,
          }
        : undefined,
      signal,
    });
  };
}
