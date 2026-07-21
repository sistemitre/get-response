"""Operations tagged 'Products' in the GetResponse API."""

from __future__ import annotations

from typing import Any

from .._core import _Core
from ..models import (
    BaseCategory,
    MetaField,
    NewProduct,
    Product,
    SortOrderEnum,
    UpdateProduct,
    UpsertMetaField,
    UpsertProductCategory,
)


class ProductsResource:
    "Operations tagged 'Products' in the GetResponse API."

    def __init__(self, core: _Core) -> None:
        self._core = core

    async def create_product(self, shop_id: str, body: NewProduct) -> Product:
        "Sending a **POST** request to this URL will create a new product resource. In order to create a new product, you need to send the product resource in the body of the request (remember that you need to serialize the body into a JSON string) You don't need a separate endpoint for each element (e.g. variant, category, meta-field). You can create them all with this method. Please note that categories aren't required, but if a product has at least one category, then one of those categories must be marked as default. This can be set by field `isDefault`. If none of the elements contains isDefault=true, then the system picks the first one from the collection by default."
        return await self._core.request(
            "POST",
            "/shops/{shopId}/products",
            path_params={"shopId": shop_id},
            query=None,
            body=body,
            return_type=Product,
        )

    async def delete_product(self, shop_id: str, product_id: str) -> None:
        "Delete product"
        return await self._core.request(
            "DELETE",
            "/shops/{shopId}/products/{productId}",
            path_params={"shopId": shop_id, "productId": product_id},
            query=None,
            body=None,
            return_type=None,
        )

    async def get_product_by_id(
        self, shop_id: str, product_id: str, *, fields: str | None = None
    ) -> Product:
        "This method returns product according to the given `productId` in the context of a given `shopId`."
        return await self._core.request(
            "GET",
            "/shops/{shopId}/products/{productId}",
            path_params={"shopId": shop_id, "productId": product_id},
            query={"fields": fields},
            body=None,
            return_type=Product,
        )

    async def get_product_list(
        self,
        shop_id: str,
        *,
        query_name: str | None = None,
        query_vendor: str | None = None,
        query_category: str | None = None,
        query_category_id: str | None = None,
        query_external_id: str | None = None,
        query_variant_name: str | None = None,
        query_meta_field_names: str | None = None,
        query_meta_field_values: str | None = None,
        query_created_on_from: dict[str, Any] | None = None,
        query_created_on_to: dict[str, Any] | None = None,
        sort_name: SortOrderEnum | None = None,
        sort_created_on: SortOrderEnum | None = None,
        fields: str | None = None,
        per_page: int | None = None,
        page: int | None = None,
    ) -> list[Product]:
        "Sending a **GET** request to this URL returns a collection of product resources that belong to the given shop. You can narrow down the list of resources by passing proper query parameters (the list of which you can find below in the request params section). You can basically search by: * name * vendor * category * categoryId * externalId * variantName * metaFieldNames * metaFieldValues * createdOn The `metaFieldNames` and `metaFieldValues` fields can be a list of values separated by a comma [,]. You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by."
        return await self._core.request(
            "GET",
            "/shops/{shopId}/products",
            path_params={"shopId": shop_id},
            query={
                "query[name]": query_name,
                "query[vendor]": query_vendor,
                "query[category]": query_category,
                "query[categoryId]": query_category_id,
                "query[externalId]": query_external_id,
                "query[variantName]": query_variant_name,
                "query[metaFieldNames]": query_meta_field_names,
                "query[metaFieldValues]": query_meta_field_values,
                "query[createdOn][from]": query_created_on_from,
                "query[createdOn][to]": query_created_on_to,
                "sort[name]": sort_name,
                "sort[createdOn]": sort_created_on,
                "fields": fields,
                "perPage": per_page,
                "page": page,
            },
            body=None,
            return_type=list[Product],
        )

    async def update_product(self, shop_id: str, product_id: str, body: UpdateProduct) -> Product:
        "Update the properties of a shop's product. You should only send those fields that need to be changed. The remaining properties will stay the same. However, when updating variants, categories, and meta fields, you need to send entire collections. Individual fields can't be updated. If you want to update particular fields, you can do so using their specific endpoints, i.e.: * categories - `POST /v3/shops/{shopId}/categories/{categoryId}` * variants - POST `/v3/shops/{shopId}/products/{productId}/variants/{variantId}` * metaFields - `POST /v3/shops/{shopId}/meta-fields/{metaFieldId}`"
        return await self._core.request(
            "POST",
            "/shops/{shopId}/products/{productId}",
            path_params={"shopId": shop_id, "productId": product_id},
            query=None,
            body=body,
            return_type=Product,
        )

    async def upsert_meta_fields(
        self, shop_id: str, product_id: str, body: UpsertMetaField
    ) -> list[MetaField]:
        "This method makes it possible to assign meta fields. It doesn't remove or unassign meta fields. It returns a list of product meta fields."
        return await self._core.request(
            "POST",
            "/shops/{shopId}/products/{productId}/meta-fields",
            path_params={"shopId": shop_id, "productId": product_id},
            query=None,
            body=body,
            return_type=list[MetaField],
        )

    async def upsert_product_categories(
        self, shop_id: str, product_id: str, body: UpsertProductCategory
    ) -> list[BaseCategory]:
        "This method makes it possible to assign product categories, and to set a default product category. This method doesn't remove or unassign product categories. It returns a list of product categories. Please note that if you assign only one category to a given product, that category is marked as default. If you try to remove the default mark, your change won't be executed."
        return await self._core.request(
            "POST",
            "/shops/{shopId}/products/{productId}/categories",
            path_params={"shopId": shop_id, "productId": product_id},
            query=None,
            body=body,
            return_type=list[BaseCategory],
        )
