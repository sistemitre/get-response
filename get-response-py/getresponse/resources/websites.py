"""Operations tagged 'Websites' in the GetResponse API."""

from __future__ import annotations

from datetime import datetime

from .._core import _Core
from ..models import (
    GetWebsitesListQueryStatus,
    SortOrderEnum,
    Website,
    WebsiteDetails,
)


class WebsitesResource:
    "Operations tagged 'Websites' in the GetResponse API."

    def __init__(self, core: _Core) -> None:
        self._core = core

    async def get_website_by_id(
        self, website_id: str, *, fields: str | None = None
    ) -> WebsiteDetails:
        "Get a single Website by ID"
        return await self._core.request(
            "GET",
            "/websites/{websiteId}",
            path_params={"websiteId": website_id},
            query={"fields": fields},
            body=None,
            return_type=WebsiteDetails,
        )

    async def get_websites_list(
        self,
        *,
        query_name: str | None = None,
        query_status: GetWebsitesListQueryStatus | None = None,
        stats_from: datetime | None = None,
        stats_to: datetime | None = None,
        sort_name: SortOrderEnum | None = None,
        sort_created_at: SortOrderEnum | None = None,
        sort_updated_at: SortOrderEnum | None = None,
        sort_page_views: SortOrderEnum | None = None,
        sort_visits: SortOrderEnum | None = None,
        sort_unique_visitors: SortOrderEnum | None = None,
        fields: str | None = None,
        per_page: int | None = None,
        page: int | None = None,
    ) -> list[Website]:
        "You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by."
        return await self._core.request(
            "GET",
            "/websites",
            path_params=None,
            query={
                "query[name]": query_name,
                "query[status]": query_status,
                "stats[from]": stats_from,
                "stats[to]": stats_to,
                "sort[name]": sort_name,
                "sort[createdAt]": sort_created_at,
                "sort[updatedAt]": sort_updated_at,
                "sort[pageViews]": sort_page_views,
                "sort[visits]": sort_visits,
                "sort[uniqueVisitors]": sort_unique_visitors,
                "fields": fields,
                "perPage": per_page,
                "page": page,
            },
            body=None,
            return_type=list[Website],
        )
