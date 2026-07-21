"""Operations tagged 'Workflows' in the GetResponse API."""

from __future__ import annotations

from .._core import _Core
from ..models import (
    UpdateWorkflow,
    Workflow,
)


class WorkflowsResource:
    "Operations tagged 'Workflows' in the GetResponse API."

    def __init__(self, core: _Core) -> None:
        self._core = core

    async def get_workflow(self, workflow_id: str, *, fields: str | None = None) -> Workflow:
        "Get a single workflow by ID."
        return await self._core.request(
            "GET",
            "/workflow/{workflowId}",
            path_params={"workflowId": workflow_id},
            query={"fields": fields},
            body=None,
            return_type=Workflow,
        )

    async def get_workflow_list(
        self, *, fields: str | None = None, per_page: int | None = None, page: int | None = None
    ) -> list[Workflow]:
        "Get the list of workflows."
        return await self._core.request(
            "GET",
            "/workflow",
            path_params=None,
            query={"fields": fields, "perPage": per_page, "page": page},
            body=None,
            return_type=list[Workflow],
        )

    async def update_workflow(self, workflow_id: str, body: UpdateWorkflow) -> Workflow:
        "Update single workflow."
        return await self._core.request(
            "POST",
            "/workflow/{workflowId}",
            path_params={"workflowId": workflow_id},
            query=None,
            body=body,
            return_type=Workflow,
        )
