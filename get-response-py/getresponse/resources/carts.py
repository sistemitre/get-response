"""Operations tagged 'Carts' in the GetResponse API."""

from __future__ import annotations

from datetime import datetime

from .._core import _Core
from ..models import (
    Cart,
    NewCart,
    SortOrderEnum,
    UpdateCart,
)


class CartsResource:
    "Operations tagged 'Carts' in the GetResponse API."

    def __init__(self, core: _Core) -> None:
        self._core = core

    async def create_cart(self, shop_id: str, body: NewCart) -> Cart:
        "Sending a **POST** request to this URL will create a new cart resource. In order to create a new cart, you need to send the cart resource in the body of the request (remember that you need to serialize the body into a JSON string)"
        return await self._core.request(
            "POST",
            "/shops/{shopId}/carts",
            path_params={"shopId": shop_id},
            query=None,
            body=body,
            return_type=Cart,
        )

    async def delete_cart(self, shop_id: str, cart_id: str) -> None:
        "Delete cart"
        return await self._core.request(
            "DELETE",
            "/shops/{shopId}/carts/{cartId}",
            path_params={"shopId": shop_id, "cartId": cart_id},
            query=None,
            body=None,
            return_type=None,
        )

    async def get_cart(self, shop_id: str, cart_id: str, *, fields: str | None = None) -> Cart:
        "This method returns cart with the given `cartId` in the context of a given `shopId`"
        return await self._core.request(
            "GET",
            "/shops/{shopId}/carts/{cartId}",
            path_params={"shopId": shop_id, "cartId": cart_id},
            query={"fields": fields},
            body=None,
            return_type=Cart,
        )

    async def get_carts(
        self,
        shop_id: str,
        *,
        query_created_on_from: datetime | None = None,
        query_created_on_to: datetime | None = None,
        query_external_id: str | None = None,
        sort_created_on: SortOrderEnum | None = None,
        fields: str | None = None,
        per_page: int | None = None,
        page: int | None = None,
    ) -> list[Cart]:
        "Sending a **GET** request to this URL returns a collection of cart resources that belong to the given shop. You can narrow down the list of resources by passing proper query parameters (the list of which you can find below in the request params section). You can basically search by: * externalId * createdOn You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by."
        return await self._core.request(
            "GET",
            "/shops/{shopId}/carts",
            path_params={"shopId": shop_id},
            query={
                "query[createdOn][from]": query_created_on_from,
                "query[createdOn][to]": query_created_on_to,
                "query[externalId]": query_external_id,
                "sort[createdOn]": sort_created_on,
                "fields": fields,
                "perPage": per_page,
                "page": page,
            },
            body=None,
            return_type=list[Cart],
        )

    async def update_cart(self, shop_id: str, cart_id: str, body: UpdateCart) -> Cart:
        "Update properties of the shop cart. You should send only those fields that need to be changed. The rest of the properties will stay the same. In case of selectedVariants, when the collection is updated, the old one is completely removed."
        return await self._core.request(
            "POST",
            "/shops/{shopId}/carts/{cartId}",
            path_params={"shopId": shop_id, "cartId": cart_id},
            query=None,
            body=body,
            return_type=Cart,
        )
