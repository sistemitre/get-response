"""Operations tagged 'Product Variants' in the GetResponse API."""

from __future__ import annotations

from datetime import datetime

from .._core import _Core
from ..models import (
    NewProductVariant,
    ProductVariant,
    SortOrderEnum,
    UpdateProductVariant,
)


class ProductVariantsResource:
    "Operations tagged 'Product Variants' in the GetResponse API."

    def __init__(self, core: _Core) -> None:
        self._core = core

    async def create_product_variant(
        self, shop_id: str, product_id: str, body: NewProductVariant
    ) -> ProductVariant:
        "Sending a **POST** request to this URL will create a new product variant resource. In order to create a new product variant, you need to send a product variant resource in the body of the request (remember that you need to serialize the body into a JSON string) There is no need to create every element (like: image, meta field, tax) one by one by their own endpoints. All these elements can be created during this method."
        return await self._core.request(
            "POST",
            "/shops/{shopId}/products/{productId}/variants",
            path_params={"shopId": shop_id, "productId": product_id},
            query=None,
            body=body,
            return_type=ProductVariant,
        )

    async def delete_product_variant(self, shop_id: str, product_id: str, variant_id: str) -> None:
        "Delete product variant"
        return await self._core.request(
            "DELETE",
            "/shops/{shopId}/products/{productId}/variants/{variantId}",
            path_params={"shopId": shop_id, "productId": product_id, "variantId": variant_id},
            query=None,
            body=None,
            return_type=None,
        )

    async def get_product_variant_by_id(
        self, shop_id: str, product_id: str, variant_id: str, *, fields: str | None = None
    ) -> ProductVariant:
        "This method returns product variant according to the given `variantId` in the context of a given `shopId` and `productId`"
        return await self._core.request(
            "GET",
            "/shops/{shopId}/products/{productId}/variants/{variantId}",
            path_params={"shopId": shop_id, "productId": product_id, "variantId": variant_id},
            query={"fields": fields},
            body=None,
            return_type=ProductVariant,
        )

    async def get_product_variant_list(
        self,
        shop_id: str,
        product_id: str,
        *,
        query_name: str | None = None,
        query_sku: str | None = None,
        query_description: str | None = None,
        query_external_id: str | None = None,
        query_created_at_from: datetime | None = None,
        query_created_at_to: datetime | None = None,
        sort_created_on: SortOrderEnum | None = None,
        fields: str | None = None,
        per_page: int | None = None,
        page: int | None = None,
    ) -> list[ProductVariant]:
        "Sending a **GET** request to this URL returns a collection of product variant resources that belong to the given shop and product. You can narrow down the list of resources by passing proper query parameters (the list of which you can find below in the request params section). You can basically search by: * name * sku * description The `description` fields can be a pattern and we'll try to match this phrase."
        return await self._core.request(
            "GET",
            "/shops/{shopId}/products/{productId}/variants",
            path_params={"shopId": shop_id, "productId": product_id},
            query={
                "query[name]": query_name,
                "query[sku]": query_sku,
                "query[description]": query_description,
                "query[externalId]": query_external_id,
                "query[createdAt][from]": query_created_at_from,
                "query[createdAt][to]": query_created_at_to,
                "sort[createdOn]": sort_created_on,
                "fields": fields,
                "perPage": per_page,
                "page": page,
            },
            body=None,
            return_type=list[ProductVariant],
        )

    async def update_product_variant(
        self, shop_id: str, product_id: str, variant_id: str, body: UpdateProductVariant
    ) -> ProductVariant:
        "Update properties of a product variant. You should send only those fields that need to be changed. The remaining properties will stay the same. However, when updating metafields, images, and taxes, you need to send entire collections. Individual fields can't be updated. If you want to update particular metafields or tax resources, you can do so using their particular endpoints, i.e: * taxes - `POST /v3/shops/{shopId}/taxes/{taxId}` * metaFields - `POST /v3/shops/{shopId}/meta-fields/{metaFieldId}`"
        return await self._core.request(
            "POST",
            "/shops/{shopId}/products/{productId}/variants/{variantId}",
            path_params={"shopId": shop_id, "productId": product_id, "variantId": variant_id},
            query=None,
            body=body,
            return_type=ProductVariant,
        )
