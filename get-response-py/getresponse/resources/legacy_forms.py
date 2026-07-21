"""Operations tagged 'Legacy Forms' in the GetResponse API."""

from __future__ import annotations

from datetime import datetime

from .._core import _Core
from ..models import (
    LegacyForm,
    SortOrderEnum,
)


class LegacyFormsResource:
    "Operations tagged 'Legacy Forms' in the GetResponse API."

    def __init__(self, core: _Core) -> None:
        self._core = core

    async def get_legacy_form_by_id(
        self, webform_id: str, *, fields: str | None = None
    ) -> LegacyForm:
        "Get Legacy Form by ID."
        return await self._core.request(
            "GET",
            "/webforms/{webformId}",
            path_params={"webformId": webform_id},
            query={"fields": fields},
            body=None,
            return_type=LegacyForm,
        )

    async def get_legacy_form_list(
        self,
        *,
        query_name: str | None = None,
        query_modified_on_from: datetime | None = None,
        query_modified_on_to: datetime | None = None,
        query_campaign_id: str | None = None,
        sort_modified_on: SortOrderEnum | None = None,
        fields: str | None = None,
        per_page: int | None = None,
        page: int | None = None,
    ) -> list[LegacyForm]:
        "Get the list of Legacy Forms. You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by."
        return await self._core.request(
            "GET",
            "/webforms",
            path_params=None,
            query={
                "query[name]": query_name,
                "query[modifiedOn][from]": query_modified_on_from,
                "query[modifiedOn][to]": query_modified_on_to,
                "query[campaignId]": query_campaign_id,
                "sort[modifiedOn]": sort_modified_on,
                "fields": fields,
                "perPage": per_page,
                "page": page,
            },
            body=None,
            return_type=list[LegacyForm],
        )
