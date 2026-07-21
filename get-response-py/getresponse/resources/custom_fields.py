"""Operations tagged 'Custom Fields' in the GetResponse API."""

from __future__ import annotations

from .._core import _Core
from ..models import (
    CustomField,
    CustomFieldResponse,
    NewCustomField,
    SortOrderEnum,
    UpdateCustomField,
)


class CustomFieldsResource:
    "Operations tagged 'Custom Fields' in the GetResponse API."

    def __init__(self, core: _Core) -> None:
        self._core = core

    async def create_custom_field(self, body: NewCustomField) -> CustomFieldResponse:
        "Create a custom field"
        return await self._core.request(
            "POST",
            "/custom-fields",
            path_params=None,
            query=None,
            body=body,
            return_type=CustomFieldResponse,
        )

    async def delete_custom_field(self, custom_field_id: str) -> None:
        "Delete a single custom field definition"
        return await self._core.request(
            "DELETE",
            "/custom-fields/{customFieldId}",
            path_params={"customFieldId": custom_field_id},
            query=None,
            body=None,
            return_type=None,
        )

    async def get_custom_field_by_id(
        self, custom_field_id: str, *, fields: str | None = None
    ) -> CustomFieldResponse:
        "Returns a list of custom fields"
        return await self._core.request(
            "GET",
            "/custom-fields/{customFieldId}",
            path_params={"customFieldId": custom_field_id},
            query={"fields": fields},
            body=None,
            return_type=CustomFieldResponse,
        )

    async def get_custom_field_list(
        self,
        *,
        query_name: str | None = None,
        sort_name: SortOrderEnum | None = None,
        fields: str | None = None,
        per_page: int | None = None,
        page: int | None = None,
    ) -> list[CustomField]:
        "You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by."
        return await self._core.request(
            "GET",
            "/custom-fields",
            path_params=None,
            query={
                "query[name]": query_name,
                "sort[name]": sort_name,
                "fields": fields,
                "perPage": per_page,
                "page": page,
            },
            body=None,
            return_type=list[CustomField],
        )

    async def update_custom_field(
        self, custom_field_id: str, body: UpdateCustomField
    ) -> CustomFieldResponse:
        "Update the custom field definition"
        return await self._core.request(
            "POST",
            "/custom-fields/{customFieldId}",
            path_params={"customFieldId": custom_field_id},
            query=None,
            body=body,
            return_type=CustomFieldResponse,
        )
