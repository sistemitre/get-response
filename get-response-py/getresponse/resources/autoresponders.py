"""Operations tagged 'Autoresponders' in the GetResponse API."""

from __future__ import annotations

from datetime import datetime
from typing import Any

from .._core import _Core
from ..models import (
    AutoresponderDetails,
    GetAutoresponderListQueryStatus,
    GetAutoresponderStatisticsCollectionQueryGroupBy,
    GetAutoresponderThumbnailSize,
    GetSingleAutoresponderStatisticsQueryGroupBy,
    MessageStatisticsListElement,
    NewAutoresponder,
    SortOrderEnum,
    UpdateAutoresponder,
)


class AutorespondersResource:
    "Operations tagged 'Autoresponders' in the GetResponse API."

    def __init__(self, core: _Core) -> None:
        self._core = core

    async def create_autoresponder(self, body: NewAutoresponder) -> AutoresponderDetails:
        "> **The action-based autoresponder feature has been migrated over to marketing automation. Your existing autoresponders are now converted into workflows. You can no longer create and update action-based autoresponders using our API.** This request allows you to create an autoresponder. Remember to select the proper `sendSettings` - depending on `type` you need to fill corresponding setting (eg. if you selected type `delay`, then you MUST fill `delayInHours` field)."
        return await self._core.request(
            "POST",
            "/autoresponders",
            path_params=None,
            query=None,
            body=body,
            return_type=AutoresponderDetails,
        )

    async def delete_autoresponder(self, autoresponder_id: str) -> None:
        "Delete autoresponder."
        return await self._core.request(
            "DELETE",
            "/autoresponders/{autoresponderId}",
            path_params={"autoresponderId": autoresponder_id},
            query=None,
            body=None,
            return_type=None,
        )

    async def get_autoresponder(
        self, autoresponder_id: str, *, fields: str | None = None
    ) -> AutoresponderDetails:
        "Get a single autoresponder by its ID"
        return await self._core.request(
            "GET",
            "/autoresponders/{autoresponderId}",
            path_params={"autoresponderId": autoresponder_id},
            query={"fields": fields},
            body=None,
            return_type=AutoresponderDetails,
        )

    async def get_autoresponder_list(
        self,
        *,
        query_subject: str | None = None,
        query_name: str | None = None,
        query_status: GetAutoresponderListQueryStatus | None = None,
        query_created_on_from: datetime | None = None,
        query_created_on_to: datetime | None = None,
        query_campaign_id: str | None = None,
        sort_name: SortOrderEnum | None = None,
        sort_subject: SortOrderEnum | None = None,
        sort_day_of_cycle: SortOrderEnum | None = None,
        sort_delivered: SortOrderEnum | None = None,
        sort_open_rate: SortOrderEnum | None = None,
        sort_click_rate: SortOrderEnum | None = None,
        sort_created_on: SortOrderEnum | None = None,
        fields: str | None = None,
        per_page: int | None = None,
        page: int | None = None,
    ) -> list[dict[str, Any]]:
        "You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by."
        return await self._core.request(
            "GET",
            "/autoresponders",
            path_params=None,
            query={
                "query[subject]": query_subject,
                "query[name]": query_name,
                "query[status]": query_status,
                "query[createdOn][from]": query_created_on_from,
                "query[createdOn][to]": query_created_on_to,
                "query[campaignId]": query_campaign_id,
                "sort[name]": sort_name,
                "sort[subject]": sort_subject,
                "sort[dayOfCycle]": sort_day_of_cycle,
                "sort[delivered]": sort_delivered,
                "sort[openRate]": sort_open_rate,
                "sort[clickRate]": sort_click_rate,
                "sort[createdOn]": sort_created_on,
                "fields": fields,
                "perPage": per_page,
                "page": page,
            },
            body=None,
            return_type=list[dict[str, Any]],
        )

    async def get_autoresponder_statistics_collection(
        self,
        *,
        query_group_by: GetAutoresponderStatisticsCollectionQueryGroupBy | None = None,
        query_autoreponder_id: str | None = None,
        query_campaign_id: str | None = None,
        query_created_on_from: datetime | None = None,
        query_created_on_to: datetime | None = None,
        fields: str | None = None,
        per_page: int | None = None,
        page: int | None = None,
    ) -> list[MessageStatisticsListElement]:
        "> This returns the statistics summary for selected autoresponders. You can select them by specifying the autoresponder or campaign IDs. As in all statistics, you can change the date and time range (hourly daily monthly or total). Keep in mind that all statistics date ranges are given in standard UTC period type objects. ([See ISO 8601 standard](http://en.wikipedia.org/wiki/ISO_8601#Time_intervals)) (https://app.getresponse.com/statistics.html?t=followup#total). You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by."
        return await self._core.request(
            "GET",
            "/autoresponders/statistics",
            path_params=None,
            query={
                "query[groupBy]": query_group_by,
                "query[autoreponderId]": query_autoreponder_id,
                "query[campaignId]": query_campaign_id,
                "query[createdOn][from]": query_created_on_from,
                "query[createdOn][to]": query_created_on_to,
                "fields": fields,
                "perPage": per_page,
                "page": page,
            },
            body=None,
            return_type=list[MessageStatisticsListElement],
        )

    async def get_autoresponder_thumbnail(
        self, autoresponder_id: str, *, size: GetAutoresponderThumbnailSize | None = None
    ) -> None:
        "Get the autoresponder thumbnail"
        return await self._core.request(
            "GET",
            "/autoresponders/{autoresponderId}/thumbnail",
            path_params={"autoresponderId": autoresponder_id},
            query={"size": size},
            body=None,
            return_type=None,
        )

    async def get_single_autoresponder_statistics(
        self,
        autoresponder_id: str,
        *,
        query_group_by: GetSingleAutoresponderStatisticsQueryGroupBy | None = None,
        query_created_on_from: datetime | None = None,
        query_created_on_to: datetime | None = None,
        fields: str | None = None,
        per_page: int | None = None,
        page: int | None = None,
    ) -> list[MessageStatisticsListElement]:
        "> This requst returns the statistics summary for a single given autoresponder. As in all statistics, you can change the date and time range (hourly daily monthly or total). Keep in mind that all statistics date ranges are given in standard UTC period type objects. ([See ISO 8601 standard](http://en.wikipedia.org/wiki/ISO_8601#Time_intervals)) (https://app.getresponse.com/statistics.html?t=followup#total). You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by."
        return await self._core.request(
            "GET",
            "/autoresponders/{autoresponderId}/statistics",
            path_params={"autoresponderId": autoresponder_id},
            query={
                "query[groupBy]": query_group_by,
                "query[createdOn][from]": query_created_on_from,
                "query[createdOn][to]": query_created_on_to,
                "fields": fields,
                "perPage": per_page,
                "page": page,
            },
            body=None,
            return_type=list[MessageStatisticsListElement],
        )

    async def update_autoresponder(
        self, autoresponder_id: str, body: UpdateAutoresponder
    ) -> AutoresponderDetails:
        "> **The action-based autoresponder feature has been migrated over to marketing automation. Your existing autoresponders are now converted into workflows. You can no longer create and update action-based autoresponders using our API.** This method allows you to update an autoresponder. The same rules as in creating an autoresponder apply."
        return await self._core.request(
            "POST",
            "/autoresponders/{autoresponderId}",
            path_params={"autoresponderId": autoresponder_id},
            query=None,
            body=body,
            return_type=AutoresponderDetails,
        )
