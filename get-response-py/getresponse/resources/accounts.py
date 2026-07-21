"""Operations tagged 'Accounts' in the GetResponse API."""

from __future__ import annotations

from typing import Any

from .._core import _Core
from ..models import (
    Account,
    AccountBadgeDetails,
    AccountBilling,
    AccountsLoginHistoryListElement,
    Blocklist,
    Callback,
    IndustryTag,
    SendingLimitsListItem,
    Timezone,
    UpdateAccount,
    UpdateAccountBlocklistAdditionalFlags,
    UpdateBlocklist,
    UpdateCallbacks,
)


class AccountsResource:
    "Operations tagged 'Accounts' in the GetResponse API."

    def __init__(self, core: _Core) -> None:
        self._core = core

    async def disable_callbacks(self) -> None:
        "Disable callbacks"
        return await self._core.request(
            "DELETE",
            "/accounts/callbacks",
            path_params=None,
            query=None,
            body=None,
            return_type=None,
        )

    async def get_account(self, *, fields: str | None = None) -> Account:
        "Account information"
        return await self._core.request(
            "GET",
            "/accounts",
            path_params=None,
            query={"fields": fields},
            body=None,
            return_type=Account,
        )

    async def get_account_badge(self) -> AccountBadgeDetails:
        "Current status of your GetResponse badge"
        return await self._core.request(
            "GET",
            "/accounts/badge",
            path_params=None,
            query=None,
            body=None,
            return_type=AccountBadgeDetails,
        )

    async def get_account_billing(self, *, fields: str | None = None) -> AccountBilling:
        "Billing information"
        return await self._core.request(
            "GET",
            "/accounts/billing",
            path_params=None,
            query={"fields": fields},
            body=None,
            return_type=AccountBilling,
        )

    async def get_account_blocklist(self, *, query_mask: str | None = None) -> Blocklist:
        "Returns account blocklist masks"
        return await self._core.request(
            "GET",
            "/accounts/blocklists",
            path_params=None,
            query={"query[mask]": query_mask},
            body=None,
            return_type=Blocklist,
        )

    async def get_account_login_history(
        self, *, fields: str | None = None, per_page: int | None = None, page: int | None = None
    ) -> list[AccountsLoginHistoryListElement]:
        "History of logins"
        return await self._core.request(
            "GET",
            "/accounts/login-history",
            path_params=None,
            query={"fields": fields, "perPage": per_page, "page": page},
            body=None,
            return_type=list[AccountsLoginHistoryListElement],
        )

    async def get_callbacks(self) -> Callback:
        "Get callbacks configuration"
        return await self._core.request(
            "GET",
            "/accounts/callbacks",
            path_params=None,
            query=None,
            body=None,
            return_type=Callback,
        )

    async def get_industries(
        self, *, fields: str | None = None, per_page: int | None = None, page: int | None = None
    ) -> list[IndustryTag]:
        "List of Industry Tags in account's language context."
        return await self._core.request(
            "GET",
            "/accounts/industries",
            path_params=None,
            query={"fields": fields, "perPage": per_page, "page": page},
            body=None,
            return_type=list[IndustryTag],
        )

    async def get_sending_limits(self, *, fields: str | None = None) -> list[SendingLimitsListItem]:
        "Send limits"
        return await self._core.request(
            "GET",
            "/accounts/sending-limits",
            path_params=None,
            query={"fields": fields},
            body=None,
            return_type=list[SendingLimitsListItem],
        )

    async def get_timezones(self, *, fields: str | None = None) -> list[Timezone]:
        "List of timezones in account's language context."
        return await self._core.request(
            "GET",
            "/accounts/timezones",
            path_params=None,
            query={"fields": fields},
            body=None,
            return_type=list[Timezone],
        )

    async def update_account(self, body: UpdateAccount) -> Account:
        "Update account"
        return await self._core.request(
            "POST",
            "/accounts",
            path_params=None,
            query=None,
            body=body,
            return_type=Account,
        )

    async def update_account_badge(self, body: dict[str, Any]) -> AccountBadgeDetails:
        "Turn on/off the GetResponse Badge"
        return await self._core.request(
            "POST",
            "/accounts/badge",
            path_params=None,
            query=None,
            body=body,
            return_type=AccountBadgeDetails,
        )

    async def update_account_blocklist(
        self,
        body: UpdateBlocklist,
        *,
        additional_flags: UpdateAccountBlocklistAdditionalFlags | None = None,
    ) -> Blocklist:
        "Update account blocklist"
        return await self._core.request(
            "POST",
            "/accounts/blocklists",
            path_params=None,
            query={"additionalFlags": additional_flags},
            body=body,
            return_type=Blocklist,
        )

    async def update_callbacks(self, body: UpdateCallbacks) -> Callback:
        "Enable or update callbacks configuration"
        return await self._core.request(
            "POST",
            "/accounts/callbacks",
            path_params=None,
            query=None,
            body=body,
            return_type=Callback,
        )
