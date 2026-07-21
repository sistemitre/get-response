"""Operations tagged 'Addresses' in the GetResponse API."""

from __future__ import annotations

from datetime import datetime

from .._core import _Core
from ..models import (
    Address,
    NewAddress,
    SortOrderEnum,
    UpdateAddress,
)


class AddressesResource:
    "Operations tagged 'Addresses' in the GetResponse API."

    def __init__(self, core: _Core) -> None:
        self._core = core

    async def create_address(self, body: NewAddress) -> Address:
        "Create address"
        return await self._core.request(
            "POST",
            "/addresses",
            path_params=None,
            query=None,
            body=body,
            return_type=Address,
        )

    async def delete_address(self, address_id: str) -> None:
        "Delete address"
        return await self._core.request(
            "DELETE",
            "/addresses/{addressId}",
            path_params={"addressId": address_id},
            query=None,
            body=None,
            return_type=None,
        )

    async def get_address(self, address_id: str, *, fields: str | None = None) -> Address:
        "Get an address by ID"
        return await self._core.request(
            "GET",
            "/addresses/{addressId}",
            path_params={"addressId": address_id},
            query={"fields": fields},
            body=None,
            return_type=Address,
        )

    async def get_address_list(
        self,
        *,
        query_name: str | None = None,
        query_first_name: str | None = None,
        query_last_name: str | None = None,
        query_address1: str | None = None,
        query_address2: str | None = None,
        query_city: str | None = None,
        query_zip: str | None = None,
        query_province: str | None = None,
        query_province_code: str | None = None,
        query_phone: str | None = None,
        query_company: str | None = None,
        query_created_on_from: datetime | None = None,
        query_created_on_to: datetime | None = None,
        sort_created_on: SortOrderEnum | None = None,
        fields: str | None = None,
        per_page: int | None = None,
        page: int | None = None,
    ) -> list[Address]:
        "Sending a **GET** request to this URL returns collection of address resources. You can narrow down the list of resources by passing proper query parameters (the list of which you can find below in the request params section). You can basically search by: * name * firstName * lastName * address1 * address2 * city * zip * province * provinceCode * phone * company * createdOn The `name` field can be a pattern and we'll try to match this phrase. You can specify which page of the results you want and how many results per page to display. You can also specify the sort-order using one or more of the allowed fields (listed below in the request params section). Last but not least, you can even specify which fields from a resource you want to get. If you pass the param `fields` with the list of fields (separated by a comma [,]) we'll return the list of resources with only those fields (we'll always add a resource ID to ensure that you can use that data later on) You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by."
        return await self._core.request(
            "GET",
            "/addresses",
            path_params=None,
            query={
                "query[name]": query_name,
                "query[firstName]": query_first_name,
                "query[lastName]": query_last_name,
                "query[address1]": query_address1,
                "query[address2]": query_address2,
                "query[city]": query_city,
                "query[zip]": query_zip,
                "query[province]": query_province,
                "query[provinceCode]": query_province_code,
                "query[phone]": query_phone,
                "query[company]": query_company,
                "query[createdOn][from]": query_created_on_from,
                "query[createdOn][to]": query_created_on_to,
                "sort[createdOn]": sort_created_on,
                "fields": fields,
                "perPage": per_page,
                "page": page,
            },
            body=None,
            return_type=list[Address],
        )

    async def update_address(self, address_id: str, body: UpdateAddress) -> Address:
        "Update an existing address. You should send only those fields that need to be changed. The rest of the properties will stay the same."
        return await self._core.request(
            "POST",
            "/addresses/{addressId}",
            path_params={"addressId": address_id},
            query=None,
            body=body,
            return_type=Address,
        )
