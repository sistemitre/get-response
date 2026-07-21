"""Operations tagged 'From Fields' in the GetResponse API."""

from __future__ import annotations

from datetime import datetime

from .._core import _Core
from ..models import (
    FromField,
    NewFromField,
    SortOrderEnum,
)


class FromFieldsResource:
    "Operations tagged 'From Fields' in the GetResponse API."

    def __init__(self, core: _Core) -> None:
        self._core = core

    async def create_from_field(self, body: NewFromField) -> FromField:
        "Create 'From' address"
        return await self._core.request(
            "POST",
            "/from-fields",
            path_params=None,
            query=None,
            body=body,
            return_type=FromField,
        )

    async def delete_from_field(
        self, from_field_id: str, *, from_field_id_to_replace_with: str | None = None
    ) -> None:
        "Delete 'From' address"
        return await self._core.request(
            "DELETE",
            "/from-fields/{fromFieldId}",
            path_params={"fromFieldId": from_field_id},
            query={"fromFieldIdToReplaceWith": from_field_id_to_replace_with},
            body=None,
            return_type=None,
        )

    async def get_from_field_by_id(
        self, from_field_id: str, *, fields: str | None = None
    ) -> FromField:
        "Get a single 'From' address by ID"
        return await self._core.request(
            "GET",
            "/from-fields/{fromFieldId}",
            path_params={"fromFieldId": from_field_id},
            query={"fields": fields},
            body=None,
            return_type=FromField,
        )

    async def get_from_field_list(
        self,
        *,
        query_email: str | None = None,
        query_name: datetime | None = None,
        query_is_default: bool | None = None,
        query_is_active: bool | None = None,
        sort_created_on: SortOrderEnum | None = None,
        fields: str | None = None,
        per_page: int | None = None,
        page: int | None = None,
    ) -> list[FromField]:
        "You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by."
        return await self._core.request(
            "GET",
            "/from-fields",
            path_params=None,
            query={
                "query[email]": query_email,
                "query[name]": query_name,
                "query[isDefault]": query_is_default,
                "query[isActive]": query_is_active,
                "sort[createdOn]": sort_created_on,
                "fields": fields,
                "perPage": per_page,
                "page": page,
            },
            body=None,
            return_type=list[FromField],
        )

    async def set_from_field_as_default(self, from_field_id: str) -> None:
        "Set a 'From' address as default"
        return await self._core.request(
            "POST",
            "/from-fields/{fromFieldId}/default",
            path_params={"fromFieldId": from_field_id},
            query=None,
            body=None,
            return_type=None,
        )
