"""Operations tagged 'Website' in the GetResponse API."""

from __future__ import annotations

from typing import Any

from .._core import _Core
from ..models import (
    GetWbeGeneralPerformanceStatsQueryDevice,
    WebsiteStats,
)


class WebsiteResource:
    "Operations tagged 'Website' in the GetResponse API."

    def __init__(self, core: _Core) -> None:
        self._core = core

    async def get_wbe_general_performance_stats(
        self,
        website_id: str,
        *,
        query_date_from: dict[str, Any] | None = None,
        query_date_to: dict[str, Any] | None = None,
        query_location: str | None = None,
        query_device: GetWbeGeneralPerformanceStatsQueryDevice | None = None,
        query_page: str | None = None,
        fields: str | None = None,
    ) -> WebsiteStats:
        "Get details for website statistics"
        return await self._core.request(
            "GET",
            "/statistics/wbe/{websiteId}/performance",
            path_params={"websiteId": website_id},
            query={
                "query[date][from]": query_date_from,
                "query[date][to]": query_date_to,
                "query[location]": query_location,
                "query[device]": query_device,
                "query[page]": query_page,
                "fields": fields,
            },
            body=None,
            return_type=WebsiteStats,
        )
