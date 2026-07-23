"""Operations tagged 'Forms' in the GetResponse API."""

from __future__ import annotations

from datetime import datetime

from .._core import _Core
from ..models import (
    Form,
    FormDetails,
    FormVariantDetails,
    GetFormListQueryStatus,
    SortOrderEnum,
)


class FormsResource:
    "Operations tagged 'Forms' in the GetResponse API."

    def __init__(self, core: _Core) -> None:
        self._core = core

    async def get_form(self, form_id: str, *, fields: str | None = None) -> FormDetails:
        "Get form by ID"
        return await self._core.request(
            "GET",
            "/forms/{formId}",
            path_params={"formId": form_id},
            query={"fields": fields},
            body=None,
            return_type=FormDetails,
        )

    async def get_form_list(
        self,
        *,
        query_name: str | None = None,
        query_created_on_from: datetime | None = None,
        query_created_on_to: datetime | None = None,
        query_campaign_id: str | None = None,
        query_status: GetFormListQueryStatus | None = None,
        sort_created_on: SortOrderEnum | None = None,
        sort_name: SortOrderEnum | None = None,
        sort_visitors: SortOrderEnum | None = None,
        sort_unique_visitors: SortOrderEnum | None = None,
        sort_subscribed: SortOrderEnum | None = None,
        sort_subscription_rate: SortOrderEnum | None = None,
        fields: str | None = None,
        per_page: int | None = None,
        page: int | None = None,
    ) -> list[Form]:
        "You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by."
        return await self._core.request(
            "GET",
            "/forms",
            path_params=None,
            query={
                "query[name]": query_name,
                "query[createdOn][from]": query_created_on_from,
                "query[createdOn][to]": query_created_on_to,
                "query[campaignId]": query_campaign_id,
                "query[status]": query_status,
                "sort[createdOn]": sort_created_on,
                "sort[name]": sort_name,
                "sort[visitors]": sort_visitors,
                "sort[uniqueVisitors]": sort_unique_visitors,
                "sort[subscribed]": sort_subscribed,
                "sort[subscriptionRate]": sort_subscription_rate,
                "fields": fields,
                "perPage": per_page,
                "page": page,
            },
            body=None,
            return_type=list[Form],
        )

    async def get_form_variant_list(
        self, form_id: str, *, fields: str | None = None
    ) -> list[FormVariantDetails]:
        "Get the list of form variants (A/B tests)"
        return await self._core.request(
            "GET",
            "/forms/{formId}/variants",
            path_params={"formId": form_id},
            query={"fields": fields},
            body=None,
            return_type=list[FormVariantDetails],
        )
