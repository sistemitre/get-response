"""Operations tagged 'Orders' in the GetResponse API."""

from __future__ import annotations

from datetime import datetime

from .._core import _Core
from ..models import (
    NewOrder,
    Order,
    OrderResponse,
    SortOrderEnum,
    UpdateOrder,
)


class OrdersResource:
    "Operations tagged 'Orders' in the GetResponse API."

    def __init__(self, core: _Core) -> None:
        self._core = core

    async def create_order(
        self, shop_id: str, body: NewOrder, *, additional_flags: str | None = None
    ) -> OrderResponse:
        "Sending a **POST** request to this URL will create a new order resource. In order to create a new order, you need to send the order resource in the body of the request (remember that you need to serialize the body into a JSON string)."
        return await self._core.request(
            "POST",
            "/shops/{shopId}/orders",
            path_params={"shopId": shop_id},
            query={"additionalFlags": additional_flags},
            body=body,
            return_type=OrderResponse,
        )

    async def delete_order(self, shop_id: str, order_id: str) -> None:
        "Delete order"
        return await self._core.request(
            "DELETE",
            "/shops/{shopId}/orders/{orderId}",
            path_params={"shopId": shop_id, "orderId": order_id},
            query=None,
            body=None,
            return_type=None,
        )

    async def get_order_by_id(
        self, shop_id: str, order_id: str, *, fields: str | None = None
    ) -> OrderResponse:
        "This method returns the order according to the given `orderId`."
        return await self._core.request(
            "GET",
            "/shops/{shopId}/orders/{orderId}",
            path_params={"shopId": shop_id, "orderId": order_id},
            query={"fields": fields},
            body=None,
            return_type=OrderResponse,
        )

    async def get_order_list(
        self,
        shop_id: str,
        *,
        query_description: str | None = None,
        query_status: str | None = None,
        query_external_id: str | None = None,
        query_processed_at_from: datetime | None = None,
        query_processed_at_to: datetime | None = None,
        sort_created_on: SortOrderEnum | None = None,
        fields: str | None = None,
        per_page: int | None = None,
        page: int | None = None,
    ) -> list[Order]:
        "Sending a **GET** request to this URL returns a collection of order resources that belong to the given shop. You can narrow down the list of resources by passing proper query parameters (the list of which you can find below in the request params section). You can basically search by: * description * status * externalId * processedAt The `description` fields can be a pattern and we'll try to match this phrase. You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by."
        return await self._core.request(
            "GET",
            "/shops/{shopId}/orders",
            path_params={"shopId": shop_id},
            query={
                "query[description]": query_description,
                "query[status]": query_status,
                "query[externalId]": query_external_id,
                "query[processedAt][from]": query_processed_at_from,
                "query[processedAt][to]": query_processed_at_to,
                "sort[createdOn]": sort_created_on,
                "fields": fields,
                "perPage": per_page,
                "page": page,
            },
            body=None,
            return_type=list[Order],
        )

    async def update_order(
        self, shop_id: str, order_id: str, body: UpdateOrder, *, additional_flags: str | None = None
    ) -> OrderResponse:
        "Update the properties of a shop's order. You should send only those fields that need to be changed. The rest of the properties will stay the same. However, in case of `billingAddress` and `shippingAddress`, you must send the entire representation. Individual fields can't be updated. If you want to update individual fields of an address, you can do so using `POST /v3/addresses/{addressId}`. In case of `selectedVariants`, when the collection is updated, the old collection is completely removed. The same goes for meta fields. Individual fields can't be updated either. The full representations of `selectedVariants` and `metaFields` must be sent instead."
        return await self._core.request(
            "POST",
            "/shops/{shopId}/orders/{orderId}",
            path_params={"shopId": shop_id, "orderId": order_id},
            query={"additionalFlags": additional_flags},
            body=body,
            return_type=OrderResponse,
        )
