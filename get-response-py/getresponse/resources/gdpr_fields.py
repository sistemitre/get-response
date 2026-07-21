"""Operations tagged 'GDPR Fields' in the GetResponse API."""

from __future__ import annotations

from .._core import _Core
from ..models import (
    GDPRField,
    GDPRFieldDetails,
    SortOrderEnum,
)


class GdprFieldsResource:
    "Operations tagged 'GDPR Fields' in the GetResponse API."

    def __init__(self, core: _Core) -> None:
        self._core = core

    async def get_gdpr_field(
        self, gdpr_field_id: str, *, fields: str | None = None
    ) -> GDPRFieldDetails:
        "Get GDPR Field details"
        return await self._core.request(
            "GET",
            "/gdpr-fields/{gdprFieldId}",
            path_params={"gdprFieldId": gdpr_field_id},
            query={"fields": fields},
            body=None,
            return_type=GDPRFieldDetails,
        )

    async def get_gdpr_field_list(
        self,
        *,
        sort_name: SortOrderEnum | None = None,
        sort_created_on: SortOrderEnum | None = None,
        fields: str | None = None,
        per_page: int | None = None,
        page: int | None = None,
    ) -> list[GDPRField]:
        "Get the GDPR fields list"
        return await self._core.request(
            "GET",
            "/gdpr-fields",
            path_params=None,
            query={
                "sort[name]": sort_name,
                "sort[createdOn]": sort_created_on,
                "fields": fields,
                "perPage": per_page,
                "page": page,
            },
            body=None,
            return_type=list[GDPRField],
        )
