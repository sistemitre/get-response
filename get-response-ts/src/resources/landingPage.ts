/** Operations tagged 'Landing Page' in the GetResponse API. */

import type { Core } from '../core.js';
import type * as M from '../models.js';

export class LandingPageResource {
  constructor(private readonly core: Core) {}

  /** Get details for landing page statistics */
  readonly getLpsGeneralPerformanceStats = async (
    lpsId: string,
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
      /** Show a single landing page statistics from this date */
      queryDateFrom?: string;
      /** Show a single landing page statistics to this date */
      queryDateTo?: string;
      /** Landing page statistics by device */
      queryDevice?: M.GetLpsGeneralPerformanceStatsQueryDevice;
      /** Landing page statistics by location */
      queryLocation?: string;
      /** Landing page statistics by page UUID */
      queryPage?: string;
    },
    signal?: AbortSignal,
  ): Promise<M.LpsStats> => {
    return this.core.request<M.LpsStats>('GET', '/statistics/lps/{lpsId}/performance', {
      pathParams: { lpsId: lpsId },
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
