"""Operations tagged 'Meta Fields' in the GetResponse API."""

from __future__ import annotations

from typing import Any

from .._core import _Core
from ..models import (
    MetaField,
    NewMetaField,
    SortOrderEnum,
    UpdateMetaField,
)


class MetaFieldsResource:
    "Operations tagged 'Meta Fields' in the GetResponse API."

    def __init__(self, core: _Core) -> None:
        self._core = core

    async def create_meta_field(self, shop_id: str, body: NewMetaField) -> MetaField:
        "Sending a **POST** request to this URL will create a new meta field resource. In order to create a new meta field, you need to send a meta field resource in the body of the request (remember that you need to serialize the body into a JSON string)"
        return await self._core.request(
            "POST",
            "/shops/{shopId}/meta-fields",
            path_params={"shopId": shop_id},
            query=None,
            body=body,
            return_type=MetaField,
        )

    async def delete_meta_field(self, shop_id: str, meta_field_id: str) -> None:
        "Delete meta field"
        return await self._core.request(
            "DELETE",
            "/shops/{shopId}/meta-fields/{metaFieldId}",
            path_params={"shopId": shop_id, "metaFieldId": meta_field_id},
            query=None,
            body=None,
            return_type=None,
        )

    async def get_meta_field(
        self, shop_id: str, meta_field_id: str, *, fields: str | None = None
    ) -> MetaField:
        "This method returns meta field with a given `metaFieldId` in the context of a given `shopId`"
        return await self._core.request(
            "GET",
            "/shops/{shopId}/meta-fields/{metaFieldId}",
            path_params={"shopId": shop_id, "metaFieldId": meta_field_id},
            query={"fields": fields},
            body=None,
            return_type=MetaField,
        )

    async def get_meta_fields(
        self,
        shop_id: str,
        *,
        query_name: str | None = None,
        query_description: str | None = None,
        query_value: str | None = None,
        query_created_on_from: dict[str, Any] | None = None,
        query_created_on_to: dict[str, Any] | None = None,
        sort_created_on: SortOrderEnum | None = None,
        fields: str | None = None,
        per_page: int | None = None,
        page: int | None = None,
    ) -> list[MetaField]:
        "Sending a **GET** request to this URL returns a collection of meta field resources that belong to the given shop. You can narrow down the list of resources by passing proper query parameters (the list of which you can find below in the request params section). You can basically search by: * name * value * description * createdOn You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by."
        return await self._core.request(
            "GET",
            "/shops/{shopId}/meta-fields",
            path_params={"shopId": shop_id},
            query={
                "query[name]": query_name,
                "query[description]": query_description,
                "query[value]": query_value,
                "query[createdOn][from]": query_created_on_from,
                "query[createdOn][to]": query_created_on_to,
                "sort[createdOn]": sort_created_on,
                "fields": fields,
                "perPage": per_page,
                "page": page,
            },
            body=None,
            return_type=list[MetaField],
        )

    async def update_meta_field(
        self, shop_id: str, meta_field_id: str, body: UpdateMetaField
    ) -> MetaField:
        "Update the properties of a shop's meta field. You should send only those fields that need to be changed. The rest of the properties will stay the same."
        return await self._core.request(
            "POST",
            "/shops/{shopId}/meta-fields/{metaFieldId}",
            path_params={"shopId": shop_id, "metaFieldId": meta_field_id},
            query=None,
            body=body,
            return_type=MetaField,
        )
