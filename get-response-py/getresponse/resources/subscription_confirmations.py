"""Operations tagged 'Subscription Confirmations' in the GetResponse API."""

from __future__ import annotations

from .._core import _Core
from ..models import (
    SubscriptionConfirmationBody,
    SubscriptionConfirmationSubject,
)


class SubscriptionConfirmationsResource:
    "Operations tagged 'Subscription Confirmations' in the GetResponse API."

    def __init__(self, core: _Core) -> None:
        self._core = core

    async def get_subscription_confirmation_body_list(
        self, language_code: str, *, fields: str | None = None
    ) -> list[SubscriptionConfirmationBody]:
        "Sending **GET** request to this url, returns collection of **SUBSCRIPTION CONFIRMATIONS** bodies. Language code used in url must be in ISO 639-1 Language Code Standard."
        return await self._core.request(
            "GET",
            "/subscription-confirmations/body/{languageCode}",
            path_params={"languageCode": language_code},
            query={"fields": fields},
            body=None,
            return_type=list[SubscriptionConfirmationBody],
        )

    async def get_subscription_confirmation_subject_list(
        self, language_code: str, *, fields: str | None = None
    ) -> list[SubscriptionConfirmationSubject]:
        "Sending **GET** request to this url, returns collection of **SUBSCRIPTION CONFIRMATIONS** subjects. Language code used in url must be in ISO 639-1 Language Code Standard."
        return await self._core.request(
            "GET",
            "/subscription-confirmations/subject/{languageCode}",
            path_params={"languageCode": language_code},
            query={"fields": fields},
            body=None,
            return_type=list[SubscriptionConfirmationSubject],
        )
