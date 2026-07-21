"""`GetResponseClient.paginate` walks full pages and stops on a short/empty one."""

from __future__ import annotations

import httpx

from getresponse import GetResponseClient


async def test_paginate_walks_full_pages_then_stops_on_short_page() -> None:
    def contact(i: int) -> dict[str, str]:
        return {"contactId": f"id{i}", "email": f"{i}@example.com", "href": "h"}

    pages = [
        [contact(i) for i in range(50)],
        [contact(i) for i in range(50, 100)],
        [contact(100)],
    ]
    calls = {"count": 0}

    def handler(request: httpx.Request) -> httpx.Response:
        page = int(request.url.params["page"])
        calls["count"] += 1
        return httpx.Response(200, json=pages[page - 1])

    async with GetResponseClient(api_key="k", transport=httpx.MockTransport(handler)) as c:
        seen = [item async for item in c.paginate(c.contacts.get_contact_list, per_page=50)]

    assert len(seen) == 101
    assert calls["count"] == 3
