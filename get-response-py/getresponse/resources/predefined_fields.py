"""Operations tagged 'Predefined Fields' in the GetResponse API."""

from __future__ import annotations

from .._core import _Core
from ..models import (
    NewPredefinedField,
    PredefinedField,
    SortOrderEnum,
    UpdatePredefinedField,
)


class PredefinedFieldsResource:
    "Operations tagged 'Predefined Fields' in the GetResponse API."

    def __init__(self, core: _Core) -> None:
        self._core = core

    async def create_predefined_field(self, body: NewPredefinedField) -> PredefinedField:
        "Makes it possible to create a new predefined field."
        return await self._core.request(
            "POST",
            "/predefined-fields",
            path_params=None,
            query=None,
            body=body,
            return_type=PredefinedField,
        )

    async def delete_predefined_field(self, predefined_field_id: str) -> None:
        "Delete a predefined field"
        return await self._core.request(
            "DELETE",
            "/predefined-fields/{predefinedFieldId}",
            path_params={"predefinedFieldId": predefined_field_id},
            query=None,
            body=None,
            return_type=None,
        )

    async def get_predefined_field_by_id(
        self, predefined_field_id: str, *, fields: str | None = None
    ) -> PredefinedField:
        "Get detailed information about a specified predefined field."
        return await self._core.request(
            "GET",
            "/predefined-fields/{predefinedFieldId}",
            path_params={"predefinedFieldId": predefined_field_id},
            query={"fields": fields},
            body=None,
            return_type=PredefinedField,
        )

    async def get_predefined_field_list(
        self,
        *,
        sort_name: SortOrderEnum | None = None,
        query_name: str | None = None,
        query_campaign_id: str | None = None,
        fields: str | None = None,
        per_page: int | None = None,
        page: int | None = None,
    ) -> list[PredefinedField]:
        "You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by."
        return await self._core.request(
            "GET",
            "/predefined-fields",
            path_params=None,
            query={
                "sort[name]": sort_name,
                "query[name]": query_name,
                "query[campaignId]": query_campaign_id,
                "fields": fields,
                "perPage": per_page,
                "page": page,
            },
            body=None,
            return_type=list[PredefinedField],
        )

    async def update_predefined_field(
        self, predefined_field_id: str, body: UpdatePredefinedField
    ) -> PredefinedField:
        "Update a predefined field"
        return await self._core.request(
            "POST",
            "/predefined-fields/{predefinedFieldId}",
            path_params={"predefinedFieldId": predefined_field_id},
            query=None,
            body=body,
            return_type=PredefinedField,
        )
