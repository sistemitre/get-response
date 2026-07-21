/** Operations tagged 'Tracking' in the GetResponse API. */

import type { Core } from '../core.js';
import type * as M from '../models.js';

export class TrackingResource {
  constructor(private readonly core: Core) {}

  /** Returns the name and ID of "Facebook Pixels" assigned to a user's account. */
  readonly getFacebookPixelList = async (signal?: AbortSignal): Promise<M.FacebookPixel[]> => {
    return this.core.request<M.FacebookPixel[]>('GET', '/tracking/facebook-pixels', {
      signal,
    });
  };

  /** With code snippets you will be able to track Purchases, Abandoned carts, and Visited URLs. Find more in our [Help Center](https://www.getresponse.com/help/marketing-automation/ecommerce-conditions/how-do-i-add-the-tracking-javascript-code-to-my-website.html). */
  readonly getTracking = async (signal?: AbortSignal): Promise<M.Tracking[]> => {
    return this.core.request<M.Tracking[]>('GET', '/tracking', {
      signal,
    });
  };
}
