"""Operations tagged 'Tags' in the GetResponse API."""

from __future__ import annotations

from typing import Any

from .._core import _Core
from ..models import (
    NewTag,
    SortOrderEnum,
    Tag,
    TagDetails,
    UpdateTag,
)


class TagsResource:
    "Operations tagged 'Tags' in the GetResponse API."

    def __init__(self, core: _Core) -> None:
        self._core = core

    async def create_tag(self, body: NewTag) -> TagDetails:
        "Add a new tag"
        return await self._core.request(
            "POST",
            "/tags",
            path_params=None,
            query=None,
            body=body,
            return_type=TagDetails,
        )

    async def delete_tag(self, tag_id: str) -> None:
        "Delete tag by ID"
        return await self._core.request(
            "DELETE",
            "/tags/{tagId}",
            path_params={"tagId": tag_id},
            query=None,
            body=None,
            return_type=None,
        )

    async def get_tag_by_id(self, tag_id: str, *, fields: str | None = None) -> TagDetails:
        "Retrieve a specific tag by its ID"
        return await self._core.request(
            "GET",
            "/tags/{tagId}",
            path_params={"tagId": tag_id},
            query={"fields": fields},
            body=None,
            return_type=TagDetails,
        )

    async def get_tags_list(
        self,
        *,
        query_name: str | None = None,
        query_created_at_from: dict[str, Any] | None = None,
        query_created_at_to: dict[str, Any] | None = None,
        sort_created_at: SortOrderEnum | None = None,
        sort_name: SortOrderEnum | None = None,
        fields: str | None = None,
        per_page: int | None = None,
        page: int | None = None,
    ) -> list[Tag]:
        "Provides a list of tags. You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by."
        return await self._core.request(
            "GET",
            "/tags",
            path_params=None,
            query={
                "query[name]": query_name,
                "query[createdAt][from]": query_created_at_from,
                "query[createdAt][to]": query_created_at_to,
                "sort[createdAt]": sort_created_at,
                "sort[name]": sort_name,
                "fields": fields,
                "perPage": per_page,
                "page": page,
            },
            body=None,
            return_type=list[Tag],
        )

    async def update_tag(self, tag_id: str, body: UpdateTag) -> TagDetails:
        "Updating the tag is not allowed. The method currently performs no update actions and only returns the current tag details."
        return await self._core.request(
            "POST",
            "/tags/{tagId}",
            path_params={"tagId": tag_id},
            query=None,
            body=body,
            return_type=TagDetails,
        )
