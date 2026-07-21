"""Operations tagged 'Multimedia' in the GetResponse API."""

from __future__ import annotations

from .._core import _Core
from ..models import ImageDetails


class MultimediaResource:
    "Operations tagged 'Multimedia' in the GetResponse API."

    def __init__(self, core: _Core) -> None:
        self._core = core

    async def get_image_list(
        self, *, fields: str | None = None, per_page: int | None = None, page: int | None = None
    ) -> list[ImageDetails]:
        "Get images list"
        return await self._core.request(
            "GET",
            "/multimedia",
            path_params=None,
            query={"fields": fields, "perPage": per_page, "page": page},
            body=None,
            return_type=list[ImageDetails],
        )

    async def upload_image(self, *, file: bytes, filename: str = "upload") -> ImageDetails:
        "Upload image Sends `file` as multipart/form-data."
        return await self._core.request(
            "POST",
            "/multimedia",
            files={"file": (filename, file)},
            return_type=ImageDetails,
        )
