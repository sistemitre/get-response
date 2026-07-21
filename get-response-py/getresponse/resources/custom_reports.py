"""Operations tagged 'Custom Reports' in the GetResponse API."""

from __future__ import annotations

from .._core import _Core
from ..models import (
    BaseCreateCustomReport,
    CustomReport,
    CustomReportDetails,
    SortOrderEnum,
)


class CustomReportsResource:
    "Operations tagged 'Custom Reports' in the GetResponse API."

    def __init__(self, core: _Core) -> None:
        self._core = core

    async def create_custom_report(self, body: BaseCreateCustomReport) -> CustomReportDetails:
        "The endpoint allows scheduling a custom report of a specific type for a given time period. Depending on the report type, you can also narrow down the data using appropriate filters. <strong>Important:</strong> The reports you can generate depend on your pricing plan. More information about using the endpoint, along with examples, can be found in the Case Study section of the [API documentation](http://apidocs.getresponse.com/v3/case-study/custom-reports-scheduling)."
        return await self._core.request(
            "POST",
            "/custom-reports",
            path_params=None,
            query=None,
            body=body,
            return_type=CustomReportDetails,
        )

    async def get_custom_report_details(
        self, custom_report_id: str, *, fields: str | None = None
    ) -> CustomReportDetails:
        "The endpoint allows retrieving detailed information about a custom report based on the provided `customReportId`. It returns report data, including: * details about the report, * generation statuses of the report files, * URLs from which the report files can be downloaded. More information on using custom reports can be found in the Case Study section of the [API documentation](http://apidocs.getresponse.com/v3/case-study/custom-reports)."
        return await self._core.request(
            "GET",
            "/custom-reports/{customReportId}",
            path_params={"customReportId": custom_report_id},
            query={"fields": fields},
            body=None,
            return_type=CustomReportDetails,
        )

    async def get_custom_report_list(
        self,
        *,
        query_name: str | None = None,
        sort_name: SortOrderEnum | None = None,
        sort_frequency: SortOrderEnum | None = None,
        sort_generated_at: SortOrderEnum | None = None,
        fields: str | None = None,
        per_page: int | None = None,
        page: int | None = None,
    ) -> list[CustomReport]:
        "You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by."
        return await self._core.request(
            "GET",
            "/custom-reports",
            path_params=None,
            query={
                "query[name]": query_name,
                "sort[name]": sort_name,
                "sort[frequency]": sort_frequency,
                "sort[generatedAt]": sort_generated_at,
                "fields": fields,
                "perPage": per_page,
                "page": page,
            },
            body=None,
            return_type=list[CustomReport],
        )
