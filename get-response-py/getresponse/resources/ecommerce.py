"""Operations tagged 'Ecommerce' in the GetResponse API."""

from __future__ import annotations

from datetime import datetime

from .._core import _Core
from ..models import (
    GeneralPerformanceStats,
    RevenueStatistics,
)


class EcommerceResource:
    "Operations tagged 'Ecommerce' in the GetResponse API."

    def __init__(self, core: _Core) -> None:
        self._core = core

    async def get_general_performance_stats(
        self,
        *,
        query_order_date_from: datetime | None = None,
        query_order_date_to: datetime | None = None,
        query_shop_id: str | None = None,
        fields: str | None = None,
    ) -> GeneralPerformanceStats:
        "Get the ecommerce general performance statistics"
        return await self._core.request(
            "GET",
            "/statistics/ecommerce/performance",
            path_params=None,
            query={
                "query[orderDate][from]": query_order_date_from,
                "query[orderDate][to]": query_order_date_to,
                "query[shopId]": query_shop_id,
                "fields": fields,
            },
            body=None,
            return_type=GeneralPerformanceStats,
        )

    async def get_revenue_stats(
        self,
        *,
        query_order_date_from: datetime | None = None,
        query_order_date_to: datetime | None = None,
        query_shop_id: str | None = None,
        fields: str | None = None,
    ) -> RevenueStatistics:
        "Get the ecommerce revenue statistics"
        return await self._core.request(
            "GET",
            "/statistics/ecommerce/revenue",
            path_params=None,
            query={
                "query[orderDate][from]": query_order_date_from,
                "query[orderDate][to]": query_order_date_to,
                "query[shopId]": query_shop_id,
                "fields": fields,
            },
            body=None,
            return_type=RevenueStatistics,
        )
