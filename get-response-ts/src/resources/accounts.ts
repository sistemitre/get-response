/** Operations tagged 'Accounts' in the GetResponse API. */

import type { Core } from '../core.js';
import type * as M from '../models.js';

export class AccountsResource {
  constructor(private readonly core: Core) {}

  /** Disable callbacks */
  readonly disableCallbacks = async (signal?: AbortSignal): Promise<void> => {
    return this.core.request<void>('DELETE', '/accounts/callbacks', {
      signal,
    });
  };

  /** Account information */
  readonly getAccount = async (
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
    },
    signal?: AbortSignal,
  ): Promise<M.Account> => {
    return this.core.request<M.Account>('GET', '/accounts', {
      query: params ? { fields: params.fields } : undefined,
      signal,
    });
  };

  /** Current status of your GetResponse badge */
  readonly getAccountBadge = async (signal?: AbortSignal): Promise<M.AccountBadgeDetails> => {
    return this.core.request<M.AccountBadgeDetails>('GET', '/accounts/badge', {
      signal,
    });
  };

  /** Billing information */
  readonly getAccountBilling = async (
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
    },
    signal?: AbortSignal,
  ): Promise<M.AccountBilling> => {
    return this.core.request<M.AccountBilling>('GET', '/accounts/billing', {
      query: params ? { fields: params.fields } : undefined,
      signal,
    });
  };

  /** Returns account blocklist masks */
  readonly getAccountBlocklist = async (
    params?: {
      /** Blocklist mask to search for */
      queryMask?: string;
    },
    signal?: AbortSignal,
  ): Promise<M.Blocklist> => {
    return this.core.request<M.Blocklist>('GET', '/accounts/blocklists', {
      query: params ? { 'query[mask]': params.queryMask } : undefined,
      signal,
    });
  };

  /** History of logins */
  readonly getAccountLoginHistory = async (
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
      /** Page number */
      page?: number;
      /** Requested number of results per page */
      perPage?: number;
    },
    signal?: AbortSignal,
  ): Promise<M.AccountsLoginHistoryListElement[]> => {
    return this.core.request<M.AccountsLoginHistoryListElement[]>(
      'GET',
      '/accounts/login-history',
      {
        query: params
          ? { fields: params.fields, perPage: params.perPage, page: params.page }
          : undefined,
        signal,
      },
    );
  };

  /** Get callbacks configuration */
  readonly getCallbacks = async (signal?: AbortSignal): Promise<M.Callback> => {
    return this.core.request<M.Callback>('GET', '/accounts/callbacks', {
      signal,
    });
  };

  /** List of Industry Tags in account's language context. */
  readonly getIndustries = async (
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
      /** Page number */
      page?: number;
      /** Requested number of results per page */
      perPage?: number;
    },
    signal?: AbortSignal,
  ): Promise<M.IndustryTag[]> => {
    return this.core.request<M.IndustryTag[]>('GET', '/accounts/industries', {
      query: params
        ? { fields: params.fields, perPage: params.perPage, page: params.page }
        : undefined,
      signal,
    });
  };

  /** Send limits */
  readonly getSendingLimits = async (
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
    },
    signal?: AbortSignal,
  ): Promise<M.SendingLimitsListItem[]> => {
    return this.core.request<M.SendingLimitsListItem[]>('GET', '/accounts/sending-limits', {
      query: params ? { fields: params.fields } : undefined,
      signal,
    });
  };

  /** List of timezones in account's language context. */
  readonly getTimezones = async (
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
    },
    signal?: AbortSignal,
  ): Promise<M.Timezone[]> => {
    return this.core.request<M.Timezone[]>('GET', '/accounts/timezones', {
      query: params ? { fields: params.fields } : undefined,
      signal,
    });
  };

  /** Update account */
  readonly updateAccount = async (
    body: M.UpdateAccount,
    signal?: AbortSignal,
  ): Promise<M.Account> => {
    return this.core.request<M.Account>('POST', '/accounts', {
      body,
      signal,
    });
  };

  /** Turn on/off the GetResponse Badge */
  readonly updateAccountBadge = async (
    body: Record<string, unknown>,
    signal?: AbortSignal,
  ): Promise<M.AccountBadgeDetails> => {
    return this.core.request<M.AccountBadgeDetails>('POST', '/accounts/badge', {
      body,
      signal,
    });
  };

  /** Update account blocklist */
  readonly updateAccountBlocklist = async (
    body: M.UpdateBlocklist,
    params?: {
      /** The flag value `add` adds the masks provided in the request body to your blocklist. The flag value `delete` deletes the masks. The masks are replaced if there are no flag values in the request body. For better performance, use the flag value `noResponse`. It removes the response body and can be used alone or combined with other flags. If multiple flags are used, separate them by a comma, like this: `additionalFlags=noResponse` or `additionalFlags=add,noResponse`. */
      additionalFlags?: M.UpdateAccountBlocklistAdditionalFlags;
    },
    signal?: AbortSignal,
  ): Promise<M.Blocklist> => {
    return this.core.request<M.Blocklist>('POST', '/accounts/blocklists', {
      query: params ? { additionalFlags: params.additionalFlags } : undefined,
      body,
      signal,
    });
  };

  /** Enable or update callbacks configuration */
  readonly updateCallbacks = async (
    body: M.UpdateCallbacks,
    signal?: AbortSignal,
  ): Promise<M.Callback> => {
    return this.core.request<M.Callback>('POST', '/accounts/callbacks', {
      body,
      signal,
    });
  };
}
