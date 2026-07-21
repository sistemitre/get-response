"""Opt-in rate limiter: disabled by default, proactive throttling, and 429 handling."""

from __future__ import annotations

import asyncio

import httpx
import pytest

from getresponse import GetResponseClient, RateLimitError, RateLimitOptions


async def test_disabled_by_default_passes_through_untouched() -> None:
    calls = {"count": 0}

    def handler(request: httpx.Request) -> httpx.Response:
        calls["count"] += 1
        return httpx.Response(200, json=[])

    async with GetResponseClient(api_key="k", transport=httpx.MockTransport(handler)) as c:
        result = await c.contacts.get_contact_list()

    assert result == []
    assert calls["count"] == 1


async def test_reactive_retry_on_429_then_success() -> None:
    calls = {"count": 0}
    sleeps: list[float] = []

    async def fake_sleep(seconds: float) -> None:
        sleeps.append(seconds)

    def handler(request: httpx.Request) -> httpx.Response:
        calls["count"] += 1
        if calls["count"] == 1:
            return httpx.Response(
                429, headers={"X-RateLimit-Reset": "1 seconds"}, json={"httpStatus": 429}
            )
        return httpx.Response(200, json=[])

    options = RateLimitOptions(sleep=fake_sleep)
    async with GetResponseClient(
        api_key="k", transport=httpx.MockTransport(handler), rate_limit=options
    ) as c:
        result = await c.contacts.get_contact_list()

    assert result == []
    assert calls["count"] == 2
    assert sleeps == [1.0]


async def test_cap_then_raise_when_reset_exceeds_max_wait() -> None:
    sleeps: list[float] = []

    async def fake_sleep(seconds: float) -> None:
        sleeps.append(seconds)

    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(
            429, headers={"X-RateLimit-Reset": "9999 seconds"}, json={"httpStatus": 429}
        )

    options = RateLimitOptions(sleep=fake_sleep, max_wait=5.0)
    async with GetResponseClient(
        api_key="k", transport=httpx.MockTransport(handler), rate_limit=options
    ) as c:
        with pytest.raises(RateLimitError) as exc_info:
            await c.contacts.get_contact_list()

    assert exc_info.value.reset_seconds == 9999.0
    assert sleeps == []  # never actually slept for the huge reset


async def test_proactive_concurrency_never_exceeds_max_concurrency() -> None:
    in_flight = {"current": 0, "max": 0}

    async def handler(request: httpx.Request) -> httpx.Response:
        in_flight["current"] += 1
        in_flight["max"] = max(in_flight["max"], in_flight["current"])
        await asyncio.sleep(0.01)
        in_flight["current"] -= 1
        return httpx.Response(200, json=[])

    options = RateLimitOptions(
        max_concurrency=3, requests_per_second=1000, requests_per_window=100000
    )
    async with GetResponseClient(
        api_key="k", transport=httpx.MockTransport(handler), rate_limit=options
    ) as c:
        await asyncio.gather(*(c.contacts.get_contact_list() for _ in range(10)))

    assert in_flight["max"] <= 3


async def test_proactive_rate_pacing_with_fake_clock() -> None:
    class FakeClock:
        def __init__(self) -> None:
            self.now = 0.0

        def __call__(self) -> float:
            return self.now

    clock = FakeClock()
    sleeps: list[float] = []

    async def fake_sleep(seconds: float) -> None:
        sleeps.append(seconds)
        clock.now += seconds

    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(200, json=[])

    options = RateLimitOptions(
        requests_per_second=2,
        requests_per_window=1000,
        sleep=fake_sleep,
        clock=clock,
    )
    async with GetResponseClient(
        api_key="k", transport=httpx.MockTransport(handler), rate_limit=options
    ) as c:
        for _ in range(4):
            await c.contacts.get_contact_list()

    # capacity starts full (2 tokens): the 3rd and 4th calls each wait ~0.5s for a refill.
    assert len(sleeps) == 2
    assert all(abs(s - 0.5) < 1e-9 for s in sleeps)
