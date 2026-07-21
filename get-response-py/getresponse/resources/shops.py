"""Operations tagged 'Shops' in the GetResponse API."""

from __future__ import annotations

from typing import Any

from .._core import _Core
from ..models import (
    NewShop,
    ShopDetails,
    SortOrderEnum,
    UpdateShop,
)


class ShopsResource:
    "Operations tagged 'Shops' in the GetResponse API."

    def __init__(self, core: _Core) -> None:
        self._core = core

    async def create_shop(self, body: NewShop) -> ShopDetails:
        "This method makes it possible to create a new shop."
        return await self._core.request(
            "POST",
            "/shops",
            path_params=None,
            query=None,
            body=body,
            return_type=ShopDetails,
        )

    async def delete_shop(self, shop_id: str) -> None:
        "This method deletes a shop."
        return await self._core.request(
            "DELETE",
            "/shops/{shopId}",
            path_params={"shopId": shop_id},
            query=None,
            body=None,
            return_type=None,
        )

    async def get_shop_by_id(self, shop_id: str, *, fields: str | None = None) -> ShopDetails:
        "This method returns the shop according to the given `shopId`"
        return await self._core.request(
            "GET",
            "/shops/{shopId}",
            path_params={"shopId": shop_id},
            query={"fields": fields},
            body=None,
            return_type=ShopDetails,
        )

    async def get_shop_list(
        self,
        *,
        query_name: str | None = None,
        sort_name: SortOrderEnum | None = None,
        sort_created_on: SortOrderEnum | None = None,
        fields: str | None = None,
        per_page: int | None = None,
        page: int | None = None,
    ) -> list[dict[str, Any]]:
        "Sending a **GET** request to this URL returns a collection of shop resources. You can narrow down the list of resources by passing proper query parameters (the list of which you can find below in the request params section). You can basically search by: * name The `name` fields can be a pattern and we'll try to match this phrase. You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by."
        return await self._core.request(
            "GET",
            "/shops",
            path_params=None,
            query={
                "query[name]": query_name,
                "sort[name]": sort_name,
                "sort[createdOn]": sort_created_on,
                "fields": fields,
                "perPage": per_page,
                "page": page,
            },
            body=None,
            return_type=list[dict[str, Any]],
        )

    async def update_shop(self, shop_id: str, body: UpdateShop) -> ShopDetails:
        "This makes it possible to update shop preferences. You should send only those fields that need to be changed. The rest of the properties remain the same."
        return await self._core.request(
            "POST",
            "/shops/{shopId}",
            path_params={"shopId": shop_id},
            query=None,
            body=body,
            return_type=ShopDetails,
        )
