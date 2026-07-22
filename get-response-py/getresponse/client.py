"""Root async client: auth, resource groups, lifecycle, and pagination."""

from __future__ import annotations

from collections.abc import AsyncIterator, Awaitable, Callable
from typing import Any

import httpx

from ._core import DEFAULT_BASE_URL, _Core
from ._ratelimit import RateLimitOptions
from ._resource_groups import _ResourceGroups


class GetResponseClient(_ResourceGroups):
    """Async GetResponse v3 API client; one resource-group attribute per tag."""

    def __init__(
        self,
        api_key: str | None = None,
        *,
        access_token: str | None = None,
        base_url: str = DEFAULT_BASE_URL,
        timeout: float = 30.0,
        transport: httpx.AsyncBaseTransport | None = None,
        rate_limit: RateLimitOptions | None = None,
    ) -> None:
        if (api_key is None) == (access_token is None):
            raise ValueError("Provide exactly one of `api_key` or `access_token`.")
        headers = (
            {"X-Auth-Token": f"api-key {api_key}"}
            if api_key is not None
            else {"Authorization": f"Bearer {access_token}"}
        )
        self._client = httpx.AsyncClient(
            base_url=base_url, headers=headers, timeout=timeout, transport=transport
        )
        self._core = _Core(self._client, rate_limit)
        self._attach_resource_groups(self._core)

    async def aclose(self) -> None:
        """Close the underlying HTTP connection pool."""
        await self._client.aclose()

    async def __aenter__(self) -> GetResponseClient:
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        tb: object | None,
    ) -> None:
        await self.aclose()

    async def paginate(
        self,
        list_method: Callable[..., Awaitable[list[Any]]],
        *,
        per_page: int = 100,
        **kwargs: Any,
    ) -> AsyncIterator[Any]:
        """Walk every page of a `list_*` resource method, yielding items one by one.

        GetResponse also reports `TotalCount`/`CurrentPage`/`TotalPages` response
        headers, but resource methods only return typed bodies (no header access),
        so this walks by page length instead: it stops once a page comes back empty
        or shorter than `per_page`.
        """
        page = 1
        while True:
            items = await list_method(page=page, per_page=per_page, **kwargs)
            if not items:
                return
            for item in items:
                yield item
            if len(items) < per_page:
                return
            page += 1
