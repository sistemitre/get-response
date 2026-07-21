"""Operations tagged 'SMS Messages' in the GetResponse API."""

from __future__ import annotations

from .._core import _Core
from ..models import (
    BaseSendSms,
    GetSmsListQuerySendingStatus,
    GetSmsListQueryType,
    SmsDetails,
    SmsListItem,
    SmsSenderName,
    SortOrderEnum,
)


class SmsMessagesResource:
    "Operations tagged 'SMS Messages' in the GetResponse API."

    def __init__(self, core: _Core) -> None:
        self._core = core

    async def get_sms_by_id(self, sms_id: str, *, fields: str | None = None) -> SmsDetails:
        "Get a single SMS message by its ID"
        return await self._core.request(
            "GET",
            "/sms/{smsId}",
            path_params={"smsId": sms_id},
            query={"fields": fields},
            body=None,
            return_type=SmsDetails,
        )

    async def get_sms_list(
        self,
        *,
        query_type: GetSmsListQueryType | None = None,
        query_name: str | None = None,
        query_sending_status: GetSmsListQuerySendingStatus | None = None,
        query_campaign_id: str | None = None,
        query_has_links: bool | None = None,
        sort_sending_status: SortOrderEnum | None = None,
        sort_name: SortOrderEnum | None = None,
        sort_send_on: SortOrderEnum | None = None,
        sort_modified_on: SortOrderEnum | None = None,
        sort_delivered: SortOrderEnum | None = None,
        sort_sent: SortOrderEnum | None = None,
        sort_clicks: SortOrderEnum | None = None,
        fields: str | None = None,
        per_page: int | None = None,
        page: int | None = None,
    ) -> SmsListItem:
        "You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by."
        return await self._core.request(
            "GET",
            "/sms",
            path_params=None,
            query={
                "query[type]": query_type,
                "query[name]": query_name,
                "query[sendingStatus]": query_sending_status,
                "query[campaignId]": query_campaign_id,
                "query[hasLinks]": query_has_links,
                "sort[sendingStatus]": sort_sending_status,
                "sort[name]": sort_name,
                "sort[sendOn]": sort_send_on,
                "sort[modifiedOn]": sort_modified_on,
                "sort[delivered]": sort_delivered,
                "sort[sent]": sort_sent,
                "sort[clicks]": sort_clicks,
                "fields": fields,
                "perPage": per_page,
                "page": page,
            },
            body=None,
            return_type=SmsListItem,
        )

    async def get_sms_sender_name_list(
        self, *, query_status: str | None = None, fields: str | None = None
    ) -> list[SmsSenderName]:
        "You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by."
        return await self._core.request(
            "GET",
            "/sms/sender-names",
            path_params=None,
            query={"query[status]": query_status, "fields": fields},
            body=None,
            return_type=list[SmsSenderName],
        )

    async def send_sms(self, body: BaseSendSms) -> SmsDetails:
        "Sends a new SMS (text) message to a list of recipients"
        return await self._core.request(
            "POST",
            "/sms",
            path_params=None,
            query=None,
            body=body,
            return_type=SmsDetails,
        )
