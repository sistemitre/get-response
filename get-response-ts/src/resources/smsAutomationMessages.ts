/** Operations tagged 'SMS Automation Messages' in the GetResponse API. */

import type { Core } from '../core.js';
import type * as M from '../models.js';

export class SmsAutomationMessagesResource {
  constructor(private readonly core: Core) {}

  /** You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by. */
  readonly getSMSAutomationList = async (
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
      /** Page number */
      page?: number;
      /** Requested number of results per page */
      perPage?: number;
      /** Search automated SMS messages by campaign (list) ID */
      queryCampaignId?: string;
      /** Search for automated SMS messages containing links */
      queryHasLinks?: boolean;
      /** Search automated SMS messages by name */
      queryName?: string;
      /** Sort by the number of link clicks */
      sortClicks?: M.SortOrderEnum;
      /** Sort by the number of delivered SMS messages */
      sortDelivered?: M.SortOrderEnum;
      /** Sort by the date the SMS message was modified on */
      sortModifiedOn?: M.SortOrderEnum;
      /** Sort by the name of the automated SMS message */
      sortName?: M.SortOrderEnum;
      /** Sort by the number of sent SMS messages */
      sortSent?: M.SortOrderEnum;
      /** Sort by the status of the SMS message */
      sortStatus?: M.SortOrderEnum;
    },
    signal?: AbortSignal,
  ): Promise<M.SmsAutomationListItem> => {
    return this.core.request<M.SmsAutomationListItem>('GET', '/sms-automation', {
      query: params
        ? {
            'query[name]': params.queryName,
            'query[campaignId]': params.queryCampaignId,
            'query[hasLinks]': params.queryHasLinks,
            'sort[status]': params.sortStatus,
            'sort[name]': params.sortName,
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

  /** Get a single automated SMS message by its ID. */
  readonly getSmsAutomationById = async (
    smsId: string,
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
    },
    signal?: AbortSignal,
  ): Promise<M.SmsAutomationDetails> => {
    return this.core.request<M.SmsAutomationDetails>('GET', '/sms-automation/{smsId}', {
      pathParams: { smsId: smsId },
      query: params ? { fields: params.fields } : undefined,
      signal,
    });
  };
}
