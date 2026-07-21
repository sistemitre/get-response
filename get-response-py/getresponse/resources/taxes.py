"""Operations tagged 'Taxes' in the GetResponse API."""

from __future__ import annotations

from typing import Any

from .._core import _Core
from ..models import (
    NewTax,
    SortOrderEnum,
    Tax,
    UpdateTax,
)


class TaxesResource:
    "Operations tagged 'Taxes' in the GetResponse API."

    def __init__(self, core: _Core) -> None:
        self._core = core

    async def create_tax(self, shop_id: str, body: NewTax) -> Tax:
        "Sending a **POST** request to this URL will create a new tax resource. In order to create a new tax, you need to send a tax resource in the body of the request (remember that you need to serialize the body into a JSON string)"
        return await self._core.request(
            "POST",
            "/shops/{shopId}/taxes",
            path_params={"shopId": shop_id},
            query=None,
            body=body,
            return_type=Tax,
        )

    async def delete_tax(self, shop_id: str, tax_id: str) -> None:
        "Delete tax by ID"
        return await self._core.request(
            "DELETE",
            "/shops/{shopId}/taxes/{taxId}",
            path_params={"shopId": shop_id, "taxId": tax_id},
            query=None,
            body=None,
            return_type=None,
        )

    async def get_tax_by_id(self, shop_id: str, tax_id: str, *, fields: str | None = None) -> Tax:
        "This method returns tax with a given `taxId` in the context of a given `shopId`"
        return await self._core.request(
            "GET",
            "/shops/{shopId}/taxes/{taxId}",
            path_params={"shopId": shop_id, "taxId": tax_id},
            query={"fields": fields},
            body=None,
            return_type=Tax,
        )

    async def get_tax_list(
        self,
        shop_id: str,
        *,
        query_name: str | None = None,
        query_created_on_from: dict[str, Any] | None = None,
        query_created_on_to: dict[str, Any] | None = None,
        sort_created_on: SortOrderEnum | None = None,
        fields: str | None = None,
        per_page: int | None = None,
        page: int | None = None,
    ) -> list[Tax]:
        "Sending **GET** request to this URL returns a collection of tax resources that belong to the given shop. You can narrow down the list of resources by passing proper query parameters (the list of which you can find below, in the request params section). You can basically search by: * name * createdOn You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by."
        return await self._core.request(
            "GET",
            "/shops/{shopId}/taxes",
            path_params={"shopId": shop_id},
            query={
                "query[name]": query_name,
                "query[createdOn][from]": query_created_on_from,
                "query[createdOn][to]": query_created_on_to,
                "sort[createdOn]": sort_created_on,
                "fields": fields,
                "perPage": per_page,
                "page": page,
            },
            body=None,
            return_type=list[Tax],
        )

    async def update_tax(self, shop_id: str, tax_id: str, body: UpdateTax) -> Tax:
        "Update the properties of the shop tax. You should only send the fields that need to be changed. The rest of the properties will stay the same."
        return await self._core.request(
            "POST",
            "/shops/{shopId}/taxes/{taxId}",
            path_params={"shopId": shop_id, "taxId": tax_id},
            query=None,
            body=body,
            return_type=Tax,
        )
