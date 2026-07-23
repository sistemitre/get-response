"""Operations tagged 'Landing Page' in the GetResponse API."""

from __future__ import annotations

from datetime import datetime

from .._core import _Core
from ..models import (
    GetLpsGeneralPerformanceStatsQueryDevice,
    LpsStats,
)


class LandingPageResource:
    "Operations tagged 'Landing Page' in the GetResponse API."

    def __init__(self, core: _Core) -> None:
        self._core = core

    async def get_lps_general_performance_stats(
        self,
        lps_id: str,
        *,
        query_date_from: datetime | None = None,
        query_date_to: datetime | None = None,
        query_location: str | None = None,
        query_device: GetLpsGeneralPerformanceStatsQueryDevice | None = None,
        query_page: str | None = None,
        fields: str | None = None,
    ) -> LpsStats:
        "Get details for landing page statistics"
        return await self._core.request(
            "GET",
            "/statistics/lps/{lpsId}/performance",
            path_params={"lpsId": lps_id},
            query={
                "query[date][from]": query_date_from,
                "query[date][to]": query_date_to,
                "query[location]": query_location,
                "query[device]": query_device,
                "query[page]": query_page,
                "fields": fields,
            },
            body=None,
            return_type=LpsStats,
        )
