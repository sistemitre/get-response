"""Operations tagged 'A/B tests - subject' in the GetResponse API."""

from __future__ import annotations

from .._core import _Core
from ..models import (
    AbtestsSubjectDetails,
    AbtestsSubjectListItem,
    ChooseWinnerAbtestsSubject,
    GetAbTestSubjectListQueryStage,
    NewAbtestsSubject,
    SortOrderEnum,
)


class AbTestsSubjectResource:
    "Operations tagged 'A/B tests - subject' in the GetResponse API."

    def __init__(self, core: _Core) -> None:
        self._core = core

    async def cancel_ab_test(self, ab_test_id: str) -> None:
        "This method allows you to schedule the cancellation of an A/B test. Cancelling an A/B test is an asynchronous operation."
        return await self._core.request(
            "POST",
            "/ab-tests/{abTestId}/cancel",
            path_params={"abTestId": ab_test_id},
            query=None,
            body=None,
            return_type=None,
        )

    async def create_subject_ab_test(self, body: NewAbtestsSubject) -> AbtestsSubjectDetails:
        "Create a new A/B test"
        return await self._core.request(
            "POST",
            "/ab-tests/subject",
            path_params=None,
            query=None,
            body=body,
            return_type=AbtestsSubjectDetails,
        )

    async def delete_ab_test(self, ab_test_id: str) -> None:
        "This method allows you to delete an A/B test. Deletion is only permitted when the test is in one of the following states: `draft`, `cancelled`, `finished`, or `completed`."
        return await self._core.request(
            "DELETE",
            "/ab-tests/{abTestId}",
            path_params={"abTestId": ab_test_id},
            query=None,
            body=None,
            return_type=None,
        )

    async def get_ab_test_subject_by_id(
        self, ab_test_id: str, *, fields: str | None = None
    ) -> AbtestsSubjectDetails:
        "Get a single A/B test by ID"
        return await self._core.request(
            "GET",
            "/ab-tests/subject/{abTestId}",
            path_params={"abTestId": ab_test_id},
            query={"fields": fields},
            body=None,
            return_type=AbtestsSubjectDetails,
        )

    async def get_ab_test_subject_list(
        self,
        *,
        query_name: str | None = None,
        query_stage: GetAbTestSubjectListQueryStage | None = None,
        query_ab_test_id: str | None = None,
        query_campaign_id: str | None = None,
        sort_name: SortOrderEnum | None = None,
        sort_stage: SortOrderEnum | None = None,
        sort_send_on: SortOrderEnum | None = None,
        sort_total_delivered: SortOrderEnum | None = None,
        fields: str | None = None,
        per_page: int | None = None,
        page: int | None = None,
    ) -> list[AbtestsSubjectListItem]:
        "You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by."
        return await self._core.request(
            "GET",
            "/ab-tests/subject",
            path_params=None,
            query={
                "query[name]": query_name,
                "query[stage]": query_stage,
                "query[abTestId]": query_ab_test_id,
                "query[campaignId]": query_campaign_id,
                "sort[name]": sort_name,
                "sort[stage]": sort_stage,
                "sort[sendOn]": sort_send_on,
                "sort[totalDelivered]": sort_total_delivered,
                "fields": fields,
                "perPage": per_page,
                "page": page,
            },
            body=None,
            return_type=list[AbtestsSubjectListItem],
        )

    async def post_abtests_subject_by_id_winner(
        self, ab_test_id: str, body: ChooseWinnerAbtestsSubject
    ) -> None:
        "Choose A/B test winner"
        return await self._core.request(
            "POST",
            "/ab-tests/subject/{abTestId}/winner",
            path_params={"abTestId": ab_test_id},
            query=None,
            body=body,
            return_type=None,
        )
