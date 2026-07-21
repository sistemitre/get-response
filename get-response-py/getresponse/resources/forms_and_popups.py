"""Operations tagged 'Forms and Popups' in the GetResponse API."""

from __future__ import annotations

from datetime import datetime

from .._core import _Core
from ..models import (
    GetPopupsListQueryStatus,
    PopupDetails,
    PopupListItem,
    SortOrderEnum,
)


class FormsAndPopupsResource:
    "Operations tagged 'Forms and Popups' in the GetResponse API."

    def __init__(self, core: _Core) -> None:
        self._core = core

    async def get_popup_details(self, popup_id: str, *, fields: str | None = None) -> PopupDetails:
        "Get a single form or popup by ID"
        return await self._core.request(
            "GET",
            "/popups/{popupId}",
            path_params={"popupId": popup_id},
            query={"fields": fields},
            body=None,
            return_type=PopupDetails,
        )

    async def get_popups_list(
        self,
        *,
        query_name: str | None = None,
        query_status: GetPopupsListQueryStatus | None = None,
        stats_from: datetime | None = None,
        stats_to: datetime | None = None,
        sort_name: SortOrderEnum | None = None,
        sort_status: SortOrderEnum | None = None,
        sort_created_at: SortOrderEnum | None = None,
        sort_updated_at: SortOrderEnum | None = None,
        sort_views: SortOrderEnum | None = None,
        sort_unique_visitors: SortOrderEnum | None = None,
        sort_leads: SortOrderEnum | None = None,
        sort_ctr: SortOrderEnum | None = None,
        fields: str | None = None,
        per_page: int | None = None,
        page: int | None = None,
    ) -> list[PopupListItem]:
        "You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by."
        return await self._core.request(
            "GET",
            "/popups",
            path_params=None,
            query={
                "query[name]": query_name,
                "query[status]": query_status,
                "stats[from]": stats_from,
                "stats[to]": stats_to,
                "sort[name]": sort_name,
                "sort[status]": sort_status,
                "sort[createdAt]": sort_created_at,
                "sort[updatedAt]": sort_updated_at,
                "sort[views]": sort_views,
                "sort[uniqueVisitors]": sort_unique_visitors,
                "sort[leads]": sort_leads,
                "sort[ctr]": sort_ctr,
                "fields": fields,
                "perPage": per_page,
                "page": page,
            },
            body=None,
            return_type=list[PopupListItem],
        )
