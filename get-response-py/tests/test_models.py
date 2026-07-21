"""Model (de)serialization: a realistic Contact payload round-trips; NewContact serializes
cleanly to camelCase with no None keys.
"""

from __future__ import annotations

from getresponse.models import CampaignReference, Contact, ContactOrigin, NewContact


def test_contact_deserializes_with_enum_and_camelcase_aliases() -> None:
    payload = {
        "contactId": "abc123",
        "name": "Jane Doe",
        "origin": "api",
        "createdOn": "2024-01-01T00:00:00+00:00",
        "campaign": {"campaignId": "c1", "name": "My Campaign"},
        "email": "jane@example.com",
        "href": "https://api.getresponse.com/v3/contacts/abc123",
    }

    contact = Contact.model_validate(payload)

    assert contact.contact_id == "abc123"
    assert contact.email == "jane@example.com"
    assert contact.origin == ContactOrigin.Api
    assert contact.campaign is not None
    assert contact.campaign.campaign_id == "c1"


def test_new_contact_serializes_to_camelcase_without_none_keys() -> None:
    new_contact = NewContact(
        contact_id="",
        href="",
        email="jane@example.com",
        campaign=CampaignReference(campaign_id="c1"),
        name="Jane Doe",
    )

    dumped = new_contact.model_dump(mode="json", by_alias=True, exclude_none=True)

    assert dumped["email"] == "jane@example.com"
    assert dumped["campaign"]["campaignId"] == "c1"
    assert dumped["contactId"] == ""
    assert "contact_id" not in dumped
    assert all(value is not None for value in dumped.values())
