/** Operations tagged 'Ecommerce' in the GetResponse API. */

import type { Core } from '../core.js';
import type * as M from '../models.js';

export class EcommerceResource {
  constructor(private readonly core: Core) {}

  /** Get the ecommerce general performance statistics */
  readonly getGeneralPerformanceStats = async (
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
      /** Show statistics for orders from this date (GetResponse date format: yyyy-MM-ddTHH:mm:ss+HHMM, e.g. 2024-01-15T10:30:00+0000 -- no colon in the offset, no sub-second precision (unlike Date.prototype.toISOString())) */
      queryOrderDateFrom?: string;
      /** Show statistics for orders to this date (GetResponse date format: yyyy-MM-ddTHH:mm:ss+HHMM, e.g. 2024-01-15T10:30:00+0000 -- no colon in the offset, no sub-second precision (unlike Date.prototype.toISOString())) */
      queryOrderDateTo?: string;
      /** Search statistics by shop ID. You can get the shop ID by calling the `/v3/shops` endpoint. You can search for multiple shops using comma-separated values, for example, `pgIH, CNXF` */
      queryShopId?: string;
    },
    signal?: AbortSignal,
  ): Promise<M.GeneralPerformanceStats> => {
    return this.core.request<M.GeneralPerformanceStats>(
      'GET',
      '/statistics/ecommerce/performance',
      {
        query: params
          ? {
              'query[orderDate][from]': params.queryOrderDateFrom,
              'query[orderDate][to]': params.queryOrderDateTo,
              'query[shopId]': params.queryShopId,
              fields: params.fields,
            }
          : undefined,
        signal,
      },
    );
  };

  /** Get the ecommerce revenue statistics */
  readonly getRevenueStats = async (
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
      /** Show statistics for orders from this date (GetResponse date format: yyyy-MM-ddTHH:mm:ss+HHMM, e.g. 2024-01-15T10:30:00+0000 -- no colon in the offset, no sub-second precision (unlike Date.prototype.toISOString())) */
      queryOrderDateFrom?: string;
      /** Show statistics for orders to this date (GetResponse date format: yyyy-MM-ddTHH:mm:ss+HHMM, e.g. 2024-01-15T10:30:00+0000 -- no colon in the offset, no sub-second precision (unlike Date.prototype.toISOString())) */
      queryOrderDateTo?: string;
      /** Search statistics by shop ID. You can get the shop ID by calling the `/v3/shops` endpoint. You can search for multiple shops using comma-separated values, for example, `pgIH, CNXF` */
      queryShopId?: string;
    },
    signal?: AbortSignal,
  ): Promise<M.RevenueStatistics> => {
    return this.core.request<M.RevenueStatistics>('GET', '/statistics/ecommerce/revenue', {
      query: params
        ? {
            'query[orderDate][from]': params.queryOrderDateFrom,
            'query[orderDate][to]': params.queryOrderDateTo,
            'query[shopId]': params.queryShopId,
            fields: params.fields,
          }
        : undefined,
      signal,
    });
  };
}
