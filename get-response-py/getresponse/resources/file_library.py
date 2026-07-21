"""Operations tagged 'File Library' in the GetResponse API."""

from __future__ import annotations

from .._core import _Core
from ..models import (
    File,
    FileGroup,
    Folder,
    NewFile,
    NewFolder,
    Quota,
    SortOrderEnum,
    StringBooleanEnum,
)


class FileLibraryResource:
    "Operations tagged 'File Library' in the GetResponse API."

    def __init__(self, core: _Core) -> None:
        self._core = core

    async def create_file(self, body: NewFile) -> File:
        "Create a file"
        return await self._core.request(
            "POST",
            "/file-library/files",
            path_params=None,
            query=None,
            body=body,
            return_type=File,
        )

    async def create_folder(self, body: NewFolder) -> list[Folder]:
        "Create a folder"
        return await self._core.request(
            "POST",
            "/file-library/folders",
            path_params=None,
            query=None,
            body=body,
            return_type=list[Folder],
        )

    async def delete_file(self, file_id: str) -> None:
        "Delete file by file ID"
        return await self._core.request(
            "DELETE",
            "/file-library/files/{fileId}",
            path_params={"fileId": file_id},
            query=None,
            body=None,
            return_type=None,
        )

    async def delete_folder(self, folder_id: str) -> None:
        "Delete folder by folder ID"
        return await self._core.request(
            "DELETE",
            "/file-library/folders/{folderId}",
            path_params={"folderId": folder_id},
            query=None,
            body=None,
            return_type=None,
        )

    async def get_file_by_id(self, file_id: str, *, fields: str | None = None) -> File:
        "Get file by ID"
        return await self._core.request(
            "GET",
            "/file-library/files/{fileId}",
            path_params={"fileId": file_id},
            query={"fields": fields},
            body=None,
            return_type=File,
        )

    async def get_file_list(
        self,
        *,
        query_all_folders: StringBooleanEnum | None = None,
        query_folder_id: str | None = None,
        query_name: str | None = None,
        query_group: FileGroup | None = None,
        sort_name: SortOrderEnum | None = None,
        sort_group: SortOrderEnum | None = None,
        sort_size: SortOrderEnum | None = None,
        fields: str | None = None,
        per_page: int | None = None,
        page: int | None = None,
    ) -> list[File]:
        "By default, you can only search files in the root directory. To search for files in all folders, use the parameter `query[allFolders]=true`. To search for files in a specified folder, use the parameter `query[folderId]=<folderId>`. **Note: these two parameters can't be used together**. You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by."
        return await self._core.request(
            "GET",
            "/file-library/files",
            path_params=None,
            query={
                "query[allFolders]": query_all_folders,
                "query[folderId]": query_folder_id,
                "query[name]": query_name,
                "query[group]": query_group,
                "sort[name]": sort_name,
                "sort[group]": sort_group,
                "sort[size]": sort_size,
                "fields": fields,
                "perPage": per_page,
                "page": page,
            },
            body=None,
            return_type=list[File],
        )

    async def get_folder_list(
        self,
        *,
        query_name: str | None = None,
        sort_name: SortOrderEnum | None = None,
        sort_size: SortOrderEnum | None = None,
        sort_created_on: SortOrderEnum | None = None,
        fields: str | None = None,
        per_page: int | None = None,
        page: int | None = None,
    ) -> list[Folder]:
        "You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by."
        return await self._core.request(
            "GET",
            "/file-library/folders",
            path_params=None,
            query={
                "query[name]": query_name,
                "sort[name]": sort_name,
                "sort[size]": sort_size,
                "sort[createdOn]": sort_created_on,
                "fields": fields,
                "perPage": per_page,
                "page": page,
            },
            body=None,
            return_type=list[Folder],
        )

    async def quota(self) -> Quota:
        "Get storage space information"
        return await self._core.request(
            "GET",
            "/file-library/quota",
            path_params=None,
            query=None,
            body=None,
            return_type=Quota,
        )
