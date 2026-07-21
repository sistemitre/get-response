"""Operations tagged 'SMS Automation Messages' in the GetResponse API."""

from __future__ import annotations

from .._core import _Core
from ..models import (
    SmsAutomationDetails,
    SmsAutomationListItem,
    SortOrderEnum,
)


class SmsAutomationMessagesResource:
    "Operations tagged 'SMS Automation Messages' in the GetResponse API."

    def __init__(self, core: _Core) -> None:
        self._core = core

    async def get_sms_automation_by_id(
        self, sms_id: str, *, fields: str | None = None
    ) -> SmsAutomationDetails:
        "Get a single automated SMS message by its ID."
        return await self._core.request(
            "GET",
            "/sms-automation/{smsId}",
            path_params={"smsId": sms_id},
            query={"fields": fields},
            body=None,
            return_type=SmsAutomationDetails,
        )

    async def get_sms_automation_list(
        self,
        *,
        query_name: str | None = None,
        query_campaign_id: str | None = None,
        query_has_links: bool | None = None,
        sort_status: SortOrderEnum | None = None,
        sort_name: SortOrderEnum | None = None,
        sort_modified_on: SortOrderEnum | None = None,
        sort_delivered: SortOrderEnum | None = None,
        sort_sent: SortOrderEnum | None = None,
        sort_clicks: SortOrderEnum | None = None,
        fields: str | None = None,
        per_page: int | None = None,
        page: int | None = None,
    ) -> SmsAutomationListItem:
        "You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by."
        return await self._core.request(
            "GET",
            "/sms-automation",
            path_params=None,
            query={
                "query[name]": query_name,
                "query[campaignId]": query_campaign_id,
                "query[hasLinks]": query_has_links,
                "sort[status]": sort_status,
                "sort[name]": sort_name,
                "sort[modifiedOn]": sort_modified_on,
                "sort[delivered]": sort_delivered,
                "sort[sent]": sort_sent,
                "sort[clicks]": sort_clicks,
                "fields": fields,
                "perPage": per_page,
                "page": page,
            },
            body=None,
            return_type=SmsAutomationListItem,
        )
