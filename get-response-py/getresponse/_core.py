"""HTTP transport: request building, auth-agnostic call plumbing, and error mapping."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Any

import httpx
from pydantic import BaseModel, TypeAdapter

from ._ratelimit import RateLimitOptions, _RateLimiter, _WaitExceedsMaxWait
from .models import ErrorResponse

DEFAULT_BASE_URL = "https://api.getresponse.com/v3"
MAX_US_BASE_URL = "https://api3.getresponse360.com/v3"
MAX_PL_BASE_URL = "https://api3.getresponse360.pl/v3"


class GetResponseApiError(Exception):
    """Raised for any non-2xx response; carries the parsed `ErrorResponse` fields."""

    def __init__(
        self,
        status_code: int,
        *,
        code: int | None = None,
        code_description: str | None = None,
        message: str | None = None,
        more_info: str | None = None,
        context: dict[str, Any] | None = None,
        uuid: str | None = None,
    ) -> None:
        self.status_code = status_code
        self.code = code
        self.code_description = code_description
        self.message = message
        self.more_info = more_info
        self.context = context
        self.uuid = uuid
        super().__init__(
            f"GetResponse API error {status_code}: {message or code_description or 'unknown error'}"
        )

    @classmethod
    def from_response(cls, response: httpx.Response) -> GetResponseApiError:
        """Build from an HTTP error response, tolerating a body that isn't an `ErrorResponse`."""
        try:
            err = ErrorResponse.model_validate(response.json())
        except Exception:
            return cls(status_code=response.status_code, message=response.text or None)
        return cls(
            status_code=response.status_code,
            code=err.code,
            code_description=err.code_description,
            message=err.message,
            more_info=err.more_info,
            context=err.context,
            uuid=err.uuid,
        )


class RateLimitError(GetResponseApiError):
    """Raised by the rate limiter: retries after a 429 were exhausted, or a wait -- proactive

    (concurrency slot / token bucket / adaptive block) or reactive (429 reset) -- would exceed
    `RateLimitOptions.max_wait`.
    """

    def __init__(
        self,
        status_code: int = 429,
        *,
        code: int | None = None,
        code_description: str | None = None,
        message: str | None = None,
        more_info: str | None = None,
        context: dict[str, Any] | None = None,
        uuid: str | None = None,
        reset_seconds: float | None = None,
        limit: int | None = None,
        remaining: int | None = None,
    ) -> None:
        super().__init__(
            status_code,
            code=code,
            code_description=code_description,
            message=message,
            more_info=more_info,
            context=context,
            uuid=uuid,
        )
        self.reset_seconds = reset_seconds
        self.limit = limit
        self.remaining = remaining

    @classmethod
    def from_error(
        cls,
        err: GetResponseApiError,
        *,
        reset_seconds: float | None,
        limit: int | None,
        remaining: int | None,
    ) -> RateLimitError:
        """Attach rate-limit fields to a `GetResponseApiError` already parsed from a 429."""
        return cls(
            err.status_code,
            code=err.code,
            code_description=err.code_description,
            message=err.message,
            more_info=err.more_info,
            context=err.context,
            uuid=err.uuid,
            reset_seconds=reset_seconds,
            limit=limit,
            remaining=remaining,
        )

    @classmethod
    def wait_too_long(cls, wait_seconds: float) -> RateLimitError:
        """Build for a proactive wait that would exceed `max_wait` (no HTTP response involved)."""
        return cls(
            429,
            message=f"rate limit wait of {wait_seconds:.1f}s exceeds max_wait",
            reset_seconds=wait_seconds,
        )


def _int_or_none(value: str | None) -> int | None:
    """Parse an optional header string as an int, tolerating a missing/invalid value."""
    if value is None:
        return None
    try:
        return int(value)
    except ValueError:
        return None


def _encode_query(query: dict[str, Any] | None) -> dict[str, Any] | None:
    """Drop `None` values; encode enums/datetimes/bools to their wire representation."""
    if not query:
        return None
    encoded: dict[str, Any] = {}
    for key, value in query.items():
        if value is None:
            continue
        if isinstance(value, Enum):
            encoded[key] = value.value
        elif isinstance(value, datetime):
            encoded[key] = value.isoformat()
        elif isinstance(value, bool):
            encoded[key] = "true" if value else "false"
        else:
            encoded[key] = value
    return encoded


class _Core:
    """Thin wrapper around an `httpx.AsyncClient`: one call site for every operation."""

    def __init__(
        self, client: httpx.AsyncClient, rate_limit: RateLimitOptions | None = None
    ) -> None:
        self._client = client
        self._limiter = (
            _RateLimiter(rate_limit) if rate_limit is not None and rate_limit.enabled else None
        )

    async def request(
        self,
        method: str,
        path: str,
        *,
        path_params: dict[str, str] | None = None,
        query: dict[str, Any] | None = None,
        body: Any = None,
        files: dict[str, Any] | None = None,
        return_type: Any = None,
    ) -> Any:
        """Send one API call and decode the response into `return_type` (or `None`)."""
        url = path.format(**(path_params or {}))
        params = _encode_query(query)
        json_body: Any = None
        if isinstance(body, BaseModel):
            json_body = body.model_dump(mode="json", by_alias=True, exclude_none=True)
        elif body is not None:
            json_body = body

        response = await self._send(method, url, params, json_body, files)
        if response.status_code >= 400:
            raise GetResponseApiError.from_response(response)
        if return_type is None or response.status_code == 204 or not response.content:
            return None
        return TypeAdapter(return_type).validate_python(response.json())

    async def _send(
        self,
        method: str,
        url: str,
        params: dict[str, Any] | None,
        json_body: Any,
        files: dict[str, Any] | None,
    ) -> httpx.Response:
        """Send the request as-is when no limiter is configured (zero overhead, unchanged

        behavior); otherwise run it through the limiter's proactive acquire and reactive
        429-retry loop.
        """
        if self._limiter is None:
            return await self._client.request(
                method, url, params=params, json=json_body, files=files
            )

        attempt = 0
        while True:
            try:
                await self._limiter.acquire()
            except _WaitExceedsMaxWait as exc:
                raise RateLimitError.wait_too_long(exc.wait_seconds) from exc
            try:
                response = await self._client.request(
                    method, url, params=params, json=json_body, files=files
                )
            finally:
                self._limiter.release()
            self._limiter.observe(response.headers)
            if response.status_code != 429:
                return response

            attempt += 1
            err = GetResponseApiError.from_response(response)
            reset = self._limiter.reset_seconds_from(response.headers, err.context)
            opts = self._limiter.options
            if attempt < opts.max_retries and reset is not None and reset <= opts.max_wait:
                await opts.sleep(reset)
                continue
            raise RateLimitError.from_error(
                err,
                reset_seconds=reset,
                limit=_int_or_none(response.headers.get("X-RateLimit-Limit")),
                remaining=_int_or_none(response.headers.get("X-RateLimit-Remaining")),
            )
