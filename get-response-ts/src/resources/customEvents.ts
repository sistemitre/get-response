/** Operations tagged 'Custom Events' in the GetResponse API. */

import type { Core } from '../core.js';
import type * as M from '../models.js';

export class CustomEventsResource {
  constructor(private readonly core: Core) {}

  /** Create custom event */
  readonly createCustomEvent = async (
    body: M.NewCustomEvent,
    signal?: AbortSignal,
  ): Promise<M.CustomEventDetails> => {
    return this.core.request<M.CustomEventDetails>('POST', '/custom-events', {
      body,
      signal,
    });
  };

  /** Delete a custom event by custom event ID */
  readonly deleteCustomEvent = async (
    customEventId: string,
    signal?: AbortSignal,
  ): Promise<void> => {
    return this.core.request<void>('DELETE', '/custom-events/{customEventId}', {
      pathParams: { customEventId: customEventId },
      signal,
    });
  };

  /** Get custom events by custom event ID */
  readonly getCustomEventById = async (
    customEventId: string,
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
    },
    signal?: AbortSignal,
  ): Promise<M.CustomEventDetails> => {
    return this.core.request<M.CustomEventDetails>('GET', '/custom-events/{customEventId}', {
      pathParams: { customEventId: customEventId },
      query: params ? { fields: params.fields } : undefined,
      signal,
    });
  };

  /** You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by. */
  readonly getCustomEventsList = async (
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
      /** Page number */
      page?: number;
      /** Requested number of results per page */
      perPage?: number;
      /** Search custom events with or without attributes */
      queryHasAttributes?: M.StringBooleanEnum;
      /** Search custom events by name */
      queryName?: string;
      /** Sort by name */
      sortName?: M.SortOrderEnum;
    },
    signal?: AbortSignal,
  ): Promise<M.CustomEventDetails[]> => {
    return this.core.request<M.CustomEventDetails[]>('GET', '/custom-events', {
      query: params
        ? {
            'query[name]': params.queryName,
            'query[hasAttributes]': params.queryHasAttributes,
            'sort[name]': params.sortName,
            fields: params.fields,
            perPage: params.perPage,
            page: params.page,
          }
        : undefined,
      signal,
    });
  };

  /** Trigger a custom event */
  readonly triggerCustomEvent = async (
    body: M.TriggerCustomEvent,
    signal?: AbortSignal,
  ): Promise<void> => {
    return this.core.request<void>('POST', '/custom-events/trigger', {
      body,
      signal,
    });
  };

  /** Update custom event details */
  readonly updateCustomEvent = async (
    customEventId: string,
    body: M.UpdateCustomEvent,
    signal?: AbortSignal,
  ): Promise<M.CustomEventDetails> => {
    return this.core.request<M.CustomEventDetails>('POST', '/custom-events/{customEventId}', {
      pathParams: { customEventId: customEventId },
      body,
      signal,
    });
  };
}
