"""Operations tagged 'A/B tests' in the GetResponse API."""

from __future__ import annotations

from datetime import datetime

from .._core import _Core
from ..models import (
    GetSplittestListQueryStatus,
    SortOrderEnum,
    Splittest,
)


class AbTestsResource:
    "Operations tagged 'A/B tests' in the GetResponse API."

    def __init__(self, core: _Core) -> None:
        self._core = core

    async def get_splittest(self, splittest_id: str, *, fields: str | None = None) -> Splittest:
        "Get a single A/B test by ID."
        return await self._core.request(
            "GET",
            "/splittests/{splittestId}",
            path_params={"splittestId": splittest_id},
            query={"fields": fields},
            body=None,
            return_type=Splittest,
        )

    async def get_splittest_list(
        self,
        *,
        query_name: str | None = None,
        query_type: str | None = None,
        query_status: GetSplittestListQueryStatus | None = None,
        query_created_on_from: datetime | None = None,
        query_created_on_to: datetime | None = None,
        sort_name: SortOrderEnum | None = None,
        sort_created_on: SortOrderEnum | None = None,
        fields: str | None = None,
        per_page: int | None = None,
        page: int | None = None,
    ) -> list[Splittest]:
        "The list of A/B tests. You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by."
        return await self._core.request(
            "GET",
            "/splittests",
            path_params=None,
            query={
                "query[name]": query_name,
                "query[type]": query_type,
                "query[status]": query_status,
                "query[createdOn][from]": query_created_on_from,
                "query[createdOn][to]": query_created_on_to,
                "sort[name]": sort_name,
                "sort[createdOn]": sort_created_on,
                "fields": fields,
                "perPage": per_page,
                "page": page,
            },
            body=None,
            return_type=list[Splittest],
        )
