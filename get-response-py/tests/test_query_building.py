"""Bracket-notation query parameter building."""

from __future__ import annotations

from datetime import datetime, timedelta, timezone

import httpx

from getresponse import GetResponseClient


async def test_datetime_query_params_use_getresponse_date_format() -> None:
    # GetResponse expects Y-m-d\TH:i:sO (PHP format): no sub-second precision, and the UTC
    # offset without a colon (+0000, not Python's default +00:00).
    captured: dict[str, httpx.URL] = {}

    def handler(request: httpx.Request) -> httpx.Response:
        captured["url"] = request.url
        return httpx.Response(200, json=[])

    async with GetResponseClient(api_key="k", transport=httpx.MockTransport(handler)) as c:
        await c.contacts.get_contact_list(
            query_created_on_from=datetime(2024, 1, 15, 10, 30, 0, 123456, tzinfo=timezone.utc),
            query_created_on_to=datetime(
                2024, 1, 16, 10, 30, 0, tzinfo=timezone(timedelta(hours=5, minutes=30))
            ),
        )

    params = captured["url"].params
    assert params["query[createdOn][from]"] == "2024-01-15T10:30:00+0000"
    assert params["query[createdOn][to]"] == "2024-01-16T10:30:00+0530"


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
