"""Operations tagged 'Newsletters' in the GetResponse API."""

from __future__ import annotations

from datetime import datetime

from .._core import _Core
from ..models import (
    GetNewsletterActivitiesQueryActivity,
    GetNewsletterListQueryStatus,
    GetNewsletterListQueryType,
    GetNewsletterStatisticsCollectionQueryGroupBy,
    GetNewsletterThumbnailSize,
    GetSingleNewsletterStatisticsQueryGroupBy,
    MessageStatisticsListElement,
    NewNewsletter,
    NewsletterActivity,
    NewsletterDetails,
    NewsletterListElement,
    SendNewsletterDraft,
    SortOrderEnum,
)


class NewslettersResource:
    "Operations tagged 'Newsletters' in the GetResponse API."

    def __init__(self, core: _Core) -> None:
        self._core = core

    async def cancel_message_send(self, newsletter_id: str) -> NewsletterDetails:
        "> Using this method, you can cancel the sending of the newsletter. It will also turn the newsletter into a **draft**."
        return await self._core.request(
            "POST",
            "/newsletters/{newsletterId}/cancel",
            path_params={"newsletterId": newsletter_id},
            query=None,
            body=None,
            return_type=NewsletterDetails,
        )

    async def create_newsletter(self, body: NewNewsletter) -> NewsletterDetails:
        "> This method creates a new newsletter and puts it in a queue to send. **NOTE: This method has a limit of 256 calls per day.**"
        return await self._core.request(
            "POST",
            "/newsletters",
            path_params=None,
            query=None,
            body=body,
            return_type=NewsletterDetails,
        )

    async def delete_newsletter(self, newsletter_id: str) -> None:
        "Delete newsletter"
        return await self._core.request(
            "DELETE",
            "/newsletters/{newsletterId}",
            path_params={"newsletterId": newsletter_id},
            query=None,
            body=None,
            return_type=None,
        )

    async def get_newsletter(
        self, newsletter_id: str, *, fields: str | None = None
    ) -> NewsletterDetails:
        "Get a single newsletter by its ID."
        return await self._core.request(
            "GET",
            "/newsletters/{newsletterId}",
            path_params={"newsletterId": newsletter_id},
            query={"fields": fields},
            body=None,
            return_type=NewsletterDetails,
        )

    async def get_newsletter_activities(
        self,
        newsletter_id: str,
        *,
        query_activity: GetNewsletterActivitiesQueryActivity | None = None,
        query_created_on_from: datetime | None = None,
        query_created_on_to: datetime | None = None,
        sort_created_on: SortOrderEnum | None = None,
        per_page: int | None = None,
        page: int | None = None,
    ) -> list[NewsletterActivity]:
        "**DEPRECATED**: This method is deprecated and scheduled for removal. To synchronise newsletter activities please use [custom reports](https://apireference.getresponse.com/#operation/createCustomReport) with type `message_activity_reports`. This is the preferred approach due to better performance. By default, activities from the **last 14 days** are listed only. You can get activities for last 30 days only. You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by."
        return await self._core.request(
            "GET",
            "/newsletters/{newsletterId}/activities",
            path_params={"newsletterId": newsletter_id},
            query={
                "query[activity]": query_activity,
                "query[createdOn][from]": query_created_on_from,
                "query[createdOn][to]": query_created_on_to,
                "sort[createdOn]": sort_created_on,
                "perPage": per_page,
                "page": page,
            },
            body=None,
            return_type=list[NewsletterActivity],
        )

    async def get_newsletter_list(
        self,
        *,
        query_subject: str | None = None,
        query_name: str | None = None,
        query_status: GetNewsletterListQueryStatus | None = None,
        query_created_on_from: datetime | None = None,
        query_created_on_to: datetime | None = None,
        query_send_on_from: datetime | None = None,
        query_send_on_to: datetime | None = None,
        query_type: GetNewsletterListQueryType | None = None,
        query_campaign_id: str | None = None,
        sort_created_on: SortOrderEnum | None = None,
        sort_send_on: SortOrderEnum | None = None,
        fields: str | None = None,
        per_page: int | None = None,
        page: int | None = None,
    ) -> list[NewsletterListElement]:
        "You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by."
        return await self._core.request(
            "GET",
            "/newsletters",
            path_params=None,
            query={
                "query[subject]": query_subject,
                "query[name]": query_name,
                "query[status]": query_status,
                "query[createdOn][from]": query_created_on_from,
                "query[createdOn][to]": query_created_on_to,
                "query[sendOn][from]": query_send_on_from,
                "query[sendOn][to]": query_send_on_to,
                "query[type]": query_type,
                "query[campaignId]": query_campaign_id,
                "sort[createdOn]": sort_created_on,
                "sort[sendOn]": sort_send_on,
                "fields": fields,
                "perPage": per_page,
                "page": page,
            },
            body=None,
            return_type=list[NewsletterListElement],
        )

    async def get_newsletter_statistics_collection(
        self,
        *,
        query_group_by: GetNewsletterStatisticsCollectionQueryGroupBy | None = None,
        query_newsletter_id: str | None = None,
        query_campaign_id: str | None = None,
        query_created_on_from: datetime | None = None,
        query_created_on_to: datetime | None = None,
        fields: str | None = None,
        per_page: int | None = None,
        page: int | None = None,
    ) -> list[MessageStatisticsListElement]:
        ">This makes it possible to fetch newsletter statistics based on the list of campaign or newsletter IDs (you can pass them in the query parameter - see the description below). Remember that all the statistics date ranges are returned in standard UTC period type objects. ([See ISO 8601 standard](http://en.wikipedia.org/wiki/ISO_8601#Time_intervals)). You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by."
        return await self._core.request(
            "GET",
            "/newsletters/statistics",
            path_params=None,
            query={
                "query[groupBy]": query_group_by,
                "query[newsletterId]": query_newsletter_id,
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

    async def get_newsletter_thumbnail(
        self, newsletter_id: str, *, size: GetNewsletterThumbnailSize | None = None
    ) -> None:
        "Get newsletter thumbnail"
        return await self._core.request(
            "GET",
            "/newsletters/{newsletterId}/thumbnail",
            path_params={"newsletterId": newsletter_id},
            query={"size": size},
            body=None,
            return_type=None,
        )

    async def get_single_newsletter_statistics(
        self,
        newsletter_id: str,
        *,
        query_group_by: GetSingleNewsletterStatisticsQueryGroupBy | None = None,
        query_created_on_from: datetime | None = None,
        query_created_on_to: datetime | None = None,
        fields: str | None = None,
        per_page: int | None = None,
        page: int | None = None,
    ) -> list[MessageStatisticsListElement]:
        "> This makes it possible to easily fetch statistics for a single newsletter. You can group the data hourly, daily, monthly and as a total sum. Remember that all statistics date ranges are given in standard UTC period type objects. ([See ISO 8601 standard](http://en.wikipedia.org/wiki/ISO_8601#Time_intervals)). You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by."
        return await self._core.request(
            "GET",
            "/newsletters/{newsletterId}/statistics",
            path_params={"newsletterId": newsletter_id},
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

    async def send_draft(self, body: SendNewsletterDraft) -> NewsletterDetails:
        "Send the newsletter draft"
        return await self._core.request(
            "POST",
            "/newsletters/send-draft",
            path_params=None,
            query=None,
            body=body,
            return_type=NewsletterDetails,
        )
