"""Root async client: auth, resource groups, lifecycle, and pagination."""

from __future__ import annotations

from collections.abc import AsyncIterator, Awaitable, Callable
from typing import Any

import httpx

from ._core import DEFAULT_BASE_URL, _Core
from ._ratelimit import RateLimitOptions
from .resources import (
    AbTestsResource,
    AbTestsSubjectResource,
    AccountsResource,
    AddressesResource,
    AutorespondersResource,
    CampaignsListsResource,
    CartsResource,
    CategoriesResource,
    ClickTracksResource,
    ContactsResource,
    CustomEventsResource,
    CustomFieldsResource,
    CustomReportsResource,
    EcommerceResource,
    FileLibraryResource,
    FormAndPopupResource,
    FormsAndPopupsResource,
    FormsResource,
    FromFieldsResource,
    GdprFieldsResource,
    ImportsResource,
    LandingPageResource,
    LandingPagesResource,
    LegacyFormsResource,
    LegacyLandingPagesResource,
    MetaFieldsResource,
    MultimediaResource,
    NewslettersResource,
    OrdersResource,
    PredefinedFieldsResource,
    ProductsResource,
    ProductVariantsResource,
    RssNewslettersResource,
    SearchContactsResource,
    ShopsResource,
    SmsAutomationMessagesResource,
    SmsMessagesResource,
    SmsResource,
    SubscriptionConfirmationsResource,
    SuppressionsResource,
    TagsResource,
    TaxesResource,
    TrackingResource,
    TransactionalEmailsResource,
    TransactionalEmailsTemplatesResource,
    WebinarsResource,
    WebsiteResource,
    WebsitesResource,
    WorkflowsResource,
)


class GetResponseClient:
    """Async GetResponse v3 API client; one resource-group attribute per tag."""

    def __init__(
        self,
        api_key: str | None = None,
        *,
        access_token: str | None = None,
        base_url: str = DEFAULT_BASE_URL,
        timeout: float = 30.0,
        transport: httpx.AsyncBaseTransport | None = None,
        rate_limit: RateLimitOptions | None = None,
    ) -> None:
        if (api_key is None) == (access_token is None):
            raise ValueError("Provide exactly one of `api_key` or `access_token`.")
        headers = (
            {"X-Auth-Token": f"api-key {api_key}"}
            if api_key is not None
            else {"Authorization": f"Bearer {access_token}"}
        )
        self._client = httpx.AsyncClient(
            base_url=base_url, headers=headers, timeout=timeout, transport=transport
        )
        self._core = _Core(self._client, rate_limit)
        self.ab_tests = AbTestsResource(self._core)
        self.ab_tests_subject = AbTestsSubjectResource(self._core)
        self.accounts = AccountsResource(self._core)
        self.addresses = AddressesResource(self._core)
        self.autoresponders = AutorespondersResource(self._core)
        self.campaigns_lists = CampaignsListsResource(self._core)
        self.carts = CartsResource(self._core)
        self.categories = CategoriesResource(self._core)
        self.click_tracks = ClickTracksResource(self._core)
        self.contacts = ContactsResource(self._core)
        self.custom_events = CustomEventsResource(self._core)
        self.custom_fields = CustomFieldsResource(self._core)
        self.custom_reports = CustomReportsResource(self._core)
        self.ecommerce = EcommerceResource(self._core)
        self.file_library = FileLibraryResource(self._core)
        self.form_and_popup = FormAndPopupResource(self._core)
        self.forms = FormsResource(self._core)
        self.forms_and_popups = FormsAndPopupsResource(self._core)
        self.from_fields = FromFieldsResource(self._core)
        self.gdpr_fields = GdprFieldsResource(self._core)
        self.imports = ImportsResource(self._core)
        self.landing_page = LandingPageResource(self._core)
        self.landing_pages = LandingPagesResource(self._core)
        self.legacy_forms = LegacyFormsResource(self._core)
        self.legacy_landing_pages = LegacyLandingPagesResource(self._core)
        self.meta_fields = MetaFieldsResource(self._core)
        self.multimedia = MultimediaResource(self._core)
        self.newsletters = NewslettersResource(self._core)
        self.orders = OrdersResource(self._core)
        self.predefined_fields = PredefinedFieldsResource(self._core)
        self.product_variants = ProductVariantsResource(self._core)
        self.products = ProductsResource(self._core)
        self.rss_newsletters = RssNewslettersResource(self._core)
        self.sms_automation_messages = SmsAutomationMessagesResource(self._core)
        self.sms_messages = SmsMessagesResource(self._core)
        self.search_contacts = SearchContactsResource(self._core)
        self.shops = ShopsResource(self._core)
        self.sms = SmsResource(self._core)
        self.subscription_confirmations = SubscriptionConfirmationsResource(self._core)
        self.suppressions = SuppressionsResource(self._core)
        self.tags = TagsResource(self._core)
        self.taxes = TaxesResource(self._core)
        self.tracking = TrackingResource(self._core)
        self.transactional_emails = TransactionalEmailsResource(self._core)
        self.transactional_emails_templates = TransactionalEmailsTemplatesResource(self._core)
        self.webinars = WebinarsResource(self._core)
        self.website = WebsiteResource(self._core)
        self.websites = WebsitesResource(self._core)
        self.workflows = WorkflowsResource(self._core)

    async def aclose(self) -> None:
        """Close the underlying HTTP connection pool."""
        await self._client.aclose()

    async def __aenter__(self) -> GetResponseClient:
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        tb: object | None,
    ) -> None:
        await self.aclose()

    async def paginate(
        self,
        list_method: Callable[..., Awaitable[list[Any]]],
        *,
        per_page: int = 100,
        **kwargs: Any,
    ) -> AsyncIterator[Any]:
        """Walk every page of a `list_*` resource method, yielding items one by one.

        GetResponse also reports `TotalCount`/`CurrentPage`/`TotalPages` response
        headers, but resource methods only return typed bodies (no header access),
        so this walks by page length instead: it stops once a page comes back empty
        or shorter than `per_page`.
        """
        page = 1
        while True:
            items = await list_method(page=page, per_page=per_page, **kwargs)
            if not items:
                return
            for item in items:
                yield item
            if len(items) < per_page:
                return
            page += 1
