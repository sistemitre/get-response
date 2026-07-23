"""Operations tagged 'Suppressions' in the GetResponse API."""

from __future__ import annotations

from datetime import datetime

from .._core import _Core
from ..models import (
    NewSuppression,
    SortOrderEnum,
    Suppression,
    SuppressionDetails,
    UpdateSuppression,
)


class SuppressionsResource:
    "Operations tagged 'Suppressions' in the GetResponse API."

    def __init__(self, core: _Core) -> None:
        self._core = core

    async def create_suppression(self, body: NewSuppression) -> SuppressionDetails:
        "Creates a new suppression list"
        return await self._core.request(
            "POST",
            "/suppressions",
            path_params=None,
            query=None,
            body=body,
            return_type=SuppressionDetails,
        )

    async def delete_suppression(self, suppression_id: str) -> None:
        "Deletes a given suppression list by ID"
        return await self._core.request(
            "DELETE",
            "/suppressions/{suppressionId}",
            path_params={"suppressionId": suppression_id},
            query=None,
            body=None,
            return_type=None,
        )

    async def get_suppression_by_id(self, suppression_id: str) -> SuppressionDetails:
        "Get a suppression list by ID"
        return await self._core.request(
            "GET",
            "/suppressions/{suppressionId}",
            path_params={"suppressionId": suppression_id},
            query=None,
            body=None,
            return_type=SuppressionDetails,
        )

    async def get_suppressions_list(
        self,
        *,
        query_name: str | None = None,
        query_created_on_from: datetime | None = None,
        query_created_on_to: datetime | None = None,
        sort_name: SortOrderEnum | None = None,
        sort_created_on: SortOrderEnum | None = None,
        fields: str | None = None,
        per_page: int | None = None,
        page: int | None = None,
    ) -> list[Suppression]:
        "Get suppression lists"
        return await self._core.request(
            "GET",
            "/suppressions",
            path_params=None,
            query={
                "query[name]": query_name,
                "query[createdOn][from]": query_created_on_from,
                "query[createdOn][to]": query_created_on_to,
                "sort[name]": sort_name,
                "sort[createdOn]": sort_created_on,
                "fields": fields,
                "perPage": per_page,
                "page": page,
            },
            body=None,
            return_type=list[Suppression],
        )

    async def update_suppression(
        self, suppression_id: str, body: UpdateSuppression
    ) -> SuppressionDetails:
        "Update a suppression list by ID"
        return await self._core.request(
            "POST",
            "/suppressions/{suppressionId}",
            path_params={"suppressionId": suppression_id},
            query=None,
            body=body,
            return_type=SuppressionDetails,
        )
