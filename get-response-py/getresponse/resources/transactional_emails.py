"""Operations tagged 'Transactional Emails' in the GetResponse API."""

from __future__ import annotations

from typing import Any

from .._core import _Core
from ..models import (
    CreateTransactionalEmail,
    GetTransactionalEmailsStatisticsQueryGroupBy,
    StringBooleanEnum,
    TransactionalEmail,
    TransactionalEmailDetails,
    TransactionalEmailListElement,
    TransactionalEmailStatistics,
)


class TransactionalEmailsResource:
    "Operations tagged 'Transactional Emails' in the GetResponse API."

    def __init__(self, core: _Core) -> None:
        self._core = core

    async def create_transactional_email(
        self, body: CreateTransactionalEmail
    ) -> TransactionalEmail:
        "Send transactional email"
        return await self._core.request(
            "POST",
            "/transactional-emails",
            path_params=None,
            query=None,
            body=body,
            return_type=TransactionalEmail,
        )

    async def get_transactional_emails_by_id(
        self, transactional_email_id: str, *, fields: str | None = None
    ) -> TransactionalEmailDetails:
        "Get transactional email details by transactional email ID"
        return await self._core.request(
            "GET",
            "/transactional-emails/{transactionalEmailId}",
            path_params={"transactionalEmailId": transactional_email_id},
            query={"fields": fields},
            body=None,
            return_type=TransactionalEmailDetails,
        )

    async def get_transactional_emails_list(
        self,
        *,
        query_sent_on_from: dict[str, Any] | None = None,
        query_sent_on_to: dict[str, Any] | None = None,
        query_tagged: StringBooleanEnum | None = None,
        query_tag_id: str | None = None,
        fields: str | None = None,
        per_page: int | None = None,
        page: int | None = None,
    ) -> list[TransactionalEmailListElement]:
        "You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by."
        return await self._core.request(
            "GET",
            "/transactional-emails",
            path_params=None,
            query={
                "query[sentOn][from]": query_sent_on_from,
                "query[sentOn][to]": query_sent_on_to,
                "query[tagged]": query_tagged,
                "query[tagId]": query_tag_id,
                "fields": fields,
                "perPage": per_page,
                "page": page,
            },
            body=None,
            return_type=list[TransactionalEmailListElement],
        )

    async def get_transactional_emails_statistics(
        self,
        *,
        query_group_by: GetTransactionalEmailsStatisticsQueryGroupBy,
        query_time_frame_from: dict[str, Any] | None = None,
        query_time_frame_to: dict[str, Any] | None = None,
        query_tagged: StringBooleanEnum | None = None,
        query_tag_id: str | None = None,
        fields: str | None = None,
    ) -> list[TransactionalEmailStatistics]:
        "Get the overall statistics of transactional emails"
        return await self._core.request(
            "GET",
            "/transactional-emails/statistics",
            path_params=None,
            query={
                "query[groupBy]": query_group_by,
                "query[timeFrame][from]": query_time_frame_from,
                "query[timeFrame][to]": query_time_frame_to,
                "query[tagged]": query_tagged,
                "query[tagId]": query_tag_id,
                "fields": fields,
            },
            body=None,
            return_type=list[TransactionalEmailStatistics],
        )
