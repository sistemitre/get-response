"""Operations tagged 'Tracking' in the GetResponse API."""

from __future__ import annotations

from .._core import _Core
from ..models import (
    FacebookPixel,
    Tracking,
)


class TrackingResource:
    "Operations tagged 'Tracking' in the GetResponse API."

    def __init__(self, core: _Core) -> None:
        self._core = core

    async def get_facebook_pixel_list(self) -> list[FacebookPixel]:
        'Returns the name and ID of "Facebook Pixels" assigned to a user\'s account.'
        return await self._core.request(
            "GET",
            "/tracking/facebook-pixels",
            path_params=None,
            query=None,
            body=None,
            return_type=list[FacebookPixel],
        )

    async def get_tracking(self) -> list[Tracking]:
        "With code snippets you will be able to track Purchases, Abandoned carts, and Visited URLs. Find more in our [Help Center](https://www.getresponse.com/help/marketing-automation/ecommerce-conditions/how-do-i-add-the-tracking-javascript-code-to-my-website.html)."
        return await self._core.request(
            "GET",
            "/tracking",
            path_params=None,
            query=None,
            body=None,
            return_type=list[Tracking],
        )
