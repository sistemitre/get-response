"""Resource-group clients, one per API tag."""

from .ab_tests import AbTestsResource
from .ab_tests_subject import AbTestsSubjectResource
from .accounts import AccountsResource
from .addresses import AddressesResource
from .autoresponders import AutorespondersResource
from .campaigns_lists import CampaignsListsResource
from .carts import CartsResource
from .categories import CategoriesResource
from .click_tracks import ClickTracksResource
from .contacts import ContactsResource
from .custom_events import CustomEventsResource
from .custom_fields import CustomFieldsResource
from .custom_reports import CustomReportsResource
from .ecommerce import EcommerceResource
from .file_library import FileLibraryResource
from .form_and_popup import FormAndPopupResource
from .forms import FormsResource
from .forms_and_popups import FormsAndPopupsResource
from .from_fields import FromFieldsResource
from .gdpr_fields import GdprFieldsResource
from .imports import ImportsResource
from .landing_page import LandingPageResource
from .landing_pages import LandingPagesResource
from .legacy_forms import LegacyFormsResource
from .legacy_landing_pages import LegacyLandingPagesResource
from .meta_fields import MetaFieldsResource
from .multimedia import MultimediaResource
from .newsletters import NewslettersResource
from .orders import OrdersResource
from .predefined_fields import PredefinedFieldsResource
from .product_variants import ProductVariantsResource
from .products import ProductsResource
from .rss_newsletters import RssNewslettersResource
from .search_contacts import SearchContactsResource
from .shops import ShopsResource
from .sms import SmsResource
from .sms_automation_messages import SmsAutomationMessagesResource
from .sms_messages import SmsMessagesResource
from .subscription_confirmations import SubscriptionConfirmationsResource
from .suppressions import SuppressionsResource
from .tags import TagsResource
from .taxes import TaxesResource
from .tracking import TrackingResource
from .transactional_emails import TransactionalEmailsResource
from .transactional_emails_templates import TransactionalEmailsTemplatesResource
from .webinars import WebinarsResource
from .website import WebsiteResource
from .websites import WebsitesResource
from .workflows import WorkflowsResource

__all__ = [
    "AbTestsResource",
    "AbTestsSubjectResource",
    "AccountsResource",
    "AddressesResource",
    "AutorespondersResource",
    "CampaignsListsResource",
    "CartsResource",
    "CategoriesResource",
    "ClickTracksResource",
    "ContactsResource",
    "CustomEventsResource",
    "CustomFieldsResource",
    "CustomReportsResource",
    "EcommerceResource",
    "FileLibraryResource",
    "FormAndPopupResource",
    "FormsResource",
    "FormsAndPopupsResource",
    "FromFieldsResource",
    "GdprFieldsResource",
    "ImportsResource",
    "LandingPageResource",
    "LandingPagesResource",
    "LegacyFormsResource",
    "LegacyLandingPagesResource",
    "MetaFieldsResource",
    "MultimediaResource",
    "NewslettersResource",
    "OrdersResource",
    "PredefinedFieldsResource",
    "ProductVariantsResource",
    "ProductsResource",
    "RssNewslettersResource",
    "SmsAutomationMessagesResource",
    "SmsMessagesResource",
    "SearchContactsResource",
    "ShopsResource",
    "SmsResource",
    "SubscriptionConfirmationsResource",
    "SuppressionsResource",
    "TagsResource",
    "TaxesResource",
    "TrackingResource",
    "TransactionalEmailsResource",
    "TransactionalEmailsTemplatesResource",
    "WebinarsResource",
    "WebsiteResource",
    "WebsitesResource",
    "WorkflowsResource",
]
