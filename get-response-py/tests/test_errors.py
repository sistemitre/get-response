"""Non-2xx responses raise `GetResponseApiError` with `ErrorResponse` fields populated."""

from __future__ import annotations

import httpx
import pytest

from getresponse import GetResponseApiError, GetResponseClient


async def test_error_response_maps_to_typed_exception() -> None:
    body = {
        "httpStatus": 400,
        "code": 1010,
        "codeDescription": "Invalid value",
        "message": "Email is invalid",
        "moreInfo": "https://apidocs.getresponse.com/errors/1010",
        "context": {"field": "email"},
        "uuid": "abc-123",
    }

    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(400, json=body)

    async with GetResponseClient(api_key="k", transport=httpx.MockTransport(handler)) as c:
        with pytest.raises(GetResponseApiError) as exc_info:
            await c.contacts.get_contact_list()

    err = exc_info.value
    assert err.status_code == 400
    assert err.code == 1010
    assert err.message == "Email is invalid"
    assert err.context == {"field": "email"}
    assert err.uuid == "abc-123"
