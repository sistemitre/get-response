"""Resource-group attributes attached to GetResponseClient. Generated from the spec's tags."""

from __future__ import annotations

from ._core import _Core
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


class _ResourceGroups:
    """Mixin providing one typed resource-group attribute per API tag."""

    ab_tests: AbTestsResource
    ab_tests_subject: AbTestsSubjectResource
    accounts: AccountsResource
    addresses: AddressesResource
    autoresponders: AutorespondersResource
    campaigns_lists: CampaignsListsResource
    carts: CartsResource
    categories: CategoriesResource
    click_tracks: ClickTracksResource
    contacts: ContactsResource
    custom_events: CustomEventsResource
    custom_fields: CustomFieldsResource
    custom_reports: CustomReportsResource
    ecommerce: EcommerceResource
    file_library: FileLibraryResource
    form_and_popup: FormAndPopupResource
    forms: FormsResource
    forms_and_popups: FormsAndPopupsResource
    from_fields: FromFieldsResource
    gdpr_fields: GdprFieldsResource
    imports: ImportsResource
    landing_page: LandingPageResource
    landing_pages: LandingPagesResource
    legacy_forms: LegacyFormsResource
    legacy_landing_pages: LegacyLandingPagesResource
    meta_fields: MetaFieldsResource
    multimedia: MultimediaResource
    newsletters: NewslettersResource
    orders: OrdersResource
    predefined_fields: PredefinedFieldsResource
    product_variants: ProductVariantsResource
    products: ProductsResource
    rss_newsletters: RssNewslettersResource
    sms_automation_messages: SmsAutomationMessagesResource
    sms_messages: SmsMessagesResource
    search_contacts: SearchContactsResource
    shops: ShopsResource
    sms: SmsResource
    subscription_confirmations: SubscriptionConfirmationsResource
    suppressions: SuppressionsResource
    tags: TagsResource
    taxes: TaxesResource
    tracking: TrackingResource
    transactional_emails: TransactionalEmailsResource
    transactional_emails_templates: TransactionalEmailsTemplatesResource
    webinars: WebinarsResource
    website: WebsiteResource
    websites: WebsitesResource
    workflows: WorkflowsResource

    def _attach_resource_groups(self, core: _Core) -> None:
        self.ab_tests = AbTestsResource(core)
        self.ab_tests_subject = AbTestsSubjectResource(core)
        self.accounts = AccountsResource(core)
        self.addresses = AddressesResource(core)
        self.autoresponders = AutorespondersResource(core)
        self.campaigns_lists = CampaignsListsResource(core)
        self.carts = CartsResource(core)
        self.categories = CategoriesResource(core)
        self.click_tracks = ClickTracksResource(core)
        self.contacts = ContactsResource(core)
        self.custom_events = CustomEventsResource(core)
        self.custom_fields = CustomFieldsResource(core)
        self.custom_reports = CustomReportsResource(core)
        self.ecommerce = EcommerceResource(core)
        self.file_library = FileLibraryResource(core)
        self.form_and_popup = FormAndPopupResource(core)
        self.forms = FormsResource(core)
        self.forms_and_popups = FormsAndPopupsResource(core)
        self.from_fields = FromFieldsResource(core)
        self.gdpr_fields = GdprFieldsResource(core)
        self.imports = ImportsResource(core)
        self.landing_page = LandingPageResource(core)
        self.landing_pages = LandingPagesResource(core)
        self.legacy_forms = LegacyFormsResource(core)
        self.legacy_landing_pages = LegacyLandingPagesResource(core)
        self.meta_fields = MetaFieldsResource(core)
        self.multimedia = MultimediaResource(core)
        self.newsletters = NewslettersResource(core)
        self.orders = OrdersResource(core)
        self.predefined_fields = PredefinedFieldsResource(core)
        self.product_variants = ProductVariantsResource(core)
        self.products = ProductsResource(core)
        self.rss_newsletters = RssNewslettersResource(core)
        self.sms_automation_messages = SmsAutomationMessagesResource(core)
        self.sms_messages = SmsMessagesResource(core)
        self.search_contacts = SearchContactsResource(core)
        self.shops = ShopsResource(core)
        self.sms = SmsResource(core)
        self.subscription_confirmations = SubscriptionConfirmationsResource(core)
        self.suppressions = SuppressionsResource(core)
        self.tags = TagsResource(core)
        self.taxes = TaxesResource(core)
        self.tracking = TrackingResource(core)
        self.transactional_emails = TransactionalEmailsResource(core)
        self.transactional_emails_templates = TransactionalEmailsTemplatesResource(core)
        self.webinars = WebinarsResource(core)
        self.website = WebsiteResource(core)
        self.websites = WebsitesResource(core)
        self.workflows = WorkflowsResource(core)
