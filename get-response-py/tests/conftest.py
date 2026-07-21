"""Shared pytest fixtures: build a `GetResponseClient` over a mocked HTTP transport."""

from __future__ import annotations

from collections.abc import Callable

import httpx

from getresponse import GetResponseClient


def make_client(
    handler: Callable[[httpx.Request], httpx.Response], *, api_key: str = "test-key"
) -> GetResponseClient:
    """Build a client whose requests are served entirely by `handler` (no real network)."""
    return GetResponseClient(api_key=api_key, transport=httpx.MockTransport(handler))
