"""Operations tagged 'Legacy Landing Pages' in the GetResponse API."""

from __future__ import annotations

from datetime import datetime

from .._core import _Core
from ..models import (
    BaseLandingPage,
    LandingPage,
    SortOrderEnum,
    StatusEnum,
)


class LegacyLandingPagesResource:
    "Operations tagged 'Legacy Landing Pages' in the GetResponse API."

    def __init__(self, core: _Core) -> None:
        self._core = core

    async def get_landing_page_by_id(
        self, landing_page_id: str, *, fields: str | None = None
    ) -> list[LandingPage]:
        "Get single landing page by ID"
        return await self._core.request(
            "GET",
            "/landing-pages/{landingPageId}",
            path_params={"landingPageId": landing_page_id},
            query={"fields": fields},
            body=None,
            return_type=list[LandingPage],
        )

    async def get_landing_page_list(
        self,
        *,
        query_domain: str | None = None,
        query_status: StatusEnum | None = None,
        query_subdomain: str | None = None,
        query_meta_title: str | None = None,
        query_user_domain: str | None = None,
        query_campaign_id: str | None = None,
        query_created_on_from: datetime | None = None,
        query_created_on_to: datetime | None = None,
        sort_created_on: SortOrderEnum | None = None,
        sort_domain: SortOrderEnum | None = None,
        sort_campaign_id: SortOrderEnum | None = None,
        sort_meta_title: SortOrderEnum | None = None,
        fields: str | None = None,
        per_page: int | None = None,
        page: int | None = None,
    ) -> list[BaseLandingPage]:
        "You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by."
        return await self._core.request(
            "GET",
            "/landing-pages",
            path_params=None,
            query={
                "query[domain]": query_domain,
                "query[status]": query_status,
                "query[subdomain]": query_subdomain,
                "query[metaTitle]": query_meta_title,
                "query[userDomain]": query_user_domain,
                "query[campaignId]": query_campaign_id,
                "query[createdOn][from]": query_created_on_from,
                "query[createdOn][to]": query_created_on_to,
                "sort[createdOn]": sort_created_on,
                "sort[domain]": sort_domain,
                "sort[campaignId]": sort_campaign_id,
                "sort[metaTitle]": sort_meta_title,
                "fields": fields,
                "perPage": per_page,
                "page": page,
            },
            body=None,
            return_type=list[BaseLandingPage],
        )
