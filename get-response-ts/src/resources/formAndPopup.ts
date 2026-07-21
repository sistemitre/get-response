/** Operations tagged 'Form and Popup' in the GetResponse API. */

import type { Core } from '../core.js';
import type * as M from '../models.js';

export class FormAndPopupResource {
  constructor(private readonly core: Core) {}

  /** Get statistics for a single form or popup */
  readonly getPopupGeneralPerformance = async (
    popupId: string,
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
      /** Get statistics for a single form or popup from this date */
      queryDateFrom?: string;
      /** Get statistics for a single form or popup to this date */
      queryDateTo?: string;
      /** Form or popup statistics by device */
      queryDevice?: M.GetPopupGeneralPerformanceQueryDevice;
      /** Form or popup statistics by location */
      queryLocation?: string;
    },
    signal?: AbortSignal,
  ): Promise<M.PopupGeneralPerformanceStats> => {
    return this.core.request<M.PopupGeneralPerformanceStats>(
      'GET',
      '/statistics/popups/{popupId}/performance',
      {
        pathParams: { popupId: popupId },
        query: params
          ? {
              'query[date][from]': params.queryDateFrom,
              'query[date][to]': params.queryDateTo,
              'query[location]': params.queryLocation,
              'query[device]': params.queryDevice,
              fields: params.fields,
            }
          : undefined,
        signal,
      },
    );
  };
}
