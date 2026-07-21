"""Operations tagged 'Webinars' in the GetResponse API."""

from __future__ import annotations

from .._core import _Core
from ..models import (
    GetWebinarListQueryStatus,
    GetWebinarListQueryType,
    SortOrderEnum,
    Webinar,
)


class WebinarsResource:
    "Operations tagged 'Webinars' in the GetResponse API."

    def __init__(self, core: _Core) -> None:
        self._core = core

    async def get_webinar_by_id(self, webinar_id: str, *, fields: str | None = None) -> Webinar:
        "Get a webinar by ID"
        return await self._core.request(
            "GET",
            "/webinars/{webinarId}",
            path_params={"webinarId": webinar_id},
            query={"fields": fields},
            body=None,
            return_type=Webinar,
        )

    async def get_webinar_list(
        self,
        *,
        query_name: str | None = None,
        query_campaign_id: str | None = None,
        query_status: GetWebinarListQueryStatus | None = None,
        sort_name: SortOrderEnum | None = None,
        sort_created_on: SortOrderEnum | None = None,
        sort_starts_on: SortOrderEnum | None = None,
        query_type: GetWebinarListQueryType | None = None,
        fields: str | None = None,
        per_page: int | None = None,
        page: int | None = None,
    ) -> list[Webinar]:
        "You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by."
        return await self._core.request(
            "GET",
            "/webinars",
            path_params=None,
            query={
                "query[name]": query_name,
                "query[campaignId]": query_campaign_id,
                "query[status]": query_status,
                "sort[name]": sort_name,
                "sort[createdOn]": sort_created_on,
                "sort[startsOn]": sort_starts_on,
                "query[type]": query_type,
                "fields": fields,
                "perPage": per_page,
                "page": page,
            },
            body=None,
            return_type=list[Webinar],
        )
