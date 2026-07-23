"""Operations tagged 'Search Contacts' in the GetResponse API."""

from __future__ import annotations

from datetime import datetime

from .._core import _Core
from ..models import (
    BaseSearchContactsDetails,
    NewSearchContacts,
    SearchContactsBySearchForm,
    SearchContactsDetails,
    SearchedContactDetails,
    SortOrderEnum,
    UpdateSearchContacts,
    UpsertContactCustomFields,
)


class SearchContactsResource:
    "Operations tagged 'Search Contacts' in the GetResponse API."

    def __init__(self, core: _Core) -> None:
        self._core = core

    async def delete_search_contacts(self, search_contact_id: str) -> None:
        "Delete search contacts"
        return await self._core.request(
            "DELETE",
            "/search-contacts/{searchContactId}",
            path_params={"searchContactId": search_contact_id},
            query=None,
            body=None,
            return_type=None,
        )

    async def get_contacts_by_id_search_contacts(
        self,
        search_contact_id: str,
        *,
        sort_name: SortOrderEnum | None = None,
        sort_email: SortOrderEnum | None = None,
        sort_created_on: SortOrderEnum | None = None,
        fields: str | None = None,
        per_page: int | None = None,
        page: int | None = None,
    ) -> list[SearchedContactDetails]:
        "Get contacts from saved search contacts by ID."
        return await self._core.request(
            "GET",
            "/search-contacts/{searchContactId}/contacts",
            path_params={"searchContactId": search_contact_id},
            query={
                "sort[name]": sort_name,
                "sort[email]": sort_email,
                "sort[createdOn]": sort_created_on,
                "fields": fields,
                "perPage": per_page,
                "page": page,
            },
            body=None,
            return_type=list[SearchedContactDetails],
        )

    async def get_contacts_from_search_contacts_conditions(
        self,
        body: SearchContactsBySearchForm,
        *,
        sort_name: SortOrderEnum | None = None,
        sort_email: SortOrderEnum | None = None,
        sort_created_on: SortOrderEnum | None = None,
        fields: str | None = None,
        per_page: int | None = None,
        page: int | None = None,
    ) -> list[SearchedContactDetails]:
        "Makes it possible to get a collection of contacts according to a given condition. Please refer to [Segments (search contacts) reference manual](https://apidocs.getresponse.com/v3/case-study/segments-manual)"
        return await self._core.request(
            "POST",
            "/search-contacts/contacts",
            path_params=None,
            query={
                "sort[name]": sort_name,
                "sort[email]": sort_email,
                "sort[createdOn]": sort_created_on,
                "fields": fields,
                "perPage": per_page,
                "page": page,
            },
            body=body,
            return_type=list[SearchedContactDetails],
        )

    async def get_search_contacts_by_id(
        self, search_contact_id: str, *, fields: str | None = None
    ) -> SearchContactsDetails:
        "Get the definition of a specific contact-search filter."
        return await self._core.request(
            "GET",
            "/search-contacts/{searchContactId}",
            path_params={"searchContactId": search_contact_id},
            query={"fields": fields},
            body=None,
            return_type=SearchContactsDetails,
        )

    async def get_search_contacts_list(
        self,
        *,
        sort_name: SortOrderEnum | None = None,
        sort_created_on: SortOrderEnum | None = None,
        query_name: str | None = None,
        query_created_on_from: datetime | None = None,
        query_created_on_to: datetime | None = None,
        fields: str | None = None,
        per_page: int | None = None,
        page: int | None = None,
    ) -> list[BaseSearchContactsDetails]:
        "Makes it possible to retrieve a collection of short representations of search-contact (known as custom filters in the panel). Every item represents a basic filter object. You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by."
        return await self._core.request(
            "GET",
            "/search-contacts",
            path_params=None,
            query={
                "sort[name]": sort_name,
                "sort[createdOn]": sort_created_on,
                "query[name]": query_name,
                "query[createdOn][from]": query_created_on_from,
                "query[createdOn][to]": query_created_on_to,
                "fields": fields,
                "perPage": per_page,
                "page": page,
            },
            body=None,
            return_type=list[BaseSearchContactsDetails],
        )

    async def new_search_contacts(self, body: NewSearchContacts) -> SearchContactsDetails:
        "Makes it possible to create a new search-contact. Please refer to [Segments (search contacts) reference manual](https://apidocs.getresponse.com/v3/case-study/segments-manual)"
        return await self._core.request(
            "POST",
            "/search-contacts",
            path_params=None,
            query=None,
            body=body,
            return_type=SearchContactsDetails,
        )

    async def update_search_contacts(
        self, search_contact_id: str, body: UpdateSearchContacts
    ) -> SearchContactsDetails:
        "Update specified search contacts."
        return await self._core.request(
            "POST",
            "/search-contacts/{searchContactId}",
            path_params={"searchContactId": search_contact_id},
            query=None,
            body=body,
            return_type=SearchContactsDetails,
        )

    async def upsert_custom_fields_by_search_contact_id(
        self, search_contact_id: str, body: UpsertContactCustomFields
    ) -> None:
        "Makes it possible to add and update custom field values for all contacts that meet the search criteria. This method doesn't remove or overwrite custom fields with the values from the request."
        return await self._core.request(
            "POST",
            "/search-contacts/{searchContactId}/custom-fields",
            path_params={"searchContactId": search_contact_id},
            query=None,
            body=body,
            return_type=None,
        )
