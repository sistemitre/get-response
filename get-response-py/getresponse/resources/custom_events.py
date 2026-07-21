"""Operations tagged 'Custom Events' in the GetResponse API."""

from __future__ import annotations

from .._core import _Core
from ..models import (
    CustomEventDetails,
    NewCustomEvent,
    SortOrderEnum,
    StringBooleanEnum,
    TriggerCustomEvent,
    UpdateCustomEvent,
)


class CustomEventsResource:
    "Operations tagged 'Custom Events' in the GetResponse API."

    def __init__(self, core: _Core) -> None:
        self._core = core

    async def create_custom_event(self, body: NewCustomEvent) -> CustomEventDetails:
        "Create custom event"
        return await self._core.request(
            "POST",
            "/custom-events",
            path_params=None,
            query=None,
            body=body,
            return_type=CustomEventDetails,
        )

    async def delete_custom_event(self, custom_event_id: str) -> None:
        "Delete a custom event by custom event ID"
        return await self._core.request(
            "DELETE",
            "/custom-events/{customEventId}",
            path_params={"customEventId": custom_event_id},
            query=None,
            body=None,
            return_type=None,
        )

    async def get_custom_event_by_id(
        self, custom_event_id: str, *, fields: str | None = None
    ) -> CustomEventDetails:
        "Get custom events by custom event ID"
        return await self._core.request(
            "GET",
            "/custom-events/{customEventId}",
            path_params={"customEventId": custom_event_id},
            query={"fields": fields},
            body=None,
            return_type=CustomEventDetails,
        )

    async def get_custom_events_list(
        self,
        *,
        query_name: str | None = None,
        query_has_attributes: StringBooleanEnum | None = None,
        sort_name: SortOrderEnum | None = None,
        fields: str | None = None,
        per_page: int | None = None,
        page: int | None = None,
    ) -> list[CustomEventDetails]:
        "You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by."
        return await self._core.request(
            "GET",
            "/custom-events",
            path_params=None,
            query={
                "query[name]": query_name,
                "query[hasAttributes]": query_has_attributes,
                "sort[name]": sort_name,
                "fields": fields,
                "perPage": per_page,
                "page": page,
            },
            body=None,
            return_type=list[CustomEventDetails],
        )

    async def trigger_custom_event(self, body: TriggerCustomEvent) -> None:
        "Trigger a custom event"
        return await self._core.request(
            "POST",
            "/custom-events/trigger",
            path_params=None,
            query=None,
            body=body,
            return_type=None,
        )

    async def update_custom_event(
        self, custom_event_id: str, body: UpdateCustomEvent
    ) -> CustomEventDetails:
        "Update custom event details"
        return await self._core.request(
            "POST",
            "/custom-events/{customEventId}",
            path_params={"customEventId": custom_event_id},
            query=None,
            body=body,
            return_type=CustomEventDetails,
        )
