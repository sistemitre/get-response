"""Bracket-notation query parameter building."""

from __future__ import annotations

import httpx

from getresponse import GetResponseClient


async def test_query_params_use_bracket_notation_and_skip_none() -> None:
    captured: dict[str, httpx.URL] = {}

    def handler(request: httpx.Request) -> httpx.Response:
        captured["url"] = request.url
        return httpx.Response(200, json=[])

    async with GetResponseClient(api_key="k", transport=httpx.MockTransport(handler)) as c:
        await c.contacts.get_contact_list(
            query_email="a@b.com", sort_name="asc", page=2, per_page=50
        )

    params = captured["url"].params
    assert params["query[email]"] == "a@b.com"
    assert params["sort[name]"] == "asc"
    assert params["page"] == "2"
    assert params["perPage"] == "50"
    assert "query[name]" not in params
