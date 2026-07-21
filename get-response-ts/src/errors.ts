/** Typed errors: every non-2xx response maps to one of these. */

import type { ErrorResponse } from './models.js';

/** Extra fields accepted by the {@link GetResponseApiError} constructor. */
export interface GetResponseApiErrorOptions {
  code?: number;
  codeDescription?: string;
  message?: string;
  moreInfo?: string;
  context?: Record<string, unknown>;
  uuid?: string;
}

/** Raised for any non-2xx response; carries the parsed `ErrorResponse` fields. */
export class GetResponseApiError extends Error {
  readonly statusCode: number;
  readonly code?: number;
  readonly codeDescription?: string;
  readonly moreInfo?: string;
  readonly context?: Record<string, unknown>;
  readonly uuid?: string;

  constructor(statusCode: number, options: GetResponseApiErrorOptions = {}) {
    super(options.message ?? options.codeDescription ?? `GetResponse API error ${statusCode}`);
    this.name = 'GetResponseApiError';
    this.statusCode = statusCode;
    this.code = options.code;
    this.codeDescription = options.codeDescription;
    this.moreInfo = options.moreInfo;
    this.context = options.context;
    this.uuid = options.uuid;
    Object.setPrototypeOf(this, new.target.prototype);
  }

  /** Build from an HTTP error response, tolerating a body that isn't an `ErrorResponse`. */
  static async fromResponse(response: Response): Promise<GetResponseApiError> {
    try {
      const body = (await response.json()) as Partial<ErrorResponse>;
      return new GetResponseApiError(response.status, {
        code: body.code,
        codeDescription: body.codeDescription,
        message: body.message,
        moreInfo: body.moreInfo,
        context: body.context,
        uuid: body.uuid,
      });
    } catch {
      return new GetResponseApiError(response.status);
    }
  }
}

/** Extra fields accepted by the {@link RateLimitError} constructor. */
export interface RateLimitErrorOptions extends GetResponseApiErrorOptions {
  resetSeconds?: number;
  limit?: number;
  remaining?: number;
}

/** Raised by the opt-in rate limiter when a wait would exceed `maxWaitSeconds` or retries are exhausted. */
export class RateLimitError extends GetResponseApiError {
  readonly resetSeconds?: number;
  readonly limit?: number;
  readonly remaining?: number;

  constructor(statusCode: number, options: RateLimitErrorOptions = {}) {
    super(statusCode, {
      ...options,
      message: options.message ?? 'Rate limit exceeded and the wait/retry budget is exhausted.',
    });
    this.name = 'RateLimitError';
    this.resetSeconds = options.resetSeconds;
    this.limit = options.limit;
    this.remaining = options.remaining;
    Object.setPrototypeOf(this, new.target.prototype);
  }
}
