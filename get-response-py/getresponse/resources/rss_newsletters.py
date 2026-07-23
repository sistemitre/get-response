"""Operations tagged 'RSS Newsletters' in the GetResponse API."""

from __future__ import annotations

from datetime import datetime

from .._core import _Core
from ..models import (
    GetRssNewslettersListQueryStatus,
    GetRssNewsletterStatisticsCollectionQueryGroupBy,
    GetSingleRssNewsletterStatisticsCollectionQueryGroupBy,
    MessageStatisticsListElement,
    NewRssNewsletter,
    RssNewsletterDetails,
    RssNewsletterListItem,
    SortOrderEnum,
    UpdateRssNewsletter,
)


class RssNewslettersResource:
    "Operations tagged 'RSS Newsletters' in the GetResponse API."

    def __init__(self, core: _Core) -> None:
        self._core = core

    async def create_rss_newsletter(self, body: NewRssNewsletter) -> RssNewsletterDetails:
        "Create RSS newsletter"
        return await self._core.request(
            "POST",
            "/rss-newsletters",
            path_params=None,
            query=None,
            body=body,
            return_type=RssNewsletterDetails,
        )

    async def delete_rss_newsletter(self, rss_newsletter_id: str) -> None:
        "Delete RSS newsletter"
        return await self._core.request(
            "DELETE",
            "/rss-newsletters/{rssNewsletterId}",
            path_params={"rssNewsletterId": rss_newsletter_id},
            query=None,
            body=None,
            return_type=None,
        )

    async def get_rss_newsletter_by_id(
        self, rss_newsletter_id: str, *, fields: str | None = None
    ) -> RssNewsletterDetails:
        "Get RSS newsletter by ID"
        return await self._core.request(
            "GET",
            "/rss-newsletters/{rssNewsletterId}",
            path_params={"rssNewsletterId": rss_newsletter_id},
            query={"fields": fields},
            body=None,
            return_type=RssNewsletterDetails,
        )

    async def get_rss_newsletter_statistics_collection(
        self,
        *,
        query_group_by: GetRssNewsletterStatisticsCollectionQueryGroupBy | None = None,
        query_rss_newsletter_id: str | None = None,
        query_campaign_id: str | None = None,
        query_created_on_from: datetime | None = None,
        query_created_on_to: datetime | None = None,
        fields: str | None = None,
        per_page: int | None = None,
        page: int | None = None,
    ) -> list[MessageStatisticsListElement]:
        "You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by."
        return await self._core.request(
            "GET",
            "/rss-newsletters/statistics",
            path_params=None,
            query={
                "query[groupBy]": query_group_by,
                "query[rssNewsletterId]": query_rss_newsletter_id,
                "query[campaignId]": query_campaign_id,
                "query[createdOn][from]": query_created_on_from,
                "query[createdOn][to]": query_created_on_to,
                "fields": fields,
                "perPage": per_page,
                "page": page,
            },
            body=None,
            return_type=list[MessageStatisticsListElement],
        )

    async def get_rss_newsletters_list(
        self,
        *,
        query_subject: str | None = None,
        query_status: GetRssNewslettersListQueryStatus | None = None,
        query_created_on_from: datetime | None = None,
        query_created_on_to: datetime | None = None,
        query_campaign_id: str | None = None,
        sort_created_on: SortOrderEnum | None = None,
        fields: str | None = None,
        per_page: int | None = None,
        page: int | None = None,
    ) -> list[RssNewsletterListItem]:
        "You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by."
        return await self._core.request(
            "GET",
            "/rss-newsletters",
            path_params=None,
            query={
                "query[subject]": query_subject,
                "query[status]": query_status,
                "query[createdOn][from]": query_created_on_from,
                "query[createdOn][to]": query_created_on_to,
                "query[campaignId]": query_campaign_id,
                "sort[createdOn]": sort_created_on,
                "fields": fields,
                "perPage": per_page,
                "page": page,
            },
            body=None,
            return_type=list[RssNewsletterListItem],
        )

    async def get_single_rss_newsletter_statistics_collection(
        self,
        rss_newsletter_id: str,
        *,
        query_group_by: GetSingleRssNewsletterStatisticsCollectionQueryGroupBy | None = None,
        query_created_on_from: datetime | None = None,
        query_created_on_to: datetime | None = None,
        fields: str | None = None,
        per_page: int | None = None,
        page: int | None = None,
    ) -> list[MessageStatisticsListElement]:
        "You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by."
        return await self._core.request(
            "GET",
            "/rss-newsletters/{rssNewsletterId}/statistics",
            path_params={"rssNewsletterId": rss_newsletter_id},
            query={
                "query[groupBy]": query_group_by,
                "query[createdOn][from]": query_created_on_from,
                "query[createdOn][to]": query_created_on_to,
                "fields": fields,
                "perPage": per_page,
                "page": page,
            },
            body=None,
            return_type=list[MessageStatisticsListElement],
        )

    async def update_rss_newsletter(
        self, rss_newsletter_id: str, body: UpdateRssNewsletter
    ) -> RssNewsletterDetails:
        "Update RSS newsletter"
        return await self._core.request(
            "POST",
            "/rss-newsletters/{rssNewsletterId}",
            path_params={"rssNewsletterId": rss_newsletter_id},
            query=None,
            body=body,
            return_type=RssNewsletterDetails,
        )
