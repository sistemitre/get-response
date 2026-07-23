"""Operations tagged 'Campaigns (Lists)' in the GetResponse API."""

from __future__ import annotations

from datetime import datetime
from typing import Any

from .._core import _Core
from ..models import (
    Blocklist,
    Campaign,
    CampaignListElement,
    CampaignListSizesStatisticsElement,
    GetCampaignStatisticsBalanceQueryGroupBy,
    GetCampaignStatisticsListSizeQueryGroupBy,
    GetCampaignStatisticsLocationsQueryGroupBy,
    GetCampaignStatisticsOriginsQueryGroupBy,
    GetCampaignStatisticsRemovalsQueryGroupBy,
    GetCampaignStatisticsSubscriptionsQueryGroupBy,
    NewCampaign,
    SortOrderEnum,
    UpdateBlocklist,
    UpdateCampaign,
    UpdateCampaignBlocklistAdditionalFlags,
)


class CampaignsListsResource:
    "Operations tagged 'Campaigns (Lists)' in the GetResponse API."

    def __init__(self, core: _Core) -> None:
        self._core = core

    async def create_campaign(self, body: NewCampaign) -> Campaign:
        "This endpoint allows you to create a campaign (contact list). You can create up to 1000 campaigns (contact lists)."
        return await self._core.request(
            "POST",
            "/campaigns",
            path_params=None,
            query=None,
            body=body,
            return_type=Campaign,
        )

    async def get_campaign(self, campaign_id: str, *, fields: str | None = None) -> Campaign:
        "Retrieve detailed information about a single campaign (contact list) by its unique campaignId. The response includes additional campaign settings such as postal address, subscription notification and confirmation settings, opt-in type, and profile information."
        return await self._core.request(
            "GET",
            "/campaigns/{campaignId}",
            path_params={"campaignId": campaign_id},
            query={"fields": fields},
            body=None,
            return_type=Campaign,
        )

    async def get_campaign_blocklist(
        self, campaign_id: str, *, query_mask: str | None = None
    ) -> Blocklist:
        "Returns campaign blocklist masks"
        return await self._core.request(
            "GET",
            "/campaigns/{campaignId}/blocklists",
            path_params={"campaignId": campaign_id},
            query={"query[mask]": query_mask},
            body=None,
            return_type=Blocklist,
        )

    async def get_campaign_list(
        self,
        *,
        query_name: str | None = None,
        query_is_default: bool | None = None,
        sort_name: SortOrderEnum | None = None,
        sort_created_on: SortOrderEnum | None = None,
        fields: str | None = None,
        per_page: int | None = None,
        page: int | None = None,
    ) -> list[CampaignListElement]:
        "Returns a list of campaigns (contact lists). You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by."
        return await self._core.request(
            "GET",
            "/campaigns",
            path_params=None,
            query={
                "query[name]": query_name,
                "query[isDefault]": query_is_default,
                "sort[name]": sort_name,
                "sort[createdOn]": sort_created_on,
                "fields": fields,
                "perPage": per_page,
                "page": page,
            },
            body=None,
            return_type=list[CampaignListElement],
        )

    async def get_campaign_statistics_balance(
        self,
        *,
        query_campaign_id: str,
        query_group_by: GetCampaignStatisticsBalanceQueryGroupBy | None = None,
        query_created_on_from: datetime | None = None,
        query_created_on_to: datetime | None = None,
    ) -> list[dict[str, Any]]:
        "Returns the balance of subscriptions. Dates in the YYYY-MM-DD format are used as keys in the response."
        return await self._core.request(
            "GET",
            "/campaigns/statistics/balance",
            path_params=None,
            query={
                "query[campaignId]": query_campaign_id,
                "query[groupBy]": query_group_by,
                "query[createdOn][from]": query_created_on_from,
                "query[createdOn][to]": query_created_on_to,
            },
            body=None,
            return_type=list[dict[str, Any]],
        )

    async def get_campaign_statistics_list_size(
        self,
        *,
        query_campaign_id: str,
        query_group_by: GetCampaignStatisticsListSizeQueryGroupBy | None = None,
        query_created_on_from: datetime | None = None,
        query_created_on_to: datetime | None = None,
    ) -> list[CampaignListSizesStatisticsElement]:
        "Returns the number of the total added and removed subscribers, grouped by default or by time period."
        return await self._core.request(
            "GET",
            "/campaigns/statistics/list-size",
            path_params=None,
            query={
                "query[campaignId]": query_campaign_id,
                "query[groupBy]": query_group_by,
                "query[createdOn][from]": query_created_on_from,
                "query[createdOn][to]": query_created_on_to,
            },
            body=None,
            return_type=list[CampaignListSizesStatisticsElement],
        )

    async def get_campaign_statistics_locations(
        self,
        *,
        query_campaign_id: str,
        query_group_by: GetCampaignStatisticsLocationsQueryGroupBy | None = None,
        query_created_on_from: datetime | None = None,
        query_created_on_to: datetime | None = None,
    ) -> list[dict[str, Any]]:
        "The results are indexed with the location name (PL, EN, etc.)."
        return await self._core.request(
            "GET",
            "/campaigns/statistics/locations",
            path_params=None,
            query={
                "query[campaignId]": query_campaign_id,
                "query[groupBy]": query_group_by,
                "query[createdOn][from]": query_created_on_from,
                "query[createdOn][to]": query_created_on_to,
            },
            body=None,
            return_type=list[dict[str, Any]],
        )

    async def get_campaign_statistics_origins(
        self,
        *,
        query_campaign_id: str,
        query_group_by: GetCampaignStatisticsOriginsQueryGroupBy | None = None,
        query_created_on_from: datetime | None = None,
        query_created_on_to: datetime | None = None,
    ) -> list[dict[str, Any]]:
        "The results are indexed with the campaign ID."
        return await self._core.request(
            "GET",
            "/campaigns/statistics/origins",
            path_params=None,
            query={
                "query[campaignId]": query_campaign_id,
                "query[groupBy]": query_group_by,
                "query[createdOn][from]": query_created_on_from,
                "query[createdOn][to]": query_created_on_to,
            },
            body=None,
            return_type=list[dict[str, Any]],
        )

    async def get_campaign_statistics_removals(
        self,
        *,
        query_campaign_id: str,
        query_group_by: GetCampaignStatisticsRemovalsQueryGroupBy | None = None,
        query_created_on_from: datetime | None = None,
        query_created_on_to: datetime | None = None,
    ) -> list[dict[str, Any]]:
        "Returns the number and reason for removed contacts. Dates in the YYYY-MM-DD format are used as keys in the response."
        return await self._core.request(
            "GET",
            "/campaigns/statistics/removals",
            path_params=None,
            query={
                "query[campaignId]": query_campaign_id,
                "query[groupBy]": query_group_by,
                "query[createdOn][from]": query_created_on_from,
                "query[createdOn][to]": query_created_on_to,
            },
            body=None,
            return_type=list[dict[str, Any]],
        )

    async def get_campaign_statistics_subscriptions(
        self,
        *,
        query_campaign_id: str,
        query_group_by: GetCampaignStatisticsSubscriptionsQueryGroupBy | None = None,
        query_created_on_from: datetime | None = None,
        query_created_on_to: datetime | None = None,
    ) -> list[dict[str, Any]]:
        "Returns the number and origin of subscriptions, grouped by a specified campaigns for each day on which any changes were made. Dates in the YYYY-MM-DD format are used as keys in the response."
        return await self._core.request(
            "GET",
            "/campaigns/statistics/subscriptions",
            path_params=None,
            query={
                "query[campaignId]": query_campaign_id,
                "query[groupBy]": query_group_by,
                "query[createdOn][from]": query_created_on_from,
                "query[createdOn][to]": query_created_on_to,
            },
            body=None,
            return_type=list[dict[str, Any]],
        )

    async def get_campaign_statistics_summary(
        self, *, query_campaign_id: str | None = None
    ) -> list[dict[str, Any]]:
        "The results are indexed with the campaign ID."
        return await self._core.request(
            "GET",
            "/campaigns/statistics/summary",
            path_params=None,
            query={"query[campaignId]": query_campaign_id},
            body=None,
            return_type=list[dict[str, Any]],
        )

    async def update_campaign(self, campaign_id: str, body: UpdateCampaign) -> Campaign:
        "Update a campaign"
        return await self._core.request(
            "POST",
            "/campaigns/{campaignId}",
            path_params={"campaignId": campaign_id},
            query=None,
            body=body,
            return_type=Campaign,
        )

    async def update_campaign_blocklist(
        self,
        campaign_id: str,
        body: UpdateBlocklist,
        *,
        additional_flags: UpdateCampaignBlocklistAdditionalFlags | None = None,
    ) -> Blocklist:
        "Updates campaign blocklist masks"
        return await self._core.request(
            "POST",
            "/campaigns/{campaignId}/blocklists",
            path_params={"campaignId": campaign_id},
            query={"additionalFlags": additional_flags},
            body=body,
            return_type=Blocklist,
        )
