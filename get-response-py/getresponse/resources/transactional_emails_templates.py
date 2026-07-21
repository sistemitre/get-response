"""Operations tagged 'Transactional Emails Templates' in the GetResponse API."""

from __future__ import annotations

from typing import Any

from .._core import _Core
from ..models import (
    CreateTransactionalEmailTemplate,
    SortOrderEnum,
    TransactionalEmailsTemplateDetails,
    TransactionalEmailsTemplateListElement,
)


class TransactionalEmailsTemplatesResource:
    "Operations tagged 'Transactional Emails Templates' in the GetResponse API."

    def __init__(self, core: _Core) -> None:
        self._core = core

    async def create_transactional_email_template(
        self, body: CreateTransactionalEmailTemplate
    ) -> TransactionalEmailsTemplateDetails:
        "This method creates a new transactional email template"
        return await self._core.request(
            "POST",
            "/transactional-emails/templates",
            path_params=None,
            query=None,
            body=body,
            return_type=TransactionalEmailsTemplateDetails,
        )

    async def delete_transactional_emails_template(
        self, transactional_email_template_id: str
    ) -> None:
        "Delete transactional email template"
        return await self._core.request(
            "DELETE",
            "/transactional-emails/templates/{transactionalEmailTemplateId}",
            path_params={"transactionalEmailTemplateId": transactional_email_template_id},
            query=None,
            body=None,
            return_type=None,
        )

    async def get_transactional_emails_templates_by_id(
        self, transactional_email_template_id: str, *, fields: str | None = None
    ) -> TransactionalEmailsTemplateDetails:
        "Get a single template by ID"
        return await self._core.request(
            "GET",
            "/transactional-emails/templates/{transactionalEmailTemplateId}",
            path_params={"transactionalEmailTemplateId": transactional_email_template_id},
            query={"fields": fields},
            body=None,
            return_type=TransactionalEmailsTemplateDetails,
        )

    async def get_transactional_emails_templates_list(
        self,
        *,
        query_subject: str | None = None,
        sort_created_on: SortOrderEnum | None = None,
        sort_subject: SortOrderEnum | None = None,
        fields: str | None = None,
        per_page: int | None = None,
        page: int | None = None,
    ) -> list[TransactionalEmailsTemplateListElement]:
        "You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by."
        return await self._core.request(
            "GET",
            "/transactional-emails/templates",
            path_params=None,
            query={
                "query[subject]": query_subject,
                "sort[createdOn]": sort_created_on,
                "sort[subject]": sort_subject,
                "fields": fields,
                "perPage": per_page,
                "page": page,
            },
            body=None,
            return_type=list[TransactionalEmailsTemplateListElement],
        )

    async def update_transactional_emails_template(
        self, transactional_email_template_id: str, body: dict[str, Any]
    ) -> TransactionalEmailsTemplateDetails:
        "This method allows you to update transactional email template"
        return await self._core.request(
            "POST",
            "/transactional-emails/templates/{transactionalEmailTemplateId}",
            path_params={"transactionalEmailTemplateId": transactional_email_template_id},
            query=None,
            body=body,
            return_type=TransactionalEmailsTemplateDetails,
        )
