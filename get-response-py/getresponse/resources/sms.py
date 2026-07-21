"""Operations tagged 'Sms' in the GetResponse API."""

from __future__ import annotations

from datetime import datetime

from .._core import _Core
from ..models import SmsStats


class SmsResource:
    "Operations tagged 'Sms' in the GetResponse API."

    def __init__(self, core: _Core) -> None:
        self._core = core

    async def get_sms_stats(
        self,
        sms_id: str,
        *,
        query_created_on_from: datetime | None = None,
        query_created_on_to: datetime | None = None,
        fields: str | None = None,
    ) -> SmsStats:
        "Get details for the SMS message statistics"
        return await self._core.request(
            "GET",
            "/statistics/sms/{smsId}",
            path_params={"smsId": sms_id},
            query={
                "query[createdOn][from]": query_created_on_from,
                "query[createdOn][to]": query_created_on_to,
                "fields": fields,
            },
            body=None,
            return_type=SmsStats,
        )
