/** Operations tagged 'SMS Messages' in the GetResponse API. */

import type { Core } from '../core.js';
import type * as M from '../models.js';

export class SmsMessagesResource {
  constructor(private readonly core: Core) {}

  /** You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by. */
  readonly getSMSList = async (
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
      /** Page number */
      page?: number;
      /** Requested number of results per page */
      perPage?: number;
      /** Search SMS messages by campaign (list) ID */
      queryCampaignId?: string;
      /** Search for SMS messages with links */
      queryHasLinks?: boolean;
      /** Search SMS messages by name */
      queryName?: string;
      /** Search SMS messages by status */
      querySendingStatus?: M.GetSmsListQuerySendingStatus;
      /** Search SMS messages by type */
      queryType?: M.GetSmsListQueryType;
      /** Sort by number of link clicks */
      sortClicks?: M.SortOrderEnum;
      /** Sort by number of delivered messages */
      sortDelivered?: M.SortOrderEnum;
      /** Sort by modification date */
      sortModifiedOn?: M.SortOrderEnum;
      /** Sort by name */
      sortName?: M.SortOrderEnum;
      /** Sort by sending date */
      sortSendOn?: M.SortOrderEnum;
      /** Sort by sending status */
      sortSendingStatus?: M.SortOrderEnum;
      /** Sort by number of sent messages */
      sortSent?: M.SortOrderEnum;
    },
    signal?: AbortSignal,
  ): Promise<M.SmsListItem> => {
    return this.core.request<M.SmsListItem>('GET', '/sms', {
      query: params
        ? {
            'query[type]': params.queryType,
            'query[name]': params.queryName,
            'query[sendingStatus]': params.querySendingStatus,
            'query[campaignId]': params.queryCampaignId,
            'query[hasLinks]': params.queryHasLinks,
            'sort[sendingStatus]': params.sortSendingStatus,
            'sort[name]': params.sortName,
            'sort[sendOn]': params.sortSendOn,
            'sort[modifiedOn]': params.sortModifiedOn,
            'sort[delivered]': params.sortDelivered,
            'sort[sent]': params.sortSent,
            'sort[clicks]': params.sortClicks,
            fields: params.fields,
            perPage: params.perPage,
            page: params.page,
          }
        : undefined,
      signal,
    });
  };

  /** Get a single SMS message by its ID */
  readonly getSmsById = async (
    smsId: string,
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
    },
    signal?: AbortSignal,
  ): Promise<M.SmsDetails> => {
    return this.core.request<M.SmsDetails>('GET', '/sms/{smsId}', {
      pathParams: { smsId: smsId },
      query: params ? { fields: params.fields } : undefined,
      signal,
    });
  };

  /** You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by. */
  readonly getSmsSenderNameList = async (
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
      /** Search sender names by status */
      queryStatus?: string;
    },
    signal?: AbortSignal,
  ): Promise<M.SmsSenderName[]> => {
    return this.core.request<M.SmsSenderName[]>('GET', '/sms/sender-names', {
      query: params ? { 'query[status]': params.queryStatus, fields: params.fields } : undefined,
      signal,
    });
  };

  /** Sends a new SMS (text) message to a list of recipients */
  readonly sendSms = async (body: M.BaseSendSms, signal?: AbortSignal): Promise<M.SmsDetails> => {
    return this.core.request<M.SmsDetails>('POST', '/sms', {
      body,
      signal,
    });
  };
}
