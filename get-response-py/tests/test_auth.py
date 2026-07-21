"""Auth header selection: `X-Auth-Token` for API keys, `Bearer` for OAuth2 tokens."""

from __future__ import annotations

import httpx
import pytest

from getresponse import GetResponseClient


async def test_api_key_sends_x_auth_token_header() -> None:
    captured: dict[str, httpx.Headers] = {}

    def handler(request: httpx.Request) -> httpx.Response:
        captured["headers"] = request.headers
        return httpx.Response(200, json=[])

    async with GetResponseClient(api_key="my-key", transport=httpx.MockTransport(handler)) as c:
        await c.contacts.get_contact_list()

    assert captured["headers"]["X-Auth-Token"] == "api-key my-key"


async def test_access_token_sends_bearer_header() -> None:
    captured: dict[str, httpx.Headers] = {}

    def handler(request: httpx.Request) -> httpx.Response:
        captured["headers"] = request.headers
        return httpx.Response(200, json=[])

    async with GetResponseClient(
        access_token="my-token", transport=httpx.MockTransport(handler)
    ) as c:
        await c.contacts.get_contact_list()

    assert captured["headers"]["Authorization"] == "Bearer my-token"


def test_requires_exactly_one_credential() -> None:
    with pytest.raises(ValueError):
        GetResponseClient()
    with pytest.raises(ValueError):
        GetResponseClient(api_key="a", access_token="b")
