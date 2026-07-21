"""Operations tagged 'Landing Pages' in the GetResponse API."""

from __future__ import annotations

from datetime import datetime

from .._core import _Core
from ..models import (
    GetLpsListQueryStatus,
    Lps,
    LpsDetails,
    SortOrderEnum,
)


class LandingPagesResource:
    "Operations tagged 'Landing Pages' in the GetResponse API."

    def __init__(self, core: _Core) -> None:
        self._core = core

    async def get_lps_by_id(self, lps_id: str, *, fields: str | None = None) -> LpsDetails:
        "Get a single landing page by ID"
        return await self._core.request(
            "GET",
            "/lps/{lpsId}",
            path_params={"lpsId": lps_id},
            query={"fields": fields},
            body=None,
            return_type=LpsDetails,
        )

    async def get_lps_list(
        self,
        *,
        query_name: str | None = None,
        query_status: GetLpsListQueryStatus | None = None,
        stats_from: datetime | None = None,
        stats_to: datetime | None = None,
        sort_name: SortOrderEnum | None = None,
        sort_created_at: SortOrderEnum | None = None,
        sort_updated_at: SortOrderEnum | None = None,
        sort_visits: SortOrderEnum | None = None,
        sort_leads: SortOrderEnum | None = None,
        sort_subscription_rate: SortOrderEnum | None = None,
        fields: str | None = None,
        per_page: int | None = None,
        page: int | None = None,
    ) -> list[Lps]:
        "You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by."
        return await self._core.request(
            "GET",
            "/lps",
            path_params=None,
            query={
                "query[name]": query_name,
                "query[status]": query_status,
                "stats[from]": stats_from,
                "stats[to]": stats_to,
                "sort[name]": sort_name,
                "sort[createdAt]": sort_created_at,
                "sort[updatedAt]": sort_updated_at,
                "sort[visits]": sort_visits,
                "sort[leads]": sort_leads,
                "sort[subscriptionRate]": sort_subscription_rate,
                "fields": fields,
                "perPage": per_page,
                "page": page,
            },
            body=None,
            return_type=list[Lps],
        )
