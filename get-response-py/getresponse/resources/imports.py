"""Operations tagged 'Imports' in the GetResponse API."""

from __future__ import annotations

from datetime import datetime

from .._core import _Core
from ..models import (
    Import,
    NewImport,
    SortOrderEnum,
)


class ImportsResource:
    "Operations tagged 'Imports' in the GetResponse API."

    def __init__(self, core: _Core) -> None:
        self._core = core

    async def create_import(self, body: NewImport) -> Import:
        "This endpoint lets you schedule a contact import. That way, you can add and update your contacts using a single API call. Since API imports are asynchronous, you should check periodically for updates while your original API request is being processed. To keep track of your import status, use [GET import](https://apireference.getresponse.com/#operation/getImportById) (provide the importId from the response), or subscribe to an [import finished](https://apidocs.getresponse.com/v3/payloads#contacts-import-finished) webhook. Please note, that this endpoint has **specific rate limits** - for details please refer to [Create Import Limits](https://apidocs.getresponse.com/v3/case-study/create-import#limits). For more information on imports, check our [API Docs](https://apidocs.getresponse.com/v3/case-study/create-import) or [Help Center](https://www.getresponse.com/help/how-do-i-prepare-a-file-for-import.html)"
        return await self._core.request(
            "POST",
            "/imports",
            path_params=None,
            query=None,
            body=body,
            return_type=Import,
        )

    async def get_import_by_id(self, import_id: str, *, fields: str | None = None) -> Import:
        "Get import details by ID."
        return await self._core.request(
            "GET",
            "/imports/{importId}",
            path_params={"importId": import_id},
            query={"fields": fields},
            body=None,
            return_type=Import,
        )

    async def get_import_list(
        self,
        *,
        query_campaign_id: str | None = None,
        query_created_on_from: datetime | None = None,
        query_created_on_to: datetime | None = None,
        sort_created_on: SortOrderEnum | None = None,
        sort_finished_on: SortOrderEnum | None = None,
        sort_campaign_name: SortOrderEnum | None = None,
        sort_uploaded_contacts: SortOrderEnum | None = None,
        sort_updated_contacts: SortOrderEnum | None = None,
        sort_added_contacts: SortOrderEnum | None = None,
        sort_invalid_contacts: SortOrderEnum | None = None,
        sort_status: SortOrderEnum | None = None,
        fields: str | None = None,
        per_page: int | None = None,
        page: int | None = None,
    ) -> list[Import]:
        "You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by."
        return await self._core.request(
            "GET",
            "/imports",
            path_params=None,
            query={
                "query[campaignId]": query_campaign_id,
                "query[createdOn][from]": query_created_on_from,
                "query[createdOn][to]": query_created_on_to,
                "sort[createdOn]": sort_created_on,
                "sort[finishedOn]": sort_finished_on,
                "sort[campaignName]": sort_campaign_name,
                "sort[uploadedContacts]": sort_uploaded_contacts,
                "sort[updatedContacts]": sort_updated_contacts,
                "sort[addedContacts]": sort_added_contacts,
                "sort[invalidContacts]": sort_invalid_contacts,
                "sort[status]": sort_status,
                "fields": fields,
                "perPage": per_page,
                "page": page,
            },
            body=None,
            return_type=list[Import],
        )
