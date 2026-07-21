"""Operations tagged 'Categories' in the GetResponse API."""

from __future__ import annotations

from datetime import datetime

from .._core import _Core
from ..models import (
    Category,
    NewCategory,
    SortOrderEnum,
)


class CategoriesResource:
    "Operations tagged 'Categories' in the GetResponse API."

    def __init__(self, core: _Core) -> None:
        self._core = core

    async def create_category(self, shop_id: str, body: NewCategory) -> Category:
        "Create shop category. You can pass the `parentId` parameter to create a sub-category of a given parent. Unlike most **POST** methods, this call is idempotent, that is: sending the same request 10 times will not create 10 new categories. Only one category will be created."
        return await self._core.request(
            "POST",
            "/shops/{shopId}/categories",
            path_params={"shopId": shop_id},
            query=None,
            body=body,
            return_type=Category,
        )

    async def delete_category(self, shop_id: str, category_id: str) -> None:
        "Delete category"
        return await self._core.request(
            "DELETE",
            "/shops/{shopId}/categories/{categoryId}",
            path_params={"shopId": shop_id, "categoryId": category_id},
            query=None,
            body=None,
            return_type=None,
        )

    async def get_categories(
        self,
        shop_id: str,
        *,
        query_name: str | None = None,
        query_parent_id: str | None = None,
        query_external_id: str | None = None,
        search_created_at_from: datetime | None = None,
        search_created_at_to: datetime | None = None,
        sort_name: SortOrderEnum | None = None,
        sort_created_at: SortOrderEnum | None = None,
        fields: str | None = None,
        per_page: int | None = None,
        page: int | None = None,
    ) -> list[Category]:
        "Sending a **GET** request to this URL returns a collection of category resources that belong to the given shop. You can narrow down the list of resources by passing proper query parameters (the list of which you can find below in the request params section). You can basically search by: *name * createdOn * parentId The `name` fields can be a pattern and we'll try to match this phrase. The `parentId` will search for sub-categories of a given parent category. You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by."
        return await self._core.request(
            "GET",
            "/shops/{shopId}/categories",
            path_params={"shopId": shop_id},
            query={
                "query[name]": query_name,
                "query[parentId]": query_parent_id,
                "query[externalId]": query_external_id,
                "search[createdAt][from]": search_created_at_from,
                "search[createdAt][to]": search_created_at_to,
                "sort[name]": sort_name,
                "sort[createdAt]": sort_created_at,
                "fields": fields,
                "perPage": per_page,
                "page": page,
            },
            body=None,
            return_type=list[Category],
        )

    async def get_category(
        self, shop_id: str, category_id: str, *, fields: str | None = None
    ) -> Category:
        "This method returns a category according to the given `categoryId`."
        return await self._core.request(
            "GET",
            "/shops/{shopId}/categories/{categoryId}",
            path_params={"shopId": shop_id, "categoryId": category_id},
            query={"fields": fields},
            body=None,
            return_type=Category,
        )

    async def update_category(self, shop_id: str, category_id: str, body: Category) -> Category:
        "Update the properties of the shop category. You can specify a `parentId` to assign a category as sub-category for an existing category. You should send only those fields that need to be changed. The rest of the properties will stay the same."
        return await self._core.request(
            "POST",
            "/shops/{shopId}/categories/{categoryId}",
            path_params={"shopId": shop_id, "categoryId": category_id},
            query=None,
            body=body,
            return_type=Category,
        )
