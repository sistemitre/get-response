"""Operations tagged 'Form and Popup' in the GetResponse API."""

from __future__ import annotations

from datetime import datetime

from .._core import _Core
from ..models import (
    GetPopupGeneralPerformanceQueryDevice,
    PopupGeneralPerformanceStats,
)


class FormAndPopupResource:
    "Operations tagged 'Form and Popup' in the GetResponse API."

    def __init__(self, core: _Core) -> None:
        self._core = core

    async def get_popup_general_performance(
        self,
        popup_id: str,
        *,
        query_date_from: datetime | None = None,
        query_date_to: datetime | None = None,
        query_location: str | None = None,
        query_device: GetPopupGeneralPerformanceQueryDevice | None = None,
        fields: str | None = None,
    ) -> PopupGeneralPerformanceStats:
        "Get statistics for a single form or popup"
        return await self._core.request(
            "GET",
            "/statistics/popups/{popupId}/performance",
            path_params={"popupId": popup_id},
            query={
                "query[date][from]": query_date_from,
                "query[date][to]": query_date_to,
                "query[location]": query_location,
                "query[device]": query_device,
                "fields": fields,
            },
            body=None,
            return_type=PopupGeneralPerformanceStats,
        )
