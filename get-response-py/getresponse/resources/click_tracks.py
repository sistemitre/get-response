"""Operations tagged 'Click Tracks' in the GetResponse API."""

from __future__ import annotations

from typing import Any

from .._core import _Core
from ..models import (
    ClickTrackResource,
    SortOrderEnum,
)


class ClickTracksResource:
    "Operations tagged 'Click Tracks' in the GetResponse API."

    def __init__(self, core: _Core) -> None:
        self._core = core

    async def get_click_track_by_id(
        self, click_track_id: str, *, fields: str | None = None
    ) -> ClickTrackResource:
        "Get click tracked link details by click track ID"
        return await self._core.request(
            "GET",
            "/click-tracks/{clickTrackId}",
            path_params={"clickTrackId": click_track_id},
            query={"fields": fields},
            body=None,
            return_type=ClickTrackResource,
        )

    async def get_click_track_list(
        self,
        *,
        query_created_on_from: dict[str, Any] | None = None,
        query_created_on_to: dict[str, Any] | None = None,
        sort_created_on: SortOrderEnum | None = None,
        fields: str | None = None,
        per_page: int | None = None,
        page: int | None = None,
    ) -> list[ClickTrackResource]:
        "You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by."
        return await self._core.request(
            "GET",
            "/click-tracks",
            path_params=None,
            query={
                "query[createdOn][from]": query_created_on_from,
                "query[createdOn][to]": query_created_on_to,
                "sort[createdOn]": sort_created_on,
                "fields": fields,
                "perPage": per_page,
                "page": page,
            },
            body=None,
            return_type=list[ClickTrackResource],
        )
