"""Opt-in rate limiter: a concurrency cap plus per-second/per-window token buckets.

Disabled unless a `RateLimitOptions` is passed to `GetResponseClient(rate_limit=...)`. `_Core`
owns one `_RateLimiter` per client and drives it around every send attempt: `acquire()` before
sending (a concurrency slot, an rps token, a window token, and any adaptive block from a prior
response), `release()` after, and `observe()`/`reset_seconds_from()` to read the response's rate
headers. Every wait is capped by `max_wait`; exceeding it raises `_WaitExceedsMaxWait`, which
`_Core` turns into the public `RateLimitError`.
"""

from __future__ import annotations

import asyncio
import re
import time
from collections.abc import Awaitable, Callable
from dataclasses import dataclass
from typing import Any

import httpx

_RESET_RE = re.compile(r"\d+")


def _parse_reset_seconds(value: str) -> int | None:
    """Extract the leading integer from a header value like `"432 seconds"`."""
    m = _RESET_RE.search(value)
    return int(m.group()) if m else None


async def _default_sleep(seconds: float) -> None:
    """Default `RateLimitOptions.sleep`: real `asyncio.sleep`, overridable in tests."""
    await asyncio.sleep(seconds)


def _default_clock() -> float:
    """Default `RateLimitOptions.clock`: real monotonic time, overridable in tests."""
    return time.monotonic()


@dataclass
class RateLimitOptions:
    """Opt-in rate-limit tuning; pass to `GetResponseClient(rate_limit=...)` to enable it.

    `safety_margin` (range `(0, 1]`) scales `requests_per_second`/`requests_per_window` down
    before they're used as bucket capacities -- concurrency is never scaled. `sleep`/`clock`
    are injectable so tests can run against a fake, instantly-advancing clock.
    """

    enabled: bool = True
    max_concurrency: int = 10
    requests_per_second: float = 80
    requests_per_window: float = 30000
    window_seconds: float = 600
    safety_margin: float = 1.0
    max_retries: int = 5
    max_wait: float = 60.0
    sleep: Callable[[float], Awaitable[None]] = _default_sleep
    clock: Callable[[], float] = _default_clock

    @property
    def effective_rps(self) -> float:
        """`requests_per_second` scaled by `safety_margin` and floored."""
        return float(int(self.requests_per_second * self.safety_margin))

    @property
    def effective_rpw(self) -> float:
        """`requests_per_window` scaled by `safety_margin` and floored."""
        return float(int(self.requests_per_window * self.safety_margin))


class _WaitExceedsMaxWait(Exception):
    """Internal signal: a proactive wait would exceed `max_wait`; `_Core` maps this to `RateLimitError`."""

    def __init__(self, wait_seconds: float) -> None:
        self.wait_seconds = wait_seconds
        super().__init__(f"wait of {wait_seconds:.1f}s exceeds max_wait")


class _TokenBucket:
    """Continuous-refill token bucket: `capacity` tokens, refilling at `rate` tokens/second."""

    def __init__(self, rate: float, capacity: float, *, clock: Callable[[], float]) -> None:
        self._rate = rate
        self._capacity = capacity
        self._clock = clock
        self._tokens = capacity
        self._last = clock()

    def _refill(self) -> None:
        now = self._clock()
        self._tokens = min(self._capacity, self._tokens + (now - self._last) * self._rate)
        self._last = now

    def wait_time(self) -> float:
        """Seconds until one token is available (0 if one already is). Does not consume it."""
        self._refill()
        if self._tokens >= 1 or self._rate <= 0:
            return 0.0
        return (1 - self._tokens) / self._rate

    def consume(self) -> None:
        """Take one token. Call only right after waiting out `wait_time()`."""
        self._refill()
        self._tokens -= 1


class _RateLimiter:
    """Per-client rate limiter: wraps every send attempt with proactive and adaptive throttling."""

    def __init__(self, options: RateLimitOptions) -> None:
        self.options = options
        self._concurrency = asyncio.Semaphore(options.max_concurrency)
        self._rps_bucket = _TokenBucket(
            options.effective_rps, options.effective_rps, clock=options.clock
        )
        self._rpw_bucket = _TokenBucket(
            options.effective_rpw / options.window_seconds,
            options.effective_rpw,
            clock=options.clock,
        )
        self._blocked_until: float | None = None

    async def acquire(self) -> None:
        """Take a concurrency slot, then wait out whichever of rps/window/adaptive-block is

        longest. Raises `_WaitExceedsMaxWait` instead of waiting past `options.max_wait`; on
        that path the concurrency slot is released again before raising.
        """
        await self._concurrency.acquire()
        try:
            wait = 0.0
            if self._blocked_until is not None:
                remaining = self._blocked_until - self.options.clock()
                if remaining <= 0:
                    self._blocked_until = None
                else:
                    wait = remaining
            wait = max(wait, self._rps_bucket.wait_time(), self._rpw_bucket.wait_time())
            if wait > self.options.max_wait:
                raise _WaitExceedsMaxWait(wait)
            if wait > 0:
                await self.options.sleep(wait)
            self._rps_bucket.consume()
            self._rpw_bucket.consume()
        except Exception:
            self._concurrency.release()
            raise

    def release(self) -> None:
        """Free the concurrency slot taken by a matching `acquire()`."""
        self._concurrency.release()

    def observe(self, headers: httpx.Headers) -> None:
        """Adaptive best-effort throttle: block new requests once a response reports 0 left."""
        remaining = headers.get("X-RateLimit-Remaining")
        if remaining is None:
            return
        try:
            if int(remaining) > 0:
                return
        except ValueError:
            return
        reset = self.reset_seconds_from(headers, None)
        wait = reset if reset is not None else self.options.window_seconds
        self._blocked_until = self.options.clock() + wait

    def reset_seconds_from(
        self, headers: httpx.Headers, context: dict[str, Any] | None
    ) -> float | None:
        """Seconds until the limit resets: the `X-RateLimit-Reset` header, else

        `context["timeToReset"]` (from a parsed `ErrorResponse`).
        """
        header_value = headers.get("X-RateLimit-Reset")
        if header_value is not None:
            parsed = _parse_reset_seconds(header_value)
            if parsed is not None:
                return float(parsed)
        if context and context.get("timeToReset") is not None:
            try:
                return float(context["timeToReset"])
            except (TypeError, ValueError):
                return None
        return None
