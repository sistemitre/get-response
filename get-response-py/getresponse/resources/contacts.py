"""Operations tagged 'Contacts' in the GetResponse API."""

from __future__ import annotations

from typing import Any

from .._core import _Core
from ..models import (
    ContactActivity,
    ContactConsent,
    ContactCustomField,
    ContactDetails,
    ContactListElement,
    GetContactListQueryOrigin,
    NewContact,
    SortOrderEnum,
    UpdateContact,
    UpsertContactCustomFields,
    UpsertContactTags,
)


class ContactsResource:
    "Operations tagged 'Contacts' in the GetResponse API."

    def __init__(self, core: _Core) -> None:
        self._core = core

    async def create_batch_contacts(self, body: dict[str, Any]) -> None:
        "This endpoint lets you create multiple contacts in one request. **Note** This endpoint is subject to special limits and throttling. You can make 80 calls per time frame (10 minutes) and only 1 call per second. The allowed batch size is 1000 contacts. For more information, check our [API Docs](https://apidocs.getresponse.com/v3/case-study/adding-batch-contacts)."
        return await self._core.request(
            "POST",
            "/contacts/batch",
            path_params=None,
            query=None,
            body=body,
            return_type=None,
        )

    async def create_contact(self, body: NewContact) -> None:
        "Create a new contact"
        return await self._core.request(
            "POST",
            "/contacts",
            path_params=None,
            query=None,
            body=body,
            return_type=None,
        )

    async def delete_contact(
        self, contact_id: str, *, message_id: str | None = None, ip_address: str | None = None
    ) -> None:
        "Delete a contact by contact ID"
        return await self._core.request(
            "DELETE",
            "/contacts/{contactId}",
            path_params={"contactId": contact_id},
            query={"messageId": message_id, "ipAddress": ip_address},
            body=None,
            return_type=None,
        )

    async def get_activities(
        self,
        contact_id: str,
        *,
        query_created_on_from: dict[str, Any] | None = None,
        query_created_on_to: dict[str, Any] | None = None,
        fields: str | None = None,
        per_page: int | None = None,
        page: int | None = None,
    ) -> list[ContactActivity]:
        "By default, only activities from the last 14 days are returned. To get earlier data, use `query[createdOn]` parameter. You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by."
        return await self._core.request(
            "GET",
            "/contacts/{contactId}/activities",
            path_params={"contactId": contact_id},
            query={
                "query[createdOn][from]": query_created_on_from,
                "query[createdOn][to]": query_created_on_to,
                "fields": fields,
                "perPage": per_page,
                "page": page,
            },
            body=None,
            return_type=list[ContactActivity],
        )

    async def get_contact_by_id(
        self, contact_id: str, *, fields: str | None = None
    ) -> ContactDetails:
        "Returns all available information about an active (non-deleted) contact identified by `contactId`. The response includes basic contact data, associated tags, and values of custom fields"
        return await self._core.request(
            "GET",
            "/contacts/{contactId}",
            path_params={"contactId": contact_id},
            query={"fields": fields},
            body=None,
            return_type=ContactDetails,
        )

    async def get_contact_consents_by_id(
        self, contact_id: str, *, fields: str | None = None
    ) -> list[ContactConsent]:
        "Returns a list of all consent fields assigned to the contact, including their current status and history of changes."
        return await self._core.request(
            "GET",
            "/contacts/{contactId}/consents",
            path_params={"contactId": contact_id},
            query={"fields": fields},
            body=None,
            return_type=list[ContactConsent],
        )

    async def get_contact_list(
        self,
        *,
        query_email: str | None = None,
        query_name: str | None = None,
        query_campaign_id: str | None = None,
        query_origin: GetContactListQueryOrigin | None = None,
        query_created_on_from: dict[str, Any] | None = None,
        query_created_on_to: dict[str, Any] | None = None,
        query_changed_on_from: dict[str, Any] | None = None,
        query_changed_on_to: dict[str, Any] | None = None,
        sort_email: SortOrderEnum | None = None,
        sort_name: SortOrderEnum | None = None,
        sort_created_on: SortOrderEnum | None = None,
        sort_changed_on: SortOrderEnum | None = None,
        sort_campaign_id: SortOrderEnum | None = None,
        additional_flags: str | None = None,
        fields: str | None = None,
        per_page: int | None = None,
        page: int | None = None,
    ) -> list[ContactListElement]:
        "You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by."
        return await self._core.request(
            "GET",
            "/contacts",
            path_params=None,
            query={
                "query[email]": query_email,
                "query[name]": query_name,
                "query[campaignId]": query_campaign_id,
                "query[origin]": query_origin,
                "query[createdOn][from]": query_created_on_from,
                "query[createdOn][to]": query_created_on_to,
                "query[changedOn][from]": query_changed_on_from,
                "query[changedOn][to]": query_changed_on_to,
                "sort[email]": sort_email,
                "sort[name]": sort_name,
                "sort[createdOn]": sort_created_on,
                "sort[changedOn]": sort_changed_on,
                "sort[campaignId]": sort_campaign_id,
                "additionalFlags": additional_flags,
                "fields": fields,
                "perPage": per_page,
                "page": page,
            },
            body=None,
            return_type=list[ContactListElement],
        )

    async def get_contacts_from_campaign(
        self,
        campaign_id: str,
        *,
        query_email: str | None = None,
        query_name: str | None = None,
        query_created_on_from: dict[str, Any] | None = None,
        query_created_on_to: dict[str, Any] | None = None,
        sort_email: SortOrderEnum | None = None,
        sort_name: SortOrderEnum | None = None,
        sort_created_on: SortOrderEnum | None = None,
        fields: str | None = None,
        per_page: int | None = None,
        page: int | None = None,
    ) -> list[ContactListElement]:
        "Provides all contacts from a single campaign. You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by."
        return await self._core.request(
            "GET",
            "/campaigns/{campaignId}/contacts",
            path_params={"campaignId": campaign_id},
            query={
                "query[email]": query_email,
                "query[name]": query_name,
                "query[createdOn][from]": query_created_on_from,
                "query[createdOn][to]": query_created_on_to,
                "sort[email]": sort_email,
                "sort[name]": sort_name,
                "sort[createdOn]": sort_created_on,
                "fields": fields,
                "perPage": per_page,
                "page": page,
            },
            body=None,
            return_type=list[ContactListElement],
        )

    async def update_contact(self, contact_id: str, body: UpdateContact) -> ContactDetails:
        "Skip the fields you don't want to update. If tags and custom fields are provided, they'll be **replaced** with the values sent in this request. If the `campaignId` changes, the contact will be moved from the original campaign (list) to the new campaign (list). Their activity history and statistics will also be moved."
        return await self._core.request(
            "POST",
            "/contacts/{contactId}",
            path_params={"contactId": contact_id},
            query=None,
            body=body,
            return_type=ContactDetails,
        )

    async def upsert_contact_customs(
        self, contact_id: str, body: UpsertContactCustomFields
    ) -> list[ContactCustomField]:
        "Upsert (add or update) the custom fields of a contact. This method doesn't remove (unassign) custom fields."
        return await self._core.request(
            "POST",
            "/contacts/{contactId}/custom-fields",
            path_params={"contactId": contact_id},
            query=None,
            body=body,
            return_type=list[ContactCustomField],
        )

    async def upsert_tags(self, contact_id: str, body: UpsertContactTags) -> list[dict[str, Any]]:
        "Upsert (add or update) the tags of a contact. This method doesn't remove (unassign) tags."
        return await self._core.request(
            "POST",
            "/contacts/{contactId}/tags",
            path_params={"contactId": contact_id},
            query=None,
            body=body,
            return_type=list[dict[str, Any]],
        )
