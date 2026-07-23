"""Generated data models: every schema in the GetResponse OpenAPI spec.

Enums come first (models may reference them), then models in name order. This
file is generated -- do not edit it directly.
"""

from __future__ import annotations

from datetime import datetime
from typing import Any

from pydantic import BaseModel, ConfigDict, Field

from ._compat import _UnknownFallbackEnum


class AbtestsSubjectDetailsEditor(_UnknownFallbackEnum):
    "The message editor used for the A/B test"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Html2 = "html2"
    Custom = "custom"
    Text = "text"
    EditorV3 = "editor_v3"
    Getresponse = "getresponse"
    Legacy = "legacy"


class AbtestsSubjectDetailsFlagsItem(_UnknownFallbackEnum):
    "Tracking options enabled for the newsletter"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Clicktrack = "clicktrack"
    SubscriptionReminder = "subscription_reminder"
    Openrate = "openrate"
    GoogleAnalytics = "google_analytics"
    ManualList = "manual_list"
    CustomFooter = "custom_footer"
    EcommerceTracking = "ecommerce_tracking"


class AbtestsSubjectDetailsStage(_UnknownFallbackEnum):
    "A/B test stage"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Preparing = "preparing"
    Testing = "testing"
    Finished = "finished"
    SendingWinner = "sending_winner"
    Cancelled = "cancelled"
    Draft = "draft"
    Completed = "completed"


class AbtestsSubjectDetailsStatus(_UnknownFallbackEnum):
    "Newsletter status"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Active = "active"
    Inactive = "inactive"
    Deleted = "deleted"


class AbtestsSubjectListItemFlagsItem(_UnknownFallbackEnum):
    "Tracking options enabled for the newsletter"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Clicktrack = "clicktrack"
    SubscriptionReminder = "subscription_reminder"
    Openrate = "openrate"
    GoogleAnalytics = "google_analytics"
    ManualList = "manual_list"
    CustomFooter = "custom_footer"
    EcommerceTracking = "ecommerce_tracking"


class AbtestsSubjectListItemStage(_UnknownFallbackEnum):
    "A/B test stage"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Preparing = "preparing"
    Testing = "testing"
    Finished = "finished"
    SendingWinner = "sending_winner"
    Cancelled = "cancelled"
    Draft = "draft"
    Completed = "completed"


class AbtestsSubjectListItemStatus(_UnknownFallbackEnum):
    "Newsletter status"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Active = "active"
    Inactive = "inactive"
    Deleted = "deleted"


class AccountBillingPaymentMethod(_UnknownFallbackEnum):
    "Payment method"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    OutsideSystem = "outside_system"
    InsideSystem = "inside_system"
    CreditCard = "credit_card"
    PlatnosciPl = "platnosci_pl"
    DirectDebit = "direct_debit"
    Paypal = "paypal"
    Yandex = "yandex"
    Alipay = "alipay"
    AlipayMobile = "alipay_mobile"
    Boleto = "boleto"
    Ideal = "ideal"
    Qiwi = "qiwi"
    Sofort = "sofort"
    Webmoney = "webmoney"


class AccountBillingPaymentPlan(_UnknownFallbackEnum):
    "Payment plan"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    FreeTrial = "Free Trial"
    Monthly = "Monthly"
    V_12Months = "12 Months"
    V_24Months = "24 Months"


class AccountNumberOfEmployees(_UnknownFallbackEnum):
    "Numbers of employees"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    V_50 = "50"
    V_250 = "250"
    V_500 = "500"
    More = "more"


class AccountTimeFormat(_UnknownFallbackEnum):
    "Account time notation"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    V_12h = "12h"
    V_24h = "24h"


class AutoresponderDayConditionConditionType(_UnknownFallbackEnum):
    "AutoresponderDayConditionConditionType enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Name = "name"
    Email = "email"
    Custom = "custom"
    SubscriptionDate = "subscription_date"
    SubscriptionMethod = "subscription_method"
    Opened = "opened"
    NotOpened = "not_opened"
    Phase = "phase"
    LastSendDate = "last_send_date"
    LastClickDate = "last_click_date"
    LastOpenDate = "last_open_date"
    Webinar = "webinar"
    Clicked = "clicked"
    NotClicked = "not_clicked"
    Sent = "sent"
    NotSent = "not_sent"
    Geo = "geo"
    Gdpr = "gdpr"
    Score = "score"
    EngagementScore = "engagement_score"
    Tag = "tag"
    Goal = "goal"
    Crm = "crm"
    EcommerceNumberOfPurchases = "ecommerce_number_of_purchases"
    EcommerceTotalSpent = "ecommerce_total_spent"
    EcommerceProductPurchased = "ecommerce_product_purchased"
    EcommerceBrandPurchased = "ecommerce_brand_purchased"
    EcommerceAbandonedCart = "ecommerce_abandoned_cart"
    SmsSent = "sms_sent"
    SmsLinkClicked = "sms_link_clicked"
    SmsLinkNotClicked = "sms_link_not_clicked"
    CustomEvent = "custom_event"


class AutoresponderDayConditionOperatorType(_UnknownFallbackEnum):
    "AutoresponderDayConditionOperatorType enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    NumericOperator = "numeric_operator"


class AutoresponderSendSettingsExcludedDaysOfWeekItem(_UnknownFallbackEnum):
    "AutoresponderSendSettingsExcludedDaysOfWeekItem enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Monday = "Monday"
    Tuesday = "Tuesday"
    Wednesday = "Wednesday"
    Thursday = "Thursday"
    Friday = "Friday"
    Saturday = "Saturday"
    Sunday = "Sunday"


class AutoresponderSendSettingsType(_UnknownFallbackEnum):
    "When to send the message"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Signup = "signup"
    Immediately = "immediately"
    Delay = "delay"
    Custom = "custom"


class BaseCreateCustomReportType(_UnknownFallbackEnum):
    "The custom report type"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    SubscriptionRejections = "subscription_rejections"
    MessageStats = "message_stats"
    UnsubscribeContactsListsReport = "unsubscribe_contacts_lists_report"
    StandardSubscriberActivityReport = "standard_subscriber_activity_report"
    Bounces = "bounces"
    AccountSummaryReport = "account_summary_report"
    UserActivity = "user_activity"
    ListSummaryReport = "list_summary_report"
    IspMessageStatsReport = "isp_message_stats_report"
    WebinarParticipantsReport = "webinar_participants_report"
    ImportErrorReport = "import_error_report"
    MessageClicksReport = "message_clicks_report"
    UnconfirmedContactsStatsReport = "unconfirmed_contacts_stats_report"
    TransactionalEmailBounceReport = "transactional_email_bounce_report"
    MessageActivityReport = "message_activity_report"


class BaseLandingPageUserDomainStatus(_UnknownFallbackEnum):
    "The DNS status for the user's private domain. Can be `null` if a private domain isn't assigned."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Active = "active"
    Inactive = "inactive"
    Waiting = "waiting"


class BaseMetaFieldValueType(_UnknownFallbackEnum):
    "The value type enumerable"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    String = "string"
    Integer = "integer"


class BaseSendSmsRecipientsType(_UnknownFallbackEnum):
    "The recipient type. To send a text message to contacts in your list, select `contacts`. To message contacts who are not in any of your lists, select `importedNumbers`"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Contacts = "contacts"
    Importednumbers = "importedNumbers"


class CampaignConfirmationMimeType(_UnknownFallbackEnum):
    "The MIME type for the confirmation message"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    TextHtml = "text/html"
    TextPlain = "text/plain"
    Combo = "combo"


class CampaignConfirmationRedirectType(_UnknownFallbackEnum):
    "What will happen after email confirmation. The values allowed include: hosted (the subscriber will stay on the default GetResponse website), customUrl (the subscriber will be redirected to a custom URL provided by the user)."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Hosted = "hosted"
    Customurl = "customUrl"


class CampaignOptinTypesApi(_UnknownFallbackEnum):
    "Single opt-in: confirmed opt-in disabled. Double opt-in: confirmed opt-in enabled. You can find more information [here](https://www.getresponse.com/resources/glossary/confirmed-opt-in.html)"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Single = "single"
    Double = "double"


class CampaignOptinTypesEmail(_UnknownFallbackEnum):
    "Single opt-in: confirmed opt-in disabled. Double opt-in: confirmed opt-in enabled. You can find more information [here](https://www.getresponse.com/resources/glossary/confirmed-opt-in.html)"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Single = "single"
    Double = "double"


class CampaignOptinTypesImport(_UnknownFallbackEnum):
    "Single opt-in: confirmed opt-in disabled. Double opt-in: confirmed opt-in enabled. You can find more information [here](https://www.getresponse.com/resources/glossary/confirmed-opt-in.html)"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Single = "single"


class CampaignOptinTypesWebform(_UnknownFallbackEnum):
    "Single opt-in: confirmed opt-in disabled. Double opt-in: confirmed opt-in enabled. You can find more information [here](https://www.getresponse.com/resources/glossary/confirmed-opt-in.html)"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Single = "single"
    Double = "double"


class ClickTrackMessageResourceType(_UnknownFallbackEnum):
    "Type of the resource that represents the message in the API"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Newsletters = "newsletters"
    Autoresponders = "autoresponders"
    RssNewsletters = "rss-newsletters"
    Splittests = "splittests"
    Sms = "sms"


class ClickTrackMessageType(_UnknownFallbackEnum):
    "The message type"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Broadcast = "broadcast"
    Automation = "automation"
    Autoresponder = "autoresponder"
    Rss = "rss"
    Splittest = "splittest"
    Sms = "sms"


class ConditionMessageOperatorOperatorType(_UnknownFallbackEnum):
    "ConditionMessageOperatorOperatorType enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    MessageOperator = "message_operator"


class ConditionStringOperatorOperator(_UnknownFallbackEnum):
    "ConditionStringOperatorOperator enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Is = "is"
    IsNot = "is_not"
    Contains = "contains"
    NotContains = "not_contains"
    Starts = "starts"
    Ends = "ends"
    NotStarts = "not_starts"
    NotEnds = "not_ends"


class ConditionStringOperatorOperatorType(_UnknownFallbackEnum):
    "ConditionStringOperatorOperatorType enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    StringOperator = "string_operator"


class ConditionTypeConditionType(_UnknownFallbackEnum):
    "ConditionTypeConditionType enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Name = "name"
    Email = "email"
    Custom = "custom"
    SubscriptionDate = "subscription_date"
    SubscriptionMethod = "subscription_method"
    Opened = "opened"
    NotOpened = "not_opened"
    Phase = "phase"
    LastSendDate = "last_send_date"
    LastClickDate = "last_click_date"
    LastOpenDate = "last_open_date"
    Webinar = "webinar"
    Clicked = "clicked"
    NotClicked = "not_clicked"
    Sent = "sent"
    NotSent = "not_sent"
    Geo = "geo"
    Gdpr = "gdpr"
    Score = "score"
    EngagementScore = "engagement_score"
    Tag = "tag"
    Goal = "goal"
    Crm = "crm"
    EcommerceNumberOfPurchases = "ecommerce_number_of_purchases"
    EcommerceTotalSpent = "ecommerce_total_spent"
    EcommerceProductPurchased = "ecommerce_product_purchased"
    EcommerceBrandPurchased = "ecommerce_brand_purchased"
    EcommerceAbandonedCart = "ecommerce_abandoned_cart"
    SmsSent = "sms_sent"
    SmsLinkClicked = "sms_link_clicked"
    SmsLinkNotClicked = "sms_link_not_clicked"
    CustomEvent = "custom_event"


class ContactActivityActivity(_UnknownFallbackEnum):
    "The type of activity"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Send = "send"
    Open = "open"
    Click = "click"


class ContactActivityResourceResourceType(_UnknownFallbackEnum):
    "ContactActivityResourceResourceType enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Newsletters = "newsletters"
    Splittests = "splittests"
    Autoresponders = "autoresponders"
    RssNewsletters = "rss-newsletters"
    Sms = "sms"


class ContactDetailsOrigin(_UnknownFallbackEnum):
    "ContactDetailsOrigin enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Import = "import"
    Email = "email"
    Www = "www"
    Panel = "panel"
    Leads = "leads"
    Sale = "sale"
    Api = "api"
    Survey = "survey"
    Iphone = "iphone"
    Copy = "copy"
    LandingPage = "landing_page"
    Webinar = "webinar"
    WebsiteBuilderElegant = "website_builder_elegant"
    Chat = "chat"
    Course = "course"
    PremiumNewsletter = "premium_newsletter"


class ContactGeolocationContinentCode(_UnknownFallbackEnum):
    "ContactGeolocationContinentCode enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Oc = "OC"
    An = "AN"
    Sa = "SA"
    Na = "NA"
    As = "AS"
    Eu = "EU"
    Af = "AF"


class ContactListElementOrigin(_UnknownFallbackEnum):
    "ContactListElementOrigin enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Import = "import"
    Email = "email"
    Www = "www"
    Panel = "panel"
    Leads = "leads"
    Sale = "sale"
    Api = "api"
    Survey = "survey"
    Iphone = "iphone"
    Copy = "copy"
    LandingPage = "landing_page"
    Webinar = "webinar"
    WebsiteBuilderElegant = "website_builder_elegant"
    Chat = "chat"
    Course = "course"
    PremiumNewsletter = "premium_newsletter"


class ContactOrigin(_UnknownFallbackEnum):
    "ContactOrigin enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Import = "import"
    Email = "email"
    Www = "www"
    Panel = "panel"
    Leads = "leads"
    Sale = "sale"
    Api = "api"
    Survey = "survey"
    Iphone = "iphone"
    Copy = "copy"
    LandingPage = "landing_page"
    Webinar = "webinar"
    WebsiteBuilderElegant = "website_builder_elegant"
    Chat = "chat"
    Course = "course"
    PremiumNewsletter = "premium_newsletter"


class CreateAccountSummaryReportType(_UnknownFallbackEnum):
    "The custom report type"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    SubscriptionRejections = "subscription_rejections"
    MessageStats = "message_stats"
    UnsubscribeContactsListsReport = "unsubscribe_contacts_lists_report"
    StandardSubscriberActivityReport = "standard_subscriber_activity_report"
    Bounces = "bounces"
    AccountSummaryReport = "account_summary_report"
    UserActivity = "user_activity"
    ListSummaryReport = "list_summary_report"
    IspMessageStatsReport = "isp_message_stats_report"
    WebinarParticipantsReport = "webinar_participants_report"
    ImportErrorReport = "import_error_report"
    MessageClicksReport = "message_clicks_report"
    UnconfirmedContactsStatsReport = "unconfirmed_contacts_stats_report"
    TransactionalEmailBounceReport = "transactional_email_bounce_report"
    MessageActivityReport = "message_activity_report"


class CreateBouncesReportType(_UnknownFallbackEnum):
    "The custom report type"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    SubscriptionRejections = "subscription_rejections"
    MessageStats = "message_stats"
    UnsubscribeContactsListsReport = "unsubscribe_contacts_lists_report"
    StandardSubscriberActivityReport = "standard_subscriber_activity_report"
    Bounces = "bounces"
    AccountSummaryReport = "account_summary_report"
    UserActivity = "user_activity"
    ListSummaryReport = "list_summary_report"
    IspMessageStatsReport = "isp_message_stats_report"
    WebinarParticipantsReport = "webinar_participants_report"
    ImportErrorReport = "import_error_report"
    MessageClicksReport = "message_clicks_report"
    UnconfirmedContactsStatsReport = "unconfirmed_contacts_stats_report"
    TransactionalEmailBounceReport = "transactional_email_bounce_report"
    MessageActivityReport = "message_activity_report"


class CreateISPMessageStatsReportType(_UnknownFallbackEnum):
    "The custom report type"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    SubscriptionRejections = "subscription_rejections"
    MessageStats = "message_stats"
    UnsubscribeContactsListsReport = "unsubscribe_contacts_lists_report"
    StandardSubscriberActivityReport = "standard_subscriber_activity_report"
    Bounces = "bounces"
    AccountSummaryReport = "account_summary_report"
    UserActivity = "user_activity"
    ListSummaryReport = "list_summary_report"
    IspMessageStatsReport = "isp_message_stats_report"
    WebinarParticipantsReport = "webinar_participants_report"
    ImportErrorReport = "import_error_report"
    MessageClicksReport = "message_clicks_report"
    UnconfirmedContactsStatsReport = "unconfirmed_contacts_stats_report"
    TransactionalEmailBounceReport = "transactional_email_bounce_report"
    MessageActivityReport = "message_activity_report"


class CreateImportErrorReportType(_UnknownFallbackEnum):
    "The custom report type"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    SubscriptionRejections = "subscription_rejections"
    MessageStats = "message_stats"
    UnsubscribeContactsListsReport = "unsubscribe_contacts_lists_report"
    StandardSubscriberActivityReport = "standard_subscriber_activity_report"
    Bounces = "bounces"
    AccountSummaryReport = "account_summary_report"
    UserActivity = "user_activity"
    ListSummaryReport = "list_summary_report"
    IspMessageStatsReport = "isp_message_stats_report"
    WebinarParticipantsReport = "webinar_participants_report"
    ImportErrorReport = "import_error_report"
    MessageClicksReport = "message_clicks_report"
    UnconfirmedContactsStatsReport = "unconfirmed_contacts_stats_report"
    TransactionalEmailBounceReport = "transactional_email_bounce_report"
    MessageActivityReport = "message_activity_report"


class CreateListSummaryReportType(_UnknownFallbackEnum):
    "The custom report type"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    SubscriptionRejections = "subscription_rejections"
    MessageStats = "message_stats"
    UnsubscribeContactsListsReport = "unsubscribe_contacts_lists_report"
    StandardSubscriberActivityReport = "standard_subscriber_activity_report"
    Bounces = "bounces"
    AccountSummaryReport = "account_summary_report"
    UserActivity = "user_activity"
    ListSummaryReport = "list_summary_report"
    IspMessageStatsReport = "isp_message_stats_report"
    WebinarParticipantsReport = "webinar_participants_report"
    ImportErrorReport = "import_error_report"
    MessageClicksReport = "message_clicks_report"
    UnconfirmedContactsStatsReport = "unconfirmed_contacts_stats_report"
    TransactionalEmailBounceReport = "transactional_email_bounce_report"
    MessageActivityReport = "message_activity_report"


class CreateMessageActivityReportType(_UnknownFallbackEnum):
    "The custom report type"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    SubscriptionRejections = "subscription_rejections"
    MessageStats = "message_stats"
    UnsubscribeContactsListsReport = "unsubscribe_contacts_lists_report"
    StandardSubscriberActivityReport = "standard_subscriber_activity_report"
    Bounces = "bounces"
    AccountSummaryReport = "account_summary_report"
    UserActivity = "user_activity"
    ListSummaryReport = "list_summary_report"
    IspMessageStatsReport = "isp_message_stats_report"
    WebinarParticipantsReport = "webinar_participants_report"
    ImportErrorReport = "import_error_report"
    MessageClicksReport = "message_clicks_report"
    UnconfirmedContactsStatsReport = "unconfirmed_contacts_stats_report"
    TransactionalEmailBounceReport = "transactional_email_bounce_report"
    MessageActivityReport = "message_activity_report"


class CreateMessageClicksReportType(_UnknownFallbackEnum):
    "The custom report type"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    SubscriptionRejections = "subscription_rejections"
    MessageStats = "message_stats"
    UnsubscribeContactsListsReport = "unsubscribe_contacts_lists_report"
    StandardSubscriberActivityReport = "standard_subscriber_activity_report"
    Bounces = "bounces"
    AccountSummaryReport = "account_summary_report"
    UserActivity = "user_activity"
    ListSummaryReport = "list_summary_report"
    IspMessageStatsReport = "isp_message_stats_report"
    WebinarParticipantsReport = "webinar_participants_report"
    ImportErrorReport = "import_error_report"
    MessageClicksReport = "message_clicks_report"
    UnconfirmedContactsStatsReport = "unconfirmed_contacts_stats_report"
    TransactionalEmailBounceReport = "transactional_email_bounce_report"
    MessageActivityReport = "message_activity_report"


class CreateMessageStatsReportType(_UnknownFallbackEnum):
    "The custom report type"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    SubscriptionRejections = "subscription_rejections"
    MessageStats = "message_stats"
    UnsubscribeContactsListsReport = "unsubscribe_contacts_lists_report"
    StandardSubscriberActivityReport = "standard_subscriber_activity_report"
    Bounces = "bounces"
    AccountSummaryReport = "account_summary_report"
    UserActivity = "user_activity"
    ListSummaryReport = "list_summary_report"
    IspMessageStatsReport = "isp_message_stats_report"
    WebinarParticipantsReport = "webinar_participants_report"
    ImportErrorReport = "import_error_report"
    MessageClicksReport = "message_clicks_report"
    UnconfirmedContactsStatsReport = "unconfirmed_contacts_stats_report"
    TransactionalEmailBounceReport = "transactional_email_bounce_report"
    MessageActivityReport = "message_activity_report"


class CreateStandardSubscriberActivityReportType(_UnknownFallbackEnum):
    "The custom report type"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    SubscriptionRejections = "subscription_rejections"
    MessageStats = "message_stats"
    UnsubscribeContactsListsReport = "unsubscribe_contacts_lists_report"
    StandardSubscriberActivityReport = "standard_subscriber_activity_report"
    Bounces = "bounces"
    AccountSummaryReport = "account_summary_report"
    UserActivity = "user_activity"
    ListSummaryReport = "list_summary_report"
    IspMessageStatsReport = "isp_message_stats_report"
    WebinarParticipantsReport = "webinar_participants_report"
    ImportErrorReport = "import_error_report"
    MessageClicksReport = "message_clicks_report"
    UnconfirmedContactsStatsReport = "unconfirmed_contacts_stats_report"
    TransactionalEmailBounceReport = "transactional_email_bounce_report"
    MessageActivityReport = "message_activity_report"


class CreateSubscriptionRejectionsReportType(_UnknownFallbackEnum):
    "The custom report type"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    SubscriptionRejections = "subscription_rejections"
    MessageStats = "message_stats"
    UnsubscribeContactsListsReport = "unsubscribe_contacts_lists_report"
    StandardSubscriberActivityReport = "standard_subscriber_activity_report"
    Bounces = "bounces"
    AccountSummaryReport = "account_summary_report"
    UserActivity = "user_activity"
    ListSummaryReport = "list_summary_report"
    IspMessageStatsReport = "isp_message_stats_report"
    WebinarParticipantsReport = "webinar_participants_report"
    ImportErrorReport = "import_error_report"
    MessageClicksReport = "message_clicks_report"
    UnconfirmedContactsStatsReport = "unconfirmed_contacts_stats_report"
    TransactionalEmailBounceReport = "transactional_email_bounce_report"
    MessageActivityReport = "message_activity_report"


class CreateTransactionalEmailBounceReportType(_UnknownFallbackEnum):
    "The custom report type"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    SubscriptionRejections = "subscription_rejections"
    MessageStats = "message_stats"
    UnsubscribeContactsListsReport = "unsubscribe_contacts_lists_report"
    StandardSubscriberActivityReport = "standard_subscriber_activity_report"
    Bounces = "bounces"
    AccountSummaryReport = "account_summary_report"
    UserActivity = "user_activity"
    ListSummaryReport = "list_summary_report"
    IspMessageStatsReport = "isp_message_stats_report"
    WebinarParticipantsReport = "webinar_participants_report"
    ImportErrorReport = "import_error_report"
    MessageClicksReport = "message_clicks_report"
    UnconfirmedContactsStatsReport = "unconfirmed_contacts_stats_report"
    TransactionalEmailBounceReport = "transactional_email_bounce_report"
    MessageActivityReport = "message_activity_report"


class CreateTransactionalEmailContentType(_UnknownFallbackEnum):
    "The message content type"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Direct = "direct"
    Template = "template"


class CreateUnconfirmedContactsStatsReportType(_UnknownFallbackEnum):
    "The custom report type"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    SubscriptionRejections = "subscription_rejections"
    MessageStats = "message_stats"
    UnsubscribeContactsListsReport = "unsubscribe_contacts_lists_report"
    StandardSubscriberActivityReport = "standard_subscriber_activity_report"
    Bounces = "bounces"
    AccountSummaryReport = "account_summary_report"
    UserActivity = "user_activity"
    ListSummaryReport = "list_summary_report"
    IspMessageStatsReport = "isp_message_stats_report"
    WebinarParticipantsReport = "webinar_participants_report"
    ImportErrorReport = "import_error_report"
    MessageClicksReport = "message_clicks_report"
    UnconfirmedContactsStatsReport = "unconfirmed_contacts_stats_report"
    TransactionalEmailBounceReport = "transactional_email_bounce_report"
    MessageActivityReport = "message_activity_report"


class CreateUnsubscribeContactsListsReportType(_UnknownFallbackEnum):
    "The custom report type"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    SubscriptionRejections = "subscription_rejections"
    MessageStats = "message_stats"
    UnsubscribeContactsListsReport = "unsubscribe_contacts_lists_report"
    StandardSubscriberActivityReport = "standard_subscriber_activity_report"
    Bounces = "bounces"
    AccountSummaryReport = "account_summary_report"
    UserActivity = "user_activity"
    ListSummaryReport = "list_summary_report"
    IspMessageStatsReport = "isp_message_stats_report"
    WebinarParticipantsReport = "webinar_participants_report"
    ImportErrorReport = "import_error_report"
    MessageClicksReport = "message_clicks_report"
    UnconfirmedContactsStatsReport = "unconfirmed_contacts_stats_report"
    TransactionalEmailBounceReport = "transactional_email_bounce_report"
    MessageActivityReport = "message_activity_report"


class CreateUserActivityReportType(_UnknownFallbackEnum):
    "The custom report type"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    SubscriptionRejections = "subscription_rejections"
    MessageStats = "message_stats"
    UnsubscribeContactsListsReport = "unsubscribe_contacts_lists_report"
    StandardSubscriberActivityReport = "standard_subscriber_activity_report"
    Bounces = "bounces"
    AccountSummaryReport = "account_summary_report"
    UserActivity = "user_activity"
    ListSummaryReport = "list_summary_report"
    IspMessageStatsReport = "isp_message_stats_report"
    WebinarParticipantsReport = "webinar_participants_report"
    ImportErrorReport = "import_error_report"
    MessageClicksReport = "message_clicks_report"
    UnconfirmedContactsStatsReport = "unconfirmed_contacts_stats_report"
    TransactionalEmailBounceReport = "transactional_email_bounce_report"
    MessageActivityReport = "message_activity_report"


class CreateWebinarParticipantsReportType(_UnknownFallbackEnum):
    "The custom report type"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    SubscriptionRejections = "subscription_rejections"
    MessageStats = "message_stats"
    UnsubscribeContactsListsReport = "unsubscribe_contacts_lists_report"
    StandardSubscriberActivityReport = "standard_subscriber_activity_report"
    Bounces = "bounces"
    AccountSummaryReport = "account_summary_report"
    UserActivity = "user_activity"
    ListSummaryReport = "list_summary_report"
    IspMessageStatsReport = "isp_message_stats_report"
    WebinarParticipantsReport = "webinar_participants_report"
    ImportErrorReport = "import_error_report"
    MessageClicksReport = "message_clicks_report"
    UnconfirmedContactsStatsReport = "unconfirmed_contacts_stats_report"
    TransactionalEmailBounceReport = "transactional_email_bounce_report"
    MessageActivityReport = "message_activity_report"


class CrmConditionConditionType(_UnknownFallbackEnum):
    "CrmConditionConditionType enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Name = "name"
    Email = "email"
    Custom = "custom"
    SubscriptionDate = "subscription_date"
    SubscriptionMethod = "subscription_method"
    Opened = "opened"
    NotOpened = "not_opened"
    Phase = "phase"
    LastSendDate = "last_send_date"
    LastClickDate = "last_click_date"
    LastOpenDate = "last_open_date"
    Webinar = "webinar"
    Clicked = "clicked"
    NotClicked = "not_clicked"
    Sent = "sent"
    NotSent = "not_sent"
    Geo = "geo"
    Gdpr = "gdpr"
    Score = "score"
    EngagementScore = "engagement_score"
    Tag = "tag"
    Goal = "goal"
    Crm = "crm"
    EcommerceNumberOfPurchases = "ecommerce_number_of_purchases"
    EcommerceTotalSpent = "ecommerce_total_spent"
    EcommerceProductPurchased = "ecommerce_product_purchased"
    EcommerceBrandPurchased = "ecommerce_brand_purchased"
    EcommerceAbandonedCart = "ecommerce_abandoned_cart"
    SmsSent = "sms_sent"
    SmsLinkClicked = "sms_link_clicked"
    SmsLinkNotClicked = "sms_link_not_clicked"
    CustomEvent = "custom_event"


class CustomEventAttributeDetailsType(_UnknownFallbackEnum):
    "Type of attribute"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    String = "string"
    Number = "number"
    Datetime = "datetime"
    Boolean = "boolean"


class CustomEventAttributeType(_UnknownFallbackEnum):
    "Type of attribute"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    String = "string"
    Number = "number"
    Datetime = "datetime"
    Boolean = "boolean"


class CustomEventConditionConditionType(_UnknownFallbackEnum):
    "CustomEventConditionConditionType enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Name = "name"
    Email = "email"
    Custom = "custom"
    SubscriptionDate = "subscription_date"
    SubscriptionMethod = "subscription_method"
    Opened = "opened"
    NotOpened = "not_opened"
    Phase = "phase"
    LastSendDate = "last_send_date"
    LastClickDate = "last_click_date"
    LastOpenDate = "last_open_date"
    Webinar = "webinar"
    Clicked = "clicked"
    NotClicked = "not_clicked"
    Sent = "sent"
    NotSent = "not_sent"
    Geo = "geo"
    Gdpr = "gdpr"
    Score = "score"
    EngagementScore = "engagement_score"
    Tag = "tag"
    Goal = "goal"
    Crm = "crm"
    EcommerceNumberOfPurchases = "ecommerce_number_of_purchases"
    EcommerceTotalSpent = "ecommerce_total_spent"
    EcommerceProductPurchased = "ecommerce_product_purchased"
    EcommerceBrandPurchased = "ecommerce_brand_purchased"
    EcommerceAbandonedCart = "ecommerce_abandoned_cart"
    SmsSent = "sms_sent"
    SmsLinkClicked = "sms_link_clicked"
    SmsLinkNotClicked = "sms_link_not_clicked"
    CustomEvent = "custom_event"


class CustomEventConditionOccurrence(_UnknownFallbackEnum):
    "Whether the custom event occurred or not"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Occurred = "occurred"
    NotOccurred = "not_occurred"


class CustomFieldConditionConditionType(_UnknownFallbackEnum):
    "CustomFieldConditionConditionType enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Name = "name"
    Email = "email"
    Custom = "custom"
    SubscriptionDate = "subscription_date"
    SubscriptionMethod = "subscription_method"
    Opened = "opened"
    NotOpened = "not_opened"
    Phase = "phase"
    LastSendDate = "last_send_date"
    LastClickDate = "last_click_date"
    LastOpenDate = "last_open_date"
    Webinar = "webinar"
    Clicked = "clicked"
    NotClicked = "not_clicked"
    Sent = "sent"
    NotSent = "not_sent"
    Geo = "geo"
    Gdpr = "gdpr"
    Score = "score"
    EngagementScore = "engagement_score"
    Tag = "tag"
    Goal = "goal"
    Crm = "crm"
    EcommerceNumberOfPurchases = "ecommerce_number_of_purchases"
    EcommerceTotalSpent = "ecommerce_total_spent"
    EcommerceProductPurchased = "ecommerce_product_purchased"
    EcommerceBrandPurchased = "ecommerce_brand_purchased"
    EcommerceAbandonedCart = "ecommerce_abandoned_cart"
    SmsSent = "sms_sent"
    SmsLinkClicked = "sms_link_clicked"
    SmsLinkNotClicked = "sms_link_not_clicked"
    CustomEvent = "custom_event"


class CustomFieldConditionOperatorType(_UnknownFallbackEnum):
    "Depends on the type of custom field, read more in [custom field condition documentation in segments (search contacts) reference manual](https://apidocs.getresponse.com/v3/case-study/segments-manual#get-by-custom-fields-search-contacts)"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    StringOperatorList = "string_operator_list"
    StringOperator = "string_operator"
    NumericOperator = "numeric_operator"
    DateOperator = "date_operator"


class CustomFieldDateOperatorEnum(_UnknownFallbackEnum):
    'Allowed operators for `"operatorType":"date_operator"`'

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    DateTo = "date_to"
    DateFrom = "date_from"
    Custom = "custom"
    SpecificDate = "specific_date"
    Assigned = "assigned"
    NotAssigned = "not_assigned"


class CustomFieldFormatEnum(_UnknownFallbackEnum):
    "CustomFieldFormatEnum enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Text = "text"
    Textarea = "textarea"
    Radio = "radio"
    Checkbox = "checkbox"
    SingleSelect = "single_select"
    MultiSelect = "multi_select"


class CustomFieldNumericOperatorEnum(_UnknownFallbackEnum):
    'Allowed operators for `"operatorType":"numeric_operator"`'

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    NumericLt = "numeric_lt"
    NumericGt = "numeric_gt"
    NumericEq = "numeric_eq"
    NumericNotEq = "numeric_not_eq"
    NumericLtEq = "numeric_lt_eq"
    NumericGtEq = "numeric_gt_eq"
    Assigned = "assigned'"
    NotAssigned = "not_assigned"


class CustomFieldStringOperatorEnum(_UnknownFallbackEnum):
    'Allowed operators for `"operatorType":"string_operator"` and `"operatorType":"string_operator_list"`'

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Is = "is"
    IsNot = "is_not"
    Contains = "contains"
    NotContains = "not_contains"
    Starts = "starts"
    Ends = "ends"
    NotStarts = "not_starts"
    NotEnds = "not_ends"
    Assigned = "assigned"
    NotAssigned = "not_assigned"


class CustomFieldTypeEnum(_UnknownFallbackEnum):
    "CustomFieldTypeEnum enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    String = "string"
    Number = "number"
    Date = "date"
    Datetime = "datetime"
    Country = "country"
    Currency = "currency"
    Phone = "phone"
    Gender = "gender"
    Ip = "ip"
    Url = "url"


class CustomFieldValueForOperatorTypeDateAndOperatorSpecificDate(_UnknownFallbackEnum):
    'Allowed values for `"operatorType":"date_operator"` with `"operator":"specific_date"`'

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Today = "today"
    Yesterday = "yesterday"
    Last7Days = "last_7_days"
    Last30Days = "last_30_days"
    LastNDays = "last_n_days"
    ThisWeek = "this_week"
    LastWeek = "last_week"
    ThisMonth = "this_month"
    LastMonth = "last_month"
    Last2Months = "last_2_months"


class CustomFieldValueType(_UnknownFallbackEnum):
    "Type of returning value, it returns `type` options extended by a `string` option if the `format` was not defined"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    String = "string"
    Number = "number"
    Date = "date"
    Datetime = "datetime"
    Country = "country"
    Currency = "currency"
    Phone = "phone"
    Gender = "gender"
    Ip = "ip"
    Url = "url"


class CustomReportDaysOfWeekEnum(_UnknownFallbackEnum):
    "CustomReportDaysOfWeekEnum enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Monday = "monday"
    Tuesday = "tuesday"
    Wednesday = "wednesday"
    Thursday = "thursday"
    Friday = "friday"
    Saturday = "saturday"
    Sunday = "sunday"


class CustomReportFileStatusesEnum(_UnknownFallbackEnum):
    "CustomReportFileStatusesEnum enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Pending = "pending"
    InProgress = "in-progress"
    Ready = "ready"
    Error = "error"


class CustomReportFrequenciesEnum(_UnknownFallbackEnum):
    "CustomReportFrequenciesEnum enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Monthly = "monthly"
    Weekly = "weekly"
    Daily = "daily"
    OneTime = "one_time"


class CustomReportTypesEnum(_UnknownFallbackEnum):
    "CustomReportTypesEnum enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    SubscriptionRejections = "subscription_rejections"
    MessageStats = "message_stats"
    UnsubscribeContactsListsReport = "unsubscribe_contacts_lists_report"
    StandardSubscriberActivityReport = "standard_subscriber_activity_report"
    Bounces = "bounces"
    AccountSummaryReport = "account_summary_report"
    UserActivity = "user_activity"
    ListSummaryReport = "list_summary_report"
    IspMessageStatsReport = "isp_message_stats_report"
    WebinarParticipantsReport = "webinar_participants_report"
    ImportErrorReport = "import_error_report"
    MessageClicksReport = "message_clicks_report"
    UnconfirmedContactsStatsReport = "unconfirmed_contacts_stats_report"
    TransactionalEmailBounceReport = "transactional_email_bounce_report"
    MessageActivityReport = "message_activity_report"


class DirectContentContentType(_UnknownFallbackEnum):
    "The message content type"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Direct = "direct"
    Template = "template"


class ECommerceAbandonedCartConditionConditionType(_UnknownFallbackEnum):
    "ECommerceAbandonedCartConditionConditionType enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Name = "name"
    Email = "email"
    Custom = "custom"
    SubscriptionDate = "subscription_date"
    SubscriptionMethod = "subscription_method"
    Opened = "opened"
    NotOpened = "not_opened"
    Phase = "phase"
    LastSendDate = "last_send_date"
    LastClickDate = "last_click_date"
    LastOpenDate = "last_open_date"
    Webinar = "webinar"
    Clicked = "clicked"
    NotClicked = "not_clicked"
    Sent = "sent"
    NotSent = "not_sent"
    Geo = "geo"
    Gdpr = "gdpr"
    Score = "score"
    EngagementScore = "engagement_score"
    Tag = "tag"
    Goal = "goal"
    Crm = "crm"
    EcommerceNumberOfPurchases = "ecommerce_number_of_purchases"
    EcommerceTotalSpent = "ecommerce_total_spent"
    EcommerceProductPurchased = "ecommerce_product_purchased"
    EcommerceBrandPurchased = "ecommerce_brand_purchased"
    EcommerceAbandonedCart = "ecommerce_abandoned_cart"
    SmsSent = "sms_sent"
    SmsLinkClicked = "sms_link_clicked"
    SmsLinkNotClicked = "sms_link_not_clicked"
    CustomEvent = "custom_event"


class ECommerceAbandonedCartConditionDateOperator(_UnknownFallbackEnum):
    "Set a date range. For the date_from and last_n_days, custom field value is required. Examples can be found here: [API Docs](https://apidocs.getresponse.com/v3/case-study/segments-manual/#ecommerce-abandoned-cart-condition-type)."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    DateFrom = "date_from"
    Anytime = "anytime"
    Never = "never"
    Today = "today"
    Yesterday = "yesterday"
    LastNDays = "last_n_days"
    ThisWeek = "this_week"
    LastWeek = "last_week"
    ThisMonth = "this_month"
    LastMonth = "last_month"
    Custom = "custom"


class ECommerceBrandPurchasedConditionConditionType(_UnknownFallbackEnum):
    "ECommerceBrandPurchasedConditionConditionType enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Name = "name"
    Email = "email"
    Custom = "custom"
    SubscriptionDate = "subscription_date"
    SubscriptionMethod = "subscription_method"
    Opened = "opened"
    NotOpened = "not_opened"
    Phase = "phase"
    LastSendDate = "last_send_date"
    LastClickDate = "last_click_date"
    LastOpenDate = "last_open_date"
    Webinar = "webinar"
    Clicked = "clicked"
    NotClicked = "not_clicked"
    Sent = "sent"
    NotSent = "not_sent"
    Geo = "geo"
    Gdpr = "gdpr"
    Score = "score"
    EngagementScore = "engagement_score"
    Tag = "tag"
    Goal = "goal"
    Crm = "crm"
    EcommerceNumberOfPurchases = "ecommerce_number_of_purchases"
    EcommerceTotalSpent = "ecommerce_total_spent"
    EcommerceProductPurchased = "ecommerce_product_purchased"
    EcommerceBrandPurchased = "ecommerce_brand_purchased"
    EcommerceAbandonedCart = "ecommerce_abandoned_cart"
    SmsSent = "sms_sent"
    SmsLinkClicked = "sms_link_clicked"
    SmsLinkNotClicked = "sms_link_not_clicked"
    CustomEvent = "custom_event"


class ECommerceBrandPurchasedConditionOperator(_UnknownFallbackEnum):
    "ECommerceBrandPurchasedConditionOperator enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Is = "is"
    NotIs = "not_is"


class ECommerceBrandPurchasedConditionOperatorType(_UnknownFallbackEnum):
    "ECommerceBrandPurchasedConditionOperatorType enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    EqualOperator = "equal_operator"


class ECommerceNumberOfPurchasesConditionConditionType(_UnknownFallbackEnum):
    "ECommerceNumberOfPurchasesConditionConditionType enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Name = "name"
    Email = "email"
    Custom = "custom"
    SubscriptionDate = "subscription_date"
    SubscriptionMethod = "subscription_method"
    Opened = "opened"
    NotOpened = "not_opened"
    Phase = "phase"
    LastSendDate = "last_send_date"
    LastClickDate = "last_click_date"
    LastOpenDate = "last_open_date"
    Webinar = "webinar"
    Clicked = "clicked"
    NotClicked = "not_clicked"
    Sent = "sent"
    NotSent = "not_sent"
    Geo = "geo"
    Gdpr = "gdpr"
    Score = "score"
    EngagementScore = "engagement_score"
    Tag = "tag"
    Goal = "goal"
    Crm = "crm"
    EcommerceNumberOfPurchases = "ecommerce_number_of_purchases"
    EcommerceTotalSpent = "ecommerce_total_spent"
    EcommerceProductPurchased = "ecommerce_product_purchased"
    EcommerceBrandPurchased = "ecommerce_brand_purchased"
    EcommerceAbandonedCart = "ecommerce_abandoned_cart"
    SmsSent = "sms_sent"
    SmsLinkClicked = "sms_link_clicked"
    SmsLinkNotClicked = "sms_link_not_clicked"
    CustomEvent = "custom_event"


class ECommerceNumberOfPurchasesConditionOperator(_UnknownFallbackEnum):
    "ECommerceNumberOfPurchasesConditionOperator enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    NumericLt = "numeric_lt"
    NumericGt = "numeric_gt"
    NumericEq = "numeric_eq"
    NumericNotEq = "numeric_not_eq"
    NumericLtEq = "numeric_lt_eq"
    NumericGtEq = "numeric_gt_eq"


class ECommerceNumberOfPurchasesConditionOperatorType(_UnknownFallbackEnum):
    "ECommerceNumberOfPurchasesConditionOperatorType enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    NumericOperator = "numeric_operator"


class ECommerceProductPurchasedConditionConditionType(_UnknownFallbackEnum):
    "ECommerceProductPurchasedConditionConditionType enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Name = "name"
    Email = "email"
    Custom = "custom"
    SubscriptionDate = "subscription_date"
    SubscriptionMethod = "subscription_method"
    Opened = "opened"
    NotOpened = "not_opened"
    Phase = "phase"
    LastSendDate = "last_send_date"
    LastClickDate = "last_click_date"
    LastOpenDate = "last_open_date"
    Webinar = "webinar"
    Clicked = "clicked"
    NotClicked = "not_clicked"
    Sent = "sent"
    NotSent = "not_sent"
    Geo = "geo"
    Gdpr = "gdpr"
    Score = "score"
    EngagementScore = "engagement_score"
    Tag = "tag"
    Goal = "goal"
    Crm = "crm"
    EcommerceNumberOfPurchases = "ecommerce_number_of_purchases"
    EcommerceTotalSpent = "ecommerce_total_spent"
    EcommerceProductPurchased = "ecommerce_product_purchased"
    EcommerceBrandPurchased = "ecommerce_brand_purchased"
    EcommerceAbandonedCart = "ecommerce_abandoned_cart"
    SmsSent = "sms_sent"
    SmsLinkClicked = "sms_link_clicked"
    SmsLinkNotClicked = "sms_link_not_clicked"
    CustomEvent = "custom_event"


class ECommerceProductPurchasedConditionOperator(_UnknownFallbackEnum):
    "ECommerceProductPurchasedConditionOperator enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Is = "is"
    IsNot = "is_not"


class ECommerceProductPurchasedConditionOperatorType(_UnknownFallbackEnum):
    "ECommerceProductPurchasedConditionOperatorType enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    EqualOperator = "equal_operator"


class ECommerceTotalSpentConditionConditionType(_UnknownFallbackEnum):
    "ECommerceTotalSpentConditionConditionType enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Name = "name"
    Email = "email"
    Custom = "custom"
    SubscriptionDate = "subscription_date"
    SubscriptionMethod = "subscription_method"
    Opened = "opened"
    NotOpened = "not_opened"
    Phase = "phase"
    LastSendDate = "last_send_date"
    LastClickDate = "last_click_date"
    LastOpenDate = "last_open_date"
    Webinar = "webinar"
    Clicked = "clicked"
    NotClicked = "not_clicked"
    Sent = "sent"
    NotSent = "not_sent"
    Geo = "geo"
    Gdpr = "gdpr"
    Score = "score"
    EngagementScore = "engagement_score"
    Tag = "tag"
    Goal = "goal"
    Crm = "crm"
    EcommerceNumberOfPurchases = "ecommerce_number_of_purchases"
    EcommerceTotalSpent = "ecommerce_total_spent"
    EcommerceProductPurchased = "ecommerce_product_purchased"
    EcommerceBrandPurchased = "ecommerce_brand_purchased"
    EcommerceAbandonedCart = "ecommerce_abandoned_cart"
    SmsSent = "sms_sent"
    SmsLinkClicked = "sms_link_clicked"
    SmsLinkNotClicked = "sms_link_not_clicked"
    CustomEvent = "custom_event"


class ECommerceTotalSpentConditionOperator(_UnknownFallbackEnum):
    "ECommerceTotalSpentConditionOperator enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    NumericLt = "numeric_lt"
    NumericGt = "numeric_gt"
    NumericEq = "numeric_eq"
    NumericNotEq = "numeric_not_eq"
    NumericLtEq = "numeric_lt_eq"
    NumericGtEq = "numeric_gt_eq"


class ECommerceTotalSpentConditionOperatorType(_UnknownFallbackEnum):
    "ECommerceTotalSpentConditionOperatorType enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    NumericOperator = "numeric_operator"


class EmailConditionConditionType(_UnknownFallbackEnum):
    "EmailConditionConditionType enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Name = "name"
    Email = "email"
    Custom = "custom"
    SubscriptionDate = "subscription_date"
    SubscriptionMethod = "subscription_method"
    Opened = "opened"
    NotOpened = "not_opened"
    Phase = "phase"
    LastSendDate = "last_send_date"
    LastClickDate = "last_click_date"
    LastOpenDate = "last_open_date"
    Webinar = "webinar"
    Clicked = "clicked"
    NotClicked = "not_clicked"
    Sent = "sent"
    NotSent = "not_sent"
    Geo = "geo"
    Gdpr = "gdpr"
    Score = "score"
    EngagementScore = "engagement_score"
    Tag = "tag"
    Goal = "goal"
    Crm = "crm"
    EcommerceNumberOfPurchases = "ecommerce_number_of_purchases"
    EcommerceTotalSpent = "ecommerce_total_spent"
    EcommerceProductPurchased = "ecommerce_product_purchased"
    EcommerceBrandPurchased = "ecommerce_brand_purchased"
    EcommerceAbandonedCart = "ecommerce_abandoned_cart"
    SmsSent = "sms_sent"
    SmsLinkClicked = "sms_link_clicked"
    SmsLinkNotClicked = "sms_link_not_clicked"
    CustomEvent = "custom_event"


class EmailConditionOperator(_UnknownFallbackEnum):
    "EmailConditionOperator enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Is = "is"
    IsNot = "is_not"
    Contains = "contains"
    NotContains = "not_contains"
    Starts = "starts"
    Ends = "ends"
    NotStarts = "not_starts"
    NotEnds = "not_ends"


class EmailConditionOperatorType(_UnknownFallbackEnum):
    "EmailConditionOperatorType enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    StringOperator = "string_operator"


class EngagementScoreConditionConditionType(_UnknownFallbackEnum):
    "EngagementScoreConditionConditionType enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Name = "name"
    Email = "email"
    Custom = "custom"
    SubscriptionDate = "subscription_date"
    SubscriptionMethod = "subscription_method"
    Opened = "opened"
    NotOpened = "not_opened"
    Phase = "phase"
    LastSendDate = "last_send_date"
    LastClickDate = "last_click_date"
    LastOpenDate = "last_open_date"
    Webinar = "webinar"
    Clicked = "clicked"
    NotClicked = "not_clicked"
    Sent = "sent"
    NotSent = "not_sent"
    Geo = "geo"
    Gdpr = "gdpr"
    Score = "score"
    EngagementScore = "engagement_score"
    Tag = "tag"
    Goal = "goal"
    Crm = "crm"
    EcommerceNumberOfPurchases = "ecommerce_number_of_purchases"
    EcommerceTotalSpent = "ecommerce_total_spent"
    EcommerceProductPurchased = "ecommerce_product_purchased"
    EcommerceBrandPurchased = "ecommerce_brand_purchased"
    EcommerceAbandonedCart = "ecommerce_abandoned_cart"
    SmsSent = "sms_sent"
    SmsLinkClicked = "sms_link_clicked"
    SmsLinkNotClicked = "sms_link_not_clicked"
    CustomEvent = "custom_event"


class EngagementScoreConditionOperator(_UnknownFallbackEnum):
    "The operator used in engagement score comparison"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    NumericLt = "numeric_lt"
    NumericGt = "numeric_gt"
    NumericEq = "numeric_eq"
    NumericNotEq = "numeric_not_eq"
    NumericLtEq = "numeric_lt_eq"
    NumericGtEq = "numeric_gt_eq"


class FileGroup(_UnknownFallbackEnum):
    "The file group"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Audio = "audio"
    Video = "video"
    Photo = "photo"
    Document = "document"


class FilePropertyName(_UnknownFallbackEnum):
    "FilePropertyName enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Width = "width"
    Height = "height"


class FormDetailsStatus(_UnknownFallbackEnum):
    "FormDetailsStatus enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Published = "published"
    Unpublished = "unpublished"
    Draft = "draft"


class FormSettingsAlreadySubscribedType(_UnknownFallbackEnum):
    "What to do when the address already exists in the campaign"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    StayOnPage = "stay_on_page"
    Default = "default"
    CustomUrl = "custom_url"


class FormSettingsForwardDataRequestType(_UnknownFallbackEnum):
    "How to forward form data to a thank-you page. [Learn more](https://www.getresponse.com/help/building-contact-lists/forms-and-pop-ups/can-i-forward-subscriber-data-to-a-custom-thank-you-page.html). `null` means that the data forwarding is turned off."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Get = "GET"
    Post = "POST"


class FormSettingsOptin(_UnknownFallbackEnum):
    "`single` - Single opt-in means that the contact will be added without confirming their subscription first. `double` - Double opt-in means that the contact will receive a subscription confirmation email."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Single = "single"
    Double = "double"


class FormSettingsThankYouType(_UnknownFallbackEnum):
    "What should happen when a new contact subscribes via the form."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    StayOnPage = "stay_on_page"
    Default = "default"
    CustomUrl = "custom_url"


class FormStatus(_UnknownFallbackEnum):
    "FormStatus enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Published = "published"
    Unpublished = "unpublished"
    Draft = "draft"


class FormVariantDetailsStatus(_UnknownFallbackEnum):
    "FormVariantDetailsStatus enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Published = "published"
    Unpublished = "unpublished"
    Disabled = "disabled"


class FormVariantDetailsWinner(_UnknownFallbackEnum):
    "Is this variant the winner in the A/B test"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Yes = "yes"
    No = "no"


class FormVariantStatus(_UnknownFallbackEnum):
    "FormVariantStatus enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Published = "published"
    Unpublished = "unpublished"
    Disabled = "disabled"


class GdprConditionConditionType(_UnknownFallbackEnum):
    "GdprConditionConditionType enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Name = "name"
    Email = "email"
    Custom = "custom"
    SubscriptionDate = "subscription_date"
    SubscriptionMethod = "subscription_method"
    Opened = "opened"
    NotOpened = "not_opened"
    Phase = "phase"
    LastSendDate = "last_send_date"
    LastClickDate = "last_click_date"
    LastOpenDate = "last_open_date"
    Webinar = "webinar"
    Clicked = "clicked"
    NotClicked = "not_clicked"
    Sent = "sent"
    NotSent = "not_sent"
    Geo = "geo"
    Gdpr = "gdpr"
    Score = "score"
    EngagementScore = "engagement_score"
    Tag = "tag"
    Goal = "goal"
    Crm = "crm"
    EcommerceNumberOfPurchases = "ecommerce_number_of_purchases"
    EcommerceTotalSpent = "ecommerce_total_spent"
    EcommerceProductPurchased = "ecommerce_product_purchased"
    EcommerceBrandPurchased = "ecommerce_brand_purchased"
    EcommerceAbandonedCart = "ecommerce_abandoned_cart"
    SmsSent = "sms_sent"
    SmsLinkClicked = "sms_link_clicked"
    SmsLinkNotClicked = "sms_link_not_clicked"
    CustomEvent = "custom_event"


class GdprConditionConsentStatus(_UnknownFallbackEnum):
    "Specify whether you want to search for contacts who have given or not given consent."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Given = "given"
    NotGiven = "not_given"


class GeolocationConditionConditionType(_UnknownFallbackEnum):
    "GeolocationConditionConditionType enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Name = "name"
    Email = "email"
    Custom = "custom"
    SubscriptionDate = "subscription_date"
    SubscriptionMethod = "subscription_method"
    Opened = "opened"
    NotOpened = "not_opened"
    Phase = "phase"
    LastSendDate = "last_send_date"
    LastClickDate = "last_click_date"
    LastOpenDate = "last_open_date"
    Webinar = "webinar"
    Clicked = "clicked"
    NotClicked = "not_clicked"
    Sent = "sent"
    NotSent = "not_sent"
    Geo = "geo"
    Gdpr = "gdpr"
    Score = "score"
    EngagementScore = "engagement_score"
    Tag = "tag"
    Goal = "goal"
    Crm = "crm"
    EcommerceNumberOfPurchases = "ecommerce_number_of_purchases"
    EcommerceTotalSpent = "ecommerce_total_spent"
    EcommerceProductPurchased = "ecommerce_product_purchased"
    EcommerceBrandPurchased = "ecommerce_brand_purchased"
    EcommerceAbandonedCart = "ecommerce_abandoned_cart"
    SmsSent = "sms_sent"
    SmsLinkClicked = "sms_link_clicked"
    SmsLinkNotClicked = "sms_link_not_clicked"
    CustomEvent = "custom_event"


class GeolocationConditionOperator(_UnknownFallbackEnum):
    "GeolocationConditionOperator enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Is = "is"
    IsNot = "is_not"
    Contains = "contains"
    NotContains = "not_contains"
    Starts = "starts"
    Ends = "ends"
    NotStarts = "not_starts"
    NotEnds = "not_ends"


class GeolocationConditionOperatorType(_UnknownFallbackEnum):
    "GeolocationConditionOperatorType enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    StringOperator = "string_operator"


class GeolocationConditionScope(_UnknownFallbackEnum):
    "Specify the search parameters"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Country = "country"
    CountryCode = "country_code"
    Region = "region"
    City = "city"
    Longitude = "longitude"
    Latitude = "latitude"
    PostalCode = "postal_code"
    DmaCode = "dma_code"


class GetAbTestSubjectListQueryStage(_UnknownFallbackEnum):
    "GetAbTestSubjectListQueryStage enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Preparing = "preparing"
    Testing = "testing"
    Finished = "finished"
    SendingWinner = "sending-winner"
    Cancelled = "cancelled"
    Draft = "draft"
    Completed = "completed"


class GetAutoresponderListQueryStatus(_UnknownFallbackEnum):
    "GetAutoresponderListQueryStatus enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Enabled = "enabled"
    Disabled = "disabled"


class GetAutoresponderStatisticsCollectionQueryGroupBy(_UnknownFallbackEnum):
    "GetAutoresponderStatisticsCollectionQueryGroupBy enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Total = "total"
    Hour = "hour"
    Day = "day"
    Month = "month"


class GetAutoresponderThumbnailSize(_UnknownFallbackEnum):
    "GetAutoresponderThumbnailSize enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Default = "default"
    Small = "small"


class GetCampaignStatisticsBalanceQueryGroupBy(_UnknownFallbackEnum):
    "GetCampaignStatisticsBalanceQueryGroupBy enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Hour = "hour"
    Day = "day"
    Month = "month"
    Total = "total"


class GetCampaignStatisticsListSizeQueryGroupBy(_UnknownFallbackEnum):
    "GetCampaignStatisticsListSizeQueryGroupBy enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Hour = "hour"
    Day = "day"
    Month = "month"
    Total = "total"


class GetCampaignStatisticsLocationsQueryGroupBy(_UnknownFallbackEnum):
    "GetCampaignStatisticsLocationsQueryGroupBy enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Hour = "hour"
    Day = "day"
    Month = "month"
    Total = "total"


class GetCampaignStatisticsOriginsQueryGroupBy(_UnknownFallbackEnum):
    "GetCampaignStatisticsOriginsQueryGroupBy enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Hour = "hour"
    Day = "day"
    Month = "month"
    Total = "total"


class GetCampaignStatisticsRemovalsQueryGroupBy(_UnknownFallbackEnum):
    "GetCampaignStatisticsRemovalsQueryGroupBy enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Hour = "hour"
    Day = "day"
    Month = "month"
    Total = "total"


class GetCampaignStatisticsSubscriptionsQueryGroupBy(_UnknownFallbackEnum):
    "GetCampaignStatisticsSubscriptionsQueryGroupBy enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Hour = "hour"
    Day = "day"
    Month = "month"
    Total = "total"


class GetContactListQueryOrigin(_UnknownFallbackEnum):
    "GetContactListQueryOrigin enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Import = "import"
    Email = "email"
    Www = "www"
    Panel = "panel"
    Leads = "leads"
    Sale = "sale"
    Api = "api"
    Survey = "survey"
    Iphone = "iphone"
    Copy = "copy"
    LandingPage = "landing_page"
    Webinar = "webinar"
    WebsiteBuilderElegant = "website_builder_elegant"
    Chat = "chat"
    Course = "course"
    PremiumNewsletter = "premium_newsletter"


class GetFormListQueryStatus(_UnknownFallbackEnum):
    "GetFormListQueryStatus enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Enabled = "enabled"
    Disabled = "disabled"
    Published = "published"
    Unpublished = "unpublished"
    Draft = "draft"


class GetLpsGeneralPerformanceStatsQueryDevice(_UnknownFallbackEnum):
    "GetLpsGeneralPerformanceStatsQueryDevice enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Desktop = "desktop"
    Mobile = "mobile"


class GetLpsListQueryStatus(_UnknownFallbackEnum):
    "GetLpsListQueryStatus enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Published = "published"
    Unpublished = "unpublished"


class GetNewsletterActivitiesQueryActivity(_UnknownFallbackEnum):
    "GetNewsletterActivitiesQueryActivity enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Send = "send"
    Open = "open"
    Click = "click"


class GetNewsletterListQueryStatus(_UnknownFallbackEnum):
    "GetNewsletterListQueryStatus enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Enabled = "enabled"
    Disabled = "disabled"


class GetNewsletterListQueryType(_UnknownFallbackEnum):
    "GetNewsletterListQueryType enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Draft = "draft"
    Broadcast = "broadcast"
    Splittest = "splittest"
    Automation = "automation"


class GetNewsletterStatisticsCollectionQueryGroupBy(_UnknownFallbackEnum):
    "GetNewsletterStatisticsCollectionQueryGroupBy enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Total = "total"
    Hour = "hour"
    Day = "day"
    Month = "month"


class GetNewsletterThumbnailSize(_UnknownFallbackEnum):
    "GetNewsletterThumbnailSize enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Default = "default"
    Small = "small"


class GetPopupGeneralPerformanceQueryDevice(_UnknownFallbackEnum):
    "GetPopupGeneralPerformanceQueryDevice enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Desktop = "desktop"
    Mobile = "mobile"


class GetPopupsListQueryStatus(_UnknownFallbackEnum):
    "GetPopupsListQueryStatus enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Published = "published"
    Unpublished = "unpublished"


class GetRssNewsletterStatisticsCollectionQueryGroupBy(_UnknownFallbackEnum):
    "GetRssNewsletterStatisticsCollectionQueryGroupBy enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Total = "total"
    Hour = "hour"
    Day = "day"
    Month = "month"


class GetRssNewslettersListQueryStatus(_UnknownFallbackEnum):
    "GetRssNewslettersListQueryStatus enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Enabled = "enabled"
    Disabled = "disabled"


class GetSingleAutoresponderStatisticsQueryGroupBy(_UnknownFallbackEnum):
    "GetSingleAutoresponderStatisticsQueryGroupBy enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Total = "total"
    Hour = "hour"
    Day = "day"
    Month = "month"


class GetSingleNewsletterStatisticsQueryGroupBy(_UnknownFallbackEnum):
    "GetSingleNewsletterStatisticsQueryGroupBy enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Total = "total"
    Hour = "hour"
    Day = "day"
    Month = "month"


class GetSingleRssNewsletterStatisticsCollectionQueryGroupBy(_UnknownFallbackEnum):
    "GetSingleRssNewsletterStatisticsCollectionQueryGroupBy enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Total = "total"
    Hour = "hour"
    Day = "day"
    Month = "month"


class GetSmsListQuerySendingStatus(_UnknownFallbackEnum):
    "GetSmsListQuerySendingStatus enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Scheduled = "scheduled"
    Sending = "sending"
    Sent = "sent"


class GetSmsListQueryType(_UnknownFallbackEnum):
    "GetSmsListQueryType enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Sms = "sms"
    Draft = "draft"


class GetSplittestListQueryStatus(_UnknownFallbackEnum):
    "GetSplittestListQueryStatus enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Active = "active"
    Inactive = "inactive"


class GetTransactionalEmailsStatisticsQueryGroupBy(_UnknownFallbackEnum):
    "GetTransactionalEmailsStatisticsQueryGroupBy enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Total = "total"
    Day = "day"


class GetWbeGeneralPerformanceStatsQueryDevice(_UnknownFallbackEnum):
    "GetWbeGeneralPerformanceStatsQueryDevice enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Desktop = "desktop"
    Mobile = "mobile"


class GetWebinarListQueryStatus(_UnknownFallbackEnum):
    "GetWebinarListQueryStatus enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Upcoming = "upcoming"
    Finished = "finished"
    Published = "published"
    Unpublished = "unpublished"


class GetWebinarListQueryType(_UnknownFallbackEnum):
    "GetWebinarListQueryType enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    All = "all"
    Live = "live"
    OnDemand = "on_demand"


class GetWebsitesListQueryStatus(_UnknownFallbackEnum):
    "GetWebsitesListQueryStatus enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Published = "published"
    Unpublished = "unpublished"


class GoalConditionConditionType(_UnknownFallbackEnum):
    "GoalConditionConditionType enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Name = "name"
    Email = "email"
    Custom = "custom"
    SubscriptionDate = "subscription_date"
    SubscriptionMethod = "subscription_method"
    Opened = "opened"
    NotOpened = "not_opened"
    Phase = "phase"
    LastSendDate = "last_send_date"
    LastClickDate = "last_click_date"
    LastOpenDate = "last_open_date"
    Webinar = "webinar"
    Clicked = "clicked"
    NotClicked = "not_clicked"
    Sent = "sent"
    NotSent = "not_sent"
    Geo = "geo"
    Gdpr = "gdpr"
    Score = "score"
    EngagementScore = "engagement_score"
    Tag = "tag"
    Goal = "goal"
    Crm = "crm"
    EcommerceNumberOfPurchases = "ecommerce_number_of_purchases"
    EcommerceTotalSpent = "ecommerce_total_spent"
    EcommerceProductPurchased = "ecommerce_product_purchased"
    EcommerceBrandPurchased = "ecommerce_brand_purchased"
    EcommerceAbandonedCart = "ecommerce_abandoned_cart"
    SmsSent = "sms_sent"
    SmsLinkClicked = "sms_link_clicked"
    SmsLinkNotClicked = "sms_link_not_clicked"
    CustomEvent = "custom_event"


class GoalConditionOperator(_UnknownFallbackEnum):
    "The relational and existence operator. For the relational operator, the value field is required."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    NumericLt = "numeric_lt"
    NumericGt = "numeric_gt"
    NumericEq = "numeric_eq"
    NumericNotEq = "numeric_not_eq"
    NumericLtEq = "numeric_lt_eq"
    NumericGtEq = "numeric_gt_eq"
    Assigned = "assigned"
    NotAssigned = "not_assigned"


class GoalConditionOperatorType(_UnknownFallbackEnum):
    "GoalConditionOperatorType enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    NumericOperator = "numeric_operator"


class ImageDetailsExtension(_UnknownFallbackEnum):
    "File extension"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Jpg = "jpg"
    Gif = "gif"
    Png = "png"
    Jpeg = "jpeg"
    Bmp = "bmp"


class ImportStatus(_UnknownFallbackEnum):
    "ImportStatus enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Uploaded = "uploaded"
    Review = "review"
    Approved = "approved"
    Rejected = "rejected"
    Finished = "finished"
    Canceled = "canceled"
    ToReview = "to_review"


class LandingPageMetaNoindex(_UnknownFallbackEnum):
    "To entirely prevent your page content from being listed in the Google web index, even if other sites link to it use a noindex meta tag"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Yes = "yes"
    No = "no"


class LandingPageOptin(_UnknownFallbackEnum):
    "The opt-in type (double or single)"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Single = "single"
    Double = "double"


class LandingPageThankYouPageType(_UnknownFallbackEnum):
    "What should happen after a contact subscribes"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    StayOnPage = "stay_on_page"
    Default = "default"
    CustomUrl = "custom_url"


class LandingPageUserDomainStatus(_UnknownFallbackEnum):
    "The DNS status for the user's private domain. Can be `null` if a private domain isn't assigned."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Active = "active"
    Inactive = "inactive"
    Waiting = "waiting"


class LastClickDateConditionConditionType(_UnknownFallbackEnum):
    "LastClickDateConditionConditionType enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Name = "name"
    Email = "email"
    Custom = "custom"
    SubscriptionDate = "subscription_date"
    SubscriptionMethod = "subscription_method"
    Opened = "opened"
    NotOpened = "not_opened"
    Phase = "phase"
    LastSendDate = "last_send_date"
    LastClickDate = "last_click_date"
    LastOpenDate = "last_open_date"
    Webinar = "webinar"
    Clicked = "clicked"
    NotClicked = "not_clicked"
    Sent = "sent"
    NotSent = "not_sent"
    Geo = "geo"
    Gdpr = "gdpr"
    Score = "score"
    EngagementScore = "engagement_score"
    Tag = "tag"
    Goal = "goal"
    Crm = "crm"
    EcommerceNumberOfPurchases = "ecommerce_number_of_purchases"
    EcommerceTotalSpent = "ecommerce_total_spent"
    EcommerceProductPurchased = "ecommerce_product_purchased"
    EcommerceBrandPurchased = "ecommerce_brand_purchased"
    EcommerceAbandonedCart = "ecommerce_abandoned_cart"
    SmsSent = "sms_sent"
    SmsLinkClicked = "sms_link_clicked"
    SmsLinkNotClicked = "sms_link_not_clicked"
    CustomEvent = "custom_event"


class LastClickDateConditionOperator(_UnknownFallbackEnum):
    "LastClickDateConditionOperator enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    DateTo = "date_to"
    DateFrom = "date_from"
    SpecificDate = "specific_date"
    Custom = "custom"


class LastClickDateConditionOperatorType(_UnknownFallbackEnum):
    "LastClickDateConditionOperatorType enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    DateOperator = "date_operator"


class LastOpenDateConditionConditionType(_UnknownFallbackEnum):
    "LastOpenDateConditionConditionType enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Name = "name"
    Email = "email"
    Custom = "custom"
    SubscriptionDate = "subscription_date"
    SubscriptionMethod = "subscription_method"
    Opened = "opened"
    NotOpened = "not_opened"
    Phase = "phase"
    LastSendDate = "last_send_date"
    LastClickDate = "last_click_date"
    LastOpenDate = "last_open_date"
    Webinar = "webinar"
    Clicked = "clicked"
    NotClicked = "not_clicked"
    Sent = "sent"
    NotSent = "not_sent"
    Geo = "geo"
    Gdpr = "gdpr"
    Score = "score"
    EngagementScore = "engagement_score"
    Tag = "tag"
    Goal = "goal"
    Crm = "crm"
    EcommerceNumberOfPurchases = "ecommerce_number_of_purchases"
    EcommerceTotalSpent = "ecommerce_total_spent"
    EcommerceProductPurchased = "ecommerce_product_purchased"
    EcommerceBrandPurchased = "ecommerce_brand_purchased"
    EcommerceAbandonedCart = "ecommerce_abandoned_cart"
    SmsSent = "sms_sent"
    SmsLinkClicked = "sms_link_clicked"
    SmsLinkNotClicked = "sms_link_not_clicked"
    CustomEvent = "custom_event"


class LastOpenDateConditionOperator(_UnknownFallbackEnum):
    "LastOpenDateConditionOperator enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    DateTo = "date_to"
    DateFrom = "date_from"
    SpecificDate = "specific_date"
    Custom = "custom"


class LastOpenDateConditionOperatorType(_UnknownFallbackEnum):
    "LastOpenDateConditionOperatorType enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    DateOperator = "date_operator"


class LastSendDateConditionConditionType(_UnknownFallbackEnum):
    "LastSendDateConditionConditionType enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Name = "name"
    Email = "email"
    Custom = "custom"
    SubscriptionDate = "subscription_date"
    SubscriptionMethod = "subscription_method"
    Opened = "opened"
    NotOpened = "not_opened"
    Phase = "phase"
    LastSendDate = "last_send_date"
    LastClickDate = "last_click_date"
    LastOpenDate = "last_open_date"
    Webinar = "webinar"
    Clicked = "clicked"
    NotClicked = "not_clicked"
    Sent = "sent"
    NotSent = "not_sent"
    Geo = "geo"
    Gdpr = "gdpr"
    Score = "score"
    EngagementScore = "engagement_score"
    Tag = "tag"
    Goal = "goal"
    Crm = "crm"
    EcommerceNumberOfPurchases = "ecommerce_number_of_purchases"
    EcommerceTotalSpent = "ecommerce_total_spent"
    EcommerceProductPurchased = "ecommerce_product_purchased"
    EcommerceBrandPurchased = "ecommerce_brand_purchased"
    EcommerceAbandonedCart = "ecommerce_abandoned_cart"
    SmsSent = "sms_sent"
    SmsLinkClicked = "sms_link_clicked"
    SmsLinkNotClicked = "sms_link_not_clicked"
    CustomEvent = "custom_event"


class LastSendDateConditionOperator(_UnknownFallbackEnum):
    "LastSendDateConditionOperator enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    DateTo = "date_to"
    DateFrom = "date_from"
    SpecificDate = "specific_date"
    Custom = "custom"


class LastSendDateConditionOperatorType(_UnknownFallbackEnum):
    "LastSendDateConditionOperatorType enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    DateOperator = "date_operator"


class LinkClickedConditionConditionType(_UnknownFallbackEnum):
    "LinkClickedConditionConditionType enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Name = "name"
    Email = "email"
    Custom = "custom"
    SubscriptionDate = "subscription_date"
    SubscriptionMethod = "subscription_method"
    Opened = "opened"
    NotOpened = "not_opened"
    Phase = "phase"
    LastSendDate = "last_send_date"
    LastClickDate = "last_click_date"
    LastOpenDate = "last_open_date"
    Webinar = "webinar"
    Clicked = "clicked"
    NotClicked = "not_clicked"
    Sent = "sent"
    NotSent = "not_sent"
    Geo = "geo"
    Gdpr = "gdpr"
    Score = "score"
    EngagementScore = "engagement_score"
    Tag = "tag"
    Goal = "goal"
    Crm = "crm"
    EcommerceNumberOfPurchases = "ecommerce_number_of_purchases"
    EcommerceTotalSpent = "ecommerce_total_spent"
    EcommerceProductPurchased = "ecommerce_product_purchased"
    EcommerceBrandPurchased = "ecommerce_brand_purchased"
    EcommerceAbandonedCart = "ecommerce_abandoned_cart"
    SmsSent = "sms_sent"
    SmsLinkClicked = "sms_link_clicked"
    SmsLinkNotClicked = "sms_link_not_clicked"
    CustomEvent = "custom_event"


class LinkClickedConditionOperatorType(_UnknownFallbackEnum):
    "LinkClickedConditionOperatorType enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    MessageOperator = "message_operator"


class LinkNotClickedConditionConditionType(_UnknownFallbackEnum):
    "LinkNotClickedConditionConditionType enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Name = "name"
    Email = "email"
    Custom = "custom"
    SubscriptionDate = "subscription_date"
    SubscriptionMethod = "subscription_method"
    Opened = "opened"
    NotOpened = "not_opened"
    Phase = "phase"
    LastSendDate = "last_send_date"
    LastClickDate = "last_click_date"
    LastOpenDate = "last_open_date"
    Webinar = "webinar"
    Clicked = "clicked"
    NotClicked = "not_clicked"
    Sent = "sent"
    NotSent = "not_sent"
    Geo = "geo"
    Gdpr = "gdpr"
    Score = "score"
    EngagementScore = "engagement_score"
    Tag = "tag"
    Goal = "goal"
    Crm = "crm"
    EcommerceNumberOfPurchases = "ecommerce_number_of_purchases"
    EcommerceTotalSpent = "ecommerce_total_spent"
    EcommerceProductPurchased = "ecommerce_product_purchased"
    EcommerceBrandPurchased = "ecommerce_brand_purchased"
    EcommerceAbandonedCart = "ecommerce_abandoned_cart"
    SmsSent = "sms_sent"
    SmsLinkClicked = "sms_link_clicked"
    SmsLinkNotClicked = "sms_link_not_clicked"
    CustomEvent = "custom_event"


class LinkNotClickedConditionDateOperator(_UnknownFallbackEnum):
    "It allows you to set a date range. For some of them `value` will be required. Examples can be found here: [API Docs](https://apidocs.getresponse.com/v3/case-study/segments-manual#not-opened-action)."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    DateFrom = "date_from"
    Never = "never"
    Today = "today"
    Yesterday = "yesterday"
    Last7Days = "last_7_days"
    Last30Days = "last_30_days"
    LastNDays = "last_n_days"
    ThisWeek = "this_week"
    ThisMonth = "this_month"


class LinkNotClickedConditionOperatorType(_UnknownFallbackEnum):
    "LinkNotClickedConditionOperatorType enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    ComplexMessageOperator = "complex_message_operator"


class LpsDetailsStatus(_UnknownFallbackEnum):
    "The landing page status"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Published = "published"
    Unpublished = "unpublished"


class LpsListItemStatus(_UnknownFallbackEnum):
    "The landing page status"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Published = "published"
    Unpublished = "unpublished"


class LpsPageStatus(_UnknownFallbackEnum):
    "The status of a page associated with the landing page (i.e., 404 page or thank you page)"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Active = "active"
    Inactive = "inactive"


class LpsStatus(_UnknownFallbackEnum):
    "The landing page status"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Published = "published"
    Unpublished = "unpublished"


class MessageActivityReportActivityTypesEnum(_UnknownFallbackEnum):
    "MessageActivityReportActivityTypesEnum enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Click = "click"
    Open = "open"
    Send = "send"


class MessageEditorEnum(_UnknownFallbackEnum):
    "Indicates how the message was created: `custom` means a custom-made message, `text` means plain text content, `getresponse` means that the message was created using the GetResponse editor."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Custom = "custom"
    Text = "text"
    Getresponse = "getresponse"
    Legacy = "legacy"
    Html2 = "html2"


class MessageFlagsArrayItem(_UnknownFallbackEnum):
    "MessageFlagsArrayItem enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Openrate = "openrate"
    Clicktrack = "clicktrack"
    GoogleAnalytics = "google_analytics"


class MessageNotSentConditionConditionType(_UnknownFallbackEnum):
    "MessageNotSentConditionConditionType enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Name = "name"
    Email = "email"
    Custom = "custom"
    SubscriptionDate = "subscription_date"
    SubscriptionMethod = "subscription_method"
    Opened = "opened"
    NotOpened = "not_opened"
    Phase = "phase"
    LastSendDate = "last_send_date"
    LastClickDate = "last_click_date"
    LastOpenDate = "last_open_date"
    Webinar = "webinar"
    Clicked = "clicked"
    NotClicked = "not_clicked"
    Sent = "sent"
    NotSent = "not_sent"
    Geo = "geo"
    Gdpr = "gdpr"
    Score = "score"
    EngagementScore = "engagement_score"
    Tag = "tag"
    Goal = "goal"
    Crm = "crm"
    EcommerceNumberOfPurchases = "ecommerce_number_of_purchases"
    EcommerceTotalSpent = "ecommerce_total_spent"
    EcommerceProductPurchased = "ecommerce_product_purchased"
    EcommerceBrandPurchased = "ecommerce_brand_purchased"
    EcommerceAbandonedCart = "ecommerce_abandoned_cart"
    SmsSent = "sms_sent"
    SmsLinkClicked = "sms_link_clicked"
    SmsLinkNotClicked = "sms_link_not_clicked"
    CustomEvent = "custom_event"


class MessageNotSentConditionOperatorType(_UnknownFallbackEnum):
    "MessageNotSentConditionOperatorType enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    MessageOperator = "message_operator"


class MessageSentConditionConditionType(_UnknownFallbackEnum):
    "MessageSentConditionConditionType enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Name = "name"
    Email = "email"
    Custom = "custom"
    SubscriptionDate = "subscription_date"
    SubscriptionMethod = "subscription_method"
    Opened = "opened"
    NotOpened = "not_opened"
    Phase = "phase"
    LastSendDate = "last_send_date"
    LastClickDate = "last_click_date"
    LastOpenDate = "last_open_date"
    Webinar = "webinar"
    Clicked = "clicked"
    NotClicked = "not_clicked"
    Sent = "sent"
    NotSent = "not_sent"
    Geo = "geo"
    Gdpr = "gdpr"
    Score = "score"
    EngagementScore = "engagement_score"
    Tag = "tag"
    Goal = "goal"
    Crm = "crm"
    EcommerceNumberOfPurchases = "ecommerce_number_of_purchases"
    EcommerceTotalSpent = "ecommerce_total_spent"
    EcommerceProductPurchased = "ecommerce_product_purchased"
    EcommerceBrandPurchased = "ecommerce_brand_purchased"
    EcommerceAbandonedCart = "ecommerce_abandoned_cart"
    SmsSent = "sms_sent"
    SmsLinkClicked = "sms_link_clicked"
    SmsLinkNotClicked = "sms_link_not_clicked"
    CustomEvent = "custom_event"


class MessageSentConditionOperatorType(_UnknownFallbackEnum):
    "MessageSentConditionOperatorType enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    MessageOperator = "message_operator"


class MessageTypeOperator(_UnknownFallbackEnum):
    "The type of message."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Autoresponder = "autoresponder"
    Newsletter = "newsletter"
    Splittest = "splittest"
    Automation = "automation"


class MetaFieldValueType(_UnknownFallbackEnum):
    "The value type enumerable"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    String = "string"
    Integer = "integer"


class NameConditionConditionType(_UnknownFallbackEnum):
    "NameConditionConditionType enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Name = "name"
    Email = "email"
    Custom = "custom"
    SubscriptionDate = "subscription_date"
    SubscriptionMethod = "subscription_method"
    Opened = "opened"
    NotOpened = "not_opened"
    Phase = "phase"
    LastSendDate = "last_send_date"
    LastClickDate = "last_click_date"
    LastOpenDate = "last_open_date"
    Webinar = "webinar"
    Clicked = "clicked"
    NotClicked = "not_clicked"
    Sent = "sent"
    NotSent = "not_sent"
    Geo = "geo"
    Gdpr = "gdpr"
    Score = "score"
    EngagementScore = "engagement_score"
    Tag = "tag"
    Goal = "goal"
    Crm = "crm"
    EcommerceNumberOfPurchases = "ecommerce_number_of_purchases"
    EcommerceTotalSpent = "ecommerce_total_spent"
    EcommerceProductPurchased = "ecommerce_product_purchased"
    EcommerceBrandPurchased = "ecommerce_brand_purchased"
    EcommerceAbandonedCart = "ecommerce_abandoned_cart"
    SmsSent = "sms_sent"
    SmsLinkClicked = "sms_link_clicked"
    SmsLinkNotClicked = "sms_link_not_clicked"
    CustomEvent = "custom_event"


class NameConditionOperator(_UnknownFallbackEnum):
    "NameConditionOperator enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Is = "is"
    IsNot = "is_not"
    Contains = "contains"
    NotContains = "not_contains"
    Starts = "starts"
    Ends = "ends"
    NotStarts = "not_starts"
    NotEnds = "not_ends"


class NameConditionOperatorType(_UnknownFallbackEnum):
    "NameConditionOperatorType enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    StringOperator = "string_operator"


class NewAbtestsSubjectFlagsItem(_UnknownFallbackEnum):
    "Tracking options enabled for the newsletter"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Clicktrack = "clicktrack"
    GoogleAnalytics = "google_analytics"
    EcommerceTracking = "ecommerce_tracking"


class NewContactOrigin(_UnknownFallbackEnum):
    "NewContactOrigin enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Import = "import"
    Email = "email"
    Www = "www"
    Panel = "panel"
    Leads = "leads"
    Sale = "sale"
    Api = "api"
    Survey = "survey"
    Iphone = "iphone"
    Copy = "copy"
    LandingPage = "landing_page"
    Webinar = "webinar"
    WebsiteBuilderElegant = "website_builder_elegant"
    Chat = "chat"
    Course = "course"
    PremiumNewsletter = "premium_newsletter"


class NewCustomFieldValueType(_UnknownFallbackEnum):
    "Type of returning value, it returns `type` options extended by a `string` option if the `format` was not defined"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    String = "string"
    Number = "number"
    Date = "date"
    Datetime = "datetime"
    Country = "country"
    Currency = "currency"
    Phone = "phone"
    Gender = "gender"
    Ip = "ip"
    Url = "url"


class NewMessageEditorEnumOutput(_UnknownFallbackEnum):
    "How the message was created: `editor_v3` - created by GetResponse editor, `text` means plain text content, `html` means custom HTML content, `getresponse` is a deprecated, legacy GetResponse editor."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    EditorV3 = "editor_v3"
    Getresponse = "getresponse"
    Text = "text"
    Html = "html"


class NewMetaFieldValueType(_UnknownFallbackEnum):
    "The value type enumerable"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    String = "string"
    Integer = "integer"


class NewNewsletterType(_UnknownFallbackEnum):
    "The newsletter type"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Broadcast = "broadcast"
    Draft = "draft"


class NewSearchContactsSectionLogicOperator(_UnknownFallbackEnum):
    "Match 'any' (`or` value) or 'all' (`and` value) of the following conditions"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Or = "or"
    And = "and"


class NewSearchContactsSubscribersTypeItem(_UnknownFallbackEnum):
    "NewSearchContactsSubscribersTypeItem enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Subscribed = "subscribed"


class NewsletterActivityActivity(_UnknownFallbackEnum):
    "The type of activity"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Send = "send"
    Open = "open"
    Click = "click"


class NewsletterDetailsType(_UnknownFallbackEnum):
    "The newsletter type"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Broadcast = "broadcast"
    Draft = "draft"


class NewsletterListElementType(_UnknownFallbackEnum):
    "The newsletter type"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Broadcast = "broadcast"
    Draft = "draft"


class NewsletterType(_UnknownFallbackEnum):
    "The newsletter type"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Broadcast = "broadcast"
    Draft = "draft"


class NotOpenedConditionConditionType(_UnknownFallbackEnum):
    "NotOpenedConditionConditionType enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Name = "name"
    Email = "email"
    Custom = "custom"
    SubscriptionDate = "subscription_date"
    SubscriptionMethod = "subscription_method"
    Opened = "opened"
    NotOpened = "not_opened"
    Phase = "phase"
    LastSendDate = "last_send_date"
    LastClickDate = "last_click_date"
    LastOpenDate = "last_open_date"
    Webinar = "webinar"
    Clicked = "clicked"
    NotClicked = "not_clicked"
    Sent = "sent"
    NotSent = "not_sent"
    Geo = "geo"
    Gdpr = "gdpr"
    Score = "score"
    EngagementScore = "engagement_score"
    Tag = "tag"
    Goal = "goal"
    Crm = "crm"
    EcommerceNumberOfPurchases = "ecommerce_number_of_purchases"
    EcommerceTotalSpent = "ecommerce_total_spent"
    EcommerceProductPurchased = "ecommerce_product_purchased"
    EcommerceBrandPurchased = "ecommerce_brand_purchased"
    EcommerceAbandonedCart = "ecommerce_abandoned_cart"
    SmsSent = "sms_sent"
    SmsLinkClicked = "sms_link_clicked"
    SmsLinkNotClicked = "sms_link_not_clicked"
    CustomEvent = "custom_event"


class NotOpenedConditionDateOperator(_UnknownFallbackEnum):
    "It allows you to set a date range. For some of them `value` will be required. Examples can be found here: [API Docs](https://apidocs.getresponse.com/v3/case-study/segments-manual#not-opened-action)."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    DateFrom = "date_from"
    Never = "never"
    Today = "today"
    Yesterday = "yesterday"
    Last7Days = "last_7_days"
    Last30Days = "last_30_days"
    LastNDays = "last_n_days"
    ThisWeek = "this_week"
    ThisMonth = "this_month"


class NotOpenedConditionOperatorType(_UnknownFallbackEnum):
    "NotOpenedConditionOperatorType enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    ComplexMessageOperator = "complex_message_operator"


class OpenedConditionConditionType(_UnknownFallbackEnum):
    "OpenedConditionConditionType enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Name = "name"
    Email = "email"
    Custom = "custom"
    SubscriptionDate = "subscription_date"
    SubscriptionMethod = "subscription_method"
    Opened = "opened"
    NotOpened = "not_opened"
    Phase = "phase"
    LastSendDate = "last_send_date"
    LastClickDate = "last_click_date"
    LastOpenDate = "last_open_date"
    Webinar = "webinar"
    Clicked = "clicked"
    NotClicked = "not_clicked"
    Sent = "sent"
    NotSent = "not_sent"
    Geo = "geo"
    Gdpr = "gdpr"
    Score = "score"
    EngagementScore = "engagement_score"
    Tag = "tag"
    Goal = "goal"
    Crm = "crm"
    EcommerceNumberOfPurchases = "ecommerce_number_of_purchases"
    EcommerceTotalSpent = "ecommerce_total_spent"
    EcommerceProductPurchased = "ecommerce_product_purchased"
    EcommerceBrandPurchased = "ecommerce_brand_purchased"
    EcommerceAbandonedCart = "ecommerce_abandoned_cart"
    SmsSent = "sms_sent"
    SmsLinkClicked = "sms_link_clicked"
    SmsLinkNotClicked = "sms_link_not_clicked"
    CustomEvent = "custom_event"


class OpenedConditionOperatorType(_UnknownFallbackEnum):
    "OpenedConditionOperatorType enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    MessageOperator = "message_operator"


class PopupDetailsStatus(_UnknownFallbackEnum):
    "The form or popup status"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Published = "published"
    Unpublished = "unpublished"


class PopupDetailsType(_UnknownFallbackEnum):
    "The form or popup type"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Popup = "popup"
    Inline = "inline"


class PopupListItemStatus(_UnknownFallbackEnum):
    "The form or popup status"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Published = "published"
    Unpublished = "unpublished"


class PopupListItemType(_UnknownFallbackEnum):
    "The form or popup type"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Popup = "popup"
    Inline = "inline"


class RelationalNumericOperatorEnum(_UnknownFallbackEnum):
    "The relational operators."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    NumericLt = "numeric_lt"
    NumericGt = "numeric_gt"
    NumericEq = "numeric_eq"
    NumericNotEq = "numeric_not_eq"
    NumericLtEq = "numeric_lt_eq"
    NumericGtEq = "numeric_gt_eq"


class RssNewsletterListSendAsapSettingsFilter(_UnknownFallbackEnum):
    "The filter settings for an RSS post"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Recent = "recent"
    Engaged = "engaged"
    Shared = "shared"
    Commented = "commented"


class RssNewsletterListSendDailySettingsFilter(_UnknownFallbackEnum):
    "The filter settings for an RSS post"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Recent = "recent"
    Engaged = "engaged"
    Shared = "shared"
    Commented = "commented"


class RssNewsletterListSendMonthlySettingsFilter(_UnknownFallbackEnum):
    "The filter settings for an RSS post"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Recent = "recent"
    Engaged = "engaged"
    Shared = "shared"
    Commented = "commented"


class RssNewsletterListSendWeeklySettingsFilter(_UnknownFallbackEnum):
    "The filter settings for an RSS post"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Recent = "recent"
    Engaged = "engaged"
    Shared = "shared"
    Commented = "commented"


class RssNewsletterListSendWeeklySettingsSendAtWeekDay(_UnknownFallbackEnum):
    "The day of the week when the message should be sent"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Monday = "Monday"
    Tuesday = "Tuesday"
    Wednesday = "Wednesday"
    Thursday = "Thursday"
    Friday = "Friday"
    Saturday = "Saturday"
    Sunday = "Sunday"


class RssNewsletterSendAsapSettingsFilter(_UnknownFallbackEnum):
    "The filter settings for an RSS post"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Recent = "recent"
    Engaged = "engaged"
    Shared = "shared"
    Commented = "commented"


class RssNewsletterSendDailySettingsFilter(_UnknownFallbackEnum):
    "The filter settings for an RSS post"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Recent = "recent"
    Engaged = "engaged"
    Shared = "shared"
    Commented = "commented"


class RssNewsletterSendMonthlySettingsFilter(_UnknownFallbackEnum):
    "The filter settings for an RSS post"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Recent = "recent"
    Engaged = "engaged"
    Shared = "shared"
    Commented = "commented"


class RssNewsletterSendSettingsDetailsFilter(_UnknownFallbackEnum):
    "The filter settings for an RSS post"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Recent = "recent"
    Engaged = "engaged"
    Shared = "shared"
    Commented = "commented"


class RssNewsletterSendSettingsListingFilter(_UnknownFallbackEnum):
    "The filter settings for an RSS post"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Recent = "recent"
    Engaged = "engaged"
    Shared = "shared"
    Commented = "commented"


class RssNewsletterSendWeeklySettingsFilter(_UnknownFallbackEnum):
    "The filter settings for an RSS post"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Recent = "recent"
    Engaged = "engaged"
    Shared = "shared"
    Commented = "commented"


class RssNewsletterSendWeeklySettingsSendAtWeekDay(_UnknownFallbackEnum):
    "The day of the week when the message should be sent"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Monday = "Monday"
    Tuesday = "Tuesday"
    Wednesday = "Wednesday"
    Thursday = "Thursday"
    Friday = "Friday"
    Saturday = "Saturday"
    Sunday = "Sunday"


class ScoringConditionConditionType(_UnknownFallbackEnum):
    "ScoringConditionConditionType enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Name = "name"
    Email = "email"
    Custom = "custom"
    SubscriptionDate = "subscription_date"
    SubscriptionMethod = "subscription_method"
    Opened = "opened"
    NotOpened = "not_opened"
    Phase = "phase"
    LastSendDate = "last_send_date"
    LastClickDate = "last_click_date"
    LastOpenDate = "last_open_date"
    Webinar = "webinar"
    Clicked = "clicked"
    NotClicked = "not_clicked"
    Sent = "sent"
    NotSent = "not_sent"
    Geo = "geo"
    Gdpr = "gdpr"
    Score = "score"
    EngagementScore = "engagement_score"
    Tag = "tag"
    Goal = "goal"
    Crm = "crm"
    EcommerceNumberOfPurchases = "ecommerce_number_of_purchases"
    EcommerceTotalSpent = "ecommerce_total_spent"
    EcommerceProductPurchased = "ecommerce_product_purchased"
    EcommerceBrandPurchased = "ecommerce_brand_purchased"
    EcommerceAbandonedCart = "ecommerce_abandoned_cart"
    SmsSent = "sms_sent"
    SmsLinkClicked = "sms_link_clicked"
    SmsLinkNotClicked = "sms_link_not_clicked"
    CustomEvent = "custom_event"


class ScoringConditionOperator(_UnknownFallbackEnum):
    "The relational operator. Required for the operatorType=numeric_operator."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    NumericLt = "numeric_lt"
    NumericGt = "numeric_gt"
    NumericEq = "numeric_eq"
    NumericNotEq = "numeric_not_eq"
    NumericLtEq = "numeric_lt_eq"
    NumericGtEq = "numeric_gt_eq"


class ScoringConditionOperatorType(_UnknownFallbackEnum):
    "ScoringConditionOperatorType enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    NumericOperator = "numeric_operator"
    NotExists = "not_exists"


class SearchContactSectionLogicOperator(_UnknownFallbackEnum):
    "SearchContactSectionLogicOperator enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    And = "and"
    Or = "or"


class SearchContactSectionSubscriberCycleItem(_UnknownFallbackEnum):
    "SearchContactSectionSubscriberCycleItem enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    ReceivingAutoresponder = "receiving_autoresponder"
    NotReceivingAutoresponder = "not_receiving_autoresponder"


class SearchContactSectionSubscriptionDate(_UnknownFallbackEnum):
    "Matches the matching period"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    AllTime = "all_time"
    Today = "today"
    Yesterday = "yesterday"
    Last7Days = "last_7_days"
    Last30Days = "last_30_days"
    ThisWeek = "this_week"
    LastWeek = "last_week"
    ThisMonth = "this_month"
    LastMonth = "last_month"
    Last2Months = "last_2_months"
    Custom = "custom"


class SearchContactsBySearchFormSectionLogicOperator(_UnknownFallbackEnum):
    "Match 'any' (`or` value) or 'all' (`and` value) of the following conditions"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Or = "or"
    And = "and"


class SearchContactsBySearchFormSubscribersTypeItem(_UnknownFallbackEnum):
    "SearchContactsBySearchFormSubscribersTypeItem enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Subscribed = "subscribed"
    Undelivered = "undelivered"
    Removed = "removed"
    Unconfirmed = "unconfirmed"


class SearchContactsConditionsDetailsSectionLogicOperator(_UnknownFallbackEnum):
    "Match 'any' (`or` value) or 'all' (`and` value) of the following conditions"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Or = "or"
    And = "and"


class SearchContactsDetailsSectionLogicOperator(_UnknownFallbackEnum):
    "Match 'any' (`or` value) or 'all' (`and` value) of the following conditions"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Or = "or"
    And = "and"


class SearchContactsDetailsSubscribersTypeItem(_UnknownFallbackEnum):
    "SearchContactsDetailsSubscribersTypeItem enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Subscribed = "subscribed"


class SearchedContactDetailsOrigin(_UnknownFallbackEnum):
    "SearchedContactDetailsOrigin enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Import = "import"
    Email = "email"
    Www = "www"
    Panel = "panel"
    Leads = "leads"
    Sale = "sale"
    Api = "api"
    Forward = "forward"
    Survey = "survey"
    Iphone = "iphone"
    Copy = "copy"
    LandingPage = "landing_page"
    Webinar = "webinar"
    Course = "course"
    PremiumNewsletter = "premium_newsletter"


class SearchedContactDetailsReason(_UnknownFallbackEnum):
    "SearchedContactDetailsReason enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Api = "api"
    Automation = "automation"
    Blacklisted = "blacklisted"
    Bounce = "bounce"
    Cleaner = "cleaner"
    Complaint = "complaint"
    Support = "support"
    Unsubscribe = "unsubscribe"
    User = "user"


class SectionAllTimeSubscriptionDateLogicOperator(_UnknownFallbackEnum):
    "SectionAllTimeSubscriptionDateLogicOperator enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    And = "and"
    Or = "or"


class SectionAllTimeSubscriptionDateSubscriberCycleItem(_UnknownFallbackEnum):
    "SectionAllTimeSubscriptionDateSubscriberCycleItem enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    ReceivingAutoresponder = "receiving_autoresponder"
    NotReceivingAutoresponder = "not_receiving_autoresponder"


class SectionAllTimeSubscriptionDateSubscriptionDate(_UnknownFallbackEnum):
    "Matches the matching period"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    AllTime = "all_time"
    Today = "today"
    Yesterday = "yesterday"
    Last7Days = "last_7_days"
    Last30Days = "last_30_days"
    ThisWeek = "this_week"
    LastWeek = "last_week"
    ThisMonth = "this_month"
    LastMonth = "last_month"
    Last2Months = "last_2_months"
    Custom = "custom"


class SectionCustomSubscriptionDateLogicOperator(_UnknownFallbackEnum):
    "SectionCustomSubscriptionDateLogicOperator enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    And = "and"
    Or = "or"


class SectionCustomSubscriptionDateSubscriberCycleItem(_UnknownFallbackEnum):
    "SectionCustomSubscriptionDateSubscriberCycleItem enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    ReceivingAutoresponder = "receiving_autoresponder"
    NotReceivingAutoresponder = "not_receiving_autoresponder"


class SectionCustomSubscriptionDateSubscriptionDate(_UnknownFallbackEnum):
    "Matches the matching period"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    AllTime = "all_time"
    Today = "today"
    Yesterday = "yesterday"
    Last7Days = "last_7_days"
    Last30Days = "last_30_days"
    ThisWeek = "this_week"
    LastWeek = "last_week"
    ThisMonth = "this_month"
    LastMonth = "last_month"
    Last2Months = "last_2_months"
    Custom = "custom"


class SectionLast2MonthsSubscriptionDateLogicOperator(_UnknownFallbackEnum):
    "SectionLast2MonthsSubscriptionDateLogicOperator enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    And = "and"
    Or = "or"


class SectionLast2MonthsSubscriptionDateSubscriberCycleItem(_UnknownFallbackEnum):
    "SectionLast2MonthsSubscriptionDateSubscriberCycleItem enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    ReceivingAutoresponder = "receiving_autoresponder"
    NotReceivingAutoresponder = "not_receiving_autoresponder"


class SectionLast2MonthsSubscriptionDateSubscriptionDate(_UnknownFallbackEnum):
    "Matches the matching period"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    AllTime = "all_time"
    Today = "today"
    Yesterday = "yesterday"
    Last7Days = "last_7_days"
    Last30Days = "last_30_days"
    ThisWeek = "this_week"
    LastWeek = "last_week"
    ThisMonth = "this_month"
    LastMonth = "last_month"
    Last2Months = "last_2_months"
    Custom = "custom"


class SectionLast30DaysSubscriptionDateLogicOperator(_UnknownFallbackEnum):
    "SectionLast30DaysSubscriptionDateLogicOperator enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    And = "and"
    Or = "or"


class SectionLast30DaysSubscriptionDateSubscriberCycleItem(_UnknownFallbackEnum):
    "SectionLast30DaysSubscriptionDateSubscriberCycleItem enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    ReceivingAutoresponder = "receiving_autoresponder"
    NotReceivingAutoresponder = "not_receiving_autoresponder"


class SectionLast30DaysSubscriptionDateSubscriptionDate(_UnknownFallbackEnum):
    "Matches the matching period"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    AllTime = "all_time"
    Today = "today"
    Yesterday = "yesterday"
    Last7Days = "last_7_days"
    Last30Days = "last_30_days"
    ThisWeek = "this_week"
    LastWeek = "last_week"
    ThisMonth = "this_month"
    LastMonth = "last_month"
    Last2Months = "last_2_months"
    Custom = "custom"


class SectionLast7DaysSubscriptionDateLogicOperator(_UnknownFallbackEnum):
    "SectionLast7DaysSubscriptionDateLogicOperator enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    And = "and"
    Or = "or"


class SectionLast7DaysSubscriptionDateSubscriberCycleItem(_UnknownFallbackEnum):
    "SectionLast7DaysSubscriptionDateSubscriberCycleItem enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    ReceivingAutoresponder = "receiving_autoresponder"
    NotReceivingAutoresponder = "not_receiving_autoresponder"


class SectionLast7DaysSubscriptionDateSubscriptionDate(_UnknownFallbackEnum):
    "Matches the matching period"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    AllTime = "all_time"
    Today = "today"
    Yesterday = "yesterday"
    Last7Days = "last_7_days"
    Last30Days = "last_30_days"
    ThisWeek = "this_week"
    LastWeek = "last_week"
    ThisMonth = "this_month"
    LastMonth = "last_month"
    Last2Months = "last_2_months"
    Custom = "custom"


class SectionLastMonthSubscriptionDateLogicOperator(_UnknownFallbackEnum):
    "SectionLastMonthSubscriptionDateLogicOperator enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    And = "and"
    Or = "or"


class SectionLastMonthSubscriptionDateSubscriberCycleItem(_UnknownFallbackEnum):
    "SectionLastMonthSubscriptionDateSubscriberCycleItem enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    ReceivingAutoresponder = "receiving_autoresponder"
    NotReceivingAutoresponder = "not_receiving_autoresponder"


class SectionLastMonthSubscriptionDateSubscriptionDate(_UnknownFallbackEnum):
    "Matches the matching period"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    AllTime = "all_time"
    Today = "today"
    Yesterday = "yesterday"
    Last7Days = "last_7_days"
    Last30Days = "last_30_days"
    ThisWeek = "this_week"
    LastWeek = "last_week"
    ThisMonth = "this_month"
    LastMonth = "last_month"
    Last2Months = "last_2_months"
    Custom = "custom"


class SectionLastWeekSubscriptionDateLogicOperator(_UnknownFallbackEnum):
    "SectionLastWeekSubscriptionDateLogicOperator enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    And = "and"
    Or = "or"


class SectionLastWeekSubscriptionDateSubscriberCycleItem(_UnknownFallbackEnum):
    "SectionLastWeekSubscriptionDateSubscriberCycleItem enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    ReceivingAutoresponder = "receiving_autoresponder"
    NotReceivingAutoresponder = "not_receiving_autoresponder"


class SectionLastWeekSubscriptionDateSubscriptionDate(_UnknownFallbackEnum):
    "Matches the matching period"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    AllTime = "all_time"
    Today = "today"
    Yesterday = "yesterday"
    Last7Days = "last_7_days"
    Last30Days = "last_30_days"
    ThisWeek = "this_week"
    LastWeek = "last_week"
    ThisMonth = "this_month"
    LastMonth = "last_month"
    Last2Months = "last_2_months"
    Custom = "custom"


class SectionThisMonthSubscriptionDateLogicOperator(_UnknownFallbackEnum):
    "SectionThisMonthSubscriptionDateLogicOperator enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    And = "and"
    Or = "or"


class SectionThisMonthSubscriptionDateSubscriberCycleItem(_UnknownFallbackEnum):
    "SectionThisMonthSubscriptionDateSubscriberCycleItem enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    ReceivingAutoresponder = "receiving_autoresponder"
    NotReceivingAutoresponder = "not_receiving_autoresponder"


class SectionThisMonthSubscriptionDateSubscriptionDate(_UnknownFallbackEnum):
    "Matches the matching period"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    AllTime = "all_time"
    Today = "today"
    Yesterday = "yesterday"
    Last7Days = "last_7_days"
    Last30Days = "last_30_days"
    ThisWeek = "this_week"
    LastWeek = "last_week"
    ThisMonth = "this_month"
    LastMonth = "last_month"
    Last2Months = "last_2_months"
    Custom = "custom"


class SectionThisWeekSubscriptionDateLogicOperator(_UnknownFallbackEnum):
    "SectionThisWeekSubscriptionDateLogicOperator enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    And = "and"
    Or = "or"


class SectionThisWeekSubscriptionDateSubscriberCycleItem(_UnknownFallbackEnum):
    "SectionThisWeekSubscriptionDateSubscriberCycleItem enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    ReceivingAutoresponder = "receiving_autoresponder"
    NotReceivingAutoresponder = "not_receiving_autoresponder"


class SectionThisWeekSubscriptionDateSubscriptionDate(_UnknownFallbackEnum):
    "Matches the matching period"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    AllTime = "all_time"
    Today = "today"
    Yesterday = "yesterday"
    Last7Days = "last_7_days"
    Last30Days = "last_30_days"
    ThisWeek = "this_week"
    LastWeek = "last_week"
    ThisMonth = "this_month"
    LastMonth = "last_month"
    Last2Months = "last_2_months"
    Custom = "custom"


class SectionTodaySubscriptionDateLogicOperator(_UnknownFallbackEnum):
    "SectionTodaySubscriptionDateLogicOperator enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    And = "and"
    Or = "or"


class SectionTodaySubscriptionDateSubscriberCycleItem(_UnknownFallbackEnum):
    "SectionTodaySubscriptionDateSubscriberCycleItem enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    ReceivingAutoresponder = "receiving_autoresponder"
    NotReceivingAutoresponder = "not_receiving_autoresponder"


class SectionTodaySubscriptionDateSubscriptionDate(_UnknownFallbackEnum):
    "Matches the matching period"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    AllTime = "all_time"
    Today = "today"
    Yesterday = "yesterday"
    Last7Days = "last_7_days"
    Last30Days = "last_30_days"
    ThisWeek = "this_week"
    LastWeek = "last_week"
    ThisMonth = "this_month"
    LastMonth = "last_month"
    Last2Months = "last_2_months"
    Custom = "custom"


class SectionYesterdaySubscriptionDateLogicOperator(_UnknownFallbackEnum):
    "SectionYesterdaySubscriptionDateLogicOperator enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    And = "and"
    Or = "or"


class SectionYesterdaySubscriptionDateSubscriberCycleItem(_UnknownFallbackEnum):
    "SectionYesterdaySubscriptionDateSubscriberCycleItem enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    ReceivingAutoresponder = "receiving_autoresponder"
    NotReceivingAutoresponder = "not_receiving_autoresponder"


class SectionYesterdaySubscriptionDateSubscriptionDate(_UnknownFallbackEnum):
    "Matches the matching period"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    AllTime = "all_time"
    Today = "today"
    Yesterday = "yesterday"
    Last7Days = "last_7_days"
    Last30Days = "last_30_days"
    ThisWeek = "this_week"
    LastWeek = "last_week"
    ThisMonth = "this_month"
    LastMonth = "last_month"
    Last2Months = "last_2_months"
    Custom = "custom"


class SendSmsToContactsRecipientsType(_UnknownFallbackEnum):
    "The recipient type. To send a text message to contacts in your list, select `contacts`. To message contacts who are not in any of your lists, select `importedNumbers`"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Contacts = "contacts"
    Importednumbers = "importedNumbers"


class SendSmsToImportedNumbersRecipientsType(_UnknownFallbackEnum):
    "The recipient type. To send a text message to contacts in your list, select `contacts`. To message contacts who are not in any of your lists, select `importedNumbers`"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Contacts = "contacts"
    Importednumbers = "importedNumbers"


class SmsAutomationDetailsStatus(_UnknownFallbackEnum):
    "The status of of the automated SMS message"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Ready = "ready"
    InUse = "in_use"


class SmsAutomationListItemStatus(_UnknownFallbackEnum):
    "The status of of the automated SMS message"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Ready = "ready"
    InUse = "in_use"


class SmsDetailsRecipientsType(_UnknownFallbackEnum):
    "Type of SMS message recipients"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Contacts = "contacts"
    Importednumbers = "importedNumbers"


class SmsDetailsType(_UnknownFallbackEnum):
    "The SMS message type"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Sms = "sms"
    Draft = "draft"


class SmsLinkClickedConditionConditionType(_UnknownFallbackEnum):
    "SmsLinkClickedConditionConditionType enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Name = "name"
    Email = "email"
    Custom = "custom"
    SubscriptionDate = "subscription_date"
    SubscriptionMethod = "subscription_method"
    Opened = "opened"
    NotOpened = "not_opened"
    Phase = "phase"
    LastSendDate = "last_send_date"
    LastClickDate = "last_click_date"
    LastOpenDate = "last_open_date"
    Webinar = "webinar"
    Clicked = "clicked"
    NotClicked = "not_clicked"
    Sent = "sent"
    NotSent = "not_sent"
    Geo = "geo"
    Gdpr = "gdpr"
    Score = "score"
    EngagementScore = "engagement_score"
    Tag = "tag"
    Goal = "goal"
    Crm = "crm"
    EcommerceNumberOfPurchases = "ecommerce_number_of_purchases"
    EcommerceTotalSpent = "ecommerce_total_spent"
    EcommerceProductPurchased = "ecommerce_product_purchased"
    EcommerceBrandPurchased = "ecommerce_brand_purchased"
    EcommerceAbandonedCart = "ecommerce_abandoned_cart"
    SmsSent = "sms_sent"
    SmsLinkClicked = "sms_link_clicked"
    SmsLinkNotClicked = "sms_link_not_clicked"
    CustomEvent = "custom_event"


class SmsLinkNotClickedConditionConditionType(_UnknownFallbackEnum):
    "SmsLinkNotClickedConditionConditionType enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Name = "name"
    Email = "email"
    Custom = "custom"
    SubscriptionDate = "subscription_date"
    SubscriptionMethod = "subscription_method"
    Opened = "opened"
    NotOpened = "not_opened"
    Phase = "phase"
    LastSendDate = "last_send_date"
    LastClickDate = "last_click_date"
    LastOpenDate = "last_open_date"
    Webinar = "webinar"
    Clicked = "clicked"
    NotClicked = "not_clicked"
    Sent = "sent"
    NotSent = "not_sent"
    Geo = "geo"
    Gdpr = "gdpr"
    Score = "score"
    EngagementScore = "engagement_score"
    Tag = "tag"
    Goal = "goal"
    Crm = "crm"
    EcommerceNumberOfPurchases = "ecommerce_number_of_purchases"
    EcommerceTotalSpent = "ecommerce_total_spent"
    EcommerceProductPurchased = "ecommerce_product_purchased"
    EcommerceBrandPurchased = "ecommerce_brand_purchased"
    EcommerceAbandonedCart = "ecommerce_abandoned_cart"
    SmsSent = "sms_sent"
    SmsLinkClicked = "sms_link_clicked"
    SmsLinkNotClicked = "sms_link_not_clicked"
    CustomEvent = "custom_event"


class SmsListItemRecipientsType(_UnknownFallbackEnum):
    "Type of SMS message recipients"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Contacts = "contacts"
    Importednumbers = "importedNumbers"


class SmsListItemType(_UnknownFallbackEnum):
    "The SMS message type"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Sms = "sms"
    Draft = "draft"


class SmsSenderNameStatusesEnum(_UnknownFallbackEnum):
    "SmsSenderNameStatusesEnum enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Pending = "pending"
    Active = "active"
    Rejected = "rejected"


class SmsSentConditionConditionType(_UnknownFallbackEnum):
    "SmsSentConditionConditionType enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Name = "name"
    Email = "email"
    Custom = "custom"
    SubscriptionDate = "subscription_date"
    SubscriptionMethod = "subscription_method"
    Opened = "opened"
    NotOpened = "not_opened"
    Phase = "phase"
    LastSendDate = "last_send_date"
    LastClickDate = "last_click_date"
    LastOpenDate = "last_open_date"
    Webinar = "webinar"
    Clicked = "clicked"
    NotClicked = "not_clicked"
    Sent = "sent"
    NotSent = "not_sent"
    Geo = "geo"
    Gdpr = "gdpr"
    Score = "score"
    EngagementScore = "engagement_score"
    Tag = "tag"
    Goal = "goal"
    Crm = "crm"
    EcommerceNumberOfPurchases = "ecommerce_number_of_purchases"
    EcommerceTotalSpent = "ecommerce_total_spent"
    EcommerceProductPurchased = "ecommerce_product_purchased"
    EcommerceBrandPurchased = "ecommerce_brand_purchased"
    EcommerceAbandonedCart = "ecommerce_abandoned_cart"
    SmsSent = "sms_sent"
    SmsLinkClicked = "sms_link_clicked"
    SmsLinkNotClicked = "sms_link_not_clicked"
    CustomEvent = "custom_event"


class SmsSentConditionDeliveryStatus(_UnknownFallbackEnum):
    "Specify the delivery status. Omit this field if the delivery status is not relevant."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Delivered = "delivered"
    Undelivered = "undelivered"
    Any = "any"


class SortOrderEnum(_UnknownFallbackEnum):
    "SortOrderEnum enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Asc = "ASC"
    Desc = "DESC"


class SpecificDateEnum(_UnknownFallbackEnum):
    "The specific date."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Today = "today"
    Yesterday = "yesterday"
    Last7Days = "last_7_days"
    Last30Days = "last_30_days"
    LastNDays = "last_n_days"
    ThisWeek = "this_week"
    LastWeek = "last_week"
    ThisMonth = "this_month"
    LastMonth = "last_month"


class SplittestChooseWinning(_UnknownFallbackEnum):
    "The method of choosing the winning A/B test"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Automatic = "automatic"
    Manual = "manual"


class SplittestNewsletterStatus(_UnknownFallbackEnum):
    "The status of the newsletter"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Sampled = "sampled"
    Chosen = "chosen"
    Rejected = "rejected"


class SplittestStage(_UnknownFallbackEnum):
    "A/B test stage"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Queued = "queued"
    ScheduleSampling = "schedule_sampling"
    EvaluateSampling = "evaluate_sampling"
    ChooseWinning = "choose_winning"
    ScheduleWinning = "schedule_winning"
    SendWinning = "send_winning"
    CanceledQueued = "canceled_queued"
    CanceledSampling = "canceled_sampling"
    CanceledWinning = "canceled_winning"
    Incomplete = "incomplete"
    Finished = "finished"


class SplittestStatus(_UnknownFallbackEnum):
    "A/B test status"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Active = "active"
    Inactive = "inactive"


class SplittestType(_UnknownFallbackEnum):
    "A/B test type"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Content = "content"
    Subject = "subject"
    Day = "day"
    Hour = "hour"
    FromField = "from_field"


class SplittestWinningCriteria(_UnknownFallbackEnum):
    "A/B test winning criteria"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Open = "open"
    Click = "click"


class StatusEnum(_UnknownFallbackEnum):
    "StatusEnum enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Enabled = "enabled"
    Disabled = "disabled"


class StringBooleanEnum(_UnknownFallbackEnum):
    "StringBooleanEnum enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    True_ = "true"
    False_ = "false"


class SubscribersTypeEnumForSearchingSubscribersTypeItem(_UnknownFallbackEnum):
    "SubscribersTypeEnumForSearchingSubscribersTypeItem enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Subscribed = "subscribed"
    Undelivered = "undelivered"
    Removed = "removed"
    Unconfirmed = "unconfirmed"


class SubscribersTypeEnumForSegmentsSubscribersTypeItem(_UnknownFallbackEnum):
    "SubscribersTypeEnumForSegmentsSubscribersTypeItem enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Subscribed = "subscribed"


class SubscriptionDateConditionConditionType(_UnknownFallbackEnum):
    "SubscriptionDateConditionConditionType enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Name = "name"
    Email = "email"
    Custom = "custom"
    SubscriptionDate = "subscription_date"
    SubscriptionMethod = "subscription_method"
    Opened = "opened"
    NotOpened = "not_opened"
    Phase = "phase"
    LastSendDate = "last_send_date"
    LastClickDate = "last_click_date"
    LastOpenDate = "last_open_date"
    Webinar = "webinar"
    Clicked = "clicked"
    NotClicked = "not_clicked"
    Sent = "sent"
    NotSent = "not_sent"
    Geo = "geo"
    Gdpr = "gdpr"
    Score = "score"
    EngagementScore = "engagement_score"
    Tag = "tag"
    Goal = "goal"
    Crm = "crm"
    EcommerceNumberOfPurchases = "ecommerce_number_of_purchases"
    EcommerceTotalSpent = "ecommerce_total_spent"
    EcommerceProductPurchased = "ecommerce_product_purchased"
    EcommerceBrandPurchased = "ecommerce_brand_purchased"
    EcommerceAbandonedCart = "ecommerce_abandoned_cart"
    SmsSent = "sms_sent"
    SmsLinkClicked = "sms_link_clicked"
    SmsLinkNotClicked = "sms_link_not_clicked"
    CustomEvent = "custom_event"


class SubscriptionDateConditionOperator(_UnknownFallbackEnum):
    "SubscriptionDateConditionOperator enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    DateTo = "date_to"
    DateFrom = "date_from"
    SpecificDate = "specific_date"
    Custom = "custom"


class SubscriptionDateConditionOperatorType(_UnknownFallbackEnum):
    "SubscriptionDateConditionOperatorType enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    DateOperator = "date_operator"


class SubscriptionMethodConditionConditionType(_UnknownFallbackEnum):
    "SubscriptionMethodConditionConditionType enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Name = "name"
    Email = "email"
    Custom = "custom"
    SubscriptionDate = "subscription_date"
    SubscriptionMethod = "subscription_method"
    Opened = "opened"
    NotOpened = "not_opened"
    Phase = "phase"
    LastSendDate = "last_send_date"
    LastClickDate = "last_click_date"
    LastOpenDate = "last_open_date"
    Webinar = "webinar"
    Clicked = "clicked"
    NotClicked = "not_clicked"
    Sent = "sent"
    NotSent = "not_sent"
    Geo = "geo"
    Gdpr = "gdpr"
    Score = "score"
    EngagementScore = "engagement_score"
    Tag = "tag"
    Goal = "goal"
    Crm = "crm"
    EcommerceNumberOfPurchases = "ecommerce_number_of_purchases"
    EcommerceTotalSpent = "ecommerce_total_spent"
    EcommerceProductPurchased = "ecommerce_product_purchased"
    EcommerceBrandPurchased = "ecommerce_brand_purchased"
    EcommerceAbandonedCart = "ecommerce_abandoned_cart"
    SmsSent = "sms_sent"
    SmsLinkClicked = "sms_link_clicked"
    SmsLinkNotClicked = "sms_link_not_clicked"
    CustomEvent = "custom_event"


class SubscriptionMethodConditionMethod(_UnknownFallbackEnum):
    "SubscriptionMethodConditionMethod enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Webform = "webform"
    Import = "import"
    LandingPage = "landing_page"
    Api = "api"
    Email = "email"
    Panel = "panel"
    Mobile = "mobile"
    Survey = "survey"
    Sales = "sales"
    Copy = "copy"
    Leads = "leads"
    Webinar = "webinar"
    Chat = "chat"
    WebsiteBuilderElegant = "website_builder_elegant"
    Course = "course"
    PremiumNewsletter = "premium_newsletter"


class SubscriptionMethodConditionWebformType(_UnknownFallbackEnum):
    "The property required for the webform subscription method. If it equals webforms, webformsv2 or popups, additonal property value is needed."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    All = "all"
    Webforms = "webforms"
    Webformsv2 = "webformsv2"
    Popups = "popups"


class TagConditionConditionType(_UnknownFallbackEnum):
    "TagConditionConditionType enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Name = "name"
    Email = "email"
    Custom = "custom"
    SubscriptionDate = "subscription_date"
    SubscriptionMethod = "subscription_method"
    Opened = "opened"
    NotOpened = "not_opened"
    Phase = "phase"
    LastSendDate = "last_send_date"
    LastClickDate = "last_click_date"
    LastOpenDate = "last_open_date"
    Webinar = "webinar"
    Clicked = "clicked"
    NotClicked = "not_clicked"
    Sent = "sent"
    NotSent = "not_sent"
    Geo = "geo"
    Gdpr = "gdpr"
    Score = "score"
    EngagementScore = "engagement_score"
    Tag = "tag"
    Goal = "goal"
    Crm = "crm"
    EcommerceNumberOfPurchases = "ecommerce_number_of_purchases"
    EcommerceTotalSpent = "ecommerce_total_spent"
    EcommerceProductPurchased = "ecommerce_product_purchased"
    EcommerceBrandPurchased = "ecommerce_brand_purchased"
    EcommerceAbandonedCart = "ecommerce_abandoned_cart"
    SmsSent = "sms_sent"
    SmsLinkClicked = "sms_link_clicked"
    SmsLinkNotClicked = "sms_link_not_clicked"
    CustomEvent = "custom_event"


class TagConditionOperator(_UnknownFallbackEnum):
    "This operator verifies whether the property you are looking for exists or not"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Exists = "exists"
    NotExists = "not_exists"


class TagConditionOperatorType(_UnknownFallbackEnum):
    "The operator for the existence of a property"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Exists = "exists"


class TemplateContentContentType(_UnknownFallbackEnum):
    "The message content type"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Direct = "direct"
    Template = "template"


class TransactionalEmailRecipientDetailsStatus(_UnknownFallbackEnum):
    "TransactionalEmailRecipientDetailsStatus enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Unknown = "unknown"
    Sent = "sent"
    Rejected = "rejected"
    Opened = "opened"
    Bounced = "bounced"
    ReportedSpam = "reported_spam"


class TransactionalEmailRecipientStatus(_UnknownFallbackEnum):
    "TransactionalEmailRecipientStatus enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Unknown = "unknown"
    Sent = "sent"
    Rejected = "rejected"
    Opened = "opened"
    Bounced = "bounced"
    ReportedSpam = "reported_spam"


class TransactionalEmailRecipientToStatus(_UnknownFallbackEnum):
    "TransactionalEmailRecipientToStatus enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Unknown = "unknown"
    Sent = "sent"
    Rejected = "rejected"
    Opened = "opened"
    Bounced = "bounced"
    ReportedSpam = "reported_spam"


class UpdateAccountBlocklistAdditionalFlags(_UnknownFallbackEnum):
    "UpdateAccountBlocklistAdditionalFlags enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Add = "add"
    Delete = "delete"
    Noresponse = "noResponse"


class UpdateAccountNumberOfEmployees(_UnknownFallbackEnum):
    "Numbers of employees"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    V_50 = "50"
    V_250 = "250"
    V_500 = "500"
    More = "more"


class UpdateAccountTimeFormat(_UnknownFallbackEnum):
    "Account time notation"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    V_12h = "12h"
    V_24h = "24h"


class UpdateCampaignBlocklistAdditionalFlags(_UnknownFallbackEnum):
    "UpdateCampaignBlocklistAdditionalFlags enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Add = "add"
    Delete = "delete"
    Noresponse = "noResponse"


class UpdateContactOrigin(_UnknownFallbackEnum):
    "UpdateContactOrigin enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Import = "import"
    Email = "email"
    Www = "www"
    Panel = "panel"
    Leads = "leads"
    Sale = "sale"
    Api = "api"
    Survey = "survey"
    Iphone = "iphone"
    Copy = "copy"
    LandingPage = "landing_page"
    Webinar = "webinar"
    WebsiteBuilderElegant = "website_builder_elegant"
    Chat = "chat"
    Course = "course"
    PremiumNewsletter = "premium_newsletter"


class UpdateMetaFieldValueType(_UnknownFallbackEnum):
    "The value type enumerable"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    String = "string"
    Integer = "integer"


class UpdateSearchContactsSectionLogicOperator(_UnknownFallbackEnum):
    "Match 'any' (`or` value) or 'all' (`and` value) of the following conditions"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Or = "or"
    And = "and"


class UpdateSearchContactsSubscribersTypeItem(_UnknownFallbackEnum):
    "UpdateSearchContactsSubscribersTypeItem enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Subscribed = "subscribed"


class UpdateWorkflowStatus(_UnknownFallbackEnum):
    "An 'incomplete' status means that the workflow is a 'draft' in the web panel"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Active = "active"
    Inactive = "inactive"
    Incomplete = "incomplete"


class WebinarConditionConditionType(_UnknownFallbackEnum):
    "WebinarConditionConditionType enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Name = "name"
    Email = "email"
    Custom = "custom"
    SubscriptionDate = "subscription_date"
    SubscriptionMethod = "subscription_method"
    Opened = "opened"
    NotOpened = "not_opened"
    Phase = "phase"
    LastSendDate = "last_send_date"
    LastClickDate = "last_click_date"
    LastOpenDate = "last_open_date"
    Webinar = "webinar"
    Clicked = "clicked"
    NotClicked = "not_clicked"
    Sent = "sent"
    NotSent = "not_sent"
    Geo = "geo"
    Gdpr = "gdpr"
    Score = "score"
    EngagementScore = "engagement_score"
    Tag = "tag"
    Goal = "goal"
    Crm = "crm"
    EcommerceNumberOfPurchases = "ecommerce_number_of_purchases"
    EcommerceTotalSpent = "ecommerce_total_spent"
    EcommerceProductPurchased = "ecommerce_product_purchased"
    EcommerceBrandPurchased = "ecommerce_brand_purchased"
    EcommerceAbandonedCart = "ecommerce_abandoned_cart"
    SmsSent = "sms_sent"
    SmsLinkClicked = "sms_link_clicked"
    SmsLinkNotClicked = "sms_link_not_clicked"
    CustomEvent = "custom_event"


class WebinarConditionContactType(_UnknownFallbackEnum):
    "WebinarConditionContactType enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Host = "host"
    Listener = "listener"
    Presenter = "presenter"
    Registrant = "registrant"
    All = "all"


class WebinarConditionWebinarCondition(_UnknownFallbackEnum):
    "WebinarConditionWebinarCondition enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Participated = "participated"
    NotParticipated = "not_participated"


class WebinarStatus(_UnknownFallbackEnum):
    "WebinarStatus enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Upcoming = "upcoming"
    Finished = "finished"
    Published = "published"
    Unpublished = "unpublished"


class WebinarType(_UnknownFallbackEnum):
    "The webinar type"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    All = "all"
    Live = "live"
    OnDemand = "on_demand"


class WebsiteDetailsStatus(_UnknownFallbackEnum):
    "The website status"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Published = "published"
    Unpublished = "unpublished"


class WebsitePageStatus(_UnknownFallbackEnum):
    "The website page status"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Active = "active"
    Inactive = "inactive"


class WebsiteStatus(_UnknownFallbackEnum):
    "The website status"

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Published = "published"
    Unpublished = "unpublished"


class WorkflowStatus(_UnknownFallbackEnum):
    "WorkflowStatus enum."

    UNKNOWN = ""  # any wire value this client doesn't recognize resolves here, see _missing_
    Active = "active"
    Inactive = "inactive"
    Incomplete = "incomplete"


class AbtestsSubject(BaseModel):
    "AbtestsSubject model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    ab_test_id: str | None = Field(default=None, alias="abTestId")
    "A/B test ID"
    name: str | None = Field(default=None, alias="name")
    "A/B test name"
    campaign: dict[str, Any] | None = Field(default=None, alias="campaign")
    "List linked to A/B test"
    from_field: dict[str, Any] | None = Field(default=None, alias="fromField")
    'Newsletter\'s From" address"'
    reply_to: dict[str, Any] | None = Field(default=None, alias="replyTo")
    "Newsletter's reply-to address"


class AbtestsSubjectDetails(BaseModel):
    "AbtestsSubjectDetails model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    ab_test_id: str | None = Field(default=None, alias="abTestId")
    "A/B test ID"
    name: str | None = Field(default=None, alias="name")
    "A/B test name"
    campaign: dict[str, Any] | None = Field(default=None, alias="campaign")
    "List linked to A/B test"
    from_field: dict[str, Any] | None = Field(default=None, alias="fromField")
    'Newsletter\'s From" address"'
    reply_to: dict[str, Any] | None = Field(default=None, alias="replyTo")
    "Newsletter's reply-to address"
    status: AbtestsSubjectDetailsStatus | None = Field(default=None, alias="status")
    "Newsletter status"
    stage: AbtestsSubjectDetailsStage | None = Field(default=None, alias="stage")
    "A/B test stage"
    delivery_settings: dict[str, Any] | None = Field(default=None, alias="deliverySettings")
    "The A/B test delivery settings"
    flags: list[AbtestsSubjectDetailsFlagsItem] | None = Field(default=None, alias="flags")
    created_on: datetime | None = Field(default=None, alias="createdOn")
    "Date the A/B test was created on"
    updated_on: datetime | None = Field(default=None, alias="updatedOn")
    "Date A/B test was updated on"
    href: str | None = Field(default=None, alias="href")
    "Direct hyperlink to a resource"
    winner_sending_start: datetime | None = Field(default=None, alias="winnerSendingStart")
    "Date the winning message was sent on"
    statistics: dict[str, Any] | None = Field(default=None, alias="statistics")
    "The statistics of A/B test"
    variants: list[dict[str, Any]] | None = Field(default=None, alias="variants")
    send_settings: dict[str, Any] | None = Field(default=None, alias="sendSettings")
    "The send settings for the A/B test"
    editor: AbtestsSubjectDetailsEditor | None = Field(default=None, alias="editor")
    "The message editor used for the A/B test"
    content: MessageContent | None = Field(default=None, alias="content")


class AbtestsSubjectListItem(BaseModel):
    "AbtestsSubjectListItem model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    ab_test_id: str | None = Field(default=None, alias="abTestId")
    "A/B test ID"
    name: str | None = Field(default=None, alias="name")
    "A/B test name"
    campaign: dict[str, Any] | None = Field(default=None, alias="campaign")
    "List linked to A/B test"
    from_field: dict[str, Any] | None = Field(default=None, alias="fromField")
    'Newsletter\'s From" address"'
    reply_to: dict[str, Any] | None = Field(default=None, alias="replyTo")
    "Newsletter's reply-to address"
    status: AbtestsSubjectListItemStatus | None = Field(default=None, alias="status")
    "Newsletter status"
    stage: AbtestsSubjectListItemStage | None = Field(default=None, alias="stage")
    "A/B test stage"
    delivery_settings: dict[str, Any] | None = Field(default=None, alias="deliverySettings")
    "The A/B test delivery settings"
    flags: list[AbtestsSubjectListItemFlagsItem] | None = Field(default=None, alias="flags")
    created_on: datetime | None = Field(default=None, alias="createdOn")
    "Date the A/B test was created on"
    updated_on: datetime | None = Field(default=None, alias="updatedOn")
    "Date A/B test was updated on"
    href: str | None = Field(default=None, alias="href")
    "Direct hyperlink to a resource"


class AbtestsSubjectStatistics(BaseModel):
    "AbtestsSubjectStatistics model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    delivered: int | None = Field(default=None, alias="delivered")
    "The total number of delivered messages"
    open_rate: float | None = Field(default=None, alias="openRate")
    "Percentage of messages that were opened"
    click_rate: float | None = Field(default=None, alias="clickRate")
    "Percentage of messages links that were clicked"


class Account(BaseModel):
    "Account model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    account_id: str | None = Field(default=None, alias="accountId")
    "Account ID"
    email: str | None = Field(default=None, alias="email")
    "Email"
    country_code: Any | None = Field(default=None, alias="countryCode")
    industry_tag: Any | None = Field(default=None, alias="industryTag")
    time_zone: Any | None = Field(default=None, alias="timeZone")
    href: str | None = Field(default=None, alias="href")
    "Direct URL to resource"
    first_name: str | None = Field(default=None, alias="firstName")
    "First name"
    last_name: str | None = Field(default=None, alias="lastName")
    "Last name"
    company_name: str | None = Field(default=None, alias="companyName")
    "Company name"
    phone: str | None = Field(default=None, alias="phone")
    "Phone number"
    state: str | None = Field(default=None, alias="state")
    "State"
    city: str | None = Field(default=None, alias="city")
    "City"
    street: str | None = Field(default=None, alias="street")
    "Street"
    zip_code: str | None = Field(default=None, alias="zipCode")
    "ZIP Code"
    number_of_employees: AccountNumberOfEmployees | None = Field(
        default=None, alias="numberOfEmployees"
    )
    "Numbers of employees"
    time_format: AccountTimeFormat | None = Field(default=None, alias="timeFormat")
    "Account time notation"


class AccountBadgeDetails(BaseModel):
    "AccountBadgeDetails model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    status: StatusEnum | None = Field(default=None, alias="status")
    "Current badge status"


class AccountBilling(BaseModel):
    "AccountBilling model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    list_size: str | None = Field(default=None, alias="listSize")
    "Billing plan maximum list size"
    payment_plan: AccountBillingPaymentPlan | None = Field(default=None, alias="paymentPlan")
    "Payment plan"
    subscription_price: int | None = Field(default=None, alias="subscriptionPrice")
    "Subscription price"
    renewal_date: datetime | None = Field(default=None, alias="renewalDate")
    "Subscription reneval date"
    currency_code: str | None = Field(default=None, alias="currencyCode")
    "Currency code compliant with ISO-4217"
    account_balance: str | None = Field(default=None, alias="accountBalance")
    "Account balance"
    price: int | None = Field(default=None, alias="price")
    "Price"
    payment_method: AccountBillingPaymentMethod | None = Field(default=None, alias="paymentMethod")
    "Payment method"
    credit_card: dict[str, Any] | None = Field(default=None, alias="creditCard")
    addons: list[dict[str, Any]] | None = Field(default=None, alias="addons")
    "Addons"


class AccountDetailsCountryCode(BaseModel):
    "AccountDetailsCountryCode model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    country_code_id: str | None = Field(default=None, alias="countryCodeId")
    "Country code ID"
    country_code: str | None = Field(default=None, alias="countryCode")
    "Country code"


class AccountSummaryReportDetails(BaseModel):
    "AccountSummaryReportDetails model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    custom_report_id: str | None = Field(default=None, alias="customReportId")
    "The custom report ID"
    name: str | None = Field(default=None, alias="name")
    "The custom report name"
    href: str | None = Field(default=None, alias="href")
    "The direct hyperlink to a resource"
    type_: Any | None = Field(default=None, alias="type")
    "The custom report type"
    scheduling: dict[str, Any] | None = Field(default=None, alias="scheduling")
    "Parameters responsible for defining the reporting period"
    files: list[dict[str, Any]] | None = Field(default=None, alias="files")
    "Files that have been generated for the given report"
    created_at: datetime | None = Field(default=None, alias="createdAt")
    "Custom report creation date"
    generated_at: datetime | None = Field(default=None, alias="generatedAt")
    "Custom report generation date"
    filters: dict[str, Any] | None = Field(default=None, alias="filters")
    "Filters used to narrow down the report data"


class AccountsLoginHistoryListElement(BaseModel):
    "AccountsLoginHistoryListElement model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    login_time: datetime | None = Field(default=None, alias="loginTime")
    "Login time"
    logout_time: datetime | None = Field(default=None, alias="logoutTime")
    "Logout time"
    is_successful: Any | None = Field(default=None, alias="isSuccessful")
    "Login was successful"
    ip: str | None = Field(default=None, alias="ip")
    "IP address"


class Address(BaseModel):
    "Address model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    created_on: datetime | None = Field(default=None, alias="createdOn")
    "The creation date"
    updated_on: datetime | None = Field(default=None, alias="updatedOn")
    "The date of the last update"
    address_id: str | None = Field(default=None, alias="addressId")
    href: str | None = Field(default=None, alias="href")
    "Direct hyperlink to a resource"
    country_code: str | None = Field(default=None, alias="countryCode")
    "The country code (ISO 3166-1 alpha-3)"
    country_name: str | None = Field(default=None, alias="countryName")
    "The country name, based on `countryCode`"
    name: str | None = Field(default=None, alias="name")
    first_name: str | None = Field(default=None, alias="firstName")
    last_name: str | None = Field(default=None, alias="lastName")
    address1: str | None = Field(default=None, alias="address1")
    "Address line 1"
    address2: str | None = Field(default=None, alias="address2")
    "Address line 2"
    city: str | None = Field(default=None, alias="city")
    zip: str | None = Field(default=None, alias="zip")
    "The ZIP/postal code, free text"
    province: str | None = Field(default=None, alias="province")
    province_code: str | None = Field(default=None, alias="provinceCode")
    "The province code, free text"
    phone: str | None = Field(default=None, alias="phone")
    "The phone number, free text"
    company: str | None = Field(default=None, alias="company")
    "The company name, free text"


class Autoresponder(BaseModel):
    "Autoresponder model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    autoresponder_id: str | None = Field(default=None, alias="autoresponderId")
    "The autoresponder ID"
    href: str | None = Field(default=None, alias="href")
    "Direct hyperlink to a resource"
    name: str | None = Field(default=None, alias="name")
    "The autoresponder name"
    subject: str | None = Field(default=None, alias="subject")
    "The autoresponder message subject"
    campaign_id: str | None = Field(default=None, alias="campaignId")
    "The campaign ID. The system will assign the autoresponder to a default campaign if you don't provide a specific campaign ID."
    status: Any | None = Field(default=None, alias="status")
    "The autoresponder status"
    from_field: Any | None = Field(default=None, alias="fromField")
    "The from email address used for the message"
    reply_to: Any | None = Field(default=None, alias="replyTo")
    "The email that will be used as a reply-to address"
    content: MessageContent | None = Field(default=None, alias="content")
    flags: list[MessageFlagsArrayItem] | None = Field(default=None, alias="flags")
    trigger_settings: Any | None = Field(default=None, alias="triggerSettings")
    "The conditions that will trigger the autoresponder"
    statistics: dict[str, Any] | None = Field(default=None, alias="statistics")
    "The autoresponder statistics summary"
    created_on: datetime | None = Field(default=None, alias="createdOn")
    "The creation date"


class AutoresponderDayCondition(BaseModel):
    "To find the autoresponder cycle day of a contact."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    condition_type: AutoresponderDayConditionConditionType = Field(alias="conditionType")
    operator_type: AutoresponderDayConditionOperatorType = Field(alias="operatorType")
    operator: dict[str, Any] = Field(alias="operator")
    value: int | None = Field(default=None, alias="value")
    "The autoresponder cycle day value. The field is prohibited for the operators assigned and not_assigned."


class AutoresponderDetails(BaseModel):
    "AutoresponderDetails model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    autoresponder_id: str | None = Field(default=None, alias="autoresponderId")
    "The autoresponder ID"
    href: str | None = Field(default=None, alias="href")
    "Direct hyperlink to a resource"
    name: str | None = Field(default=None, alias="name")
    "The autoresponder name"
    subject: str | None = Field(default=None, alias="subject")
    "The autoresponder message subject"
    campaign_id: str | None = Field(default=None, alias="campaignId")
    "The campaign ID. The system will assign the autoresponder to a default campaign if you don't provide a specific campaign ID."
    status: Any | None = Field(default=None, alias="status")
    "The autoresponder status"
    from_field: Any | None = Field(default=None, alias="fromField")
    "The from email address used for the message"
    reply_to: Any | None = Field(default=None, alias="replyTo")
    "The email that will be used as a reply-to address"
    content: MessageContent | None = Field(default=None, alias="content")
    flags: list[MessageFlagsArrayItem] | None = Field(default=None, alias="flags")
    trigger_settings: Any | None = Field(default=None, alias="triggerSettings")
    "The conditions that will trigger the autoresponder"
    statistics: dict[str, Any] | None = Field(default=None, alias="statistics")
    "The autoresponder statistics summary"
    created_on: datetime | None = Field(default=None, alias="createdOn")
    "The creation date"
    click_tracks: list[ClickTrack] | None = Field(default=None, alias="clickTracks")
    "The list of tracked links"
    campaign: Any | None = Field(default=None, alias="campaign")
    "The autoresponder campaign (list)"
    editor: Any | None = Field(default=None, alias="editor")
    send_settings: dict[str, Any] | None = Field(default=None, alias="sendSettings")


class AutoresponderSendCustomSettings(BaseModel):
    "AutoresponderSendCustomSettings model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    type_: AutoresponderSendSettingsType = Field(alias="type")
    time_travel: str | None = Field(default=None, alias="timeTravel")
    excluded_days_of_week: list[AutoresponderSendSettingsExcludedDaysOfWeekItem] | None = Field(
        default=None, alias="excludedDaysOfWeek"
    )
    external_lexpad: ExternalLexpad | None = Field(default=None, alias="externalLexpad")
    send_at_hour: int = Field(alias="sendAtHour")


class AutoresponderSendDelaySettings(BaseModel):
    "AutoresponderSendDelaySettings model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    type_: AutoresponderSendSettingsType = Field(alias="type")
    time_travel: str | None = Field(default=None, alias="timeTravel")
    excluded_days_of_week: list[AutoresponderSendSettingsExcludedDaysOfWeekItem] | None = Field(
        default=None, alias="excludedDaysOfWeek"
    )
    external_lexpad: ExternalLexpad | None = Field(default=None, alias="externalLexpad")
    delay_in_hours: int = Field(alias="delayInHours")


class AutoresponderSendImmediatelySettings(BaseModel):
    "AutoresponderSendImmediatelySettings model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    type_: AutoresponderSendSettingsType = Field(alias="type")
    time_travel: str | None = Field(default=None, alias="timeTravel")
    excluded_days_of_week: list[AutoresponderSendSettingsExcludedDaysOfWeekItem] | None = Field(
        default=None, alias="excludedDaysOfWeek"
    )
    external_lexpad: ExternalLexpad | None = Field(default=None, alias="externalLexpad")


class AutoresponderSendSettingsInput(BaseModel):
    "How the message will be delivered to the subscriber"

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    type_: AutoresponderSendSettingsType = Field(alias="type")
    time_travel: str | None = Field(default=None, alias="timeTravel")
    excluded_days_of_week: list[AutoresponderSendSettingsExcludedDaysOfWeekItem] | None = Field(
        default=None, alias="excludedDaysOfWeek"
    )
    external_lexpad: ExternalLexpad | None = Field(default=None, alias="externalLexpad")


class AutoresponderSendSettingsOutput(BaseModel):
    "How the message will be delivered to the subscriber"

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    type_: AutoresponderSendSettingsType | None = Field(default=None, alias="type")
    time_travel: str | None = Field(default=None, alias="timeTravel")
    excluded_days_of_week: list[AutoresponderSendSettingsExcludedDaysOfWeekItem] | None = Field(
        default=None, alias="excludedDaysOfWeek"
    )
    delay_in_hours: int | None = Field(default=None, alias="delayInHours")
    send_at_hour: int | None = Field(default=None, alias="sendAtHour")
    recurrence: Any | None = Field(default=None, alias="recurrence")


class AutoresponderSendSignupSettings(BaseModel):
    "AutoresponderSendSignupSettings model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    type_: AutoresponderSendSettingsType = Field(alias="type")
    time_travel: str | None = Field(default=None, alias="timeTravel")
    excluded_days_of_week: list[AutoresponderSendSettingsExcludedDaysOfWeekItem] | None = Field(
        default=None, alias="excludedDaysOfWeek"
    )
    external_lexpad: ExternalLexpad | None = Field(default=None, alias="externalLexpad")


class AutoresponderTriggerSettings(BaseModel):
    "The conditions that will trigger the autoresponder"

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    type_: str | None = Field(default=None, alias="type")
    "The trigger type"
    day_of_cycle: int | None = Field(default=None, alias="dayOfCycle")
    "For onday type the day of the autoresponder cycle in the 0-9999 format"
    autoresponder: str | None = Field(default=None, alias="autoresponder")
    newsletter: str | None = Field(default=None, alias="newsletter")
    click_track_id: str | None = Field(default=None, alias="clickTrackId")
    goal: str | None = Field(default=None, alias="goal")
    custom: str | None = Field(default=None, alias="custom")
    new_custom_value: str | None = Field(default=None, alias="newCustomValue")
    action: str | None = Field(default=None, alias="action")
    selected_campaigns: Any | None = Field(default=None, alias="selectedCampaigns")
    selected_segments: Any | None = Field(default=None, alias="selectedSegments")


class BaseCampaign(BaseModel):
    "BaseCampaign model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    campaign_id: str | None = Field(default=None, alias="campaignId")
    "Unique identifier of the campaign (contact list)"
    name: str | None = Field(default=None, alias="name")
    "The campaign (list) name. * You can use each list name just once in your account. * The name must be between 3-64 characters. * All alphabets supported by GetResponse, including right-to-left ones, are allowed. * You can use upper and lower case letters, numbers, spaces and special characters apart from the ones listed below. * You can’t use emojis and the following special characters: `/`, `\\`, `@`, and `[` or `]`."
    tech_name: str | None = Field(default=None, alias="techName")
    "Tech name is a unique internal ID of a list used for [FTP imports](https://www.getresponse.com/help/how-to-import-files-via-ftp.html) (available in GetResponse MAX accounts only)"
    language_code: str | None = Field(default=None, alias="languageCode")
    "The campaign language code according to ISO 639-1, plus: zt - Chinese (Traditional), fs - Afghan Persian (Dari), md - Moldavian"
    is_default: Any | None = Field(default=None, alias="isDefault")
    "Is the campaign default"
    created_on: datetime | None = Field(default=None, alias="createdOn")
    "The date of creation"
    href: str | None = Field(default=None, alias="href")
    "Direct hyperlink to a resource"


class BaseCategory(BaseModel):
    "BaseCategory model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    category_id: str | None = Field(default=None, alias="categoryId")
    "The category ID"
    href: str | None = Field(default=None, alias="href")
    "Direct hyperlink to a resource"
    name: str | None = Field(default=None, alias="name")
    "The name of the category"
    parent_id: str | None = Field(default=None, alias="parentId")
    "The parent category ID"
    is_default: bool | None = Field(default=None, alias="isDefault")
    "This is a default category"
    url: str | None = Field(default=None, alias="url")
    "The external URL to the category"
    external_id: str | None = Field(default=None, alias="externalId")
    "The external ID is the identifying string or number of the category given by another software"


class BaseCreateCustomReport(BaseModel):
    "BaseCreateCustomReport model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    name: str = Field(alias="name")
    "The custom report name"
    type_: BaseCreateCustomReportType = Field(alias="type")
    "The custom report type"
    scheduling: dict[str, Any] = Field(alias="scheduling")
    "Parameters responsible for defining the reporting period"


class BaseFile(BaseModel):
    "BaseFile model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    name: str | None = Field(default=None, alias="name")
    "The file name"
    extension: str | None = Field(default=None, alias="extension")
    "The file extension"
    folder: dict[str, Any] | None = Field(default=None, alias="folder")
    "The folder where the file is stored"


class BaseLandingPage(BaseModel):
    "BaseLandingPage model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    landing_page_id: str | None = Field(default=None, alias="landingPageId")
    "The landing page ID"
    href: str | None = Field(default=None, alias="href")
    "Direct hyperlink to a resource"
    meta_title: str | None = Field(default=None, alias="metaTitle")
    "The landing page meta title property"
    domain: str | None = Field(default=None, alias="domain")
    "The domain where the landing page is hosted"
    subdomain: str | None = Field(default=None, alias="subdomain")
    "The subdomain where the landing page is assigned"
    user_domain: str | None = Field(default=None, alias="userDomain")
    "The private domain provided by the user"
    user_domain_path: str | None = Field(default=None, alias="userDomainPath")
    "The private domain path provided by the user"
    campaign: Any | None = Field(default=None, alias="campaign")
    "The campaign to which the landing page is linked"
    status: Any | None = Field(default=None, alias="status")
    "The landing page status"
    user_domain_status: BaseLandingPageUserDomainStatus | None = Field(
        default=None, alias="userDomainStatus"
    )
    "The DNS status for the user's private domain. Can be `null` if a private domain isn't assigned."
    test_ab: Any | None = Field(default=None, alias="testAB")
    "Does the landing page have AB testing (variants) enabled"
    created_on: datetime | None = Field(default=None, alias="createdOn")
    "The creation date"
    updated_on: datetime | None = Field(default=None, alias="updatedOn")
    "The date of the last page update"


class BaseMetaField(BaseModel):
    "BaseMetaField model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    href: str | None = Field(default=None, alias="href")
    "Direct hyperlink to a resource"
    meta_field_id: str | None = Field(default=None, alias="metaFieldId")
    "The meta field ID"
    name: str | None = Field(default=None, alias="name")
    "The meta field name"
    value: str | None = Field(default=None, alias="value")
    "The meta field value"
    value_type: BaseMetaFieldValueType | None = Field(default=None, alias="valueType")
    "The value type enumerable"
    description: str | None = Field(default=None, alias="description")
    "The meta field description"


class BaseProductVariant(BaseModel):
    "BaseProductVariant model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    variant_id: str | None = Field(default=None, alias="variantId")
    "The product ID"
    href: str | None = Field(default=None, alias="href")
    "Direct hyperlink to a resource"
    name: str | None = Field(default=None, alias="name")
    "The product name"
    url: str | None = Field(default=None, alias="url")
    "The external URL to the product variant"
    sku: str | None = Field(default=None, alias="sku")
    "The stock-keeping unit of a variant. Must be unique within the product"
    price: float | None = Field(default=None, alias="price")
    "The price"
    price_tax: float | None = Field(default=None, alias="priceTax")
    "The price including tax"
    previous_price: float | None = Field(default=None, alias="previousPrice")
    "The price before the change"
    previous_price_tax: float | None = Field(default=None, alias="previousPriceTax")
    "The price before the change including tax"
    quantity: int | None = Field(default=None, alias="quantity")
    "The quantity of variant items"
    position: int | None = Field(default=None, alias="position")
    "The position of a variant"
    barcode: str | None = Field(default=None, alias="barcode")
    "The barcode of a variant"
    external_id: str | None = Field(default=None, alias="externalId")
    "The external ID is the identifying string or number of the variant given by another software"
    description: str | None = Field(default=None, alias="description")
    "The description of a variant"
    images: list[NewProductVariantImage] | None = Field(default=None, alias="images")
    meta_fields: list[NewMetaField] | None = Field(default=None, alias="metaFields")
    taxes: list[NewTax] | None = Field(default=None, alias="taxes")


class BaseSearchContacts(BaseModel):
    "The short description of a saved search."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    search_contact_id: str | None = Field(default=None, alias="searchContactId")
    "The unique search-contact identifier"
    name: str | None = Field(default=None, alias="name")
    "The unique name of search-contact"
    created_on: datetime | None = Field(default=None, alias="createdOn")
    "The UTC date time format ISO 8601, e.g. 2018-04-10T10:02:57+0000"
    href: str | None = Field(default=None, alias="href")
    "Direct hyperlink to a resource"


class BaseSearchContactsDetails(BaseModel):
    "BaseSearchContactsDetails model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    search_contact_id: str = Field(alias="searchContactId")
    "The unique search-contact identifier"
    name: str | None = Field(default=None, alias="name")
    "The unique name of search-contact"
    created_on: datetime | None = Field(default=None, alias="createdOn")
    "The UTC date time format ISO 8601, e.g. 2018-04-10T10:02:57+0000"
    href: str | None = Field(default=None, alias="href")
    "Direct hyperlink to a resource"


class BaseSendSms(BaseModel):
    "BaseSendSms model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    name: str = Field(alias="name")
    "The SMS message name"
    content: str = Field(alias="content")
    "The SMS message content"
    recipients_type: BaseSendSmsRecipientsType = Field(alias="recipientsType")
    "The recipient type. To send a text message to contacts in your list, select `contacts`. To message contacts who are not in any of your lists, select `importedNumbers`"


class BaseSuppression(BaseModel):
    "BaseSuppression model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    name: str | None = Field(default=None, alias="name")
    "The name of the suppression list"
    masks: list[str] | None = Field(default=None, alias="masks")


class BaseTag(BaseModel):
    "BaseTag model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    name: str | None = Field(default=None, alias="name")
    "The tag name"
    color: str | None = Field(default=None, alias="color")
    "The tag color (deprecated)"


class BaseTax(BaseModel):
    "BaseTax model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    tax_id: str | None = Field(default=None, alias="taxId")
    "The tax ID"
    href: str | None = Field(default=None, alias="href")
    "Direct hyperlink to a resource"
    name: str | None = Field(default=None, alias="name")
    "The tax name"
    rate: float | None = Field(default=None, alias="rate")
    "The rate value"


class Blocklist(BaseModel):
    "Blocklist model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    masks: list[str] | None = Field(default=None, alias="masks")


class BouncesReportDetails(BaseModel):
    "BouncesReportDetails model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    custom_report_id: str | None = Field(default=None, alias="customReportId")
    "The custom report ID"
    name: str | None = Field(default=None, alias="name")
    "The custom report name"
    href: str | None = Field(default=None, alias="href")
    "The direct hyperlink to a resource"
    type_: Any | None = Field(default=None, alias="type")
    "The custom report type"
    scheduling: dict[str, Any] | None = Field(default=None, alias="scheduling")
    "Parameters responsible for defining the reporting period"
    files: list[dict[str, Any]] | None = Field(default=None, alias="files")
    "Files that have been generated for the given report"
    created_at: datetime | None = Field(default=None, alias="createdAt")
    "Custom report creation date"
    generated_at: datetime | None = Field(default=None, alias="generatedAt")
    "Custom report generation date"
    filters: dict[str, Any] | None = Field(default=None, alias="filters")
    "Filters used to narrow down the report data"


class Callback(BaseModel):
    "Callback model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    url: Any | None = Field(default=None, alias="url")
    "URL to use to post notifications"
    actions: CallbackActions | None = Field(default=None, alias="actions")


class CallbackActions(BaseModel):
    "CallbackActions model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    open: bool | None = Field(default=None, alias="open")
    "Is `open` callback enabled"
    click: bool | None = Field(default=None, alias="click")
    "Is `click` callback enabled"
    subscribe: bool | None = Field(default=None, alias="subscribe")
    "Is `subscribe` callback enabled"
    unsubscribe: bool | None = Field(default=None, alias="unsubscribe")
    "Is `unsubscribe` callback enabled"
    survey: bool | None = Field(default=None, alias="survey")
    "Is `survey` callback enabled"


class Campaign(BaseModel):
    "Campaign model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    campaign_id: str | None = Field(default=None, alias="campaignId")
    "Unique identifier of the campaign (contact list)"
    name: str = Field(alias="name")
    "The campaign (list) name. * You can use each list name just once in your account. * The name must be between 3-64 characters. * All alphabets supported by GetResponse, including right-to-left ones, are allowed. * You can use upper and lower case letters, numbers, spaces and special characters apart from the ones listed below. * You can’t use emojis and the following special characters: `/`, `\\`, `@`, and `[` or `]`."
    tech_name: str | None = Field(default=None, alias="techName")
    "Tech name is a unique internal ID of a list used for [FTP imports](https://www.getresponse.com/help/how-to-import-files-via-ftp.html) (available in GetResponse MAX accounts only)"
    language_code: str | None = Field(default=None, alias="languageCode")
    "The campaign language code according to ISO 639-1, plus: zt - Chinese (Traditional), fs - Afghan Persian (Dari), md - Moldavian"
    is_default: Any | None = Field(default=None, alias="isDefault")
    "Is the campaign default"
    created_on: datetime | None = Field(default=None, alias="createdOn")
    "The date of creation"
    href: str | None = Field(default=None, alias="href")
    "Direct hyperlink to a resource"
    postal: CampaignPostal | None = Field(default=None, alias="postal")
    confirmation: CampaignConfirmation | None = Field(default=None, alias="confirmation")
    optin_types: CampaignOptinTypes | None = Field(default=None, alias="optinTypes")
    subscription_notifications: CampaignSubscriptionNotifications | None = Field(
        default=None, alias="subscriptionNotifications"
    )
    profile: CampaignProfile | None = Field(default=None, alias="profile")


class CampaignAdditionalProperties(BaseModel):
    "CampaignAdditionalProperties model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    postal: CampaignPostal | None = Field(default=None, alias="postal")
    confirmation: CampaignConfirmation | None = Field(default=None, alias="confirmation")
    optin_types: CampaignOptinTypes | None = Field(default=None, alias="optinTypes")
    subscription_notifications: CampaignSubscriptionNotifications | None = Field(
        default=None, alias="subscriptionNotifications"
    )
    profile: CampaignProfile | None = Field(default=None, alias="profile")


class CampaignConfirmation(BaseModel):
    "CampaignConfirmation model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    from_field: FromFieldReference | None = Field(default=None, alias="fromField")
    redirect_type: CampaignConfirmationRedirectType | None = Field(
        default=None, alias="redirectType"
    )
    "What will happen after email confirmation. The values allowed include: hosted (the subscriber will stay on the default GetResponse website), customUrl (the subscriber will be redirected to a custom URL provided by the user)."
    mime_type: CampaignConfirmationMimeType | None = Field(default=None, alias="mimeType")
    "The MIME type for the confirmation message"
    redirect_url: str | None = Field(default=None, alias="redirectUrl")
    "Required if the redirectType is customUrl. The URL a subscriber will be redirected to if the redirectType is set to customUrl."
    reply_to: FromFieldReference | None = Field(default=None, alias="replyTo")
    subscription_confirmation_body_id: str | None = Field(
        default=None, alias="subscriptionConfirmationBodyId"
    )
    "The subscription confirmation body ID"
    subscription_confirmation_subject_id: str | None = Field(
        default=None, alias="subscriptionConfirmationSubjectId"
    )
    "Subscription confirmation subject ID"


class CampaignListElement(BaseModel):
    "CampaignListElement model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    campaign_id: str | None = Field(default=None, alias="campaignId")
    "Unique identifier of the campaign (contact list)"
    name: str | None = Field(default=None, alias="name")
    "The campaign (list) name. * You can use each list name just once in your account. * The name must be between 3-64 characters. * All alphabets supported by GetResponse, including right-to-left ones, are allowed. * You can use upper and lower case letters, numbers, spaces and special characters apart from the ones listed below. * You can’t use emojis and the following special characters: `/`, `\\`, `@`, and `[` or `]`."
    tech_name: str | None = Field(default=None, alias="techName")
    "Tech name is a unique internal ID of a list used for [FTP imports](https://www.getresponse.com/help/how-to-import-files-via-ftp.html) (available in GetResponse MAX accounts only)"
    language_code: str | None = Field(default=None, alias="languageCode")
    "The campaign language code according to ISO 639-1, plus: zt - Chinese (Traditional), fs - Afghan Persian (Dari), md - Moldavian"
    is_default: Any | None = Field(default=None, alias="isDefault")
    "Is the campaign default"
    created_on: datetime | None = Field(default=None, alias="createdOn")
    "The date of creation"
    href: str | None = Field(default=None, alias="href")
    "Direct hyperlink to a resource"
    description: str | None = Field(default=None, alias="description")
    "It's the same as the campaign name, kept for compatibility reasons"


class CampaignListSizesStatisticsElement(BaseModel):
    "CampaignListSizesStatisticsElement model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    total_subscribers: int | None = Field(default=None, alias="totalSubscribers")
    "The total amount of subscribers for a given datetime and grouping"
    added_subscribers: int | None = Field(default=None, alias="addedSubscribers")
    "The amount of subscribers added since the previous statistics frame"
    removed_subscribers: int | None = Field(default=None, alias="removedSubscribers")
    "The amount of subscribers removed since the previous statistics frame"
    created_on: str | None = Field(default=None, alias="createdOn")
    "The statistics frame timestamp. The value depends on the groupBy parameter. For the hour, use datetime in the format YYYY-mm-dd HH:mm:ss; for the day, use date in the format YYYY-mm-dd; for the month, use a string in the format YYYY-mm; and for the total, use the string total."


class CampaignOptinTypes(BaseModel):
    "CampaignOptinTypes model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    email: CampaignOptinTypesEmail | None = Field(default=None, alias="email")
    "Single opt-in: confirmed opt-in disabled. Double opt-in: confirmed opt-in enabled. You can find more information [here](https://www.getresponse.com/resources/glossary/confirmed-opt-in.html)"
    api: CampaignOptinTypesApi | None = Field(default=None, alias="api")
    "Single opt-in: confirmed opt-in disabled. Double opt-in: confirmed opt-in enabled. You can find more information [here](https://www.getresponse.com/resources/glossary/confirmed-opt-in.html)"
    import_: CampaignOptinTypesImport | None = Field(default=None, alias="import")
    "Single opt-in: confirmed opt-in disabled. Double opt-in: confirmed opt-in enabled. You can find more information [here](https://www.getresponse.com/resources/glossary/confirmed-opt-in.html)"
    webform: CampaignOptinTypesWebform | None = Field(default=None, alias="webform")
    "Single opt-in: confirmed opt-in disabled. Double opt-in: confirmed opt-in enabled. You can find more information [here](https://www.getresponse.com/resources/glossary/confirmed-opt-in.html)"


class CampaignPostal(BaseModel):
    "CampaignPostal model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    add_postal_to_messages: Any | None = Field(default=None, alias="addPostalToMessages")
    "Should the postal address be included in all message footers for this campaign (mandatory for Canada and the US)"
    city: str | None = Field(default=None, alias="city")
    "The city, free-text"
    company_name: str | None = Field(default=None, alias="companyName")
    "The company name, free-text"
    country: str | None = Field(default=None, alias="country")
    "The country name, free-text"
    design: str | None = Field(default=None, alias="design")
    "How the postal address will display in messages. The available fields include: [[name]], [[address]], [[city]], [[state]] [[zip]], [[country]]"
    state: str | None = Field(default=None, alias="state")
    "The state, free-text"
    street: str | None = Field(default=None, alias="street")
    "The street, free-text"
    zip_code: str | None = Field(default=None, alias="zipCode")
    "The ZIP code"


class CampaignProfile(BaseModel):
    "CampaignProfile model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    description: str | None = Field(default=None, alias="description")
    "The campaign description"
    industry_tag_id: str | None = Field(default=None, alias="industryTagId")
    "The industry tag ID"
    logo: str | None = Field(default=None, alias="logo")
    "The logo URL"
    logo_link_url: str | None = Field(default=None, alias="logoLinkUrl")
    "The logo link URL"
    title: str | None = Field(default=None, alias="title")
    "The profile title"


class CampaignReference(BaseModel):
    "CampaignReference model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    campaign_id: str = Field(alias="campaignId")
    "Campaign ID"
    href: str | None = Field(default=None, alias="href")
    "Direct hyperlink to a resource"
    name: str | None = Field(default=None, alias="name")
    "The campaign name"


class CampaignSubscriptionNotifications(BaseModel):
    "CampaignSubscriptionNotifications model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    status: Any | None = Field(default=None, alias="status")
    "Are notifications enabled. Possible values include: enabled, disabled."
    recipients: list[FromFieldReference] | None = Field(default=None, alias="recipients")


class CampaignSubscriptionStatisticsItem(BaseModel):
    "CampaignSubscriptionStatisticsItem model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    import_: int | None = Field(default=None, alias="import")
    email: int | None = Field(default=None, alias="email")
    www: int | None = Field(default=None, alias="www")
    panel: int | None = Field(default=None, alias="panel")
    leads: int | None = Field(default=None, alias="leads")
    sale: int | None = Field(default=None, alias="sale")
    api: int | None = Field(default=None, alias="api")
    forward: int | None = Field(default=None, alias="forward")
    survey: int | None = Field(default=None, alias="survey")
    mobile: int | None = Field(default=None, alias="mobile")
    copy_: int | None = Field(default=None, alias="copy")
    landing_page: int | None = Field(default=None, alias="landing_page")
    webinar: int | None = Field(default=None, alias="webinar")
    premium_newsletter: int | None = Field(default=None, alias="premium_newsletter")
    course: int | None = Field(default=None, alias="course")
    website_buider_elegant: int | None = Field(default=None, alias="website_buider_elegant")
    chat: int | None = Field(default=None, alias="chat")
    summary: int | None = Field(default=None, alias="summary")


class Cart(BaseModel):
    "Cart model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    created_on: datetime | None = Field(default=None, alias="createdOn")
    "The creation date"
    updated_on: datetime | None = Field(default=None, alias="updatedOn")
    "The date of the last update"
    cart_id: str | None = Field(default=None, alias="cartId")
    "The contact ID"
    href: str | None = Field(default=None, alias="href")
    "Direct hyperlink to a resource"
    contact_id: str | None = Field(default=None, alias="contactId")
    "The ID of the contact that the cart belongs to. You must first create the contact using POST /v3/contacts, or if it already exists, using GET /v3/contacts"
    total_price: float | None = Field(default=None, alias="totalPrice")
    "The total cart price, tax excluded"
    total_tax_price: float | None = Field(default=None, alias="totalTaxPrice")
    "The total cart price, tax included"
    currency: str | None = Field(default=None, alias="currency")
    "The currency code (ISO 4217)"
    selected_variants: list[NewCartSelectedProductVariant] | None = Field(
        default=None, alias="selectedVariants"
    )
    external_id: str | None = Field(default=None, alias="externalId")
    "The external ID is the identifying string or number of the cart, given by another software"
    cart_url: str | None = Field(default=None, alias="cartUrl")
    "The external cart URL"


class Category(BaseModel):
    "Category model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    category_id: str | None = Field(default=None, alias="categoryId")
    "The category ID"
    href: str | None = Field(default=None, alias="href")
    "Direct hyperlink to a resource"
    name: str | None = Field(default=None, alias="name")
    "The name of the category"
    parent_id: str | None = Field(default=None, alias="parentId")
    "The parent category ID"
    is_default: bool | None = Field(default=None, alias="isDefault")
    "This is a default category"
    url: str | None = Field(default=None, alias="url")
    "The external URL to the category"
    external_id: str | None = Field(default=None, alias="externalId")
    "The external ID is the identifying string or number of the category given by another software"
    created_on: datetime | None = Field(default=None, alias="createdOn")
    "The creation date"
    updated_on: datetime | None = Field(default=None, alias="updatedOn")
    "The date of the last update"


class ChooseWinnerAbtestsSubject(BaseModel):
    "ChooseWinnerAbtestsSubject model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    variant_id: str = Field(alias="variantId")
    "The message variant ID. A variant identifier from https://apireference.getresponse.com/#operation/getAbtestsSubjectById."


class ClickTrack(BaseModel):
    "ClickTrack model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    click_track_id: str | None = Field(default=None, alias="clickTrackId")
    url: str | None = Field(default=None, alias="url")
    "The tracked link"
    name: str | None = Field(default=None, alias="name")
    "The tracked link name"
    amount: str | None = Field(default=None, alias="amount")
    "The number of clicks on a link in a message"


class ClickTrackMessage(BaseModel):
    "The source message reference for a click track"

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    resource_id: str | None = Field(default=None, alias="resourceId")
    "The ID identifying message resource"
    type_: ClickTrackMessageType | None = Field(default=None, alias="type")
    "The message type"
    created_on: datetime | None = Field(default=None, alias="createdOn")
    "The message creation date"
    resource_type: ClickTrackMessageResourceType | None = Field(default=None, alias="resourceType")
    "Type of the resource that represents the message in the API"
    href: str | None = Field(default=None, alias="href")
    "Direct URL to the resource that represents the message"


class ClickTrackResource(BaseModel):
    "ClickTrackResource model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    click_track_id: str | None = Field(default=None, alias="clickTrackId")
    name: str | None = Field(default=None, alias="name")
    "The name (label) of a click track"
    url: str | None = Field(default=None, alias="url")
    "The link URL of a click track"
    clicks: int | None = Field(default=None, alias="clicks")
    "The number of clicks counted for a click track"
    message: ClickTrackMessage | None = Field(default=None, alias="message")
    href: str | None = Field(default=None, alias="href")
    "Direct hyperlink to a resource"


class ConditionMessageOperator(BaseModel):
    "The operator allows searching by message type."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    operator_type: ConditionMessageOperatorOperatorType = Field(alias="operatorType")
    operator: MessageTypeOperator = Field(alias="operator")
    value: str = Field(alias="value")
    "The identifier of a selected resource: autoresponder, newsletter, split test or automation message"


class ConditionStringOperator(BaseModel):
    "ConditionStringOperator model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    operator_type: ConditionStringOperatorOperatorType = Field(alias="operatorType")
    operator: ConditionStringOperatorOperator = Field(alias="operator")
    value: str = Field(alias="value")


class ConditionType(BaseModel):
    "ConditionType model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    condition_type: ConditionTypeConditionType = Field(alias="conditionType")


class Contact(BaseModel):
    "Contact model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    contact_id: str = Field(alias="contactId")
    name: str | None = Field(default=None, alias="name")
    origin: ContactOrigin | None = Field(default=None, alias="origin")
    time_zone: str | None = Field(default=None, alias="timeZone")
    "The time zone of a contact, uses the time zone database format (https://www.iana.org/time-zones)"
    activities: str | None = Field(default=None, alias="activities")
    changed_on: datetime | None = Field(default=None, alias="changedOn")
    created_on: datetime | None = Field(default=None, alias="createdOn")
    campaign: CampaignReference | None = Field(default=None, alias="campaign")
    email: str = Field(alias="email")
    day_of_cycle: str | None = Field(default=None, alias="dayOfCycle")
    "The day on which the contact is in the Autoresponder cycle. `null` indicates the contacts is not in the cycle."
    scoring: float | None = Field(default=None, alias="scoring")
    "Contact scoring, pass null to remove the score from a contact"
    engagement_score: int | None = Field(default=None, alias="engagementScore")
    "Engagement Score is a feature that presents a visual estimate of a contact's engagement with mailings. The score is based on the contact's interactions with your e-mails. Via API, it's returned in the form of numbers ranging from 1 (Not Engaged) to 5 (Highly Engaged)."
    href: str = Field(alias="href")
    "Direct hyperlink to a resource"


class ContactActivity(BaseModel):
    "ContactActivity model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    activity: ContactActivityActivity | None = Field(default=None, alias="activity")
    "The type of activity"
    subject: str | None = Field(default=None, alias="subject")
    created_on: datetime | None = Field(default=None, alias="createdOn")
    "The activity date"
    preview_url: str | None = Field(default=None, alias="previewUrl")
    "This is only available for the `send` activity. It includes a link to the message preview"
    resource: ContactActivityResource | None = Field(default=None, alias="resource")
    click_track: ContactActivityClickTrack | None = Field(default=None, alias="clickTrack")
    "This is only available for the `click` activity. It includes the clicked link data"


class ContactActivityClickTrack(BaseModel):
    "ContactActivityClickTrack model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    id: str | None = Field(default=None, alias="id")
    "The click tracking ID"
    name: str | None = Field(default=None, alias="name")
    "The name of the clicked link"
    url: str | None = Field(default=None, alias="url")
    "The URL of the clicked link"


class ContactActivityResource(BaseModel):
    "ContactActivityResource model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    resource_id: str | None = Field(default=None, alias="resourceId")
    resource_type: ContactActivityResourceResourceType | None = Field(
        default=None, alias="resourceType"
    )
    href: str | None = Field(default=None, alias="href")
    "Direct hyperlink to a resource"


class ContactConsent(BaseModel):
    "ContactConsent model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    consent_id: str | None = Field(default=None, alias="consentId")
    "The unique identifier of the consent field."
    name: str | None = Field(default=None, alias="name")
    "The name of the consent field."
    content: str | None = Field(default=None, alias="content")
    "The actual text content of the consent field."
    is_granted: bool | None = Field(default=None, alias="isGranted")
    "Information whether the consent field is currently granted (true) or not (false)."
    history: list[ContactConsentHistoryItem] | None = Field(default=None, alias="history")
    "The history of changes to the consent field text."


class ContactConsentHistoryItem(BaseModel):
    "ContactConsentHistoryItem model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    content: str | None = Field(default=None, alias="content")
    "The text content of the consent field."
    was_granted: bool | None = Field(default=None, alias="wasGranted")
    "Information whether the consent field was granted."
    declared_at: datetime | None = Field(default=None, alias="declaredAt")
    "The date and time when the consent field status was declared by the contact (ISO 8601)."
    created_at: datetime | None = Field(default=None, alias="createdAt")
    "The date and time when this consent field version was created (ISO 8601)."


class ContactCustomField(BaseModel):
    "ContactCustomField model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    custom_field_id: str | None = Field(default=None, alias="customFieldId")
    values: list[str] | None = Field(default=None, alias="values")


class ContactCustomFieldValue(BaseModel):
    "ContactCustomFieldValue model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    custom_field_id: str = Field(alias="customFieldId")
    "Custom field ID"
    name: str = Field(alias="name")
    value: list[str] = Field(alias="value")
    values: list[str] = Field(alias="values")
    type_: str = Field(alias="type")
    field_type: str | None = Field(default=None, alias="fieldType")
    value_type: str | None = Field(default=None, alias="valueType")


class ContactDetails(BaseModel):
    "ContactDetails model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    contact_id: str = Field(alias="contactId")
    name: str | None = Field(default=None, alias="name")
    origin: ContactDetailsOrigin | None = Field(default=None, alias="origin")
    time_zone: str | None = Field(default=None, alias="timeZone")
    "The time zone of a contact, uses the time zone database format (https://www.iana.org/time-zones)"
    activities: str | None = Field(default=None, alias="activities")
    changed_on: datetime | None = Field(default=None, alias="changedOn")
    created_on: datetime | None = Field(default=None, alias="createdOn")
    campaign: CampaignReference | None = Field(default=None, alias="campaign")
    email: str = Field(alias="email")
    day_of_cycle: str | None = Field(default=None, alias="dayOfCycle")
    "The day on which the contact is in the Autoresponder cycle. `null` indicates the contacts is not in the cycle."
    scoring: float | None = Field(default=None, alias="scoring")
    "Contact scoring, pass null to remove the score from a contact"
    engagement_score: int | None = Field(default=None, alias="engagementScore")
    "Engagement Score is a feature that presents a visual estimate of a contact's engagement with mailings. The score is based on the contact's interactions with your e-mails. Via API, it's returned in the form of numbers ranging from 1 (Not Engaged) to 5 (Highly Engaged)."
    href: str = Field(alias="href")
    "Direct hyperlink to a resource"
    note: str | None = Field(default=None, alias="note")
    ip_address: str | None = Field(default=None, alias="ipAddress")
    "The contact's IP address. IPv4 and IPv6 formats are accepted."
    geolocation: ContactGeolocation | None = Field(default=None, alias="geolocation")
    tags: list[ContactTag] | None = Field(default=None, alias="tags")
    "The list of contact tags, limited to 500 tags."
    custom_field_values: list[ContactCustomFieldValue] | None = Field(
        default=None, alias="customFieldValues"
    )


class ContactGeolocation(BaseModel):
    "ContactGeolocation model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    latitude: str | None = Field(default=None, alias="latitude")
    longitude: str | None = Field(default=None, alias="longitude")
    continent_code: ContactGeolocationContinentCode | None = Field(
        default=None, alias="continentCode"
    )
    country_code: str | None = Field(default=None, alias="countryCode")
    "The country code, compliant with ISO 3166-1 alpha-2"
    region: str | None = Field(default=None, alias="region")
    postal_code: str | None = Field(default=None, alias="postalCode")
    dma_code: str | None = Field(default=None, alias="dmaCode")
    city: str | None = Field(default=None, alias="city")


class ContactListElement(BaseModel):
    "ContactListElement model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    contact_id: str = Field(alias="contactId")
    name: str | None = Field(default=None, alias="name")
    origin: ContactListElementOrigin | None = Field(default=None, alias="origin")
    time_zone: str | None = Field(default=None, alias="timeZone")
    "The time zone of a contact, uses the time zone database format (https://www.iana.org/time-zones)"
    activities: str | None = Field(default=None, alias="activities")
    changed_on: datetime | None = Field(default=None, alias="changedOn")
    created_on: datetime | None = Field(default=None, alias="createdOn")
    campaign: CampaignReference | None = Field(default=None, alias="campaign")
    email: str = Field(alias="email")
    day_of_cycle: str | None = Field(default=None, alias="dayOfCycle")
    "The day on which the contact is in the Autoresponder cycle. `null` indicates the contacts is not in the cycle."
    scoring: float | None = Field(default=None, alias="scoring")
    "Contact scoring, pass null to remove the score from a contact"
    engagement_score: int | None = Field(default=None, alias="engagementScore")
    "Engagement Score is a feature that presents a visual estimate of a contact's engagement with mailings. The score is based on the contact's interactions with your e-mails. Via API, it's returned in the form of numbers ranging from 1 (Not Engaged) to 5 (Highly Engaged)."
    href: str = Field(alias="href")
    "Direct hyperlink to a resource"
    note: str | None = Field(default=None, alias="note")
    ip_address: str | None = Field(default=None, alias="ipAddress")
    "The contact's IP address. IPv4 and IPv6 formats are accepted."


class ContactTag(BaseModel):
    "ContactTag model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    tag_id: str | None = Field(default=None, alias="tagId")
    name: str | None = Field(default=None, alias="name")
    href: str | None = Field(default=None, alias="href")
    color: str | None = Field(default=None, alias="color")


class CreateAccountSummaryReport(BaseModel):
    "CreateAccountSummaryReport model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    name: str = Field(alias="name")
    "The custom report name"
    type_: CreateAccountSummaryReportType = Field(alias="type")
    "The custom report type"
    scheduling: dict[str, Any] = Field(alias="scheduling")
    "Parameters responsible for defining the reporting period"


class CreateAndUpdate(BaseModel):
    "CreateAndUpdate model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    created_on: datetime | None = Field(default=None, alias="createdOn")
    "The creation date"
    updated_on: datetime | None = Field(default=None, alias="updatedOn")
    "The date of the last update"


class CreateBouncesReport(BaseModel):
    "CreateBouncesReport model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    name: str = Field(alias="name")
    "The custom report name"
    type_: CreateBouncesReportType = Field(alias="type")
    "The custom report type"
    scheduling: dict[str, Any] = Field(alias="scheduling")
    "Parameters responsible for defining the reporting period"


class CreateISPMessageStatsReport(BaseModel):
    "CreateISPMessageStatsReport model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    name: str = Field(alias="name")
    "The custom report name"
    type_: CreateISPMessageStatsReportType = Field(alias="type")
    "The custom report type"
    scheduling: dict[str, Any] = Field(alias="scheduling")
    "Parameters responsible for defining the reporting period"


class CreateImportErrorReport(BaseModel):
    "CreateImportErrorReport model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    name: str = Field(alias="name")
    "The custom report name"
    type_: CreateImportErrorReportType = Field(alias="type")
    "The custom report type"
    scheduling: dict[str, Any] = Field(alias="scheduling")
    "Parameters responsible for defining the reporting period"


class CreateListSummaryReport(BaseModel):
    "CreateListSummaryReport model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    name: str = Field(alias="name")
    "The custom report name"
    type_: CreateListSummaryReportType = Field(alias="type")
    "The custom report type"
    scheduling: dict[str, Any] = Field(alias="scheduling")
    "Parameters responsible for defining the reporting period"


class CreateMessageActivityReport(BaseModel):
    "CreateMessageActivityReport model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    name: str = Field(alias="name")
    "The custom report name"
    type_: CreateMessageActivityReportType = Field(alias="type")
    "The custom report type"
    scheduling: dict[str, Any] = Field(alias="scheduling")
    "Parameters responsible for defining the reporting period"
    filters: dict[str, Any] = Field(alias="filters")
    "Filters used to narrow down the report data"


class CreateMessageActivityReportFilters(BaseModel):
    "CreateMessageActivityReportFilters model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    filters: dict[str, Any] = Field(alias="filters")
    "Filters used to narrow down the report data"


class CreateMessageClicksReport(BaseModel):
    "CreateMessageClicksReport model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    name: str = Field(alias="name")
    "The custom report name"
    type_: CreateMessageClicksReportType = Field(alias="type")
    "The custom report type"
    scheduling: dict[str, Any] = Field(alias="scheduling")
    "Parameters responsible for defining the reporting period"


class CreateMessageStatsReport(BaseModel):
    "CreateMessageStatsReport model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    name: str = Field(alias="name")
    "The custom report name"
    type_: CreateMessageStatsReportType = Field(alias="type")
    "The custom report type"
    scheduling: dict[str, Any] = Field(alias="scheduling")
    "Parameters responsible for defining the reporting period"


class CreateMultimedia(BaseModel):
    "CreateMultimedia model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    file: str | None = Field(default=None, alias="file")


class CreateStandardSubscriberActivityReport(BaseModel):
    "CreateStandardSubscriberActivityReport model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    name: str = Field(alias="name")
    "The custom report name"
    type_: CreateStandardSubscriberActivityReportType = Field(alias="type")
    "The custom report type"
    scheduling: dict[str, Any] = Field(alias="scheduling")
    "Parameters responsible for defining the reporting period"


class CreateSubscriptionRejectionsReport(BaseModel):
    "CreateSubscriptionRejectionsReport model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    name: str = Field(alias="name")
    "The custom report name"
    type_: CreateSubscriptionRejectionsReportType = Field(alias="type")
    "The custom report type"
    scheduling: dict[str, Any] = Field(alias="scheduling")
    "Parameters responsible for defining the reporting period"


class CreateTransactionalEmail(BaseModel):
    "CreateTransactionalEmail model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    from_field: Any = Field(alias="fromField")
    "The 'From' address ID to be used as the message sender"
    reply_to: Any | None = Field(default=None, alias="replyTo")
    "The 'From' address ID to be used as the Reply-to"
    tag: Any | None = Field(default=None, alias="tag")
    "The tag ID used for statistical data collection"
    recipients: TransactionalEmailRecipients = Field(alias="recipients")
    content_type: CreateTransactionalEmailContentType = Field(alias="contentType")
    "The message content type"


class CreateTransactionalEmailBounceReport(BaseModel):
    "CreateTransactionalEmailBounceReport model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    name: str = Field(alias="name")
    "The custom report name"
    type_: CreateTransactionalEmailBounceReportType = Field(alias="type")
    "The custom report type"
    scheduling: dict[str, Any] = Field(alias="scheduling")
    "Parameters responsible for defining the reporting period"


class CreateTransactionalEmailTemplate(BaseModel):
    "CreateTransactionalEmailTemplate model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    subject: str = Field(alias="subject")
    "The template subject"
    content: TransactionalEmailTemplateContent | None = Field(default=None, alias="content")


class CreateUnconfirmedContactsStatsReport(BaseModel):
    "CreateUnconfirmedContactsStatsReport model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    name: str = Field(alias="name")
    "The custom report name"
    type_: CreateUnconfirmedContactsStatsReportType = Field(alias="type")
    "The custom report type"
    scheduling: dict[str, Any] = Field(alias="scheduling")
    "Parameters responsible for defining the reporting period"


class CreateUnsubscribeContactsListsReport(BaseModel):
    "CreateUnsubscribeContactsListsReport model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    name: str = Field(alias="name")
    "The custom report name"
    type_: CreateUnsubscribeContactsListsReportType = Field(alias="type")
    "The custom report type"
    scheduling: dict[str, Any] = Field(alias="scheduling")
    "Parameters responsible for defining the reporting period"


class CreateUserActivityReport(BaseModel):
    "CreateUserActivityReport model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    name: str = Field(alias="name")
    "The custom report name"
    type_: CreateUserActivityReportType = Field(alias="type")
    "The custom report type"
    scheduling: dict[str, Any] = Field(alias="scheduling")
    "Parameters responsible for defining the reporting period"


class CreateWebinarParticipantsReport(BaseModel):
    "CreateWebinarParticipantsReport model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    name: str = Field(alias="name")
    "The custom report name"
    type_: CreateWebinarParticipantsReportType = Field(alias="type")
    "The custom report type"
    scheduling: dict[str, Any] = Field(alias="scheduling")
    "Parameters responsible for defining the reporting period"


class CrmCondition(BaseModel):
    "This makes it possible to search contacts by CRM conditions."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    condition_type: CrmConditionConditionType = Field(alias="conditionType")
    pipeline_scope: str = Field(alias="pipelineScope")
    "The pipeline identifier"
    stage_scope: dict[str, Any] = Field(alias="stageScope")


class CustomDateRange(BaseModel):
    "CustomDateRange model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    from_: datetime = Field(alias="from")
    "The UTC date format"
    to: datetime = Field(alias="to")
    "The UTC date format"


class CustomEvent(BaseModel):
    "CustomEvent model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    name: str = Field(alias="name")
    "Unique name of custom event"
    attributes: list[CustomEventAttributeDetails] = Field(alias="attributes")
    "Optional collection of attributes"


class CustomEventAttribute(BaseModel):
    "CustomEventAttribute model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    name: str = Field(alias="name")
    "Unique name of attribute"
    type_: CustomEventAttributeType = Field(alias="type")
    "Type of attribute"


class CustomEventAttributeDetails(BaseModel):
    "CustomEventAttributeDetails model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    name: str = Field(alias="name")
    "Unique name of attribute"
    type_: CustomEventAttributeDetailsType = Field(alias="type")
    "Type of attribute"
    custom_event_attribute_id: str = Field(alias="customEventAttributeId")


class CustomEventCondition(BaseModel):
    "Search contacts for which an custom event occurred / not occurred"

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    condition_type: CustomEventConditionConditionType = Field(alias="conditionType")
    custom_event_id: str = Field(alias="customEventId")
    "The custom event identifier"
    occurrence: CustomEventConditionOccurrence = Field(alias="occurrence")
    "Whether the custom event occurred or not"
    date_operator: dict[str, Any] = Field(alias="dateOperator")
    "Show contacts for which a custom event occurred / not occurred in certain date range"
    date: dict[str, Any] | None = Field(default=None, alias="date")
    "The operators `date_to`, `date_from`, and `customDate` require you to provide, respectively, a date, datetime, or a time interval."


class CustomEventDetails(BaseModel):
    "CustomEventDetails model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    name: str = Field(alias="name")
    "Unique name of custom event"
    attributes: list[CustomEventAttributeDetails] = Field(alias="attributes")
    "Optional collection of attributes"
    custom_event_id: str = Field(alias="customEventId")
    "The custom event ID"
    created_on: datetime = Field(alias="createdOn")
    "Date of creation custom event definition"
    href: str | None = Field(default=None, alias="href")
    "Direct hyperlink to a resource"


class CustomField(BaseModel):
    "CustomField model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    custom_field_id: str | None = Field(default=None, alias="customFieldId")
    "Custom field ID"
    href: str | None = Field(default=None, alias="href")
    "Direct hyperlink to a resource"
    name: str | None = Field(default=None, alias="name")
    "The name of the custom field. It must meet the following requirements: * be unique * use only lowercase letters, underscores and digits * not be equal to one of the merge words used in messages, i.e. `name, email, twitter, facebook, buzz, myspace, linkedin, digg, googleplus, pinterest, responder, campaign, change`."
    type_: Any | None = Field(default=None, alias="type")
    "The custom field `type` accepts the following values: * `string` - input for a string value * `number` - input for a numeric value * `date` - input for a date * `datetime` - input for date and time * `country` - input for a country * `currency` - input for a currency, allows all ISO 4217 currency codes * `phone` - input for a phone number * `gender` - input for gender, allows `Male`, `Female` or `Prefer not to say` * `ip` - input for an IP address * `url` - input for a URL."
    value_type: CustomFieldValueType | None = Field(default=None, alias="valueType")
    "Type of returning value, it returns `type` options extended by a `string` option if the `format` was not defined"
    format: Any | None = Field(default=None, alias="format")
    "The custom field `format` accepts following values: * `text` - text input (doesn't require values in the `values` field, you can pass empty array) * `textarea` - textarea input (doesn't require values in the `values` field, you can pass empty array) * `radio` - radio input (requires at least 2 values in the `values` field) * `checkbox` - checkbox input (doesn't require values in the `values` field, you can pass empty array) * `single_select` - single select input (requires at least 2 values in the `values` field) * `multi_select` - multi select input (requires at least 2 values in the `values` field)."
    field_type: str | None = Field(default=None, alias="fieldType")
    "Returns the same as `format`"
    hidden: Any | None = Field(default=None, alias="hidden")
    "Whether the custom field is visible to contacts"
    values: list[str] | None = Field(default=None, alias="values")
    "The list of assigned default values, starting from zero depending on the custom field format. (Please see description)."


class CustomFieldCondition(BaseModel):
    "Search a contact by custom fields."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    condition_type: CustomFieldConditionConditionType = Field(alias="conditionType")
    operator_type: CustomFieldConditionOperatorType = Field(alias="operatorType")
    "Depends on the type of custom field, read more in [custom field condition documentation in segments (search contacts) reference manual](https://apidocs.getresponse.com/v3/case-study/segments-manual#get-by-custom-fields-search-contacts)"
    operator: dict[str, Any] = Field(alias="operator")
    'Depends on selected `"operatorType"`, read more in [custom field condition documentation in segments (search contacts) reference manual](https://apidocs.getresponse.com/v3/case-study/segments-manual#get-by-custom-fields-search-contacts)'
    value: dict[str, Any] | None = Field(default=None, alias="value")
    'Depends on selected `"operator"` and `"operatorType"`, read more in [custom field condition documentation in segments (search contacts) reference manual](https://apidocs.getresponse.com/v3/case-study/segments-manual#get-by-custom-fields-search-contacts)'
    scope: str = Field(alias="scope")
    "The identifier of the custom field, read more in [custom field condition documentation in segments (search contacts) reference manual](https://apidocs.getresponse.com/v3/case-study/segments-manual#get-by-custom-fields-search-contacts)"
    number_of_days: int | None = Field(default=None, alias="numberOfDays")
    'Required only when `"value":"last_n_days"`, read more in [custom field condition documentation in segments (search contacts) reference manual](https://apidocs.getresponse.com/v3/case-study/segments-manual#get-by-custom-fields-search-contacts)'
    include_current_period: bool | None = Field(default=None, alias="includeCurrentPeriod")
    "Flag determines if current day will be included into chosen range. This flag can be used with `last_n_days`."


class CustomFieldReference(BaseModel):
    "CustomFieldReference model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    custom_field_id: str | None = Field(default=None, alias="customFieldId")
    name: str | None = Field(default=None, alias="name")
    "The name of the custom field. It must meet the following requirements: * be unique * use only lowercase letters, underscores and digits: [a-z0-9_]{1,128} * not be equal to one of the merge words used in messages, i.e. `name`, `email`, `twitter`, `facebook`, `buzz`, `myspace`, `linkedin`, `digg`, `googleplus`, `pinterest`, `responder`, `campaign`, `change`."
    values: list[str] | None = Field(default=None, alias="values")
    "The list of assigned default values, starting from zero depending on the custom field format. (Please see description)."


class CustomFieldResponse(BaseModel):
    "CustomFieldResponse model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    custom_field_id: str | None = Field(default=None, alias="customFieldId")
    "Custom field ID"
    href: str | None = Field(default=None, alias="href")
    "Direct hyperlink to a resource"
    name: str | None = Field(default=None, alias="name")
    "The name of the custom field"
    type_: Any | None = Field(default=None, alias="type")
    value_type: str | None = Field(default=None, alias="valueType")
    "Type of returning value, it returns `type` options extended by a `string` option if the `format` was not defined"
    format: Any | None = Field(default=None, alias="format")
    field_type: str | None = Field(default=None, alias="fieldType")
    "Returns the same as `format`"
    hidden: Any | None = Field(default=None, alias="hidden")
    "Whether the custom field is visible to contacts"
    values: list[str] | None = Field(default=None, alias="values")
    "The list of assigned default values, starting from zero depending on the custom field format. (Please see description)."


class CustomReport(BaseModel):
    "CustomReport model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    custom_report_id: str | None = Field(default=None, alias="customReportId")
    "The custom report ID"
    name: str | None = Field(default=None, alias="name")
    "The custom report name"
    href: str | None = Field(default=None, alias="href")
    "The direct hyperlink to a resource"
    frequency: Any | None = Field(default=None, alias="frequency")
    "The custom report frequency"
    created_at: datetime | None = Field(default=None, alias="createdAt")
    generated_at: datetime | None = Field(default=None, alias="generatedAt")


class CustomReportDetails(BaseModel):
    "CustomReportDetails model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    custom_report_id: str | None = Field(default=None, alias="customReportId")
    "The custom report ID"
    name: str | None = Field(default=None, alias="name")
    "The custom report name"
    href: str | None = Field(default=None, alias="href")
    "The direct hyperlink to a resource"
    type_: Any | None = Field(default=None, alias="type")
    "The custom report type"
    scheduling: dict[str, Any] | None = Field(default=None, alias="scheduling")
    "Parameters responsible for defining the reporting period"
    files: list[dict[str, Any]] | None = Field(default=None, alias="files")
    "Files that have been generated for the given report"
    created_at: datetime | None = Field(default=None, alias="createdAt")
    "Custom report creation date"
    generated_at: datetime | None = Field(default=None, alias="generatedAt")
    "Custom report generation date"


class CustomReportFilterActivityType(BaseModel):
    "CustomReportFilterActivityType model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    activity_type: list[Any] = Field(alias="activityType")
    "Types of activities included in the report"


class CustomReportFilterMessageId(BaseModel):
    "CustomReportFilterMessageId model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    message_id: list[str] = Field(alias="messageId")
    "Message IDs included in the report"


class CustomReportScheduling(BaseModel):
    "CustomReportScheduling model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    frequency: Any | None = Field(default=None, alias="frequency")
    "The custom report frequency"


class DailyReportScheduling(BaseModel):
    "DailyReportScheduling model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    frequency: Any | None = Field(default=None, alias="frequency")
    "The custom report frequency"
    one_time: dict[str, Any] | None = Field(default=None, alias="oneTime")
    "Field not applicable to the selected frequency"
    recurring: dict[str, Any] | None = Field(default=None, alias="recurring")
    "A field containing configuration parameters for recurring scheduling"


class DirectContent(BaseModel):
    "DirectContent model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    from_field: Any = Field(alias="fromField")
    "The 'From' address ID to be used as the message sender"
    reply_to: Any | None = Field(default=None, alias="replyTo")
    "The 'From' address ID to be used as the Reply-to"
    tag: Any | None = Field(default=None, alias="tag")
    "The tag ID used for statistical data collection"
    recipients: TransactionalEmailRecipients = Field(alias="recipients")
    content_type: DirectContentContentType = Field(alias="contentType")
    "The message content type"
    subject: str | None = Field(default=None, alias="subject")
    attachments: list[TransactionalEmailAttachment] | None = Field(
        default=None, alias="attachments"
    )
    content: dict[str, Any] = Field(alias="content")
    "The message content. At least one field is required. The maximum combined size of plain text and HTML is 16MB"


class ECommerceAbandonedCartCondition(BaseModel):
    "Search contacts by abandoned cart."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    condition_type: ECommerceAbandonedCartConditionConditionType = Field(alias="conditionType")
    shop_scope: dict[str, Any] = Field(alias="shopScope")
    "Limit the searched shops"
    cart_value: dict[str, Any] = Field(alias="cartValue")
    "Limit search by cart value"
    date_operator: ECommerceAbandonedCartConditionDateOperator = Field(alias="dateOperator")
    "Set a date range. For the date_from and last_n_days, custom field value is required. Examples can be found here: [API Docs](https://apidocs.getresponse.com/v3/case-study/segments-manual/#ecommerce-abandoned-cart-condition-type)."
    value: dict[str, Any] | None = Field(default=None, alias="value")
    "This field is required only for `date_from` and `last_n_days` date operators."
    include_current_period: bool | None = Field(default=None, alias="includeCurrentPeriod")
    "Flag determines if current day will be included into chosen range. This flag can be used with `last_n_days`."
    range: Any | None = Field(default=None, alias="range")
    "Date interval string compliant with ISO 8601, supported format: <start_date>/<end_date>, allowed only for `custom` date operator"


class ECommerceBrandPurchasedCondition(BaseModel):
    "Search contacts by brand purchased."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    condition_type: ECommerceBrandPurchasedConditionConditionType = Field(alias="conditionType")
    scope: str = Field(alias="scope")
    "The shop identifier"
    operator_type: ECommerceBrandPurchasedConditionOperatorType = Field(alias="operatorType")
    operator: ECommerceBrandPurchasedConditionOperator = Field(alias="operator")
    value: str = Field(alias="value")


class ECommerceNumberOfPurchasesCondition(BaseModel):
    "Search contacts by the number of purchases."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    condition_type: ECommerceNumberOfPurchasesConditionConditionType = Field(alias="conditionType")
    operator_type: ECommerceNumberOfPurchasesConditionOperatorType = Field(alias="operatorType")
    operator: ECommerceNumberOfPurchasesConditionOperator = Field(alias="operator")
    scope: dict[str, Any] = Field(alias="scope")
    "The condition limiting the searched shop"
    value: int = Field(alias="value")
    date: dict[str, Any] = Field(alias="date")
    "Limit search by date range"


class ECommerceProductPurchasedCondition(BaseModel):
    "Search the product purchased."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    condition_type: ECommerceProductPurchasedConditionConditionType = Field(alias="conditionType")
    shop_scope: dict[str, Any] = Field(alias="shopScope")
    "Limit the searched shops"
    category_scope: dict[str, Any] = Field(alias="categoryScope")
    "The product category"
    operator_type: ECommerceProductPurchasedConditionOperatorType = Field(alias="operatorType")
    operator: ECommerceProductPurchasedConditionOperator = Field(alias="operator")
    product_scope: dict[str, Any] = Field(alias="productScope")
    date_operator: dict[str, Any] = Field(alias="dateOperator")
    "Set a date range. For the date_from and date_to, custom field value is required."
    value: dict[str, Any] | None = Field(default=None, alias="value")
    "This field stores the date or time interval for the `date_to`, `date_from`, or `custom` date operator"
    number_of_days: int | None = Field(default=None, alias="numberOfDays")
    "Number of days, required for the `last_n_days` date operator"
    include_current_period: bool | None = Field(default=None, alias="includeCurrentPeriod")
    "Flag determines if current day will be included into chosen range. This flag is required for `last_n_days` date operator. Can be used with `last_7_days` and `last_30_days` date operators"


class ECommerceTotalSpentCondition(BaseModel):
    "Search contacts by total spent."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    condition_type: ECommerceTotalSpentConditionConditionType = Field(alias="conditionType")
    operator_type: ECommerceTotalSpentConditionOperatorType = Field(alias="operatorType")
    operator: ECommerceTotalSpentConditionOperator = Field(alias="operator")
    scope: dict[str, Any] = Field(alias="scope")
    "The condition limiting the searched shop"
    value: float = Field(alias="value")
    currency: str = Field(alias="currency")
    "The currency code according to ISO 4217, i.e. USD, GBP, PLN"
    date: dict[str, Any] = Field(alias="date")
    "Limit search by date range"


class EmailCondition(BaseModel):
    "EmailCondition model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    condition_type: EmailConditionConditionType = Field(alias="conditionType")
    operator_type: EmailConditionOperatorType = Field(alias="operatorType")
    operator: EmailConditionOperator = Field(alias="operator")
    value: str = Field(alias="value")


class EmptyReportFilters(BaseModel):
    "EmptyReportFilters model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    filters: dict[str, Any] | None = Field(default=None, alias="filters")
    "Filters used to narrow down the report data"


class EngagementScoreCondition(BaseModel):
    "Search contacts by their engagement score"

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    condition_type: EngagementScoreConditionConditionType = Field(alias="conditionType")
    operator: EngagementScoreConditionOperator = Field(alias="operator")
    "The operator used in engagement score comparison"
    value: int = Field(alias="value")
    "The condition value"


class ErrorResponse(BaseModel):
    "ErrorResponse model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    http_status: int = Field(alias="httpStatus")
    "HTTP response code"
    code: int = Field(alias="code")
    "API error code"
    code_description: str = Field(alias="codeDescription")
    "API error code description"
    message: str = Field(alias="message")
    "Error message"
    more_info: str = Field(alias="moreInfo")
    "URL to error description in the API Docs"
    context: dict[str, Any] = Field(alias="context")
    uuid: str = Field(alias="uuid")
    "UUID of the error response"


class ExternalLexpad(BaseModel):
    "External Lexpad settings for the message, read more: [External Lexpad](https://apidocs.getresponse.com/v3/dynamic-content/external-lexpad)"

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    data_source_url: str = Field(alias="dataSourceUrl")
    "URL to the endpoint that will provide data for External Lexpad"
    data_source_token: str | None = Field(default=None, alias="dataSourceToken")
    "Token that will be sent in `X-Auth-Token` header to authenticate the requests made to the endpoint"


class FacebookPixel(BaseModel):
    "FacebookPixel model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    name: str | None = Field(default=None, alias="name")
    pixel_id: str | None = Field(default=None, alias="pixelId")


class File(BaseModel):
    "File model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    name: str | None = Field(default=None, alias="name")
    "The file name"
    extension: str | None = Field(default=None, alias="extension")
    "The file extension"
    folder: dict[str, Any] | None = Field(default=None, alias="folder")
    "The folder where the file is stored"
    file_id: str = Field(alias="fileId")
    "The file ID"
    file_size: int | None = Field(default=None, alias="fileSize")
    "The file size"
    group: FileGroup | None = Field(default=None, alias="group")
    thumbnail: str | None = Field(default=None, alias="thumbnail")
    "The direct URL to the file thumbnail"
    url: str | None = Field(default=None, alias="url")
    "The direct URL to resource"
    properties: list[FileProperty] | None = Field(default=None, alias="properties")
    "The file properties (available only for the `photos` group)"
    created_on: datetime | None = Field(default=None, alias="createdOn")
    "The creation date"
    href: str | None = Field(default=None, alias="href")
    "Direct hyperlink to a resource"


class FileProperty(BaseModel):
    "FileProperty model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    name: FilePropertyName = Field(alias="name")
    value: dict[str, Any] = Field(alias="value")


class Folder(BaseModel):
    "Folder model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    folder_id: str = Field(alias="folderId")
    "The folder ID"
    name: str | None = Field(default=None, alias="name")
    "The folder name"
    size: int | None = Field(default=None, alias="size")
    "The size of all files in the directory"
    created_on: datetime | None = Field(default=None, alias="createdOn")
    "The creation date"


class FolderShort(BaseModel):
    "FolderShort model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    folder_id: str = Field(alias="folderId")
    "The folder ID"


class Form(BaseModel):
    "Form model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    form_id: str | None = Field(default=None, alias="formId")
    webform_id: str | None = Field(default=None, alias="webformId")
    "Same as `formId`"
    name: str | None = Field(default=None, alias="name")
    href: str | None = Field(default=None, alias="href")
    "Direct hyperlink to a resource"
    has_variants: bool | None = Field(default=None, alias="hasVariants")
    "Indicates if the form has variants (A/B tests)"
    script_url: str | None = Field(default=None, alias="scriptUrl")
    "The URL to a JavaScript file of the form. This is used to embed the form within a web page."
    status: FormStatus | None = Field(default=None, alias="status")
    created_on: datetime | None = Field(default=None, alias="createdOn")
    statistics: FormStatistics | None = Field(default=None, alias="statistics")
    campaign: CampaignReference | None = Field(default=None, alias="campaign")


class FormDetails(BaseModel):
    "FormDetails model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    form_id: str | None = Field(default=None, alias="formId")
    webform_id: str | None = Field(default=None, alias="webformId")
    "Same as `formId`"
    name: str | None = Field(default=None, alias="name")
    href: str | None = Field(default=None, alias="href")
    "Direct hyperlink to a resource"
    has_variants: bool | None = Field(default=None, alias="hasVariants")
    "Indicates if the form has variants (A/B tests)"
    script_url: str | None = Field(default=None, alias="scriptUrl")
    "The URL to a JavaScript file of the form. This is used to embed the form within a web page."
    status: FormDetailsStatus | None = Field(default=None, alias="status")
    created_on: datetime | None = Field(default=None, alias="createdOn")
    statistics: FormStatistics | None = Field(default=None, alias="statistics")
    campaign: CampaignReference | None = Field(default=None, alias="campaign")
    settings: FormSettings | None = Field(default=None, alias="settings")
    variants: list[FormVariant] | None = Field(default=None, alias="variants")


class FormSettings(BaseModel):
    "FormSettings model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    optin: FormSettingsOptin | None = Field(default=None, alias="optin")
    "`single` - Single opt-in means that the contact will be added without confirming their subscription first. `double` - Double opt-in means that the contact will receive a subscription confirmation email."
    phase: int | None = Field(default=None, alias="phase")
    "The contact who subscribed via this form will be added to the selected day in the autoresponder cycle. If null, the contact won't be added to the cycle."
    thank_you_type: FormSettingsThankYouType | None = Field(default=None, alias="thankYouType")
    "What should happen when a new contact subscribes via the form."
    thank_you_url: str | None = Field(default=None, alias="thankYouUrl")
    "The URL used to redirect the newly subscribed contacts when they complete this form. Used if `thankYouType` is `custom_url`."
    already_subscribed_type: FormSettingsAlreadySubscribedType | None = Field(
        default=None, alias="alreadySubscribedType"
    )
    "What to do when the address already exists in the campaign"
    already_subscribed_url: str | None = Field(default=None, alias="alreadySubscribedUrl")
    "The URL used to redirect the already subscribed contacts when they complete this form. Used if `alreadySubscribedType` is `custom_url`."
    second_stage_captcha: StringBooleanEnum | None = Field(default=None, alias="secondStageCaptcha")
    "Is captcha enabled for the form"
    forward_data_request_type: FormSettingsForwardDataRequestType | None = Field(
        default=None, alias="forwardDataRequestType"
    )
    "How to forward form data to a thank-you page. [Learn more](https://www.getresponse.com/help/building-contact-lists/forms-and-pop-ups/can-i-forward-subscriber-data-to-a-custom-thank-you-page.html). `null` means that the data forwarding is turned off."
    tracking_custom_field: CustomFieldReference | None = Field(
        default=None, alias="trackingCustomField"
    )
    "Subscribers added via this form will have this custom field set with a value passed in `trackingCustomFieldValue`"
    tracking_custom_field_value: str | None = Field(default=None, alias="trackingCustomFieldValue")
    "See the `trackingCustomField` description"


class FormStatistics(BaseModel):
    "FormStatistics model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    visitors: int | None = Field(default=None, alias="visitors")
    "The total number of form visitors"
    unique_visitors: int | None = Field(default=None, alias="uniqueVisitors")
    "The number of unique form visitors"
    subscribed: int | None = Field(default=None, alias="subscribed")
    "The number of visitors that subscribed using this form"
    subscription_rate: float | None = Field(default=None, alias="subscriptionRate")
    "The ratio of `subscribed` to `visitors`"


class FormVariant(BaseModel):
    "FormVariant model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    variant: str | None = Field(default=None, alias="variant")
    "The index of variants"
    variant_name: str | None = Field(default=None, alias="variantName")
    winner: StringBooleanEnum | None = Field(default=None, alias="winner")
    "Is this variant the winner in the A/B test"
    status: FormVariantStatus | None = Field(default=None, alias="status")
    created_on: datetime | None = Field(default=None, alias="createdOn")
    statistics: FormStatistics | None = Field(default=None, alias="statistics")


class FormVariantDetails(BaseModel):
    "FormVariantDetails model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    form_id: str | None = Field(default=None, alias="formId")
    webform_id: str | None = Field(default=None, alias="webformId")
    "Same as `formId`"
    variant: str | None = Field(default=None, alias="variant")
    "The index of variants"
    variant_name: str | None = Field(default=None, alias="variantName")
    winner: FormVariantDetailsWinner | None = Field(default=None, alias="winner")
    "Is this variant the winner in the A/B test"
    status: FormVariantDetailsStatus | None = Field(default=None, alias="status")
    created_on: datetime | None = Field(default=None, alias="createdOn")
    number_of_visitors: int | None = Field(default=None, alias="numberOfVisitors")
    "The total number of form visitors"
    number_of_unique_visitors: int | None = Field(default=None, alias="numberOfUniqueVisitors")
    "The number of unique form visitors"
    number_of_subscribers: int | None = Field(default=None, alias="numberOfSubscribers")
    "The number of visitors who subscribed through this form"
    subscription_rate: float | None = Field(default=None, alias="subscriptionRate")
    "The ratio of `numberOfSubscribers` to `numberOfVisitors`"


class FromField(BaseModel):
    "FromField model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    from_field_id: str | None = Field(default=None, alias="fromFieldId")
    "The 'From' address ID"
    href: str | None = Field(default=None, alias="href")
    "Direct hyperlink to a resource"
    email: str | None = Field(default=None, alias="email")
    "The email address"
    rewritten_email: str | None = Field(default=None, alias="rewrittenEmail")
    "Email address used to send message."
    name: str | None = Field(default=None, alias="name")
    "The name connected to the email address"
    is_active: Any | None = Field(default=None, alias="isActive")
    "Flag if the 'From' address is active"
    is_default: Any | None = Field(default=None, alias="isDefault")
    "Flag if the 'From' address is default for the account"
    created_on: datetime | None = Field(default=None, alias="createdOn")
    "The creation date"
    domain: dict[str, Any] | None = Field(default=None, alias="domain")


class FromFieldReference(BaseModel):
    "FromFieldReference model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    from_field_id: str = Field(alias="fromFieldId")
    "The 'From' address ID"
    href: str | None = Field(default=None, alias="href")
    "Direct hyperlink to a resource"


class GDPRField(BaseModel):
    "GDPRField model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    gdpr_field_id: str | None = Field(default=None, alias="gdprFieldId")
    name: str | None = Field(default=None, alias="name")
    "The name of the GDPR field"
    created_on: datetime | None = Field(default=None, alias="createdOn")
    href: str | None = Field(default=None, alias="href")
    "The direct hyperlink to the resource"


class GDPRFieldDetails(BaseModel):
    "GDPRFieldDetails model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    gdpr_field_id: str | None = Field(default=None, alias="gdprFieldId")
    name: str | None = Field(default=None, alias="name")
    "The name of the GDPR field"
    created_on: datetime | None = Field(default=None, alias="createdOn")
    href: str | None = Field(default=None, alias="href")
    "The direct hyperlink to the resource"
    latest_version: GDPRFieldLatestVersion | None = Field(default=None, alias="latestVersion")


class GDPRFieldLatestVersion(BaseModel):
    "GDPRFieldLatestVersion model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    gdpr_field_version_id: str | None = Field(default=None, alias="gdprFieldVersionId")
    content: str | None = Field(default=None, alias="content")
    "The content of the GDPR field"
    created_on: datetime | None = Field(default=None, alias="createdOn")


class GdprCondition(BaseModel):
    "Find contacts based on whether they have given or not given specific consents."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    condition_type: GdprConditionConditionType = Field(alias="conditionType")
    gdpr_field_id: str = Field(alias="gdprFieldId")
    "The ID of the consent field. You can retrieve it using [this API call](https://apireference.getresponse.com/#operation/getGDPRFieldList)."
    consent_status: GdprConditionConsentStatus = Field(alias="consentStatus")
    "Specify whether you want to search for contacts who have given or not given consent."
    consent_date: dict[str, Any] | None = Field(default=None, alias="consentDate")
    "Specify when consent was given or not given. Not providing this field is equivalent to using the `anytime` operator."


class GeneralPerformanceStats(BaseModel):
    "GeneralPerformanceStats model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    currency: str | None = Field(default=None, alias="currency")
    "Statistics currency"
    order: dict[str, Any] | None = Field(default=None, alias="order")
    "Order statistics"
    revenue: dict[str, Any] | None = Field(default=None, alias="revenue")
    "Revenue statistics"


class GeolocationCondition(BaseModel):
    "Search contacts by geolocation."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    condition_type: GeolocationConditionConditionType = Field(alias="conditionType")
    operator_type: GeolocationConditionOperatorType = Field(alias="operatorType")
    operator: GeolocationConditionOperator = Field(alias="operator")
    value: str = Field(alias="value")
    scope: GeolocationConditionScope = Field(alias="scope")
    "Specify the search parameters"


class GoalCondition(BaseModel):
    "Search contacts by a defined goal."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    condition_type: GoalConditionConditionType = Field(alias="conditionType")
    operator_type: GoalConditionOperatorType = Field(alias="operatorType")
    operator: GoalConditionOperator = Field(alias="operator")
    "The relational and existence operator. For the relational operator, the value field is required."
    value: int | None = Field(default=None, alias="value")
    "The value to be compared for the relational operator. For the assigned, the not_assigned operator field is prohibited."
    scope: str = Field(alias="scope")
    "The goal identifier"


class ImageDetails(BaseModel):
    "ImageDetails model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    image_id: str | None = Field(default=None, alias="imageId")
    "Image ID"
    original_image_url: str | None = Field(default=None, alias="originalImageUrl")
    "URL from which image was downloaded"
    size: str | None = Field(default=None, alias="size")
    "Size in bytes"
    name: str | None = Field(default=None, alias="name")
    "Original name"
    thumbnail_url: str | None = Field(default=None, alias="thumbnailUrl")
    "Thumbnail URL"
    url: str | None = Field(default=None, alias="url")
    "Asset URL"
    extension: ImageDetailsExtension | None = Field(default=None, alias="extension")
    "File extension"


class Import(BaseModel):
    "Import model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    import_id: str | None = Field(default=None, alias="importId")
    "The import ID"
    campaign: CampaignReference | None = Field(default=None, alias="campaign")
    status: ImportStatus | None = Field(default=None, alias="status")
    statistics: ImportStatistics | None = Field(default=None, alias="statistics")
    "The import statistics"
    error_statistics: ImportErrorStatistics | None = Field(default=None, alias="errorStatistics")
    "The detailed import error statistics"
    created_on: datetime | None = Field(default=None, alias="createdOn")
    finished_on: datetime | None = Field(default=None, alias="finishedOn")
    href: str | None = Field(default=None, alias="href")
    "Direct hyperlink to a resource"


class ImportErrorReportDetails(BaseModel):
    "ImportErrorReportDetails model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    custom_report_id: str | None = Field(default=None, alias="customReportId")
    "The custom report ID"
    name: str | None = Field(default=None, alias="name")
    "The custom report name"
    href: str | None = Field(default=None, alias="href")
    "The direct hyperlink to a resource"
    type_: Any | None = Field(default=None, alias="type")
    "The custom report type"
    scheduling: dict[str, Any] | None = Field(default=None, alias="scheduling")
    "Parameters responsible for defining the reporting period"
    files: list[dict[str, Any]] | None = Field(default=None, alias="files")
    "Files that have been generated for the given report"
    created_at: datetime | None = Field(default=None, alias="createdAt")
    "Custom report creation date"
    generated_at: datetime | None = Field(default=None, alias="generatedAt")
    "Custom report generation date"
    filters: dict[str, Any] | None = Field(default=None, alias="filters")
    "Filters used to narrow down the report data"


class ImportErrorStatistics(BaseModel):
    "ImportErrorStatistics model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    syntax_errors: int | None = Field(default=None, alias="syntaxErrors")
    "The number of contacts with a syntax error"
    already_in_queue: int | None = Field(default=None, alias="alreadyInQueue")
    "The number of contacts already in queue"
    invalid_domains: int | None = Field(default=None, alias="invalidDomains")
    "The number of contacts with invalid domains"
    blacklist: int | None = Field(default=None, alias="blacklist")
    "The number of blocked contacts"
    policy_failures: int | None = Field(default=None, alias="policyFailures")
    "The number of contacts rejected for policy reasons"
    mismatched_criteria: int | None = Field(default=None, alias="mismatchedCriteria")
    "The number of contacts rejected because of mismatched criteria, [learn more](https://www.getresponse.com/help/managing-contacts/working-with-contact-lists/where-can-i-find-import-statistics.html#what-do-the-numbers-for-uploaded-approved-and-import-errors-mean)"


class ImportStatistics(BaseModel):
    "ImportStatistics model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    uploaded: int = Field(alias="uploaded")
    "The number of uploaded contacts"
    invalid: int = Field(alias="invalid")
    "The number of invalid contacts"
    updated: int = Field(alias="updated")
    "The number of updated contacts"
    added_to_list: int = Field(alias="addedToList")
    "The number of added contacts"


class IndustryTag(BaseModel):
    "IndustryTag model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    industry_tag_id: str = Field(alias="industryTagId")
    "Industry tag ID"
    name: str | None = Field(default=None, alias="name")
    description: str | None = Field(default=None, alias="description")


class IndustryTagId(BaseModel):
    "IndustryTagId model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    industry_tag_id: str | None = Field(default=None, alias="industryTagId")
    "Industry tag ID"


class IndustryTagProperties(BaseModel):
    "IndustryTagProperties model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    name: str | None = Field(default=None, alias="name")
    description: str | None = Field(default=None, alias="description")


class IspMessageStatsReportDetails(BaseModel):
    "IspMessageStatsReportDetails model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    custom_report_id: str | None = Field(default=None, alias="customReportId")
    "The custom report ID"
    name: str | None = Field(default=None, alias="name")
    "The custom report name"
    href: str | None = Field(default=None, alias="href")
    "The direct hyperlink to a resource"
    type_: Any | None = Field(default=None, alias="type")
    "The custom report type"
    scheduling: dict[str, Any] | None = Field(default=None, alias="scheduling")
    "Parameters responsible for defining the reporting period"
    files: list[dict[str, Any]] | None = Field(default=None, alias="files")
    "Files that have been generated for the given report"
    created_at: datetime | None = Field(default=None, alias="createdAt")
    "Custom report creation date"
    generated_at: datetime | None = Field(default=None, alias="generatedAt")
    "Custom report generation date"
    filters: dict[str, Any] | None = Field(default=None, alias="filters")
    "Filters used to narrow down the report data"


class LandingPage(BaseModel):
    "LandingPage model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    landing_page_id: str | None = Field(default=None, alias="landingPageId")
    "The landing page ID"
    href: str | None = Field(default=None, alias="href")
    "Direct hyperlink to a resource"
    meta_title: str | None = Field(default=None, alias="metaTitle")
    "The landing page meta title property"
    domain: str | None = Field(default=None, alias="domain")
    "The domain where the landing page is hosted"
    subdomain: str | None = Field(default=None, alias="subdomain")
    "The subdomain where the landing page is assigned"
    user_domain: str | None = Field(default=None, alias="userDomain")
    "The private domain provided by the user"
    user_domain_path: str | None = Field(default=None, alias="userDomainPath")
    "The private domain path provided by the user"
    campaign: Any | None = Field(default=None, alias="campaign")
    "The campaign to which the landing page is linked"
    status: Any | None = Field(default=None, alias="status")
    "The landing page status"
    user_domain_status: LandingPageUserDomainStatus | None = Field(
        default=None, alias="userDomainStatus"
    )
    "The DNS status for the user's private domain. Can be `null` if a private domain isn't assigned."
    test_ab: Any | None = Field(default=None, alias="testAB")
    "Does the landing page have AB testing (variants) enabled"
    created_on: datetime | None = Field(default=None, alias="createdOn")
    "The creation date"
    updated_on: datetime | None = Field(default=None, alias="updatedOn")
    "The date of the last page update"
    meta_description: str | None = Field(default=None, alias="metaDescription")
    "The landing page meta description property"
    meta_noindex: LandingPageMetaNoindex | None = Field(default=None, alias="metaNoindex")
    "To entirely prevent your page content from being listed in the Google web index, even if other sites link to it use a noindex meta tag"
    day_of_cycle: int | None = Field(default=None, alias="dayOfCycle")
    "Contacts subscribed via the landing page will be added to the autoresponder cycle. `Null` if contacts shouldn't be added to the cycle."
    optin: LandingPageOptin | None = Field(default=None, alias="optin")
    "The opt-in type (double or single)"
    favico_url: str | None = Field(default=None, alias="favicoUrl")
    "The favicon URL. Can be `null` if a favicon isn't present"
    thank_you_page_type: LandingPageThankYouPageType | None = Field(
        default=None, alias="thankYouPageType"
    )
    "What should happen after a contact subscribes"
    thank_you_page_url: str | None = Field(default=None, alias="thankYouPageUrl")
    "The `thank-you` page URL. Can be empty if a custom thank-you page isn't being used"
    url: str | None = Field(default=None, alias="url")
    "The landing page URL"
    variants: list[LandingPageVariant] | None = Field(default=None, alias="variants")


class LandingPageVariant(BaseModel):
    "LandingPageVariant model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    variant_id: str | None = Field(default=None, alias="variantId")
    "The landing page variant ID."
    variant: str | None = Field(default=None, alias="variant")
    "The variant index."
    winner: bool | None = Field(default=None, alias="winner")
    visitors: str | None = Field(default=None, alias="visitors")
    unique_visitors: str | None = Field(default=None, alias="uniqueVisitors")
    subscribed: str | None = Field(default=None, alias="subscribed")


class LastClickDateCondition(BaseModel):
    "This is used to find the last time when a contact clicked a message."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    condition_type: LastClickDateConditionConditionType = Field(alias="conditionType")
    operator_type: LastClickDateConditionOperatorType = Field(alias="operatorType")
    operator: LastClickDateConditionOperator = Field(alias="operator")
    value: dict[str, Any] = Field(alias="value")


class LastOpenDateCondition(BaseModel):
    "Search the last time when a contact opened a message."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    condition_type: LastOpenDateConditionConditionType = Field(alias="conditionType")
    operator_type: LastOpenDateConditionOperatorType = Field(alias="operatorType")
    operator: LastOpenDateConditionOperator = Field(alias="operator")
    value: dict[str, Any] = Field(alias="value")


class LastSendDateCondition(BaseModel):
    "Search the last time when an email message was sent to a contact."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    condition_type: LastSendDateConditionConditionType = Field(alias="conditionType")
    operator_type: LastSendDateConditionOperatorType = Field(alias="operatorType")
    operator: LastSendDateConditionOperator = Field(alias="operator")
    value: dict[str, Any] = Field(alias="value")


class LegacyForm(BaseModel):
    "LegacyForm model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    webform_id: str | None = Field(default=None, alias="webformId")
    "The webform (Legacy Form) ID"
    name: str | None = Field(default=None, alias="name")
    href: str | None = Field(default=None, alias="href")
    "Direct hyperlink to a resource"
    script_url: str | None = Field(default=None, alias="scriptUrl")
    "The URL of the script that displays the Legacy Form"
    status: StatusEnum | None = Field(default=None, alias="status")
    modified_on: datetime | None = Field(default=None, alias="modifiedOn")
    "The modification date"
    statistics: LegacyFormStatistics | None = Field(default=None, alias="statistics")
    campaign: CampaignReference | None = Field(default=None, alias="campaign")


class LegacyFormStatistics(BaseModel):
    "LegacyFormStatistics model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    opened: int | None = Field(default=None, alias="opened")
    "The number of Legacy Form views"
    subscribed: int | None = Field(default=None, alias="subscribed")
    "The number of contacts that subscribed using this Legacy Form"


class LinkClickedCondition(BaseModel):
    "Search contacts that clicked on a link."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    condition_type: LinkClickedConditionConditionType = Field(alias="conditionType")
    operator_type: LinkClickedConditionOperatorType = Field(alias="operatorType")
    operator: MessageTypeOperator = Field(alias="operator")
    scope: str = Field(alias="scope")
    "The message identifier"
    click_track_id: dict[str, Any] = Field(alias="clickTrackId")


class LinkNotClickedCondition(BaseModel):
    "Search contacts that didn't click a link."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    condition_type: LinkNotClickedConditionConditionType = Field(alias="conditionType")
    operator_type: LinkNotClickedConditionOperatorType = Field(alias="operatorType")
    operator: dict[str, Any] = Field(alias="operator")
    date_operator: LinkNotClickedConditionDateOperator = Field(alias="dateOperator")
    "It allows you to set a date range. For some of them `value` will be required. Examples can be found here: [API Docs](https://apidocs.getresponse.com/v3/case-study/segments-manual#not-opened-action)."
    value: dict[str, Any] | None = Field(default=None, alias="value")
    "This field is required only for `date_from` and `last_n_days` date operators."
    include_current_period: bool | None = Field(default=None, alias="includeCurrentPeriod")
    "Flag determines if current day will be included into chosen range. This flag can be used with `last_7_days`, `last_30_days`, `last_n_days`."
    scope: str | None = Field(default=None, alias="scope")
    "The message identifier. This field is prohibited for the 'all' operator."
    click_track_id: dict[str, Any] | None = Field(default=None, alias="clickTrackId")
    "The click track identifier"


class ListSummaryReportDetails(BaseModel):
    "ListSummaryReportDetails model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    custom_report_id: str | None = Field(default=None, alias="customReportId")
    "The custom report ID"
    name: str | None = Field(default=None, alias="name")
    "The custom report name"
    href: str | None = Field(default=None, alias="href")
    "The direct hyperlink to a resource"
    type_: Any | None = Field(default=None, alias="type")
    "The custom report type"
    scheduling: dict[str, Any] | None = Field(default=None, alias="scheduling")
    "Parameters responsible for defining the reporting period"
    files: list[dict[str, Any]] | None = Field(default=None, alias="files")
    "Files that have been generated for the given report"
    created_at: datetime | None = Field(default=None, alias="createdAt")
    "Custom report creation date"
    generated_at: datetime | None = Field(default=None, alias="generatedAt")
    "Custom report generation date"
    filters: dict[str, Any] | None = Field(default=None, alias="filters")
    "Filters used to narrow down the report data"


class Lps(BaseModel):
    "Lps model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    lps_id: str | None = Field(default=None, alias="lpsId")
    "The landing page ID"
    href: str | None = Field(default=None, alias="href")
    "Direct hyperlink to a resource"
    name: str | None = Field(default=None, alias="name")
    "The landing page name"
    status: LpsStatus | None = Field(default=None, alias="status")
    "The landing page status"
    domain_url: str | None = Field(default=None, alias="domainUrl")
    "The landing page domain"
    thumbnail_url: str | None = Field(default=None, alias="thumbnailUrl")
    "The URL of a landing page thumbnail"
    is_chats_enabled: Any | None = Field(default=None, alias="isChatsEnabled")
    "Chats is enabled on the landing page"
    created_at: datetime | None = Field(default=None, alias="createdAt")
    "The date (in GMT) the landing page was created"
    updated_at: datetime | None = Field(default=None, alias="updatedAt")
    "The date (in GMT) the landing page was updated"
    statistics: LpsListItemStatistics | None = Field(default=None, alias="statistics")
    "The landing page statistics"


class LpsDetails(BaseModel):
    "LpsDetails model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    lps_id: str | None = Field(default=None, alias="lpsId")
    "The landing page ID"
    href: str | None = Field(default=None, alias="href")
    "Direct hyperlink to a resource"
    name: str | None = Field(default=None, alias="name")
    "The landing page name"
    status: LpsDetailsStatus | None = Field(default=None, alias="status")
    "The landing page status"
    domain_url: str | None = Field(default=None, alias="domainUrl")
    "The landing page domain"
    thumbnail_url: str | None = Field(default=None, alias="thumbnailUrl")
    "The URL of a landing page thumbnail"
    is_chats_enabled: Any | None = Field(default=None, alias="isChatsEnabled")
    "Chats is enabled on the landing page"
    created_at: datetime | None = Field(default=None, alias="createdAt")
    "The date (in GMT) the landing page was created"
    updated_at: datetime | None = Field(default=None, alias="updatedAt")
    "The date (in GMT) the landing page was updated"
    page_views: int | None = Field(default=None, alias="pageViews")
    "The total number of times your landing page was viewed or refreshed"
    visits: int | None = Field(default=None, alias="visits")
    "The number of browsing sessions initiated on your landing page"
    unique_visitors: int | None = Field(default=None, alias="uniqueVisitors")
    "The number of people who visited your landing page"
    pages: list[LpsPage] | None = Field(default=None, alias="pages")


class LpsDetailsStatistics(BaseModel):
    "LpsDetailsStatistics model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    page_views: int | None = Field(default=None, alias="pageViews")
    "The total number of times your landing page was viewed or refreshed"
    visits: int | None = Field(default=None, alias="visits")
    "The number of browsing sessions initiated on your landing page"
    unique_visitors: int | None = Field(default=None, alias="uniqueVisitors")
    "The number of people who visited your landing page"


class LpsListItem(BaseModel):
    "LpsListItem model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    lps_id: str | None = Field(default=None, alias="lpsId")
    "The landing page ID"
    href: str | None = Field(default=None, alias="href")
    "Direct hyperlink to a resource"
    name: str | None = Field(default=None, alias="name")
    "The landing page name"
    status: LpsListItemStatus | None = Field(default=None, alias="status")
    "The landing page status"
    domain_url: str | None = Field(default=None, alias="domainUrl")
    "The landing page domain"
    thumbnail_url: str | None = Field(default=None, alias="thumbnailUrl")
    "The URL of a landing page thumbnail"
    is_chats_enabled: Any | None = Field(default=None, alias="isChatsEnabled")
    "Chats is enabled on the landing page"
    created_at: datetime | None = Field(default=None, alias="createdAt")
    "The date (in GMT) the landing page was created"
    updated_at: datetime | None = Field(default=None, alias="updatedAt")
    "The date (in GMT) the landing page was updated"


class LpsListItemStatistics(BaseModel):
    "LpsListItemStatistics model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    visits: int | None = Field(default=None, alias="visits")
    "The number of browsing sessions initiated on your landing page"
    leads: int | None = Field(default=None, alias="leads")
    "Number of leads"
    subscription_rate: int | None = Field(default=None, alias="subscriptionRate")
    "The number of leads divided by the number of visitors, shown as a percentage"


class LpsPage(BaseModel):
    "LpsPage model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    uuid: str | None = Field(default=None, alias="uuid")
    "The ID of a page associated with the landing page (i.e., 404 page and thank you page)"
    name: str | None = Field(default=None, alias="name")
    "The name of a page associated with the landing page (i.e., 404 page and thank you page)"
    status: LpsPageStatus | None = Field(default=None, alias="status")
    "The status of a page associated with the landing page (i.e., 404 page or thank you page)"
    url: str | None = Field(default=None, alias="url")
    "Direct hyperlink to a resource"
    redirect_url: str | None = Field(default=None, alias="redirectUrl")
    "Direct hyperlink to a resource"
    created_at: datetime | None = Field(default=None, alias="createdAt")
    "The date (in GMT) a page associated with the landing page (i.e., 404 page or thank you page) was created"


class LpsStats(BaseModel):
    "LpsStats model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    lps_id: str = Field(alias="lpsId")
    "The landing page ID"
    name: str | None = Field(default=None, alias="name")
    page_views: int | None = Field(default=None, alias="pageViews")
    "The total number of times your landing page was viewed or refreshed"
    visits: int | None = Field(default=None, alias="visits")
    "The number of browsing sessions initiated on your landing page"
    unique_visitors: int | None = Field(default=None, alias="uniqueVisitors")
    "The number of people who visited your landing page"
    thumbnail_url: str | None = Field(default=None, alias="thumbnailUrl")
    "Direct hyperlink to a resource"


class MessageActivityReportDetails(BaseModel):
    "MessageActivityReportDetails model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    custom_report_id: str | None = Field(default=None, alias="customReportId")
    "The custom report ID"
    name: str | None = Field(default=None, alias="name")
    "The custom report name"
    href: str | None = Field(default=None, alias="href")
    "The direct hyperlink to a resource"
    type_: Any | None = Field(default=None, alias="type")
    "The custom report type"
    scheduling: dict[str, Any] | None = Field(default=None, alias="scheduling")
    "Parameters responsible for defining the reporting period"
    files: list[dict[str, Any]] | None = Field(default=None, alias="files")
    "Files that have been generated for the given report"
    created_at: datetime | None = Field(default=None, alias="createdAt")
    "Custom report creation date"
    generated_at: datetime | None = Field(default=None, alias="generatedAt")
    "Custom report generation date"
    filters: dict[str, Any] | None = Field(default=None, alias="filters")
    "Filters used to narrow down the report data"


class MessageActivityReportFilters(BaseModel):
    "MessageActivityReportFilters model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    filters: dict[str, Any] | None = Field(default=None, alias="filters")
    "Filters used to narrow down the report data"


class MessageClicksReportDetails(BaseModel):
    "MessageClicksReportDetails model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    custom_report_id: str | None = Field(default=None, alias="customReportId")
    "The custom report ID"
    name: str | None = Field(default=None, alias="name")
    "The custom report name"
    href: str | None = Field(default=None, alias="href")
    "The direct hyperlink to a resource"
    type_: Any | None = Field(default=None, alias="type")
    "The custom report type"
    scheduling: dict[str, Any] | None = Field(default=None, alias="scheduling")
    "Parameters responsible for defining the reporting period"
    files: list[dict[str, Any]] | None = Field(default=None, alias="files")
    "Files that have been generated for the given report"
    created_at: datetime | None = Field(default=None, alias="createdAt")
    "Custom report creation date"
    generated_at: datetime | None = Field(default=None, alias="generatedAt")
    "Custom report generation date"
    filters: dict[str, Any] | None = Field(default=None, alias="filters")
    "Filters used to narrow down the report data"


class MessageContent(BaseModel):
    "The message content."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    html: str | None = Field(default=None, alias="html")
    "The message content in HTML"
    plain: str | None = Field(default=None, alias="plain")
    "The plain text equivalent of the message content"


class MessageNotSentCondition(BaseModel):
    "Search contacts who didn't receive a certain message."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    condition_type: MessageNotSentConditionConditionType = Field(alias="conditionType")
    operator_type: MessageNotSentConditionOperatorType = Field(alias="operatorType")
    operator: MessageTypeOperator = Field(alias="operator")
    value: str = Field(alias="value")
    "The message identifier"


class MessageSentCondition(BaseModel):
    "Search contacts who received a certain message."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    condition_type: MessageSentConditionConditionType = Field(alias="conditionType")
    operator_type: MessageSentConditionOperatorType = Field(alias="operatorType")
    operator: MessageTypeOperator = Field(alias="operator")
    value: str = Field(alias="value")
    "The message identifier"


class MessageStatisticsListElement(BaseModel):
    "MessageStatisticsListElement model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    time_interval: str | None = Field(default=None, alias="timeInterval")
    "The statistics time frame in the ISO 8601 datetime format with duration interval"
    sent: int | None = Field(default=None, alias="sent")
    total_opened: int | None = Field(default=None, alias="totalOpened")
    total_human_opened: int | None = Field(default=None, alias="totalHumanOpened")
    unique_opened: int | None = Field(default=None, alias="uniqueOpened")
    unique_human_opened: int | None = Field(default=None, alias="uniqueHumanOpened")
    total_clicked: int | None = Field(default=None, alias="totalClicked")
    total_human_clicked: int | None = Field(default=None, alias="totalHumanClicked")
    unique_clicked: int | None = Field(default=None, alias="uniqueClicked")
    unique_human_clicked: int | None = Field(default=None, alias="uniqueHumanClicked")
    goals: int | None = Field(default=None, alias="goals")
    unique_goals: int | None = Field(default=None, alias="uniqueGoals")
    forwarded: int | None = Field(default=None, alias="forwarded")
    unsubscribed: int | None = Field(default=None, alias="unsubscribed")
    bounced: int | None = Field(default=None, alias="bounced")
    complaints: int | None = Field(default=None, alias="complaints")


class MessageStatsReportDetails(BaseModel):
    "MessageStatsReportDetails model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    custom_report_id: str | None = Field(default=None, alias="customReportId")
    "The custom report ID"
    name: str | None = Field(default=None, alias="name")
    "The custom report name"
    href: str | None = Field(default=None, alias="href")
    "The direct hyperlink to a resource"
    type_: Any | None = Field(default=None, alias="type")
    "The custom report type"
    scheduling: dict[str, Any] | None = Field(default=None, alias="scheduling")
    "Parameters responsible for defining the reporting period"
    files: list[dict[str, Any]] | None = Field(default=None, alias="files")
    "Files that have been generated for the given report"
    created_at: datetime | None = Field(default=None, alias="createdAt")
    "Custom report creation date"
    generated_at: datetime | None = Field(default=None, alias="generatedAt")
    "Custom report generation date"
    filters: dict[str, Any] | None = Field(default=None, alias="filters")
    "Filters used to narrow down the report data"


class MetaField(BaseModel):
    "MetaField model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    href: str | None = Field(default=None, alias="href")
    "Direct hyperlink to a resource"
    meta_field_id: str | None = Field(default=None, alias="metaFieldId")
    "The meta field ID"
    name: str | None = Field(default=None, alias="name")
    "The meta field name"
    value: str | None = Field(default=None, alias="value")
    "The meta field value"
    value_type: MetaFieldValueType | None = Field(default=None, alias="valueType")
    "The value type enumerable"
    description: str | None = Field(default=None, alias="description")
    "The meta field description"
    created_on: datetime | None = Field(default=None, alias="createdOn")
    "The creation date"
    updated_on: datetime | None = Field(default=None, alias="updatedOn")
    "The date of the last update"


class MonthlyReportScheduling(BaseModel):
    "MonthlyReportScheduling model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    frequency: Any | None = Field(default=None, alias="frequency")
    "The custom report frequency"
    one_time: dict[str, Any] | None = Field(default=None, alias="oneTime")
    "Field not applicable to the selected frequency"
    recurring: dict[str, Any] | None = Field(default=None, alias="recurring")
    "A field containing configuration parameters for recurring scheduling"


class NameCondition(BaseModel):
    "NameCondition model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    condition_type: NameConditionConditionType = Field(alias="conditionType")
    operator_type: NameConditionOperatorType = Field(alias="operatorType")
    operator: NameConditionOperator = Field(alias="operator")
    value: str = Field(alias="value")


class NewAbtestsSubject(BaseModel):
    "NewAbtestsSubject model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    ab_test_id: str | None = Field(default=None, alias="abTestId")
    "A/B test ID"
    name: str = Field(alias="name")
    "A/B test name"
    campaign: CampaignReference = Field(alias="campaign")
    "List linked to A/B test"
    from_field: FromFieldReference = Field(alias="fromField")
    'Newsletter\'s From" address"'
    reply_to: FromFieldReference | None = Field(default=None, alias="replyTo")
    "Newsletter's reply-to address"
    delivery_settings: dict[str, Any] = Field(alias="deliverySettings")
    "The A/B test delivery settings"
    flags: list[NewAbtestsSubjectFlagsItem] | None = Field(default=None, alias="flags")
    variants: list[str] = Field(alias="variants")
    "Message variants. Please note, the number of subject variants should be between 2 and 5"
    send_settings: dict[str, Any] = Field(alias="sendSettings")
    "The send settings for the A/B test"
    content: MessageContent = Field(alias="content")


class NewAddress(BaseModel):
    "NewAddress model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    created_on: datetime | None = Field(default=None, alias="createdOn")
    "The creation date"
    updated_on: datetime | None = Field(default=None, alias="updatedOn")
    "The date of the last update"
    address_id: str | None = Field(default=None, alias="addressId")
    href: str | None = Field(default=None, alias="href")
    "Direct hyperlink to a resource"
    country_code: str = Field(alias="countryCode")
    "The country code (ISO 3166-1 alpha-3)"
    country_name: str | None = Field(default=None, alias="countryName")
    "The country name, based on `countryCode`"
    name: str = Field(alias="name")
    first_name: str | None = Field(default=None, alias="firstName")
    last_name: str | None = Field(default=None, alias="lastName")
    address1: str | None = Field(default=None, alias="address1")
    "Address line 1"
    address2: str | None = Field(default=None, alias="address2")
    "Address line 2"
    city: str | None = Field(default=None, alias="city")
    zip: str | None = Field(default=None, alias="zip")
    "The ZIP/postal code, free text"
    province: str | None = Field(default=None, alias="province")
    province_code: str | None = Field(default=None, alias="provinceCode")
    "The province code, free text"
    phone: str | None = Field(default=None, alias="phone")
    "The phone number, free text"
    company: str | None = Field(default=None, alias="company")
    "The company name, free text"


class NewAutoresponder(BaseModel):
    "NewAutoresponder model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    autoresponder_id: str | None = Field(default=None, alias="autoresponderId")
    "The autoresponder ID"
    href: str | None = Field(default=None, alias="href")
    "Direct hyperlink to a resource"
    name: str | None = Field(default=None, alias="name")
    "The autoresponder name"
    subject: str = Field(alias="subject")
    "The autoresponder message subject"
    campaign_id: str | None = Field(default=None, alias="campaignId")
    "The campaign ID. The system will assign the autoresponder to a default campaign if you don't provide a specific campaign ID."
    status: Any = Field(alias="status")
    "The autoresponder status"
    from_field: Any | None = Field(default=None, alias="fromField")
    "The from email address used for the message"
    reply_to: Any | None = Field(default=None, alias="replyTo")
    "The email that will be used as a reply-to address"
    content: MessageContent = Field(alias="content")
    flags: list[MessageFlagsArrayItem] | None = Field(default=None, alias="flags")
    trigger_settings: Any = Field(alias="triggerSettings")
    "The conditions that will trigger the autoresponder"
    statistics: dict[str, Any] | None = Field(default=None, alias="statistics")
    "The autoresponder statistics summary"
    created_on: datetime | None = Field(default=None, alias="createdOn")
    "The creation date"
    send_settings: AutoresponderSendSettingsInput = Field(alias="sendSettings")
    "How the message will be delivered to the subscriber"


class NewCampaign(BaseModel):
    "NewCampaign model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    campaign_id: str | None = Field(default=None, alias="campaignId")
    "Unique identifier of the campaign (contact list)"
    name: str = Field(alias="name")
    "The campaign (list) name. * You can use each list name just once in your account. * The name must be between 3-64 characters. * All alphabets supported by GetResponse, including right-to-left ones, are allowed. * You can use upper and lower case letters, numbers, spaces and special characters apart from the ones listed below. * You can’t use emojis and the following special characters: `/`, `\\`, `@`, and `[` or `]`."
    tech_name: str | None = Field(default=None, alias="techName")
    "Tech name is a unique internal ID of a list used for [FTP imports](https://www.getresponse.com/help/how-to-import-files-via-ftp.html) (available in GetResponse MAX accounts only)"
    language_code: str | None = Field(default=None, alias="languageCode")
    "The campaign language code according to ISO 639-1, plus: zt - Chinese (Traditional), fs - Afghan Persian (Dari), md - Moldavian"
    is_default: Any | None = Field(default=None, alias="isDefault")
    "Is the campaign default"
    created_on: datetime | None = Field(default=None, alias="createdOn")
    "The date of creation"
    href: str | None = Field(default=None, alias="href")
    "Direct hyperlink to a resource"
    postal: CampaignPostal | None = Field(default=None, alias="postal")
    confirmation: CampaignConfirmation | None = Field(default=None, alias="confirmation")
    optin_types: CampaignOptinTypes | None = Field(default=None, alias="optinTypes")
    subscription_notifications: CampaignSubscriptionNotifications | None = Field(
        default=None, alias="subscriptionNotifications"
    )
    profile: CampaignProfile | None = Field(default=None, alias="profile")


class NewCart(BaseModel):
    "NewCart model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    created_on: datetime | None = Field(default=None, alias="createdOn")
    "The creation date"
    updated_on: datetime | None = Field(default=None, alias="updatedOn")
    "The date of the last update"
    cart_id: str | None = Field(default=None, alias="cartId")
    "The contact ID"
    href: str | None = Field(default=None, alias="href")
    "Direct hyperlink to a resource"
    contact_id: str = Field(alias="contactId")
    "The ID of the contact that the cart belongs to. You must first create the contact using POST /v3/contacts, or if it already exists, using GET /v3/contacts"
    total_price: float = Field(alias="totalPrice")
    "The total cart price, tax excluded"
    total_tax_price: float | None = Field(default=None, alias="totalTaxPrice")
    "The total cart price, tax included"
    currency: str = Field(alias="currency")
    "The currency code (ISO 4217)"
    selected_variants: list[NewCartSelectedProductVariant] = Field(alias="selectedVariants")
    external_id: str | None = Field(default=None, alias="externalId")
    "The external ID is the identifying string or number of the cart, given by another software"
    cart_url: str | None = Field(default=None, alias="cartUrl")
    "The external cart URL"


class NewCartSelectedProductVariant(BaseModel):
    "NewCartSelectedProductVariant model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    variant_id: str = Field(alias="variantId")
    "The ID of a selected variant. You must first create a variant using: `POST` [Create product](https://apireference.getresponse.com/#operation/createProduct) `POST` [Create product variant](https://apireference.getresponse.com/#operation/createProductVariant) or get ID from variants created already: `GET` [Get a list of product variants](https://apireference.getresponse.com/#operation/getProductVariantList)"
    quantity: int = Field(alias="quantity")
    "The quantity"
    price: float = Field(alias="price")
    "The price, tax excluded"
    price_tax: float = Field(alias="priceTax")
    "The price, tax included"
    href: str | None = Field(default=None, alias="href")
    "Direct hyperlink to a resource"


class NewCategory(BaseModel):
    "NewCategory model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    category_id: str | None = Field(default=None, alias="categoryId")
    "The category ID"
    href: str | None = Field(default=None, alias="href")
    "Direct hyperlink to a resource"
    name: str = Field(alias="name")
    "The name of the category"
    parent_id: str | None = Field(default=None, alias="parentId")
    "The parent category ID"
    is_default: bool | None = Field(default=None, alias="isDefault")
    "This is a default category"
    url: str | None = Field(default=None, alias="url")
    "The external URL to the category"
    external_id: str | None = Field(default=None, alias="externalId")
    "The external ID is the identifying string or number of the category given by another software"
    created_on: datetime | None = Field(default=None, alias="createdOn")
    "The creation date"
    updated_on: datetime | None = Field(default=None, alias="updatedOn")
    "The date of the last update"


class NewContact(BaseModel):
    "NewContact model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    contact_id: str = Field(alias="contactId")
    name: str | None = Field(default=None, alias="name")
    origin: NewContactOrigin | None = Field(default=None, alias="origin")
    time_zone: str | None = Field(default=None, alias="timeZone")
    "The time zone of a contact, uses the time zone database format (https://www.iana.org/time-zones)"
    activities: str | None = Field(default=None, alias="activities")
    changed_on: datetime | None = Field(default=None, alias="changedOn")
    created_on: datetime | None = Field(default=None, alias="createdOn")
    campaign: CampaignReference = Field(alias="campaign")
    email: str = Field(alias="email")
    day_of_cycle: str | None = Field(default=None, alias="dayOfCycle")
    "The day on which the contact is in the Autoresponder cycle. `null` indicates the contacts is not in the cycle."
    scoring: float | None = Field(default=None, alias="scoring")
    "Contact scoring, pass null to remove the score from a contact"
    engagement_score: int | None = Field(default=None, alias="engagementScore")
    "Engagement Score is a feature that presents a visual estimate of a contact's engagement with mailings. The score is based on the contact's interactions with your e-mails. Via API, it's returned in the form of numbers ranging from 1 (Not Engaged) to 5 (Highly Engaged)."
    href: str = Field(alias="href")
    "Direct hyperlink to a resource"
    ip_address: str | None = Field(default=None, alias="ipAddress")
    "The contact's IP address. IPv4 and IPv6 formats are accepted."
    tags: list[NewContactTag] | None = Field(default=None, alias="tags")
    custom_field_values: list[NewContactCustomFieldValue] | None = Field(
        default=None, alias="customFieldValues"
    )


class NewContactCustomFieldValue(BaseModel):
    "NewContactCustomFieldValue model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    custom_field_id: str = Field(alias="customFieldId")
    "Custom field ID"
    value: list[str] = Field(alias="value")


class NewContactCustomFieldValues(BaseModel):
    "NewContactCustomFieldValues model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    custom_field_values: list[NewContactCustomFieldValue] | None = Field(
        default=None, alias="customFieldValues"
    )


class NewContactTag(BaseModel):
    "NewContactTag model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    tag_id: str = Field(alias="tagId")


class NewContactTags(BaseModel):
    "NewContactTags model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    tags: list[NewContactTag] | None = Field(default=None, alias="tags")


class NewCustomEvent(BaseModel):
    "NewCustomEvent model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    name: str = Field(alias="name")
    "Unique name of custom event"
    attributes: list[CustomEventAttributeDetails] = Field(alias="attributes")
    "Optional collection of attributes"


class NewCustomField(BaseModel):
    "NewCustomField model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    custom_field_id: str | None = Field(default=None, alias="customFieldId")
    "Custom field ID"
    href: str | None = Field(default=None, alias="href")
    "Direct hyperlink to a resource"
    name: str = Field(alias="name")
    "The name of the custom field. It must meet the following requirements: * be unique * use only lowercase letters, underscores and digits * not be equal to one of the merge words used in messages, i.e. `name, email, twitter, facebook, buzz, myspace, linkedin, digg, googleplus, pinterest, responder, campaign, change`."
    type_: Any = Field(alias="type")
    "The custom field `type` accepts the following values: * `string` - input for a string value * `number` - input for a numeric value * `date` - input for a date * `datetime` - input for date and time * `country` - input for a country * `currency` - input for a currency, allows all ISO 4217 currency codes * `phone` - input for a phone number * `gender` - input for gender, allows `Male`, `Female` or `Prefer not to say` * `ip` - input for an IP address * `url` - input for a URL."
    value_type: NewCustomFieldValueType | None = Field(default=None, alias="valueType")
    "Type of returning value, it returns `type` options extended by a `string` option if the `format` was not defined"
    format: Any = Field(alias="format")
    "The custom field `format` accepts following values: * `text` - text input (doesn't require values in the `values` field, you can pass empty array) * `textarea` - textarea input (doesn't require values in the `values` field, you can pass empty array) * `radio` - radio input (requires at least 2 values in the `values` field) * `checkbox` - checkbox input (doesn't require values in the `values` field, you can pass empty array) * `single_select` - single select input (requires at least 2 values in the `values` field) * `multi_select` - multi select input (requires at least 2 values in the `values` field)."
    field_type: str | None = Field(default=None, alias="fieldType")
    "Returns the same as `format`"
    hidden: Any = Field(alias="hidden")
    "Whether the custom field is visible to contacts"
    values: list[str] = Field(alias="values")
    "The list of assigned default values, starting from zero depending on the custom field format. (Please see description)."


class NewFile(BaseModel):
    "NewFile model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    name: str = Field(alias="name")
    "The file name"
    extension: str = Field(alias="extension")
    "The file extension"
    folder: dict[str, Any] = Field(alias="folder")
    "The folder where the file is stored"
    content: str = Field(alias="content")
    "The base64 encoded file content"


class NewFolder(BaseModel):
    "NewFolder model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    name: str = Field(alias="name")
    "The folder name"


class NewFromField(BaseModel):
    "NewFromField model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    email: str = Field(alias="email")
    "The email address"
    name: str = Field(alias="name")
    "The name connected to the email address"


class NewImport(BaseModel):
    "NewImport model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    campaign_id: str = Field(alias="campaignId")
    "The ID of the destination campaign (list)"
    field_mapping: list[str] = Field(alias="fieldMapping")
    "Mapping definition for such contact properties as email address, name, or custom fields. It's the equivalent of column headers in a CSV file used to import contacts in a GetResponse account. The `email` value is required. For custom fields, provide only custom fields name in the mapping. Include their values in the corresponding field in the contact array"
    contacts: list[list[str]] = Field(alias="contacts")
    "Container for a contact definition. Include the values defined in the `fieldMapping` array"


class NewMetaField(BaseModel):
    "NewMetaField model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    href: str | None = Field(default=None, alias="href")
    "Direct hyperlink to a resource"
    meta_field_id: str | None = Field(default=None, alias="metaFieldId")
    "The meta field ID"
    name: str = Field(alias="name")
    "The meta field name"
    value: str = Field(alias="value")
    "The meta field value"
    value_type: NewMetaFieldValueType = Field(alias="valueType")
    "The value type enumerable"
    description: str | None = Field(default=None, alias="description")
    "The meta field description"


class NewNewsletter(BaseModel):
    "NewNewsletter model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    content: MessageContent = Field(alias="content")
    flags: list[MessageFlagsArrayItem] | None = Field(default=None, alias="flags")
    name: str | None = Field(default=None, alias="name")
    "The newsletter name"
    type_: NewNewsletterType | None = Field(default=None, alias="type")
    "The newsletter type"
    subject: str = Field(alias="subject")
    "The message subject"
    from_field: Any = Field(alias="fromField")
    "The 'From' email address used for the message"
    reply_to: Any | None = Field(default=None, alias="replyTo")
    "The email that will be used as the reply-to address"
    campaign: Any = Field(alias="campaign")
    "The newsletter must be assigned to a campaign"
    attachments: list[NewsletterAttachment] | None = Field(default=None, alias="attachments")
    "The newsletter attachments. The size of all attachments combined can't exceed 400KB"
    send_settings: Any = Field(alias="sendSettings")
    "How the message will be delivered to the subscriber. You can specify multiple parameters. Then the system uses AND logic."


class NewOrder(BaseModel):
    "NewOrder model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    order_id: str | None = Field(default=None, alias="orderId")
    "The order ID"
    href: str | None = Field(default=None, alias="href")
    "Direct hyperlink to a resource"
    contact_id: str = Field(alias="contactId")
    "Create a contact by using `POST /v3/contacts`. Or, if the contact already exists, using `GET /v3/contacts`"
    order_url: str | None = Field(default=None, alias="orderUrl")
    "The external URL for an order"
    external_id: str | None = Field(default=None, alias="externalId")
    "The external ID is the identifying string or number of the order given by another software"
    total_price: float = Field(alias="totalPrice")
    "The total price of an order"
    total_price_tax: float | None = Field(default=None, alias="totalPriceTax")
    "The total price tax of an order"
    currency: str = Field(alias="currency")
    "The order currency code (ISO 4217)"
    status: str | None = Field(default=None, alias="status")
    "The status value"
    cart_id: str | None = Field(default=None, alias="cartId")
    "Create a cart by using `POST /v3/shops/{shopId}/carts`"
    description: str | None = Field(default=None, alias="description")
    "The order description"
    shipping_price: float | None = Field(default=None, alias="shippingPrice")
    "The shipping price for an order"
    shipping_address: Any | None = Field(default=None, alias="shippingAddress")
    "The shipping address for an order"
    billing_status: str | None = Field(default=None, alias="billingStatus")
    "The billing status of an order"
    billing_address: Any | None = Field(default=None, alias="billingAddress")
    "The billing address for an order"
    processed_at: datetime | None = Field(default=None, alias="processedAt")
    "The exact time an order was made"
    meta_fields: list[NewMetaField] | None = Field(default=None, alias="metaFields")
    selected_variants: list[NewSelectedProductVariant] = Field(alias="selectedVariants")


class NewPredefinedField(BaseModel):
    "NewPredefinedField model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    predefined_field_id: str | None = Field(default=None, alias="predefinedFieldId")
    href: str | None = Field(default=None, alias="href")
    "Direct hyperlink to a resource"
    name: str = Field(alias="name")
    value: str = Field(alias="value")
    campaign: CampaignReference = Field(alias="campaign")


class NewProduct(BaseModel):
    "NewProduct model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    created_on: datetime | None = Field(default=None, alias="createdOn")
    "The creation date"
    updated_on: datetime | None = Field(default=None, alias="updatedOn")
    "The date of the last update"
    product_id: str | None = Field(default=None, alias="productId")
    "The product ID"
    href: str | None = Field(default=None, alias="href")
    "Direct hyperlink to a resource"
    name: str = Field(alias="name")
    "The product name"
    type_: str | None = Field(default=None, alias="type")
    "The product type"
    url: str | None = Field(default=None, alias="url")
    "The external URL for the product"
    vendor: str | None = Field(default=None, alias="vendor")
    "The product vendor"
    external_id: str | None = Field(default=None, alias="externalId")
    "The external ID is the identifying string or number of the product given by another software"
    categories: list[NewProductCategory] | None = Field(default=None, alias="categories")
    variants: list[NewProductVariant] = Field(alias="variants")
    meta_fields: list[NewMetaField] | None = Field(default=None, alias="metaFields")


class NewProductCategory(BaseModel):
    "NewProductCategory model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    category_id: str | None = Field(default=None, alias="categoryId")
    "The category ID"
    href: str | None = Field(default=None, alias="href")
    "Direct hyperlink to a resource"
    name: str = Field(alias="name")
    "The name of the category"
    parent_id: str | None = Field(default=None, alias="parentId")
    "The parent category ID"
    is_default: bool | None = Field(default=None, alias="isDefault")
    "This is a default category"
    url: str | None = Field(default=None, alias="url")
    "The external URL to the category"
    external_id: str | None = Field(default=None, alias="externalId")
    "The external ID is the identifying string or number of the category given by another software"


class NewProductVariant(BaseModel):
    "NewProductVariant model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    variant_id: str | None = Field(default=None, alias="variantId")
    "The product ID"
    href: str | None = Field(default=None, alias="href")
    "Direct hyperlink to a resource"
    name: str = Field(alias="name")
    "The product name"
    url: str | None = Field(default=None, alias="url")
    "The external URL to the product variant"
    sku: str = Field(alias="sku")
    "The stock-keeping unit of a variant. Must be unique within the product"
    price: float = Field(alias="price")
    "The price"
    price_tax: float = Field(alias="priceTax")
    "The price including tax"
    previous_price: float | None = Field(default=None, alias="previousPrice")
    "The price before the change"
    previous_price_tax: float | None = Field(default=None, alias="previousPriceTax")
    "The price before the change including tax"
    quantity: int | None = Field(default=None, alias="quantity")
    "The quantity of variant items"
    position: int | None = Field(default=None, alias="position")
    "The position of a variant"
    barcode: str | None = Field(default=None, alias="barcode")
    "The barcode of a variant"
    external_id: str | None = Field(default=None, alias="externalId")
    "The external ID is the identifying string or number of the variant given by another software"
    description: str | None = Field(default=None, alias="description")
    "The description of a variant"
    images: list[NewProductVariantImage] | None = Field(default=None, alias="images")
    meta_fields: list[NewMetaField] | None = Field(default=None, alias="metaFields")
    taxes: list[NewTax] | None = Field(default=None, alias="taxes")


class NewProductVariantImage(BaseModel):
    "NewProductVariantImage model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    image_id: str | None = Field(default=None, alias="imageId")
    "The image ID"
    href: str | None = Field(default=None, alias="href")
    "Direct hyperlink to a resource"
    src: str = Field(alias="src")
    "The source URL of an image"
    position: int = Field(alias="position")
    "The position of an image"


class NewRssNewsletter(BaseModel):
    "NewRssNewsletter model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    rss_newsletter_id: str = Field(alias="rssNewsletterId")
    "The RSS newsletter ID"
    href: str = Field(alias="href")
    "Direct hyperlink to a resource"
    rss_feed_url: str = Field(alias="rssFeedUrl")
    "The URL for the RSS Feed"
    subject: str = Field(alias="subject")
    "The RSS message subject"
    name: str | None = Field(default=None, alias="name")
    "How your newsletters will be seen inside the application"
    status: Any = Field(alias="status")
    "The status of the RSS newsletter"
    editor: Any | None = Field(default=None, alias="editor")
    from_field: Any = Field(alias="fromField")
    "The 'From' email address used for the message"
    reply_to: Any | None = Field(default=None, alias="replyTo")
    "The email that will be used as a reply-to address"
    content: MessageContent = Field(alias="content")
    send_settings: Any = Field(alias="sendSettings")
    "How the message will be delivered to the subscriber"
    created_on: datetime | None = Field(default=None, alias="createdOn")
    "The creation date"
    flags: list[MessageFlagsArrayItem] | None = Field(default=None, alias="flags")


class NewSearchContacts(BaseModel):
    "New search contacts."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    subscribers_type: list[NewSearchContactsSubscribersTypeItem] | None = Field(
        default=None, alias="subscribersType"
    )
    "Only one subscription status"
    section_logic_operator: NewSearchContactsSectionLogicOperator = Field(
        alias="sectionLogicOperator"
    )
    "Match 'any' (`or` value) or 'all' (`and` value) of the following conditions"
    section: list[SearchContactSection] = Field(alias="section")
    search_contact_id: str | None = Field(default=None, alias="searchContactId")
    "The unique search-contact identifier"
    name: str = Field(alias="name")
    "The unique name of search-contact"
    created_on: datetime | None = Field(default=None, alias="createdOn")
    "The UTC date time format ISO 8601, e.g. 2018-04-10T10:02:57+0000"
    href: str | None = Field(default=None, alias="href")
    "Direct hyperlink to a resource"


class NewSelectedProductVariant(BaseModel):
    "NewSelectedProductVariant model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    href: str | None = Field(default=None, alias="href")
    "Direct hyperlink to a resource"
    variant_id: str = Field(alias="variantId")
    "The ID of a selected variant. You must first create a variant using: `POST` [Create product](https://apireference.getresponse.com/#operation/createProduct) `POST` [Create product variant](https://apireference.getresponse.com/#operation/createProductVariant) or get ID from variants created already: `GET` [Get a list of product variants](https://apireference.getresponse.com/#operation/getProductVariantList)"
    price: float = Field(alias="price")
    "The product variant price"
    price_tax: float | None = Field(default=None, alias="priceTax")
    "The product variant price tax"
    quantity: int = Field(alias="quantity")
    "The product variant quantity"
    taxes: list[NewTax] | None = Field(default=None, alias="taxes")


class NewShop(BaseModel):
    "NewShop model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    created_on: datetime | None = Field(default=None, alias="createdOn")
    "The creation date"
    updated_on: datetime | None = Field(default=None, alias="updatedOn")
    "The date of the last update"
    shop_id: str | None = Field(default=None, alias="shopId")
    "The shop ID"
    href: str | None = Field(default=None, alias="href")
    "Direct hyperlink to a resource"
    name: str = Field(alias="name")
    "The shop name"
    locale: str = Field(alias="locale")
    "The language locale (ISO 639-1)"
    currency: str = Field(alias="currency")
    "The currency code (ISO 4217)"


class NewSuppression(BaseModel):
    "NewSuppression model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    name: str = Field(alias="name")
    "The name of the suppression list"
    masks: list[str] | None = Field(default=None, alias="masks")


class NewTag(BaseModel):
    "NewTag model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    name: str = Field(alias="name")
    "The tag name"
    color: str | None = Field(default=None, alias="color")
    "The tag color (deprecated)"


class NewTax(BaseModel):
    "NewTax model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    tax_id: str | None = Field(default=None, alias="taxId")
    "The tax ID"
    href: str | None = Field(default=None, alias="href")
    "Direct hyperlink to a resource"
    name: str = Field(alias="name")
    "The tax name"
    rate: float = Field(alias="rate")
    "The rate value"


class NewTransactionalEmailTag(BaseModel):
    "NewTransactionalEmailTag model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    tag_id: str = Field(alias="tagId")


class Newsletter(BaseModel):
    "Newsletter model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    newsletter_id: str = Field(alias="newsletterId")
    "The newsletter ID"
    href: str = Field(alias="href")
    "Direct hyperlink to a resource"
    name: str | None = Field(default=None, alias="name")
    "The newsletter name"
    type_: NewsletterType | None = Field(default=None, alias="type")
    "The newsletter type"
    status: Any | None = Field(default=None, alias="status")
    "The newsletter status"
    editor: Any | None = Field(default=None, alias="editor")
    "This describes how the content of the message was created"
    subject: str | None = Field(default=None, alias="subject")
    "The message subject"
    from_field: Any | None = Field(default=None, alias="fromField")
    "The 'From' email address used for the message"
    reply_to: Any | None = Field(default=None, alias="replyTo")
    "The email that will be used as the reply-to address"
    campaign: Any | None = Field(default=None, alias="campaign")
    "The newsletter must be assigned to a campaign"
    send_on: datetime | None = Field(default=None, alias="sendOn")
    "The scheduled send date and time for the newsletter in the ISO 8601 format."
    attachments: list[NewsletterAttachment] | None = Field(default=None, alias="attachments")
    "The newsletter attachments. The size of all attachments combined can't exceed 400KB"
    send_settings: Any | None = Field(default=None, alias="sendSettings")
    "How the message will be delivered to the subscriber. You can specify multiple parameters. Then the system uses AND logic."
    send_metrics: dict[str, Any] | None = Field(default=None, alias="sendMetrics")
    "The sending metrics"
    created_on: datetime | None = Field(default=None, alias="createdOn")
    "The creation date"


class NewsletterActivity(BaseModel):
    "NewsletterActivity model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    activity: NewsletterActivityActivity | None = Field(default=None, alias="activity")
    "The type of activity"
    created_on: datetime | None = Field(default=None, alias="createdOn")
    "The date when activity occurred"
    contact: Any | None = Field(default=None, alias="contact")
    "The contact ID"


class NewsletterActivityContactReference(BaseModel):
    "NewsletterActivityContactReference model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    contact_id: str | None = Field(default=None, alias="contactId")
    "Unique identifier of the contact. You can retrieve this ID from the [list of contacts](https://apireference.getresponse.com/#operation/getContactList) field: contactId"
    email: str | None = Field(default=None, alias="email")
    "The contact email"
    href: str | None = Field(default=None, alias="href")
    "Direct hyperlink to a resource"


class NewsletterAttachment(BaseModel):
    "NewsletterAttachment model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    file_name: str | None = Field(default=None, alias="fileName")
    "The file name"
    content: str | None = Field(default=None, alias="content")
    "The base64 encoded file content"
    mime_type: str | None = Field(default=None, alias="mimeType")
    "The file mime type"


class NewsletterDetails(BaseModel):
    "NewsletterDetails model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    newsletter_id: str = Field(alias="newsletterId")
    "The newsletter ID"
    href: str = Field(alias="href")
    "Direct hyperlink to a resource"
    name: str | None = Field(default=None, alias="name")
    "The newsletter name"
    type_: NewsletterDetailsType | None = Field(default=None, alias="type")
    "The newsletter type"
    status: Any | None = Field(default=None, alias="status")
    "The newsletter status"
    editor: Any | None = Field(default=None, alias="editor")
    "This describes how the content of the message was created"
    subject: str | None = Field(default=None, alias="subject")
    "The message subject"
    from_field: Any | None = Field(default=None, alias="fromField")
    "The 'From' email address used for the message"
    reply_to: Any | None = Field(default=None, alias="replyTo")
    "The email that will be used as the reply-to address"
    campaign: Any | None = Field(default=None, alias="campaign")
    "The newsletter must be assigned to a campaign"
    send_on: datetime | None = Field(default=None, alias="sendOn")
    "The scheduled send date and time for the newsletter in the ISO 8601 format."
    attachments: list[NewsletterAttachment] | None = Field(default=None, alias="attachments")
    "The newsletter attachments. The size of all attachments combined can't exceed 400KB"
    send_settings: Any | None = Field(default=None, alias="sendSettings")
    "How the message will be delivered to the subscriber. You can specify multiple parameters. Then the system uses AND logic."
    send_metrics: dict[str, Any] | None = Field(default=None, alias="sendMetrics")
    "The sending metrics"
    created_on: datetime | None = Field(default=None, alias="createdOn")
    "The creation date"
    content: MessageContent | None = Field(default=None, alias="content")
    click_tracks: list[ClickTrack] | None = Field(default=None, alias="clickTracks")
    "The list of tracked links"
    flags: list[MessageFlagsArrayItem] | None = Field(default=None, alias="flags")


class NewsletterListElement(BaseModel):
    "NewsletterListElement model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    newsletter_id: str = Field(alias="newsletterId")
    "The newsletter ID"
    href: str = Field(alias="href")
    "Direct hyperlink to a resource"
    name: str | None = Field(default=None, alias="name")
    "The newsletter name"
    type_: NewsletterListElementType | None = Field(default=None, alias="type")
    "The newsletter type"
    status: Any | None = Field(default=None, alias="status")
    "The newsletter status"
    editor: Any | None = Field(default=None, alias="editor")
    "This describes how the content of the message was created"
    subject: str | None = Field(default=None, alias="subject")
    "The message subject"
    campaign: Any | None = Field(default=None, alias="campaign")
    "The newsletter must be assigned to a campaign"
    send_on: datetime | None = Field(default=None, alias="sendOn")
    "The scheduled send date and time for the newsletter in the ISO 8601 format."
    send_settings: Any | None = Field(default=None, alias="sendSettings")
    "How the message will be delivered to the subscriber. You can specify multiple parameters. Then the system uses AND logic."
    send_metrics: dict[str, Any] | None = Field(default=None, alias="sendMetrics")
    "The sending metrics"
    created_on: datetime | None = Field(default=None, alias="createdOn")
    "The creation date"
    flags: str | None = Field(default=None, alias="flags")


class NewsletterSendSettingsDetails(BaseModel):
    "NewsletterSendSettingsDetails model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    selected_campaigns: Any | None = Field(default=None, alias="selectedCampaigns")
    "The list of selected campaigns"
    selected_segments: Any | None = Field(default=None, alias="selectedSegments")
    "The list of selected segments"
    selected_suppressions: Any | None = Field(default=None, alias="selectedSuppressions")
    "The list of selected suppressions (suppressions exclude contacts)"
    excluded_campaigns: Any | None = Field(default=None, alias="excludedCampaigns")
    "The list of excluded campaigns"
    excluded_segments: Any | None = Field(default=None, alias="excludedSegments")
    "The list of excluded segments"
    selected_contacts: Any | None = Field(default=None, alias="selectedContacts")
    "The list of selected contacts"
    time_travel: Any | None = Field(default=None, alias="timeTravel")
    "Use the time travel functionality. This means that the system will match the scheduled sending hour for the message to the time zone of each recipient. As a result, sending may take up to 24 hours."
    perfect_timing: Any | None = Field(default=None, alias="perfectTiming")
    "Use the perfect timing functionality"
    external_lexpad: dict[str, Any] | None = Field(default=None, alias="externalLexpad")
    "External Lexpad settings for the message, read more: [External Lexpad](https://apidocs.getresponse.com/v3/dynamic-content/external-lexpad)"
    send_on: dict[str, Any] | None = Field(default=None, alias="sendOn")
    "The scheduled send date and time for the newsletter. **Please note:** To send your message immediately, omit the `sendOn` section"


class NewsletterSendSettingsListing(BaseModel):
    "NewsletterSendSettingsListing model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    time_travel: Any | None = Field(default=None, alias="timeTravel")
    "Use the time travel functionality. This means that the system will match the scheduled sending hour for the message to the time zone of each recipient. As a result, sending may take up to 24 hours."
    perfect_timing: Any | None = Field(default=None, alias="perfectTiming")
    "Use the perfect timing functionality"


class NotOpenedCondition(BaseModel):
    "Search contacts who didn't open a message."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    condition_type: NotOpenedConditionConditionType = Field(alias="conditionType")
    operator_type: NotOpenedConditionOperatorType = Field(alias="operatorType")
    operator: dict[str, Any] = Field(alias="operator")
    "Specifies the type of message to search for"
    scope: str | None = Field(default=None, alias="scope")
    "The message identifier. Required only for the operator different from 'all'."
    date_operator: NotOpenedConditionDateOperator = Field(alias="dateOperator")
    "It allows you to set a date range. For some of them `value` will be required. Examples can be found here: [API Docs](https://apidocs.getresponse.com/v3/case-study/segments-manual#not-opened-action)."
    value: dict[str, Any] | None = Field(default=None, alias="value")
    "This field is required only for `date_from` and `last_n_days` date operators."
    include_current_period: bool | None = Field(default=None, alias="includeCurrentPeriod")
    "Flag determines if current day will be included into chosen range. This flag can be used with `last_7_days`, `last_30_days`, `last_n_days`."


class OneTimeReportScheduling(BaseModel):
    "OneTimeReportScheduling model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    frequency: Any | None = Field(default=None, alias="frequency")
    "The custom report frequency"
    one_time: dict[str, Any] | None = Field(default=None, alias="oneTime")
    "A field containing configuration parameters for one-time scheduling"
    recurring: dict[str, Any] | None = Field(default=None, alias="recurring")
    "Field not applicable to the selected frequency"


class OneTimeScheduling(BaseModel):
    "OneTimeScheduling model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    one_time: dict[str, Any] | None = Field(default=None, alias="oneTime")
    "A field containing configuration parameters for one-time scheduling"
    recurring: dict[str, Any] | None = Field(default=None, alias="recurring")
    "Field not applicable to the selected frequency"


class OpenedCondition(BaseModel):
    "Search contacts who did open a message."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    condition_type: OpenedConditionConditionType = Field(alias="conditionType")
    operator_type: OpenedConditionOperatorType = Field(alias="operatorType")
    operator: MessageTypeOperator = Field(alias="operator")
    value: str = Field(alias="value")
    "The identifier of a selected resource: autoresponder, newsletter, split test or automation message"


class Order(BaseModel):
    "Order model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    order_id: str | None = Field(default=None, alias="orderId")
    "The order ID"
    href: str | None = Field(default=None, alias="href")
    "Direct hyperlink to a resource"
    contact_id: str | None = Field(default=None, alias="contactId")
    "Create a contact by using `POST /v3/contacts`. Or, if the contact already exists, using `GET /v3/contacts`"
    order_url: str | None = Field(default=None, alias="orderUrl")
    "The external URL for an order"
    external_id: str | None = Field(default=None, alias="externalId")
    "The external ID is the identifying string or number of the order given by another software"
    total_price: float | None = Field(default=None, alias="totalPrice")
    "The total price of an order"
    total_price_tax: float | None = Field(default=None, alias="totalPriceTax")
    "The total price tax of an order"
    currency: str | None = Field(default=None, alias="currency")
    "The order currency code (ISO 4217)"
    status: str | None = Field(default=None, alias="status")
    "The status value"
    cart_id: str | None = Field(default=None, alias="cartId")
    "Create a cart by using `POST /v3/shops/{shopId}/carts`"
    description: str | None = Field(default=None, alias="description")
    "The order description"
    shipping_price: float | None = Field(default=None, alias="shippingPrice")
    "The shipping price for an order"
    shipping_address: Any | None = Field(default=None, alias="shippingAddress")
    "The shipping address for an order"
    billing_status: str | None = Field(default=None, alias="billingStatus")
    "The billing status of an order"
    billing_address: Any | None = Field(default=None, alias="billingAddress")
    "The billing address for an order"
    processed_at: datetime | None = Field(default=None, alias="processedAt")
    "The exact time an order was made"
    meta_fields: list[NewMetaField] | None = Field(default=None, alias="metaFields")


class OrderResponse(BaseModel):
    "OrderResponse model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    order_id: str | None = Field(default=None, alias="orderId")
    "The order ID"
    href: str | None = Field(default=None, alias="href")
    "Direct hyperlink to a resource"
    contact_id: str | None = Field(default=None, alias="contactId")
    "Create a contact by using `POST /v3/contacts`. Or, if the contact already exists, using `GET /v3/contacts`"
    order_url: str | None = Field(default=None, alias="orderUrl")
    "The external URL for an order"
    external_id: str | None = Field(default=None, alias="externalId")
    "The external ID is the identifying string or number of the order given by another software"
    total_price: float | None = Field(default=None, alias="totalPrice")
    "The total price of an order"
    total_price_tax: float | None = Field(default=None, alias="totalPriceTax")
    "The total price tax of an order"
    currency: str | None = Field(default=None, alias="currency")
    "The order currency code (ISO 4217)"
    status: str | None = Field(default=None, alias="status")
    "The status value"
    cart_id: str | None = Field(default=None, alias="cartId")
    "Create a cart by using `POST /v3/shops/{shopId}/carts`"
    description: str | None = Field(default=None, alias="description")
    "The order description"
    shipping_price: float | None = Field(default=None, alias="shippingPrice")
    "The shipping price for an order"
    shipping_address: Any | None = Field(default=None, alias="shippingAddress")
    "The shipping address for an order"
    billing_status: str | None = Field(default=None, alias="billingStatus")
    "The billing status of an order"
    billing_address: Any | None = Field(default=None, alias="billingAddress")
    "The billing address for an order"
    processed_at: datetime | None = Field(default=None, alias="processedAt")
    "The exact time an order was made"
    meta_fields: list[NewMetaField] | None = Field(default=None, alias="metaFields")
    selected_variants: list[OrderSelectedProductVariant] | None = Field(
        default=None, alias="selectedVariants"
    )


class OrderSelectedProductVariant(BaseModel):
    "OrderSelectedProductVariant model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    href: str | None = Field(default=None, alias="href")
    "Direct hyperlink to a resource"
    variant_id: str = Field(alias="variantId")
    "The ID of a selected variant. You must first create a variant using: `POST` [Create product](https://apireference.getresponse.com/#operation/createProduct) `POST` [Create product variant](https://apireference.getresponse.com/#operation/createProductVariant) or get ID from variants created already: `GET` [Get a list of product variants](https://apireference.getresponse.com/#operation/getProductVariantList)"
    price: float = Field(alias="price")
    "The product variant price"
    price_tax: float | None = Field(default=None, alias="priceTax")
    "The product variant price tax"
    quantity: int = Field(alias="quantity")
    "The product variant quantity"
    taxes: list[NewTax] | None = Field(default=None, alias="taxes")
    categories: list[BaseCategory] | None = Field(default=None, alias="categories")


class PopupDetails(BaseModel):
    "PopupDetails model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    popup_id: str | None = Field(default=None, alias="popupId")
    "The form or popup ID"
    href: str | None = Field(default=None, alias="href")
    "Direct hyperlink to a resource"
    name: str | None = Field(default=None, alias="name")
    "The form or popup name"
    status: PopupDetailsStatus | None = Field(default=None, alias="status")
    "The form or popup status"
    type_: PopupDetailsType | None = Field(default=None, alias="type")
    "The form or popup type"
    thumbnail_url: str | None = Field(default=None, alias="thumbnailUrl")
    "Direct hyperlink to a resource"
    created_at: datetime | None = Field(default=None, alias="createdAt")
    "The date (in GMT) the form or popup was created. Shown in format `ISO 8601` without timezone offset e.g. `2024-01-01T10:35:00`."
    updated_at: datetime | None = Field(default=None, alias="updatedAt")
    "The date (in GMT) the form or popup was updated. Shown in format `ISO 8601` without timezone offset e.g. `2024-01-10T10:00:00`."


class PopupGeneralPerformanceStats(BaseModel):
    "PopupGeneralPerformanceStats model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    popup_id: str = Field(alias="popupId")
    "The form or popup ID"
    views: int | None = Field(default=None, alias="views")
    "The total number of times your popup was viewed by website visitors"
    clicks: int | None = Field(default=None, alias="clicks")
    "The number of clicks"
    ctr: int | None = Field(default=None, alias="ctr")
    "The number of clicks divided by the number of views, shown as a percentage"
    leads: int | None = Field(default=None, alias="leads")
    "The number of leads"


class PopupListItem(BaseModel):
    "PopupListItem model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    popup_id: str | None = Field(default=None, alias="popupId")
    "The form or popup ID"
    href: str | None = Field(default=None, alias="href")
    "Direct hyperlink to a resource"
    name: str | None = Field(default=None, alias="name")
    "The form or popup name"
    status: PopupListItemStatus | None = Field(default=None, alias="status")
    "The form or popup status"
    type_: PopupListItemType | None = Field(default=None, alias="type")
    "The form or popup type"
    created_at: datetime | None = Field(default=None, alias="createdAt")
    "The date (in GMT) the form or popup was created. Shown in format `ISO 8601` without timezone offset e.g. `2024-01-01T10:35:00`."
    updated_at: datetime | None = Field(default=None, alias="updatedAt")
    "The date (in GMT) the form or popup was updated. Shown in format `ISO 8601` without timezone offset e.g. `2024-01-10T10:00:00`."
    statistics: PopupListItemStatistics | None = Field(default=None, alias="statistics")
    "The landing page statistics"


class PopupListItemStatistics(BaseModel):
    "PopupListItemStatistics model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    views: int | None = Field(default=None, alias="views")
    "The total number of times your popup was viewed by website visitors"
    unique_visitors: int | None = Field(default=None, alias="uniqueVisitors")
    "The total number of visitors"
    leads: int | None = Field(default=None, alias="leads")
    "The number of leads"
    ctr: int | None = Field(default=None, alias="ctr")
    "The number of clicks divided by the number of views, shown as a percentage"


class PredefinedField(BaseModel):
    "PredefinedField model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    predefined_field_id: str | None = Field(default=None, alias="predefinedFieldId")
    href: str | None = Field(default=None, alias="href")
    "Direct hyperlink to a resource"
    name: str | None = Field(default=None, alias="name")
    value: str | None = Field(default=None, alias="value")
    campaign: CampaignReference | None = Field(default=None, alias="campaign")


class PredefinedFieldDetails(BaseModel):
    "The predefined field details."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    predefined_field_id: str | None = Field(default=None, alias="predefinedFieldId")
    href: str | None = Field(default=None, alias="href")
    "Direct hyperlink to a resource"
    name: str | None = Field(default=None, alias="name")
    value: str | None = Field(default=None, alias="value")
    campaign: CampaignReference | None = Field(default=None, alias="campaign")


class Product(BaseModel):
    "Product model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    created_on: datetime | None = Field(default=None, alias="createdOn")
    "The creation date"
    updated_on: datetime | None = Field(default=None, alias="updatedOn")
    "The date of the last update"
    product_id: str | None = Field(default=None, alias="productId")
    "The product ID"
    href: str | None = Field(default=None, alias="href")
    "Direct hyperlink to a resource"
    name: str | None = Field(default=None, alias="name")
    "The product name"
    type_: str | None = Field(default=None, alias="type")
    "The product type"
    url: str | None = Field(default=None, alias="url")
    "The external URL for the product"
    vendor: str | None = Field(default=None, alias="vendor")
    "The product vendor"
    external_id: str | None = Field(default=None, alias="externalId")
    "The external ID is the identifying string or number of the product given by another software"
    categories: list[NewProductCategory] | None = Field(default=None, alias="categories")
    variants: list[NewProductVariant] | None = Field(default=None, alias="variants")
    meta_fields: list[NewMetaField] | None = Field(default=None, alias="metaFields")


class ProductCategory(BaseModel):
    "ProductCategory model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    category_id: str | None = Field(default=None, alias="categoryId")
    "The category ID"
    href: str | None = Field(default=None, alias="href")
    "Direct hyperlink to a resource"
    name: str | None = Field(default=None, alias="name")
    "The name of the category"
    parent_id: str | None = Field(default=None, alias="parentId")
    "The parent category ID"
    is_default: bool | None = Field(default=None, alias="isDefault")
    "This is a default category"
    url: str | None = Field(default=None, alias="url")
    "The external URL to the category"
    external_id: str | None = Field(default=None, alias="externalId")
    "The external ID is the identifying string or number of the category given by another software"
    created_on: datetime | None = Field(default=None, alias="createdOn")
    "The creation date"
    updated_on: datetime | None = Field(default=None, alias="updatedOn")
    "The date of the last update"


class ProductVariant(BaseModel):
    "ProductVariant model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    variant_id: str | None = Field(default=None, alias="variantId")
    "The product ID"
    href: str | None = Field(default=None, alias="href")
    "Direct hyperlink to a resource"
    name: str | None = Field(default=None, alias="name")
    "The product name"
    url: str | None = Field(default=None, alias="url")
    "The external URL to the product variant"
    sku: str | None = Field(default=None, alias="sku")
    "The stock-keeping unit of a variant. Must be unique within the product"
    price: float | None = Field(default=None, alias="price")
    "The price"
    price_tax: float | None = Field(default=None, alias="priceTax")
    "The price including tax"
    previous_price: float | None = Field(default=None, alias="previousPrice")
    "The price before the change"
    previous_price_tax: float | None = Field(default=None, alias="previousPriceTax")
    "The price before the change including tax"
    quantity: int | None = Field(default=None, alias="quantity")
    "The quantity of variant items"
    position: int | None = Field(default=None, alias="position")
    "The position of a variant"
    barcode: str | None = Field(default=None, alias="barcode")
    "The barcode of a variant"
    external_id: str | None = Field(default=None, alias="externalId")
    "The external ID is the identifying string or number of the variant given by another software"
    description: str | None = Field(default=None, alias="description")
    "The description of a variant"
    images: list[NewProductVariantImage] | None = Field(default=None, alias="images")
    meta_fields: list[NewMetaField] | None = Field(default=None, alias="metaFields")
    taxes: list[NewTax] | None = Field(default=None, alias="taxes")
    created_on: datetime | None = Field(default=None, alias="createdOn")
    "The creation date"
    updated_on: datetime | None = Field(default=None, alias="updatedOn")
    "The date of the last update"


class Quota(BaseModel):
    "Quota model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    limit: int | None = Field(default=None, alias="limit")
    "The total size of available storage space"
    usage: int | None = Field(default=None, alias="usage")
    "The currently used storage space"


class RecurringScheduling(BaseModel):
    "RecurringScheduling model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    one_time: dict[str, Any] | None = Field(default=None, alias="oneTime")
    "Field not applicable to the selected frequency"
    recurring: dict[str, Any] | None = Field(default=None, alias="recurring")
    "A field containing configuration parameters for recurring scheduling"


class RevenueStatistics(BaseModel):
    "RevenueStatistics model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    currency: str | None = Field(default=None, alias="currency")
    "Statistics currency"
    time_series: list[dict[str, Any]] | None = Field(default=None, alias="timeSeries")


class RssNewsletter(BaseModel):
    "RssNewsletter model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    rss_newsletter_id: str = Field(alias="rssNewsletterId")
    "The RSS newsletter ID"
    href: str = Field(alias="href")
    "Direct hyperlink to a resource"
    rss_feed_url: str | None = Field(default=None, alias="rssFeedUrl")
    "The URL for the RSS Feed"
    subject: str | None = Field(default=None, alias="subject")
    "The RSS message subject"
    name: str | None = Field(default=None, alias="name")
    "How your newsletters will be seen inside the application"
    status: Any | None = Field(default=None, alias="status")
    "The status of the RSS newsletter"
    editor: Any | None = Field(default=None, alias="editor")
    from_field: Any | None = Field(default=None, alias="fromField")
    "The 'From' email address used for the message"
    reply_to: Any | None = Field(default=None, alias="replyTo")
    "The email that will be used as a reply-to address"
    content: MessageContent | None = Field(default=None, alias="content")
    send_settings: Any | None = Field(default=None, alias="sendSettings")
    "How the message will be delivered to the subscriber"
    created_on: datetime | None = Field(default=None, alias="createdOn")
    "The creation date"


class RssNewsletterDetails(BaseModel):
    "RssNewsletterDetails model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    rss_newsletter_id: str = Field(alias="rssNewsletterId")
    "The RSS newsletter ID"
    href: str = Field(alias="href")
    "Direct hyperlink to a resource"
    rss_feed_url: str | None = Field(default=None, alias="rssFeedUrl")
    "The URL for the RSS Feed"
    subject: str | None = Field(default=None, alias="subject")
    "The RSS message subject"
    name: str | None = Field(default=None, alias="name")
    "How your newsletters will be seen inside the application"
    status: Any | None = Field(default=None, alias="status")
    "The status of the RSS newsletter"
    editor: Any | None = Field(default=None, alias="editor")
    from_field: Any | None = Field(default=None, alias="fromField")
    "The 'From' email address used for the message"
    reply_to: Any | None = Field(default=None, alias="replyTo")
    "The email that will be used as a reply-to address"
    content: MessageContent | None = Field(default=None, alias="content")
    send_settings: Any | None = Field(default=None, alias="sendSettings")
    "How the message will be delivered to the subscriber"
    created_on: datetime | None = Field(default=None, alias="createdOn")
    "The creation date"
    click_tracks: list[ClickTrack] | None = Field(default=None, alias="clickTracks")
    "The list of tracked links"
    flags: list[MessageFlagsArrayItem] | None = Field(default=None, alias="flags")


class RssNewsletterListItem(BaseModel):
    "RssNewsletterListItem model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    rss_newsletter_id: str = Field(alias="rssNewsletterId")
    "The RSS newsletter ID"
    href: str = Field(alias="href")
    "Direct hyperlink to a resource"
    rss_feed_url: str | None = Field(default=None, alias="rssFeedUrl")
    "The URL for the RSS Feed"
    subject: str | None = Field(default=None, alias="subject")
    "The RSS message subject"
    name: str | None = Field(default=None, alias="name")
    "How your newsletters will be seen inside the application"
    status: Any | None = Field(default=None, alias="status")
    "The status of the RSS newsletter"
    editor: Any | None = Field(default=None, alias="editor")
    from_field: Any | None = Field(default=None, alias="fromField")
    "The 'From' email address used for the message"
    reply_to: Any | None = Field(default=None, alias="replyTo")
    "The email that will be used as a reply-to address"
    content: MessageContent | None = Field(default=None, alias="content")
    send_settings: Any | None = Field(default=None, alias="sendSettings")
    "How the message will be delivered to the subscriber"
    created_on: datetime | None = Field(default=None, alias="createdOn")
    "The creation date"
    flags: str | None = Field(default=None, alias="flags")


class RssNewsletterListSendAsapSettings(BaseModel):
    "RssNewsletterListSendAsapSettings model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    frequency: str = Field(alias="frequency")
    "When to send the message"
    filter: RssNewsletterListSendAsapSettingsFilter = Field(alias="filter")
    "The filter settings for an RSS post"
    max_articles: int | None = Field(default=None, alias="maxArticles")
    "How many articles to display in a list"
    selected_campaigns: Any | None = Field(default=None, alias="selectedCampaigns")
    selected_segments: Any | None = Field(default=None, alias="selectedSegments")
    selected_suppressions: Any | None = Field(default=None, alias="selectedSuppressions")
    excluded_campaigns: Any | None = Field(default=None, alias="excludedCampaigns")
    excluded_segments: Any | None = Field(default=None, alias="excludedSegments")


class RssNewsletterListSendDailySettings(BaseModel):
    "RssNewsletterListSendDailySettings model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    frequency: str = Field(alias="frequency")
    "When to send the message"
    filter: RssNewsletterListSendDailySettingsFilter = Field(alias="filter")
    "The filter settings for an RSS post"
    max_articles: int | None = Field(default=None, alias="maxArticles")
    "How many articles to display in a list"
    selected_campaigns: Any | None = Field(default=None, alias="selectedCampaigns")
    selected_segments: Any | None = Field(default=None, alias="selectedSegments")
    selected_suppressions: Any | None = Field(default=None, alias="selectedSuppressions")
    excluded_campaigns: Any | None = Field(default=None, alias="excludedCampaigns")
    excluded_segments: Any | None = Field(default=None, alias="excludedSegments")
    send_at_hour: int = Field(alias="sendAtHour")
    "The hour when the message should be sent"


class RssNewsletterListSendMonthlySettings(BaseModel):
    "RssNewsletterListSendMonthlySettings model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    frequency: str = Field(alias="frequency")
    "When to send the message"
    filter: RssNewsletterListSendMonthlySettingsFilter = Field(alias="filter")
    "The filter settings for an RSS post"
    max_articles: int | None = Field(default=None, alias="maxArticles")
    "How many articles to display in a list"
    selected_campaigns: Any | None = Field(default=None, alias="selectedCampaigns")
    selected_segments: Any | None = Field(default=None, alias="selectedSegments")
    selected_suppressions: Any | None = Field(default=None, alias="selectedSuppressions")
    excluded_campaigns: Any | None = Field(default=None, alias="excludedCampaigns")
    excluded_segments: Any | None = Field(default=None, alias="excludedSegments")
    send_at_hour: int = Field(alias="sendAtHour")
    "The hour when the message should be sent"
    send_at_month_day: int = Field(alias="sendAtMonthDay")
    "The day of the month when the message should be sent or 31 representing last day of month"


class RssNewsletterListSendWeeklySettings(BaseModel):
    "RssNewsletterListSendWeeklySettings model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    frequency: str = Field(alias="frequency")
    "When to send the message"
    filter: RssNewsletterListSendWeeklySettingsFilter = Field(alias="filter")
    "The filter settings for an RSS post"
    max_articles: int | None = Field(default=None, alias="maxArticles")
    "How many articles to display in a list"
    selected_campaigns: Any | None = Field(default=None, alias="selectedCampaigns")
    selected_segments: Any | None = Field(default=None, alias="selectedSegments")
    selected_suppressions: Any | None = Field(default=None, alias="selectedSuppressions")
    excluded_campaigns: Any | None = Field(default=None, alias="excludedCampaigns")
    excluded_segments: Any | None = Field(default=None, alias="excludedSegments")
    send_at_hour: int = Field(alias="sendAtHour")
    "The hour when the message should be sent"
    send_at_week_day: RssNewsletterListSendWeeklySettingsSendAtWeekDay = Field(
        alias="sendAtWeekDay"
    )
    "The day of the week when the message should be sent"


class RssNewsletterListing(BaseModel):
    "RssNewsletterListing model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    rss_newsletter_id: str = Field(alias="rssNewsletterId")
    "The RSS newsletter ID"
    href: str = Field(alias="href")
    "Direct hyperlink to a resource"
    rss_feed_url: str | None = Field(default=None, alias="rssFeedUrl")
    "The URL for the RSS Feed"
    subject: str | None = Field(default=None, alias="subject")
    "The RSS message subject"
    name: str | None = Field(default=None, alias="name")
    "How your newsletters will be seen inside the application"
    status: Any | None = Field(default=None, alias="status")
    "The status of the RSS newsletter"
    editor: Any | None = Field(default=None, alias="editor")
    from_field: Any | None = Field(default=None, alias="fromField")
    "The 'From' email address used for the message"
    reply_to: Any | None = Field(default=None, alias="replyTo")
    "The email that will be used as a reply-to address"
    content: MessageContent | None = Field(default=None, alias="content")
    send_settings: Any | None = Field(default=None, alias="sendSettings")
    "How the message will be delivered to the subscriber"
    created_on: datetime | None = Field(default=None, alias="createdOn")
    "The creation date"


class RssNewsletterSendAsapSettings(BaseModel):
    "RssNewsletterSendAsapSettings model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    frequency: str = Field(alias="frequency")
    "When to send the message"
    filter: RssNewsletterSendAsapSettingsFilter = Field(alias="filter")
    "The filter settings for an RSS post"
    max_articles: int | None = Field(default=None, alias="maxArticles")
    "How many articles to display in a list"
    selected_campaigns: Any | None = Field(default=None, alias="selectedCampaigns")
    selected_segments: Any | None = Field(default=None, alias="selectedSegments")
    selected_suppressions: Any | None = Field(default=None, alias="selectedSuppressions")
    excluded_campaigns: Any | None = Field(default=None, alias="excludedCampaigns")
    excluded_segments: Any | None = Field(default=None, alias="excludedSegments")
    selected_contacts: Any | None = Field(default=None, alias="selectedContacts")


class RssNewsletterSendDailySettings(BaseModel):
    "RssNewsletterSendDailySettings model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    frequency: str = Field(alias="frequency")
    "When to send the message"
    filter: RssNewsletterSendDailySettingsFilter = Field(alias="filter")
    "The filter settings for an RSS post"
    max_articles: int | None = Field(default=None, alias="maxArticles")
    "How many articles to display in a list"
    selected_campaigns: Any | None = Field(default=None, alias="selectedCampaigns")
    selected_segments: Any | None = Field(default=None, alias="selectedSegments")
    selected_suppressions: Any | None = Field(default=None, alias="selectedSuppressions")
    excluded_campaigns: Any | None = Field(default=None, alias="excludedCampaigns")
    excluded_segments: Any | None = Field(default=None, alias="excludedSegments")
    selected_contacts: Any | None = Field(default=None, alias="selectedContacts")
    send_at_hour: int = Field(alias="sendAtHour")
    "The hour when the message should be sent"


class RssNewsletterSendMonthlySettings(BaseModel):
    "RssNewsletterSendMonthlySettings model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    frequency: str = Field(alias="frequency")
    "When to send the message"
    filter: RssNewsletterSendMonthlySettingsFilter = Field(alias="filter")
    "The filter settings for an RSS post"
    max_articles: int | None = Field(default=None, alias="maxArticles")
    "How many articles to display in a list"
    selected_campaigns: Any | None = Field(default=None, alias="selectedCampaigns")
    selected_segments: Any | None = Field(default=None, alias="selectedSegments")
    selected_suppressions: Any | None = Field(default=None, alias="selectedSuppressions")
    excluded_campaigns: Any | None = Field(default=None, alias="excludedCampaigns")
    excluded_segments: Any | None = Field(default=None, alias="excludedSegments")
    selected_contacts: Any | None = Field(default=None, alias="selectedContacts")
    send_at_hour: int = Field(alias="sendAtHour")
    "The hour when the message should be sent"
    send_at_month_day: dict[str, Any] = Field(alias="sendAtMonthDay")
    "The day of the month when the message should be sent or 31 representing last day of month"


class RssNewsletterSendSettingsDetails(BaseModel):
    "RssNewsletterSendSettingsDetails model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    frequency: str = Field(alias="frequency")
    "When to send the message"
    filter: RssNewsletterSendSettingsDetailsFilter = Field(alias="filter")
    "The filter settings for an RSS post"
    max_articles: int | None = Field(default=None, alias="maxArticles")
    "How many articles to display in a list"
    selected_campaigns: Any | None = Field(default=None, alias="selectedCampaigns")
    selected_segments: Any | None = Field(default=None, alias="selectedSegments")
    selected_suppressions: Any | None = Field(default=None, alias="selectedSuppressions")
    excluded_campaigns: Any | None = Field(default=None, alias="excludedCampaigns")
    excluded_segments: Any | None = Field(default=None, alias="excludedSegments")
    selected_contacts: Any | None = Field(default=None, alias="selectedContacts")


class RssNewsletterSendSettingsListing(BaseModel):
    "RssNewsletterSendSettingsListing model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    frequency: str = Field(alias="frequency")
    "When to send the message"
    filter: RssNewsletterSendSettingsListingFilter = Field(alias="filter")
    "The filter settings for an RSS post"
    max_articles: int | None = Field(default=None, alias="maxArticles")
    "How many articles to display in a list"
    selected_campaigns: Any | None = Field(default=None, alias="selectedCampaigns")
    selected_segments: Any | None = Field(default=None, alias="selectedSegments")
    selected_suppressions: Any | None = Field(default=None, alias="selectedSuppressions")
    excluded_campaigns: Any | None = Field(default=None, alias="excludedCampaigns")
    excluded_segments: Any | None = Field(default=None, alias="excludedSegments")


class RssNewsletterSendWeeklySettings(BaseModel):
    "RssNewsletterSendWeeklySettings model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    frequency: str = Field(alias="frequency")
    "When to send the message"
    filter: RssNewsletterSendWeeklySettingsFilter = Field(alias="filter")
    "The filter settings for an RSS post"
    max_articles: int | None = Field(default=None, alias="maxArticles")
    "How many articles to display in a list"
    selected_campaigns: Any | None = Field(default=None, alias="selectedCampaigns")
    selected_segments: Any | None = Field(default=None, alias="selectedSegments")
    selected_suppressions: Any | None = Field(default=None, alias="selectedSuppressions")
    excluded_campaigns: Any | None = Field(default=None, alias="excludedCampaigns")
    excluded_segments: Any | None = Field(default=None, alias="excludedSegments")
    selected_contacts: Any | None = Field(default=None, alias="selectedContacts")
    send_at_hour: int = Field(alias="sendAtHour")
    "The hour when the message should be sent"
    send_at_week_day: RssNewsletterSendWeeklySettingsSendAtWeekDay = Field(alias="sendAtWeekDay")
    "The day of the week when the message should be sent"


class ScoringCondition(BaseModel):
    "Search contacts by scoring."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    condition_type: ScoringConditionConditionType = Field(alias="conditionType")
    operator_type: ScoringConditionOperatorType = Field(alias="operatorType")
    operator: ScoringConditionOperator | None = Field(default=None, alias="operator")
    "The relational operator. Required for the operatorType=numeric_operator."
    value: int | None = Field(default=None, alias="value")
    "This field is required for the relational operator, and prohibited for the not_exists operator type"


class SearchContactSection(BaseModel):
    "SearchContactSection model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    campaign_ids_list: list[str] = Field(alias="campaignIdsList")
    "An array of campaign identifiers"
    logic_operator: SearchContactSectionLogicOperator = Field(alias="logicOperator")
    subscriber_cycle: list[SearchContactSectionSubscriberCycleItem] = Field(alias="subscriberCycle")
    "Defining whether or not a subscriber is in an autoresponder cycle"
    conditions: list[ConditionType] | None = Field(default=None, alias="conditions")
    "One of the search contact conditions"
    subscription_date: SearchContactSectionSubscriptionDate = Field(alias="subscriptionDate")
    "Matches the matching period"


class SearchContactsBySearchForm(BaseModel):
    "SearchContactsBySearchForm model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    subscribers_type: list[SearchContactsBySearchFormSubscribersTypeItem] = Field(
        alias="subscribersType"
    )
    "Only one subscription status"
    section_logic_operator: SearchContactsBySearchFormSectionLogicOperator = Field(
        alias="sectionLogicOperator"
    )
    "Match 'any' (`or` value) or 'all' (`and` value) of the following conditions"
    section: list[SearchContactSection] = Field(alias="section")


class SearchContactsConditionsDetails(BaseModel):
    "SearchContactsConditionsDetails model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    section_logic_operator: SearchContactsConditionsDetailsSectionLogicOperator = Field(
        alias="sectionLogicOperator"
    )
    "Match 'any' (`or` value) or 'all' (`and` value) of the following conditions"
    section: list[SearchContactSection] = Field(alias="section")


class SearchContactsDetails(BaseModel):
    "Search contact details."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    subscribers_type: list[SearchContactsDetailsSubscribersTypeItem] | None = Field(
        default=None, alias="subscribersType"
    )
    "Only one subscription status"
    section_logic_operator: SearchContactsDetailsSectionLogicOperator = Field(
        alias="sectionLogicOperator"
    )
    "Match 'any' (`or` value) or 'all' (`and` value) of the following conditions"
    section: list[SearchContactSection] = Field(alias="section")
    search_contact_id: str = Field(alias="searchContactId")
    "The unique search-contact identifier"
    name: str = Field(alias="name")
    "The unique name of search-contact"
    created_on: datetime = Field(alias="createdOn")
    "The UTC date time format ISO 8601, e.g. 2018-04-10T10:02:57+0000"
    href: str = Field(alias="href")
    "Direct hyperlink to a resource"


class SearchedContactDetails(BaseModel):
    "SearchedContactDetails model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    contact_id: str | None = Field(default=None, alias="contactId")
    "The contact identifier"
    name: str | None = Field(default=None, alias="name")
    "The contact description"
    email: str | None = Field(default=None, alias="email")
    origin: SearchedContactDetailsOrigin | None = Field(default=None, alias="origin")
    day_of_cycle: str | None = Field(default=None, alias="dayOfCycle")
    created_on: datetime | None = Field(default=None, alias="createdOn")
    campaign: CampaignReference | None = Field(default=None, alias="campaign")
    score: str | None = Field(default=None, alias="score")
    reason: SearchedContactDetailsReason | None = Field(default=None, alias="reason")
    deleted_on: datetime | None = Field(default=None, alias="deletedOn")


class SectionAllTimeSubscriptionDate(BaseModel):
    "SectionAllTimeSubscriptionDate model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    campaign_ids_list: list[str] = Field(alias="campaignIdsList")
    "An array of campaign identifiers"
    logic_operator: SectionAllTimeSubscriptionDateLogicOperator = Field(alias="logicOperator")
    subscriber_cycle: list[SectionAllTimeSubscriptionDateSubscriberCycleItem] = Field(
        alias="subscriberCycle"
    )
    "Defining whether or not a subscriber is in an autoresponder cycle"
    conditions: list[ConditionType] | None = Field(default=None, alias="conditions")
    "One of the search contact conditions"
    subscription_date: SectionAllTimeSubscriptionDateSubscriptionDate = Field(
        alias="subscriptionDate"
    )
    "Matches the matching period"


class SectionCustomSubscriptionDate(BaseModel):
    "SectionCustomSubscriptionDate model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    campaign_ids_list: list[str] = Field(alias="campaignIdsList")
    "An array of campaign identifiers"
    logic_operator: SectionCustomSubscriptionDateLogicOperator = Field(alias="logicOperator")
    subscriber_cycle: list[SectionCustomSubscriptionDateSubscriberCycleItem] = Field(
        alias="subscriberCycle"
    )
    "Defining whether or not a subscriber is in an autoresponder cycle"
    conditions: list[ConditionType] | None = Field(default=None, alias="conditions")
    "One of the search contact conditions"
    subscription_date: SectionCustomSubscriptionDateSubscriptionDate = Field(
        alias="subscriptionDate"
    )
    "Matches the matching period"
    custom_date: CustomDateRange = Field(alias="customDate")


class SectionLast2MonthsSubscriptionDate(BaseModel):
    "SectionLast2MonthsSubscriptionDate model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    campaign_ids_list: list[str] = Field(alias="campaignIdsList")
    "An array of campaign identifiers"
    logic_operator: SectionLast2MonthsSubscriptionDateLogicOperator = Field(alias="logicOperator")
    subscriber_cycle: list[SectionLast2MonthsSubscriptionDateSubscriberCycleItem] = Field(
        alias="subscriberCycle"
    )
    "Defining whether or not a subscriber is in an autoresponder cycle"
    conditions: list[ConditionType] | None = Field(default=None, alias="conditions")
    "One of the search contact conditions"
    subscription_date: SectionLast2MonthsSubscriptionDateSubscriptionDate = Field(
        alias="subscriptionDate"
    )
    "Matches the matching period"


class SectionLast30DaysSubscriptionDate(BaseModel):
    "SectionLast30DaysSubscriptionDate model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    campaign_ids_list: list[str] = Field(alias="campaignIdsList")
    "An array of campaign identifiers"
    logic_operator: SectionLast30DaysSubscriptionDateLogicOperator = Field(alias="logicOperator")
    subscriber_cycle: list[SectionLast30DaysSubscriptionDateSubscriberCycleItem] = Field(
        alias="subscriberCycle"
    )
    "Defining whether or not a subscriber is in an autoresponder cycle"
    conditions: list[ConditionType] | None = Field(default=None, alias="conditions")
    "One of the search contact conditions"
    subscription_date: SectionLast30DaysSubscriptionDateSubscriptionDate = Field(
        alias="subscriptionDate"
    )
    "Matches the matching period"


class SectionLast7DaysSubscriptionDate(BaseModel):
    "SectionLast7DaysSubscriptionDate model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    campaign_ids_list: list[str] = Field(alias="campaignIdsList")
    "An array of campaign identifiers"
    logic_operator: SectionLast7DaysSubscriptionDateLogicOperator = Field(alias="logicOperator")
    subscriber_cycle: list[SectionLast7DaysSubscriptionDateSubscriberCycleItem] = Field(
        alias="subscriberCycle"
    )
    "Defining whether or not a subscriber is in an autoresponder cycle"
    conditions: list[ConditionType] | None = Field(default=None, alias="conditions")
    "One of the search contact conditions"
    subscription_date: SectionLast7DaysSubscriptionDateSubscriptionDate = Field(
        alias="subscriptionDate"
    )
    "Matches the matching period"


class SectionLastMonthSubscriptionDate(BaseModel):
    "SectionLastMonthSubscriptionDate model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    campaign_ids_list: list[str] = Field(alias="campaignIdsList")
    "An array of campaign identifiers"
    logic_operator: SectionLastMonthSubscriptionDateLogicOperator = Field(alias="logicOperator")
    subscriber_cycle: list[SectionLastMonthSubscriptionDateSubscriberCycleItem] = Field(
        alias="subscriberCycle"
    )
    "Defining whether or not a subscriber is in an autoresponder cycle"
    conditions: list[ConditionType] | None = Field(default=None, alias="conditions")
    "One of the search contact conditions"
    subscription_date: SectionLastMonthSubscriptionDateSubscriptionDate = Field(
        alias="subscriptionDate"
    )
    "Matches the matching period"


class SectionLastWeekSubscriptionDate(BaseModel):
    "SectionLastWeekSubscriptionDate model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    campaign_ids_list: list[str] = Field(alias="campaignIdsList")
    "An array of campaign identifiers"
    logic_operator: SectionLastWeekSubscriptionDateLogicOperator = Field(alias="logicOperator")
    subscriber_cycle: list[SectionLastWeekSubscriptionDateSubscriberCycleItem] = Field(
        alias="subscriberCycle"
    )
    "Defining whether or not a subscriber is in an autoresponder cycle"
    conditions: list[ConditionType] | None = Field(default=None, alias="conditions")
    "One of the search contact conditions"
    subscription_date: SectionLastWeekSubscriptionDateSubscriptionDate = Field(
        alias="subscriptionDate"
    )
    "Matches the matching period"


class SectionThisMonthSubscriptionDate(BaseModel):
    "SectionThisMonthSubscriptionDate model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    campaign_ids_list: list[str] = Field(alias="campaignIdsList")
    "An array of campaign identifiers"
    logic_operator: SectionThisMonthSubscriptionDateLogicOperator = Field(alias="logicOperator")
    subscriber_cycle: list[SectionThisMonthSubscriptionDateSubscriberCycleItem] = Field(
        alias="subscriberCycle"
    )
    "Defining whether or not a subscriber is in an autoresponder cycle"
    conditions: list[ConditionType] | None = Field(default=None, alias="conditions")
    "One of the search contact conditions"
    subscription_date: SectionThisMonthSubscriptionDateSubscriptionDate = Field(
        alias="subscriptionDate"
    )
    "Matches the matching period"


class SectionThisWeekSubscriptionDate(BaseModel):
    "SectionThisWeekSubscriptionDate model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    campaign_ids_list: list[str] = Field(alias="campaignIdsList")
    "An array of campaign identifiers"
    logic_operator: SectionThisWeekSubscriptionDateLogicOperator = Field(alias="logicOperator")
    subscriber_cycle: list[SectionThisWeekSubscriptionDateSubscriberCycleItem] = Field(
        alias="subscriberCycle"
    )
    "Defining whether or not a subscriber is in an autoresponder cycle"
    conditions: list[ConditionType] | None = Field(default=None, alias="conditions")
    "One of the search contact conditions"
    subscription_date: SectionThisWeekSubscriptionDateSubscriptionDate = Field(
        alias="subscriptionDate"
    )
    "Matches the matching period"


class SectionTodaySubscriptionDate(BaseModel):
    "SectionTodaySubscriptionDate model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    campaign_ids_list: list[str] = Field(alias="campaignIdsList")
    "An array of campaign identifiers"
    logic_operator: SectionTodaySubscriptionDateLogicOperator = Field(alias="logicOperator")
    subscriber_cycle: list[SectionTodaySubscriptionDateSubscriberCycleItem] = Field(
        alias="subscriberCycle"
    )
    "Defining whether or not a subscriber is in an autoresponder cycle"
    conditions: list[ConditionType] | None = Field(default=None, alias="conditions")
    "One of the search contact conditions"
    subscription_date: SectionTodaySubscriptionDateSubscriptionDate = Field(
        alias="subscriptionDate"
    )
    "Matches the matching period"


class SectionYesterdaySubscriptionDate(BaseModel):
    "SectionYesterdaySubscriptionDate model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    campaign_ids_list: list[str] = Field(alias="campaignIdsList")
    "An array of campaign identifiers"
    logic_operator: SectionYesterdaySubscriptionDateLogicOperator = Field(alias="logicOperator")
    subscriber_cycle: list[SectionYesterdaySubscriptionDateSubscriberCycleItem] = Field(
        alias="subscriberCycle"
    )
    "Defining whether or not a subscriber is in an autoresponder cycle"
    conditions: list[ConditionType] | None = Field(default=None, alias="conditions")
    "One of the search contact conditions"
    subscription_date: SectionYesterdaySubscriptionDateSubscriptionDate = Field(
        alias="subscriptionDate"
    )
    "Matches the matching period"


class SendNewsletterDraft(BaseModel):
    "SendNewsletterDraft model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    message_id: str = Field(alias="messageId")
    "The message identifier (equals to newsletterId)"
    send_settings: Any = Field(alias="sendSettings")
    "How the message will be delivered to the subscriber"


class SendSmsToContacts(BaseModel):
    "SendSmsToContacts model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    name: str = Field(alias="name")
    "The SMS message name"
    content: str = Field(alias="content")
    "The SMS message content"
    recipients_type: SendSmsToContactsRecipientsType = Field(alias="recipientsType")
    "The recipient type. To send a text message to contacts in your list, select `contacts`. To message contacts who are not in any of your lists, select `importedNumbers`"
    send_settings: dict[str, Any] = Field(alias="sendSettings")
    "How the message will be delivered to the subscriber"


class SendSmsToImportedNumbers(BaseModel):
    "SendSmsToImportedNumbers model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    name: str = Field(alias="name")
    "The SMS message name"
    content: str = Field(alias="content")
    "The SMS message content"
    recipients_type: SendSmsToImportedNumbersRecipientsType = Field(alias="recipientsType")
    "The recipient type. To send a text message to contacts in your list, select `contacts`. To message contacts who are not in any of your lists, select `importedNumbers`"
    send_settings: dict[str, Any] = Field(alias="sendSettings")
    "How the message will be delivered to the subscriber"


class SendingLimitsListItem(BaseModel):
    "SendingLimitsListItem model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    time_frame: int | None = Field(default=None, alias="timeFrame")
    "Time frame, measured in seconds"
    limit: int | None = Field(default=None, alias="limit")
    "The number of email sends available within a given time frame"
    used: int | None = Field(default=None, alias="used")
    "The number of email sends used within the given time frame"


class Shop(BaseModel):
    "Shop model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    created_on: datetime | None = Field(default=None, alias="createdOn")
    "The creation date"
    updated_on: datetime | None = Field(default=None, alias="updatedOn")
    "The date of the last update"
    shop_id: str | None = Field(default=None, alias="shopId")
    "The shop ID"
    href: str | None = Field(default=None, alias="href")
    "Direct hyperlink to a resource"
    name: str | None = Field(default=None, alias="name")
    "The shop name"
    locale: str | None = Field(default=None, alias="locale")
    "The language locale (ISO 639-1)"
    currency: str | None = Field(default=None, alias="currency")
    "The currency code (ISO 4217)"


class ShopDetails(BaseModel):
    "ShopDetails model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    created_on: datetime | None = Field(default=None, alias="createdOn")
    "The creation date"
    updated_on: datetime | None = Field(default=None, alias="updatedOn")
    "The date of the last update"
    shop_id: str | None = Field(default=None, alias="shopId")
    "The shop ID"
    href: str | None = Field(default=None, alias="href")
    "Direct hyperlink to a resource"
    name: str | None = Field(default=None, alias="name")
    "The shop name"
    locale: str | None = Field(default=None, alias="locale")
    "The language locale (ISO 639-1)"
    currency: str | None = Field(default=None, alias="currency")
    "The currency code (ISO 4217)"
    product_count: int | None = Field(default=None, alias="productCount")
    "Amount of products in the shop"
    product_revenue: float | None = Field(default=None, alias="productRevenue")
    "Total revenue from purchased products"
    revenue_currency: str | None = Field(default=None, alias="revenueCurrency")
    "The revenue currency code (ISO 4217)"


class SmsAutomationDetails(BaseModel):
    "SmsAutomationDetails model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    sms_id: str = Field(alias="smsId")
    "The automated SMS message ID"
    href: str | None = Field(default=None, alias="href")
    "Direct hyperlink to a resource"
    name: str | None = Field(default=None, alias="name")
    "The automated SMS message name"
    campaign: Any | None = Field(default=None, alias="campaign")
    "The campaign the SMS message is in"
    modified_on: datetime | None = Field(default=None, alias="modifiedOn")
    "The date the automated SMS message was last modified on, shown in `ISO 8601` date and time format. e.g. `2022-04-10T10:02:57+0000`"
    status: SmsAutomationDetailsStatus | None = Field(default=None, alias="status")
    "The status of of the automated SMS message"
    statistics: Any | None = Field(default=None, alias="statistics")
    "Automate SMS message statistics"
    sender_name: str | None = Field(default=None, alias="senderName")
    "The name of the sender of the automated SMS message"
    has_links: bool | None = Field(default=None, alias="hasLinks")
    "Information is the automated SMS message contains links"
    workflows: list[Any] | None = Field(default=None, alias="workflows")
    "Details of the workflows in which the given automated SMS is used"
    click_tracks: list[Any] | None = Field(default=None, alias="clickTracks")
    "Details of links attached to automated SMS message"
    content: str | None = Field(default=None, alias="content")
    "The automated SMS message content"


class SmsAutomationListItem(BaseModel):
    "SmsAutomationListItem model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    sms_id: str = Field(alias="smsId")
    "The automated SMS message ID"
    href: str | None = Field(default=None, alias="href")
    "Direct hyperlink to a resource"
    name: str | None = Field(default=None, alias="name")
    "The automated SMS message name"
    campaign: Any | None = Field(default=None, alias="campaign")
    "The campaign the SMS message is in"
    modified_on: datetime | None = Field(default=None, alias="modifiedOn")
    "The date the automated SMS message was last modified on, shown in `ISO 8601` date and time format. e.g. `2022-04-10T10:02:57+0000`"
    status: SmsAutomationListItemStatus | None = Field(default=None, alias="status")
    "The status of of the automated SMS message"
    statistics: Any | None = Field(default=None, alias="statistics")
    "Automate SMS message statistics"
    sender_name: str | None = Field(default=None, alias="senderName")
    "The name of the sender of the automated SMS message"
    has_links: bool | None = Field(default=None, alias="hasLinks")
    "Information is the automated SMS message contains links"


class SmsDetails(BaseModel):
    "SmsDetails model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    sms_id: str | None = Field(default=None, alias="smsId")
    "The SMS message ID"
    href: str | None = Field(default=None, alias="href")
    "Direct hyperlink to a resource"
    name: str | None = Field(default=None, alias="name")
    "The SMS message name"
    campaign: Any | None = Field(default=None, alias="campaign")
    "The SMS message campaign"
    modified_on: datetime | None = Field(default=None, alias="modifiedOn")
    "The date the SMS message was last modified on, shown in `ISO 8601` date and time format. e.g. `2022-04-10T10:02:57+0000`"
    type_: SmsDetailsType | None = Field(default=None, alias="type")
    "The SMS message type"
    send_on: dict[str, Any] | None = Field(default=None, alias="sendOn")
    "SMS message send date details"
    recipients_type: SmsDetailsRecipientsType | None = Field(default=None, alias="recipientsType")
    "Type of SMS message recipients"
    sender_name: str | None = Field(default=None, alias="senderName")
    "The SMS message sender name"
    content: str | None = Field(default=None, alias="content")
    "The SMS message content"
    send_metrics: dict[str, Any] | None = Field(default=None, alias="sendMetrics")
    "Information about sending process"
    statistics: Any | None = Field(default=None, alias="statistics")
    "Message statistics"
    send_settings: dict[str, Any] | None = Field(default=None, alias="sendSettings")
    "How the message will be delivered to the subscriber"
    click_tracks: list[Any] | None = Field(default=None, alias="clickTracks")
    "Details of links attached to SMS message. Maximum 20 links will be returned."


class SmsLinkClickedCondition(BaseModel):
    "Find contacts who clicked a link from an SMS"

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    condition_type: SmsLinkClickedConditionConditionType = Field(alias="conditionType")
    sms_id: str = Field(alias="smsId")
    "The SMS message ID"
    click_track_id: str = Field(alias="clickTrackId")
    "The click track ID"


class SmsLinkNotClickedCondition(BaseModel):
    "Find contacts who didn't click a link from an SMS"

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    condition_type: SmsLinkNotClickedConditionConditionType = Field(alias="conditionType")
    sms_id: str = Field(alias="smsId")
    "The SMS message ID"
    click_track_id: str = Field(alias="clickTrackId")
    "The click track ID"


class SmsListItem(BaseModel):
    "SmsListItem model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    sms_id: str | None = Field(default=None, alias="smsId")
    "The SMS message ID"
    href: str | None = Field(default=None, alias="href")
    "Direct hyperlink to a resource"
    name: str | None = Field(default=None, alias="name")
    "The SMS message name"
    campaign: Any | None = Field(default=None, alias="campaign")
    "The SMS message campaign"
    modified_on: datetime | None = Field(default=None, alias="modifiedOn")
    "The date the SMS message was last modified on, shown in `ISO 8601` date and time format. e.g. `2022-04-10T10:02:57+0000`"
    type_: SmsListItemType | None = Field(default=None, alias="type")
    "The SMS message type"
    send_on: dict[str, Any] | None = Field(default=None, alias="sendOn")
    "SMS message send date details"
    recipients_type: SmsListItemRecipientsType | None = Field(default=None, alias="recipientsType")
    "Type of SMS message recipients"
    sender_name: str | None = Field(default=None, alias="senderName")
    "The SMS message sender name"
    content: str | None = Field(default=None, alias="content")
    "The SMS message content"
    send_metrics: dict[str, Any] | None = Field(default=None, alias="sendMetrics")
    "Information about sending process"
    statistics: Any | None = Field(default=None, alias="statistics")
    "Message statistics"


class SmsSenderName(BaseModel):
    "SmsSenderName model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    sender_name_id: str | None = Field(default=None, alias="senderNameId")
    "The sender name id"
    name: str | None = Field(default=None, alias="name")
    "The sender name"
    status: Any | None = Field(default=None, alias="status")
    "Status of the sender name"
    is_default: bool | None = Field(default=None, alias="isDefault")
    "Is the sender name default"


class SmsSentCondition(BaseModel):
    "Find contacts who were sent an SMS"

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    condition_type: SmsSentConditionConditionType = Field(alias="conditionType")
    sms_id: str = Field(alias="smsId")
    "The SMS message ID"
    delivery_status: SmsSentConditionDeliveryStatus | None = Field(
        default=None, alias="deliveryStatus"
    )
    "Specify the delivery status. Omit this field if the delivery status is not relevant."


class SmsStats(BaseModel):
    "SmsStats model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    sms_id: str = Field(alias="smsId")
    "The SMS message ID"
    total_sms: int | None = Field(default=None, alias="totalSms")
    "The number of SMS messages sent"
    total_recipients: int | None = Field(default=None, alias="totalRecipients")
    "The number of recipients"
    total_clicks: int | None = Field(default=None, alias="totalClicks")
    "The number of link clicks from an SMS message"
    total_unique_clicks: int | None = Field(default=None, alias="totalUniqueClicks")
    "The number of total unique link clicks from an SMS message"
    total_unsubscribes: int | None = Field(default=None, alias="totalUnsubscribes")
    "The number of opt-outs from an SMS message"
    total_delivered: int | None = Field(default=None, alias="totalDelivered")
    "The number of delivered SMS messages"
    total_price: dict[str, Any] | None = Field(default=None, alias="totalPrice")
    "Cost details of a specific SMS"
    link: dict[str, Any] | None = Field(default=None, alias="link")
    "Link details"
    country_statistics: dict[str, Any] | None = Field(default=None, alias="countryStatistics")
    "SMS message statistics per country"


class Splittest(BaseModel):
    "Splittest model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    splittest_id: str | None = Field(default=None, alias="splittestId")
    "A/B test ID"
    href: str | None = Field(default=None, alias="href")
    "Direct hyperlink to a resource"
    name: str | None = Field(default=None, alias="name")
    "A/B test name"
    campaign: CampaignReference | None = Field(default=None, alias="campaign")
    "A/B test campaign"
    status: SplittestStatus | None = Field(default=None, alias="status")
    "A/B test status"
    winning_criteria: SplittestWinningCriteria | None = Field(default=None, alias="winningCriteria")
    "A/B test winning criteria"
    winning_target: str | None = Field(default=None, alias="winningTarget")
    "A/B test wining target"
    stage: SplittestStage | None = Field(default=None, alias="stage")
    "A/B test stage"
    type_: SplittestType | None = Field(default=None, alias="type")
    "A/B test type"
    sampling_percentage: str | None = Field(default=None, alias="samplingPercentage")
    "A/B test sample percentage"
    sampling_time: str | None = Field(default=None, alias="samplingTime")
    "A/B test sampling time in seconds"
    choose_winning: SplittestChooseWinning | None = Field(default=None, alias="chooseWinning")
    "The method of choosing the winning A/B test"
    winning_score_opens: str | None = Field(default=None, alias="winningScoreOpens")
    "The open rate of the winning A/B test"
    winning_score_clicks: str | None = Field(default=None, alias="winningScoreClicks")
    "The click rate of the winning A/B test"
    winning_delivered: str | None = Field(default=None, alias="winningDelivered")
    "The delivery rate of the winning A/B test"
    winning_schedule_on: datetime | None = Field(default=None, alias="winningScheduleOn")
    "The date for wchich the winning A/B test was scheduled"
    next_step_on: datetime | None = Field(default=None, alias="nextStepOn")
    "The date of the next step in the A/B test"
    evaluation_skipped_on: datetime | None = Field(default=None, alias="evaluationSkippedOn")
    "The date when the A/B test was skipped"
    canceled_on: datetime | None = Field(default=None, alias="canceledOn")
    "The date when the A/B test was canceled"
    created_on: datetime | None = Field(default=None, alias="createdOn")
    "The date when the A/B test was created"
    newsletters: list[SplittestNewsletter] | None = Field(default=None, alias="newsletters")
    "The newsletters that are associated with the A/B test"
    send_settings: dict[str, Any] | None = Field(default=None, alias="sendSettings")
    "The send settings for the A/B test"


class SplittestNewsletter(BaseModel):
    "SplittestNewsletter model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    newsletter_id: str | None = Field(default=None, alias="newsletterId")
    "The newsletter ID"
    href: str | None = Field(default=None, alias="href")
    "The direct newsletter URL"
    name: str | None = Field(default=None, alias="name")
    "The newsletter name"
    subject: str | None = Field(default=None, alias="subject")
    "The newsletter subject"
    from_field: FromFieldReference | None = Field(default=None, alias="fromField")
    'The \\"From\\" address for the newsletter'
    status: SplittestNewsletterStatus | None = Field(default=None, alias="status")
    "The status of the newsletter"
    send_on: datetime | None = Field(default=None, alias="sendOn")
    "The date when the newsletter was sent"
    sampling_targets: str | None = Field(default=None, alias="samplingTargets")
    "The newsletter sample targets"
    sampling_delivered: str | None = Field(default=None, alias="samplingDelivered")
    "The newsletter sample delivery"
    score_opens: str | None = Field(default=None, alias="scoreOpens")
    "The newsletter open rate"
    score_clicks: str | None = Field(default=None, alias="scoreClicks")
    "The newsletter click rate"


class StandardSubscriberActivityReportDetails(BaseModel):
    "StandardSubscriberActivityReportDetails model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    custom_report_id: str | None = Field(default=None, alias="customReportId")
    "The custom report ID"
    name: str | None = Field(default=None, alias="name")
    "The custom report name"
    href: str | None = Field(default=None, alias="href")
    "The direct hyperlink to a resource"
    type_: Any | None = Field(default=None, alias="type")
    "The custom report type"
    scheduling: dict[str, Any] | None = Field(default=None, alias="scheduling")
    "Parameters responsible for defining the reporting period"
    files: list[dict[str, Any]] | None = Field(default=None, alias="files")
    "Files that have been generated for the given report"
    created_at: datetime | None = Field(default=None, alias="createdAt")
    "Custom report creation date"
    generated_at: datetime | None = Field(default=None, alias="generatedAt")
    "Custom report generation date"
    filters: dict[str, Any] | None = Field(default=None, alias="filters")
    "Filters used to narrow down the report data"


class SubscribersTypeEnumForSearching(BaseModel):
    "SubscribersTypeEnumForSearching model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    subscribers_type: list[SubscribersTypeEnumForSearchingSubscribersTypeItem] | None = Field(
        default=None, alias="subscribersType"
    )
    "Only one subscription status"


class SubscribersTypeEnumForSegments(BaseModel):
    "SubscribersTypeEnumForSegments model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    subscribers_type: list[SubscribersTypeEnumForSegmentsSubscribersTypeItem] | None = Field(
        default=None, alias="subscribersType"
    )
    "Only one subscription status"


class SubscriptionConfirmationBody(BaseModel):
    "SubscriptionConfirmationBody model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    subscription_confirmation_body_id: str | None = Field(
        default=None, alias="subscriptionConfirmationBodyId"
    )
    "Subscription confirmation subject ID"
    name: str | None = Field(default=None, alias="name")
    "Name"
    content_plain: str | None = Field(default=None, alias="contentPlain")
    "Plain text content equivalent of confirmation message"
    content_html: str | None = Field(default=None, alias="contentHtml")
    "HTML content of confirmation message"


class SubscriptionConfirmationSubject(BaseModel):
    "SubscriptionConfirmationSubject model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    subscription_confirmation_subject_id: str | None = Field(
        default=None, alias="subscriptionConfirmationSubjectId"
    )
    "Subscription confirmation subject ID"
    subject: str | None = Field(default=None, alias="subject")
    "Subject"
    is_private: Any | None = Field(default=None, alias="isPrivate")
    "Is private"


class SubscriptionDateCondition(BaseModel):
    "Use this to find a contact by subscription date, use."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    condition_type: SubscriptionDateConditionConditionType = Field(alias="conditionType")
    operator_type: SubscriptionDateConditionOperatorType = Field(alias="operatorType")
    operator: SubscriptionDateConditionOperator = Field(alias="operator")
    value: dict[str, Any] = Field(alias="value")


class SubscriptionMethodCondition(BaseModel):
    "The subscription method."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    condition_type: SubscriptionMethodConditionConditionType = Field(alias="conditionType")
    method: SubscriptionMethodConditionMethod = Field(alias="method")
    webform_type: SubscriptionMethodConditionWebformType | None = Field(
        default=None, alias="webformType"
    )
    "The property required for the webform subscription method. If it equals webforms, webformsv2 or popups, additonal property value is needed."
    value: dict[str, Any] | None = Field(default=None, alias="value")
    "The field required for `import`, `landing_page`, `webinar` and `website_builder_elegant`, optional for the `webform` method"


class SubscriptionRejectionsReportDetails(BaseModel):
    "SubscriptionRejectionsReportDetails model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    custom_report_id: str | None = Field(default=None, alias="customReportId")
    "The custom report ID"
    name: str | None = Field(default=None, alias="name")
    "The custom report name"
    href: str | None = Field(default=None, alias="href")
    "The direct hyperlink to a resource"
    type_: Any | None = Field(default=None, alias="type")
    "The custom report type"
    scheduling: dict[str, Any] | None = Field(default=None, alias="scheduling")
    "Parameters responsible for defining the reporting period"
    files: list[dict[str, Any]] | None = Field(default=None, alias="files")
    "Files that have been generated for the given report"
    created_at: datetime | None = Field(default=None, alias="createdAt")
    "Custom report creation date"
    generated_at: datetime | None = Field(default=None, alias="generatedAt")
    "Custom report generation date"
    filters: dict[str, Any] | None = Field(default=None, alias="filters")
    "Filters used to narrow down the report data"


class Suppression(BaseModel):
    "Suppression model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    suppression_id: str = Field(alias="suppressionId")
    "The suppression ID"
    name: str | None = Field(default=None, alias="name")
    "The suppression name"
    created_on: datetime | None = Field(default=None, alias="createdOn")
    "Created on DateTime in the ISO8601 format"
    href: str | None = Field(default=None, alias="href")
    "Direct hyperlink to a resource"


class SuppressionDetails(BaseModel):
    "SuppressionDetails model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    suppression_id: str = Field(alias="suppressionId")
    "The suppression ID"
    name: str | None = Field(default=None, alias="name")
    "The name of the suppression list"
    created_on: datetime | None = Field(default=None, alias="createdOn")
    "Created on DateTime in the ISO8601 format"
    href: str | None = Field(default=None, alias="href")
    "Direct hyperlink to a resource"
    masks: list[str] | None = Field(default=None, alias="masks")


class Tag(BaseModel):
    "Tag model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    name: str | None = Field(default=None, alias="name")
    "The tag name"
    color: str | None = Field(default=None, alias="color")
    "The tag color (deprecated)"
    tag_id: str | None = Field(default=None, alias="tagId")
    "The tag ID"
    href: str | None = Field(default=None, alias="href")
    "The direct hyperlink to a resource"
    created_at: datetime | None = Field(default=None, alias="createdAt")


class TagCondition(BaseModel):
    "Search contacts by tag."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    condition_type: TagConditionConditionType = Field(alias="conditionType")
    operator_type: TagConditionOperatorType = Field(alias="operatorType")
    "The operator for the existence of a property"
    operator: TagConditionOperator = Field(alias="operator")
    "This operator verifies whether the property you are looking for exists or not"
    value: str = Field(alias="value")
    "The tag identifier"


class TagDetails(BaseModel):
    "TagDetails model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    name: str | None = Field(default=None, alias="name")
    "The tag name"
    color: str | None = Field(default=None, alias="color")
    "The tag color (deprecated)"
    tag_id: str | None = Field(default=None, alias="tagId")
    "The tag ID."
    created_at: datetime | None = Field(default=None, alias="createdAt")


class Tax(BaseModel):
    "Tax model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    tax_id: str | None = Field(default=None, alias="taxId")
    "The tax ID"
    href: str | None = Field(default=None, alias="href")
    "Direct hyperlink to a resource"
    name: str | None = Field(default=None, alias="name")
    "The tax name"
    rate: float | None = Field(default=None, alias="rate")
    "The rate value"
    created_on: datetime | None = Field(default=None, alias="createdOn")
    "The creation date"
    updated_on: datetime | None = Field(default=None, alias="updatedOn")
    "The date of the last update"


class TemplateContent(BaseModel):
    "TemplateContent model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    from_field: Any = Field(alias="fromField")
    "The 'From' address ID to be used as the message sender"
    reply_to: Any | None = Field(default=None, alias="replyTo")
    "The 'From' address ID to be used as the Reply-to"
    tag: Any | None = Field(default=None, alias="tag")
    "The tag ID used for statistical data collection"
    recipients: TransactionalEmailRecipients = Field(alias="recipients")
    content_type: TemplateContentContentType = Field(alias="contentType")
    "The message content type"
    attachments: list[TransactionalEmailAttachment] | None = Field(
        default=None, alias="attachments"
    )
    template: dict[str, Any] = Field(alias="template")
    "The message template. At least templateId is required"


class TimeZone(BaseModel):
    "TimeZone model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    time_zone_id: int = Field(alias="timeZoneId")
    "Time zone ID: [Link to resource](https://apireference.getresponse.com/#operation/getTimezones)"


class Timezone(BaseModel):
    "Timezone model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    timezone_id: int = Field(alias="timezoneId")
    name: str | None = Field(default=None, alias="name")
    "Time zone name as defined by https://en.wikipedia.org/wiki/List_of_tz_database_time_zones"
    offset: str | None = Field(default=None, alias="offset")
    country: str | None = Field(default=None, alias="country")


class TimezoneCountry(BaseModel):
    "TimezoneCountry model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    country: str | None = Field(default=None, alias="country")


class TimezoneId(BaseModel):
    "TimezoneId model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    timezone_id: int | None = Field(default=None, alias="timezoneId")


class TimezoneName(BaseModel):
    "TimezoneName model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    name: str | None = Field(default=None, alias="name")
    "Time zone name as defined by https://en.wikipedia.org/wiki/List_of_tz_database_time_zones"


class TimezoneOffset(BaseModel):
    "TimezoneOffset model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    offset: str | None = Field(default=None, alias="offset")


class Tracking(BaseModel):
    "Tracking model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    grid: str | None = Field(default=None, alias="grid")
    snippet: str | None = Field(default=None, alias="snippet")
    snippet_v2: str | None = Field(default=None, alias="snippetV2")


class TransactionalEmail(BaseModel):
    "TransactionalEmail model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    transactional_email_id: str | None = Field(default=None, alias="transactionalEmailId")


class TransactionalEmailAttachment(BaseModel):
    "TransactionalEmailAttachment model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    file_name: str = Field(alias="fileName")
    "The attachment file name"
    mime_type: str = Field(alias="mimeType")
    "The MIME attachment type"
    content: str = Field(alias="content")
    "The base64-encoded attachment"


class TransactionalEmailBounceReportDetails(BaseModel):
    "TransactionalEmailBounceReportDetails model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    custom_report_id: str | None = Field(default=None, alias="customReportId")
    "The custom report ID"
    name: str | None = Field(default=None, alias="name")
    "The custom report name"
    href: str | None = Field(default=None, alias="href")
    "The direct hyperlink to a resource"
    type_: Any | None = Field(default=None, alias="type")
    "The custom report type"
    scheduling: dict[str, Any] | None = Field(default=None, alias="scheduling")
    "Parameters responsible for defining the reporting period"
    files: list[dict[str, Any]] | None = Field(default=None, alias="files")
    "Files that have been generated for the given report"
    created_at: datetime | None = Field(default=None, alias="createdAt")
    "Custom report creation date"
    generated_at: datetime | None = Field(default=None, alias="generatedAt")
    "Custom report generation date"
    filters: dict[str, Any] | None = Field(default=None, alias="filters")
    "Filters used to narrow down the report data"


class TransactionalEmailContent(BaseModel):
    "TransactionalEmailContent model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    subject: str | None = Field(default=None, alias="subject")
    attachments: list[TransactionalEmailAttachment] | None = Field(
        default=None, alias="attachments"
    )
    content: dict[str, Any] = Field(alias="content")
    "The message content. At least one field is required. The maximum combined size of plain text and HTML is 16MB"


class TransactionalEmailDetails(BaseModel):
    "TransactionalEmailDetails model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    transactional_email_id: str = Field(alias="transactionalEmailId")
    from_field: Any = Field(alias="fromField")
    "The 'From' address ID to be used as the message sender"
    reply_to: Any | None = Field(default=None, alias="replyTo")
    "The 'From' address ID to be used as the Reply-to"
    subject: str = Field(alias="subject")
    tag: Any | None = Field(default=None, alias="tag")
    "The tag ID used for statistical data collection"
    recipients: Any = Field(alias="recipients")
    href: str | None = Field(default=None, alias="href")
    "Direct hyperlink to a resource"


class TransactionalEmailListElement(BaseModel):
    "TransactionalEmailListElement model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    transactional_email_id: str = Field(alias="transactionalEmailId")
    from_field: FromFieldReference = Field(alias="fromField")
    recipients: Any = Field(alias="recipients")
    subject: str = Field(alias="subject")
    tag: TransactionalEmailTag | None = Field(default=None, alias="tag")
    href: str | None = Field(default=None, alias="href")
    "Direct hyperlink to a resource"


class TransactionalEmailRecipient(BaseModel):
    "TransactionalEmailRecipient model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    email: str = Field(alias="email")
    name: str | None = Field(default=None, alias="name")
    status: TransactionalEmailRecipientStatus | None = Field(default=None, alias="status")


class TransactionalEmailRecipientClickedLink(BaseModel):
    "TransactionalEmailRecipientClickedLink model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    url: str | None = Field(default=None, alias="url")
    clicked_on: datetime | None = Field(default=None, alias="clickedOn")


class TransactionalEmailRecipientDetails(BaseModel):
    "TransactionalEmailRecipientDetails model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    email: str = Field(alias="email")
    name: str | None = Field(default=None, alias="name")
    status: TransactionalEmailRecipientDetailsStatus | None = Field(default=None, alias="status")
    statuses: TransactionalEmailRecipientStatuses | None = Field(default=None, alias="statuses")
    clicked_links: list[TransactionalEmailRecipientClickedLink] | None = Field(
        default=None, alias="clickedLinks"
    )


class TransactionalEmailRecipientSentOnStatus(BaseModel):
    "TransactionalEmailRecipientSentOnStatus model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    sent_on: datetime | None = Field(default=None, alias="sentOn")


class TransactionalEmailRecipientStatuses(BaseModel):
    "TransactionalEmailRecipientStatuses model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    sent_on: datetime | None = Field(default=None, alias="sentOn")
    rejected_on: datetime | None = Field(default=None, alias="rejectedOn")
    opened_on: datetime | None = Field(default=None, alias="openedOn")
    bounced_on: datetime | None = Field(default=None, alias="bouncedOn")
    complained_on: datetime | None = Field(default=None, alias="complainedOn")


class TransactionalEmailRecipientTo(BaseModel):
    "TransactionalEmailRecipientTo model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    email: str = Field(alias="email")
    name: str | None = Field(default=None, alias="name")
    status: TransactionalEmailRecipientToStatus | None = Field(default=None, alias="status")
    valid_since: datetime | None = Field(default=None, alias="validSince")
    "The first time this address appeared in your system"


class TransactionalEmailRecipients(BaseModel):
    "A field containing the message recipients. You can enter up to 8 recipients."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    to: TransactionalEmailRecipientTo = Field(alias="to")
    cc: list[TransactionalEmailRecipient] | None = Field(default=None, alias="cc")
    bcc: list[TransactionalEmailRecipient] | None = Field(default=None, alias="bcc")


class TransactionalEmailRecipientsDetails(BaseModel):
    "TransactionalEmailRecipientsDetails model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    to: TransactionalEmailRecipientDetails = Field(alias="to")
    cc: list[TransactionalEmailRecipientDetails] | None = Field(default=None, alias="cc")
    bcc: list[TransactionalEmailRecipientDetails] | None = Field(default=None, alias="bcc")


class TransactionalEmailStatistics(BaseModel):
    "TransactionalEmailStatistics model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    time_frame: str | None = Field(default=None, alias="timeFrame")
    "The statistics time frame in the ISO 8601 date format with duration interval"
    sent: int | None = Field(default=None, alias="sent")
    opened: int | None = Field(default=None, alias="opened")
    bounced: int | None = Field(default=None, alias="bounced")
    complaint: int | None = Field(default=None, alias="complaint")
    clicks: int | None = Field(default=None, alias="clicks")


class TransactionalEmailTag(BaseModel):
    "TransactionalEmailTag model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    tag_id: str = Field(alias="tagId")


class TransactionalEmailTemplate(BaseModel):
    "The template content"

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    attachments: list[TransactionalEmailAttachment] | None = Field(
        default=None, alias="attachments"
    )
    template: dict[str, Any] = Field(alias="template")
    "The message template. At least templateId is required"


class TransactionalEmailTemplateContent(BaseModel):
    "The template content. At least one field is required"

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    plain: str | None = Field(default=None, alias="plain")
    "The plain text equivalent of template content"
    html: str | None = Field(default=None, alias="html")
    "The template content in HTML"


class TransactionalEmailsTemplateDetails(BaseModel):
    "TransactionalEmailsTemplateDetails model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    template_id: str | None = Field(default=None, alias="templateId")
    "Transactional email template ID"
    href: str | None = Field(default=None, alias="href")
    "Direct hyperlink to a resource"
    subject: str | None = Field(default=None, alias="subject")
    "The template subject"
    created_on: datetime | None = Field(default=None, alias="createdOn")
    "The creation date"
    updated_on: datetime | None = Field(default=None, alias="updatedOn")
    "The date of the last template update"
    editor: Any | None = Field(default=None, alias="editor")
    "The Editor type"
    content: TransactionalEmailTemplateContent | None = Field(default=None, alias="content")


class TransactionalEmailsTemplateListElement(BaseModel):
    "TransactionalEmailsTemplateListElement model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    template_id: str | None = Field(default=None, alias="templateId")
    "Transactional email template ID"
    href: str | None = Field(default=None, alias="href")
    "Direct hyperlink to a resource"
    subject: str | None = Field(default=None, alias="subject")
    "The template subject"
    created_on: datetime | None = Field(default=None, alias="createdOn")
    "The creation date"
    updated_on: datetime | None = Field(default=None, alias="updatedOn")
    "The date of the last template update"
    editor: Any | None = Field(default=None, alias="editor")
    "The Editor type"


class TriggerCustomEvent(BaseModel):
    "TriggerCustomEvent model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    name: str = Field(alias="name")
    "The name of custom event. Custom event with this name must already exist"
    contact_id: str = Field(alias="contactId")
    "The contact ID"
    attributes: list[TriggerCustomEventAttribute] | None = Field(default=None, alias="attributes")
    "The attributes for the trigger"


class TriggerCustomEventAttribute(BaseModel):
    "TriggerCustomEventAttribute model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    name: str = Field(alias="name")
    "The name of the attribute. It must be already defined for the custom event"
    value: dict[str, Any] = Field(alias="value")


class UnconfirmedContactsStatsReportDetails(BaseModel):
    "UnconfirmedContactsStatsReportDetails model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    custom_report_id: str | None = Field(default=None, alias="customReportId")
    "The custom report ID"
    name: str | None = Field(default=None, alias="name")
    "The custom report name"
    href: str | None = Field(default=None, alias="href")
    "The direct hyperlink to a resource"
    type_: Any | None = Field(default=None, alias="type")
    "The custom report type"
    scheduling: dict[str, Any] | None = Field(default=None, alias="scheduling")
    "Parameters responsible for defining the reporting period"
    files: list[dict[str, Any]] | None = Field(default=None, alias="files")
    "Files that have been generated for the given report"
    created_at: datetime | None = Field(default=None, alias="createdAt")
    "Custom report creation date"
    generated_at: datetime | None = Field(default=None, alias="generatedAt")
    "Custom report generation date"
    filters: dict[str, Any] | None = Field(default=None, alias="filters")
    "Filters used to narrow down the report data"


class UnsubscribeContactsListsReportDetails(BaseModel):
    "UnsubscribeContactsListsReportDetails model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    custom_report_id: str | None = Field(default=None, alias="customReportId")
    "The custom report ID"
    name: str | None = Field(default=None, alias="name")
    "The custom report name"
    href: str | None = Field(default=None, alias="href")
    "The direct hyperlink to a resource"
    type_: Any | None = Field(default=None, alias="type")
    "The custom report type"
    scheduling: dict[str, Any] | None = Field(default=None, alias="scheduling")
    "Parameters responsible for defining the reporting period"
    files: list[dict[str, Any]] | None = Field(default=None, alias="files")
    "Files that have been generated for the given report"
    created_at: datetime | None = Field(default=None, alias="createdAt")
    "Custom report creation date"
    generated_at: datetime | None = Field(default=None, alias="generatedAt")
    "Custom report generation date"
    filters: dict[str, Any] | None = Field(default=None, alias="filters")
    "Filters used to narrow down the report data"


class UpdateAccount(BaseModel):
    "UpdateAccount model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    account_id: str | None = Field(default=None, alias="accountId")
    "Account ID"
    email: str | None = Field(default=None, alias="email")
    "Email"
    country_code: Any | None = Field(default=None, alias="countryCode")
    industry_tag: Any | None = Field(default=None, alias="industryTag")
    time_zone: Any | None = Field(default=None, alias="timeZone")
    href: str | None = Field(default=None, alias="href")
    "Direct URL to resource"
    first_name: str | None = Field(default=None, alias="firstName")
    "First name"
    last_name: str | None = Field(default=None, alias="lastName")
    "Last name"
    company_name: str | None = Field(default=None, alias="companyName")
    "Company name"
    phone: str | None = Field(default=None, alias="phone")
    "Phone number"
    state: str | None = Field(default=None, alias="state")
    "State"
    city: str | None = Field(default=None, alias="city")
    "City"
    street: str | None = Field(default=None, alias="street")
    "Street"
    zip_code: str | None = Field(default=None, alias="zipCode")
    "ZIP Code"
    number_of_employees: UpdateAccountNumberOfEmployees | None = Field(
        default=None, alias="numberOfEmployees"
    )
    "Numbers of employees"
    time_format: UpdateAccountTimeFormat | None = Field(default=None, alias="timeFormat")
    "Account time notation"


class UpdateAddress(BaseModel):
    "UpdateAddress model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    created_on: datetime | None = Field(default=None, alias="createdOn")
    "The creation date"
    updated_on: datetime | None = Field(default=None, alias="updatedOn")
    "The date of the last update"
    address_id: str | None = Field(default=None, alias="addressId")
    href: str | None = Field(default=None, alias="href")
    "Direct hyperlink to a resource"
    country_code: str | None = Field(default=None, alias="countryCode")
    "The country code (ISO 3166-1 alpha-3)"
    country_name: str | None = Field(default=None, alias="countryName")
    "The country name, based on `countryCode`"
    name: str | None = Field(default=None, alias="name")
    first_name: str | None = Field(default=None, alias="firstName")
    last_name: str | None = Field(default=None, alias="lastName")
    address1: str | None = Field(default=None, alias="address1")
    "Address line 1"
    address2: str | None = Field(default=None, alias="address2")
    "Address line 2"
    city: str | None = Field(default=None, alias="city")
    zip: str | None = Field(default=None, alias="zip")
    "The ZIP/postal code, free text"
    province: str | None = Field(default=None, alias="province")
    province_code: str | None = Field(default=None, alias="provinceCode")
    "The province code, free text"
    phone: str | None = Field(default=None, alias="phone")
    "The phone number, free text"
    company: str | None = Field(default=None, alias="company")
    "The company name, free text"


class UpdateAutoresponder(BaseModel):
    "UpdateAutoresponder model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    autoresponder_id: str | None = Field(default=None, alias="autoresponderId")
    "The autoresponder ID"
    href: str | None = Field(default=None, alias="href")
    "Direct hyperlink to a resource"
    name: str | None = Field(default=None, alias="name")
    "The autoresponder name"
    subject: str | None = Field(default=None, alias="subject")
    "The autoresponder message subject"
    campaign_id: str | None = Field(default=None, alias="campaignId")
    "The campaign ID. The system will assign the autoresponder to a default campaign if you don't provide a specific campaign ID."
    status: Any | None = Field(default=None, alias="status")
    "The autoresponder status"
    from_field: Any | None = Field(default=None, alias="fromField")
    "The from email address used for the message"
    reply_to: Any | None = Field(default=None, alias="replyTo")
    "The email that will be used as a reply-to address"
    content: MessageContent | None = Field(default=None, alias="content")
    flags: list[MessageFlagsArrayItem] | None = Field(default=None, alias="flags")
    trigger_settings: Any | None = Field(default=None, alias="triggerSettings")
    "The conditions that will trigger the autoresponder"
    statistics: dict[str, Any] | None = Field(default=None, alias="statistics")
    "The autoresponder statistics summary"
    created_on: datetime | None = Field(default=None, alias="createdOn")
    "The creation date"
    send_settings: AutoresponderSendSettingsInput | None = Field(default=None, alias="sendSettings")
    "How the message will be delivered to the subscriber"


class UpdateBlocklist(BaseModel):
    "UpdateBlocklist model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    masks: list[str] = Field(alias="masks")


class UpdateCallbacks(BaseModel):
    "UpdateCallbacks model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    url: str | None = Field(default=None, alias="url")
    "URL to use to post notifications, required if callbacks are not yet enabled"
    actions: CallbackActions | None = Field(default=None, alias="actions")


class UpdateCampaign(BaseModel):
    "UpdateCampaign model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    campaign_id: str | None = Field(default=None, alias="campaignId")
    "Unique identifier of the campaign (contact list)"
    name: str = Field(alias="name")
    "The campaign (list) name. * You can use each list name just once in your account. * The name must be between 3-64 characters. * All alphabets supported by GetResponse, including right-to-left ones, are allowed. * You can use upper and lower case letters, numbers, spaces and special characters apart from the ones listed below. * You can’t use emojis and the following special characters: `/`, `\\`, `@`, and `[` or `]`."
    tech_name: str | None = Field(default=None, alias="techName")
    "Tech name is a unique internal ID of a list used for [FTP imports](https://www.getresponse.com/help/how-to-import-files-via-ftp.html) (available in GetResponse MAX accounts only)"
    language_code: str | None = Field(default=None, alias="languageCode")
    "The campaign language code according to ISO 639-1, plus: zt - Chinese (Traditional), fs - Afghan Persian (Dari), md - Moldavian"
    is_default: Any | None = Field(default=None, alias="isDefault")
    "Is the campaign default"
    created_on: datetime | None = Field(default=None, alias="createdOn")
    "The date of creation"
    href: str | None = Field(default=None, alias="href")
    "Direct hyperlink to a resource"
    postal: CampaignPostal | None = Field(default=None, alias="postal")
    confirmation: CampaignConfirmation | None = Field(default=None, alias="confirmation")
    optin_types: CampaignOptinTypes | None = Field(default=None, alias="optinTypes")
    subscription_notifications: CampaignSubscriptionNotifications | None = Field(
        default=None, alias="subscriptionNotifications"
    )
    profile: CampaignProfile | None = Field(default=None, alias="profile")


class UpdateCart(BaseModel):
    "UpdateCart model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    created_on: datetime | None = Field(default=None, alias="createdOn")
    "The creation date"
    updated_on: datetime | None = Field(default=None, alias="updatedOn")
    "The date of the last update"
    cart_id: str | None = Field(default=None, alias="cartId")
    "The contact ID"
    href: str | None = Field(default=None, alias="href")
    "Direct hyperlink to a resource"
    contact_id: str | None = Field(default=None, alias="contactId")
    "The ID of the contact that the cart belongs to. You must first create the contact using POST /v3/contacts, or if it already exists, using GET /v3/contacts"
    total_price: float | None = Field(default=None, alias="totalPrice")
    "The total cart price, tax excluded"
    total_tax_price: float | None = Field(default=None, alias="totalTaxPrice")
    "The total cart price, tax included"
    currency: str | None = Field(default=None, alias="currency")
    "The currency code (ISO 4217)"
    selected_variants: list[NewCartSelectedProductVariant] | None = Field(
        default=None, alias="selectedVariants"
    )
    external_id: str | None = Field(default=None, alias="externalId")
    "The external ID is the identifying string or number of the cart, given by another software"
    cart_url: str | None = Field(default=None, alias="cartUrl")
    "The external cart URL"


class UpdateContact(BaseModel):
    "UpdateContact model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    contact_id: str | None = Field(default=None, alias="contactId")
    name: str | None = Field(default=None, alias="name")
    origin: UpdateContactOrigin | None = Field(default=None, alias="origin")
    time_zone: str | None = Field(default=None, alias="timeZone")
    "The time zone of a contact, uses the time zone database format (https://www.iana.org/time-zones)"
    activities: str | None = Field(default=None, alias="activities")
    changed_on: datetime | None = Field(default=None, alias="changedOn")
    created_on: datetime | None = Field(default=None, alias="createdOn")
    campaign: dict[str, Any] | None = Field(default=None, alias="campaign")
    email: str | None = Field(default=None, alias="email")
    day_of_cycle: str | None = Field(default=None, alias="dayOfCycle")
    "The day on which the contact is in the Autoresponder cycle. `null` indicates the contacts is not in the cycle."
    scoring: float | None = Field(default=None, alias="scoring")
    "Contact scoring, pass null to remove the score from a contact"
    engagement_score: int | None = Field(default=None, alias="engagementScore")
    "Engagement Score is a feature that presents a visual estimate of a contact's engagement with mailings. The score is based on the contact's interactions with your e-mails. Via API, it's returned in the form of numbers ranging from 1 (Not Engaged) to 5 (Highly Engaged)."
    href: str | None = Field(default=None, alias="href")
    "Direct hyperlink to a resource"
    note: str | None = Field(default=None, alias="note")
    tags: list[NewContactTag] | None = Field(default=None, alias="tags")
    custom_field_values: list[NewContactCustomFieldValue] | None = Field(
        default=None, alias="customFieldValues"
    )


class UpdateCustomEvent(BaseModel):
    "UpdateCustomEvent model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    name: str = Field(alias="name")
    "Unique name of custom event"
    attributes: list[CustomEventAttributeDetails] = Field(alias="attributes")
    "Optional collection of attributes"


class UpdateCustomField(BaseModel):
    "UpdateCustomField model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    hidden: Any = Field(alias="hidden")
    "Whether the custom field is visible to contacts"
    values: list[str] = Field(alias="values")
    "The list of assigned values (zero or more - depending on the custom field type. Please see description)"


class UpdateMetaField(BaseModel):
    "UpdateMetaField model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    href: str | None = Field(default=None, alias="href")
    "Direct hyperlink to a resource"
    meta_field_id: str | None = Field(default=None, alias="metaFieldId")
    "The meta field ID"
    name: str | None = Field(default=None, alias="name")
    "The meta field name"
    value: str | None = Field(default=None, alias="value")
    "The meta field value"
    value_type: UpdateMetaFieldValueType | None = Field(default=None, alias="valueType")
    "The value type enumerable"
    description: str | None = Field(default=None, alias="description")
    "The meta field description"
    created_on: datetime | None = Field(default=None, alias="createdOn")
    "The creation date"
    updated_on: datetime | None = Field(default=None, alias="updatedOn")
    "The date of the last update"


class UpdateOrder(BaseModel):
    "UpdateOrder model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    order_id: str | None = Field(default=None, alias="orderId")
    "The order ID"
    href: str | None = Field(default=None, alias="href")
    "Direct hyperlink to a resource"
    contact_id: str | None = Field(default=None, alias="contactId")
    "Create a contact by using `POST /v3/contacts`. Or, if the contact already exists, using `GET /v3/contacts`"
    order_url: str | None = Field(default=None, alias="orderUrl")
    "The external URL for an order"
    external_id: str | None = Field(default=None, alias="externalId")
    "The external ID is the identifying string or number of the order given by another software"
    total_price: float | None = Field(default=None, alias="totalPrice")
    "The total price of an order"
    total_price_tax: float | None = Field(default=None, alias="totalPriceTax")
    "The total price tax of an order"
    currency: str | None = Field(default=None, alias="currency")
    "The order currency code (ISO 4217)"
    status: str | None = Field(default=None, alias="status")
    "The status value"
    cart_id: str | None = Field(default=None, alias="cartId")
    "Create a cart by using `POST /v3/shops/{shopId}/carts`"
    description: str | None = Field(default=None, alias="description")
    "The order description"
    shipping_price: float | None = Field(default=None, alias="shippingPrice")
    "The shipping price for an order"
    shipping_address: Any | None = Field(default=None, alias="shippingAddress")
    "The shipping address for an order"
    billing_status: str | None = Field(default=None, alias="billingStatus")
    "The billing status of an order"
    billing_address: Any | None = Field(default=None, alias="billingAddress")
    "The billing address for an order"
    processed_at: datetime | None = Field(default=None, alias="processedAt")
    "The exact time an order was made"
    meta_fields: list[NewMetaField] | None = Field(default=None, alias="metaFields")


class UpdatePredefinedField(BaseModel):
    "UpdatePredefinedField model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    value: str = Field(alias="value")


class UpdateProduct(BaseModel):
    "UpdateProduct model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    created_on: datetime | None = Field(default=None, alias="createdOn")
    "The creation date"
    updated_on: datetime | None = Field(default=None, alias="updatedOn")
    "The date of the last update"
    product_id: str | None = Field(default=None, alias="productId")
    "The product ID"
    href: str | None = Field(default=None, alias="href")
    "Direct hyperlink to a resource"
    name: str | None = Field(default=None, alias="name")
    "The product name"
    type_: str | None = Field(default=None, alias="type")
    "The product type"
    url: str | None = Field(default=None, alias="url")
    "The external URL for the product"
    vendor: str | None = Field(default=None, alias="vendor")
    "The product vendor"
    external_id: str | None = Field(default=None, alias="externalId")
    "The external ID is the identifying string or number of the product given by another software"
    categories: list[NewProductCategory] | None = Field(default=None, alias="categories")
    variants: list[NewProductVariant] | None = Field(default=None, alias="variants")
    meta_fields: list[NewMetaField] | None = Field(default=None, alias="metaFields")


class UpdateProductVariant(BaseModel):
    "UpdateProductVariant model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    variant_id: str | None = Field(default=None, alias="variantId")
    "The product ID"
    href: str | None = Field(default=None, alias="href")
    "Direct hyperlink to a resource"
    name: str | None = Field(default=None, alias="name")
    "The product name"
    url: str | None = Field(default=None, alias="url")
    "The external URL to the product variant"
    sku: str | None = Field(default=None, alias="sku")
    "The stock-keeping unit of a variant. Must be unique within the product"
    price: float | None = Field(default=None, alias="price")
    "The price"
    price_tax: float | None = Field(default=None, alias="priceTax")
    "The price including tax"
    previous_price: float | None = Field(default=None, alias="previousPrice")
    "The price before the change"
    previous_price_tax: float | None = Field(default=None, alias="previousPriceTax")
    "The price before the change including tax"
    quantity: int | None = Field(default=None, alias="quantity")
    "The quantity of variant items"
    position: int | None = Field(default=None, alias="position")
    "The position of a variant"
    barcode: str | None = Field(default=None, alias="barcode")
    "The barcode of a variant"
    external_id: str | None = Field(default=None, alias="externalId")
    "The external ID is the identifying string or number of the variant given by another software"
    description: str | None = Field(default=None, alias="description")
    "The description of a variant"
    images: list[NewProductVariantImage] | None = Field(default=None, alias="images")
    meta_fields: list[NewMetaField] | None = Field(default=None, alias="metaFields")
    taxes: list[NewTax] | None = Field(default=None, alias="taxes")
    created_on: datetime | None = Field(default=None, alias="createdOn")
    "The creation date"
    updated_on: datetime | None = Field(default=None, alias="updatedOn")
    "The date of the last update"


class UpdateRssNewsletter(BaseModel):
    "UpdateRssNewsletter model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    rss_newsletter_id: str = Field(alias="rssNewsletterId")
    "The RSS newsletter ID"
    href: str = Field(alias="href")
    "Direct hyperlink to a resource"
    rss_feed_url: str | None = Field(default=None, alias="rssFeedUrl")
    "The URL for the RSS Feed"
    subject: str | None = Field(default=None, alias="subject")
    "The RSS message subject"
    name: str | None = Field(default=None, alias="name")
    "How your newsletters will be seen inside the application"
    status: Any | None = Field(default=None, alias="status")
    "The status of the RSS newsletter"
    editor: Any | None = Field(default=None, alias="editor")
    from_field: Any | None = Field(default=None, alias="fromField")
    "The 'From' email address used for the message"
    reply_to: Any | None = Field(default=None, alias="replyTo")
    "The email that will be used as a reply-to address"
    content: MessageContent | None = Field(default=None, alias="content")
    send_settings: Any | None = Field(default=None, alias="sendSettings")
    "How the message will be delivered to the subscriber"
    created_on: datetime | None = Field(default=None, alias="createdOn")
    "The creation date"
    flags: list[MessageFlagsArrayItem] | None = Field(default=None, alias="flags")


class UpdateSearchContacts(BaseModel):
    "New search contacts."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    subscribers_type: list[UpdateSearchContactsSubscribersTypeItem] | None = Field(
        default=None, alias="subscribersType"
    )
    "Only one subscription status"
    section_logic_operator: UpdateSearchContactsSectionLogicOperator = Field(
        alias="sectionLogicOperator"
    )
    "Match 'any' (`or` value) or 'all' (`and` value) of the following conditions"
    section: list[SearchContactSection] = Field(alias="section")
    search_contact_id: str | None = Field(default=None, alias="searchContactId")
    "The unique search-contact identifier"
    name: str = Field(alias="name")
    "The unique name of search-contact"
    created_on: datetime | None = Field(default=None, alias="createdOn")
    "The UTC date time format ISO 8601, e.g. 2018-04-10T10:02:57+0000"
    href: str | None = Field(default=None, alias="href")
    "Direct hyperlink to a resource"


class UpdateShop(BaseModel):
    "UpdateShop model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    created_on: datetime | None = Field(default=None, alias="createdOn")
    "The creation date"
    updated_on: datetime | None = Field(default=None, alias="updatedOn")
    "The date of the last update"
    shop_id: str | None = Field(default=None, alias="shopId")
    "The shop ID"
    href: str | None = Field(default=None, alias="href")
    "Direct hyperlink to a resource"
    name: str | None = Field(default=None, alias="name")
    "The shop name"
    locale: str | None = Field(default=None, alias="locale")
    "The language locale (ISO 639-1)"
    currency: str | None = Field(default=None, alias="currency")
    "The currency code (ISO 4217)"


class UpdateSuppression(BaseModel):
    "UpdateSuppression model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    name: str = Field(alias="name")
    "The name of the suppression list"
    masks: list[str] = Field(alias="masks")


class UpdateTag(BaseModel):
    "UpdateTag model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    name: str = Field(alias="name")
    "The tag name"
    color: str | None = Field(default=None, alias="color")
    "The tag color (deprecated)"


class UpdateTax(BaseModel):
    "UpdateTax model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    tax_id: str | None = Field(default=None, alias="taxId")
    "The tax ID"
    href: str | None = Field(default=None, alias="href")
    "Direct hyperlink to a resource"
    name: str | None = Field(default=None, alias="name")
    "The tax name"
    rate: float | None = Field(default=None, alias="rate")
    "The rate value"


class UpdateWorkflow(BaseModel):
    "UpdateWorkflow model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    status: UpdateWorkflowStatus = Field(alias="status")
    "An 'incomplete' status means that the workflow is a 'draft' in the web panel"


class UpsertContactCustomFields(BaseModel):
    "UpsertContactCustomFields model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    custom_field_values: list[NewContactCustomFieldValue] = Field(alias="customFieldValues")


class UpsertContactTags(BaseModel):
    "UpsertContactTags model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    tags: list[NewContactTag] = Field(alias="tags")


class UpsertMetaField(BaseModel):
    "This method assigns metafields. It doesn't unassign or delete them."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    meta_fields: list[UpsertSingleMetaField] = Field(alias="metaFields")


class UpsertProductCategory(BaseModel):
    "This method makes it possible to assign product categories, and to set a default product category. It doesn't remove or unassign product categories."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    categories: list[UpsertSingleProductCategory] = Field(alias="categories")


class UpsertSingleMetaField(BaseModel):
    "UpsertSingleMetaField model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    meta_field_id: str = Field(alias="metaFieldId")
    "MetaField ID"


class UpsertSingleProductCategory(BaseModel):
    "UpsertSingleProductCategory model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    category_id: str = Field(alias="categoryId")
    "The category ID"
    is_default: bool | None = Field(default=None, alias="isDefault")
    "This is a default category"


class UserActivityReportDetails(BaseModel):
    "UserActivityReportDetails model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    custom_report_id: str | None = Field(default=None, alias="customReportId")
    "The custom report ID"
    name: str | None = Field(default=None, alias="name")
    "The custom report name"
    href: str | None = Field(default=None, alias="href")
    "The direct hyperlink to a resource"
    type_: Any | None = Field(default=None, alias="type")
    "The custom report type"
    scheduling: dict[str, Any] | None = Field(default=None, alias="scheduling")
    "Parameters responsible for defining the reporting period"
    files: list[dict[str, Any]] | None = Field(default=None, alias="files")
    "Files that have been generated for the given report"
    created_at: datetime | None = Field(default=None, alias="createdAt")
    "Custom report creation date"
    generated_at: datetime | None = Field(default=None, alias="generatedAt")
    "Custom report generation date"
    filters: dict[str, Any] | None = Field(default=None, alias="filters")
    "Filters used to narrow down the report data"


class Webinar(BaseModel):
    "Webinar model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    webinar_id: str | None = Field(default=None, alias="webinarId")
    href: str | None = Field(default=None, alias="href")
    "Direct hyperlink to a resource"
    created_on: datetime | None = Field(default=None, alias="createdOn")
    starts_on: datetime | None = Field(default=None, alias="startsOn")
    webinar_url: str | None = Field(default=None, alias="webinarUrl")
    "The URL to the webinar room"
    status: WebinarStatus | None = Field(default=None, alias="status")
    type_: WebinarType | None = Field(default=None, alias="type")
    "The webinar type"
    campaigns: list[CampaignReference] | None = Field(default=None, alias="campaigns")
    newsletters: list[WebinarNewsletter] | None = Field(default=None, alias="newsletters")
    "The list of invitation messages"
    statistics: WebinarStatistics | None = Field(default=None, alias="statistics")


class WebinarCondition(BaseModel):
    "Search contacts that have participated/not participated in a specific webinar as a host/listener/presenter/registrant/any user."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    condition_type: WebinarConditionConditionType = Field(alias="conditionType")
    scope: str = Field(alias="scope")
    "The identifier of a webinar"
    webinar_condition: WebinarConditionWebinarCondition = Field(alias="webinarCondition")
    contact_type: WebinarConditionContactType = Field(alias="contactType")


class WebinarNewsletter(BaseModel):
    "WebinarNewsletter model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    newsletter_id: str = Field(alias="newsletterId")
    "The ID of the webinar invitation message"
    href: str = Field(alias="href")
    "Direct hyperlink to a resource"


class WebinarParticipantsReportDetails(BaseModel):
    "WebinarParticipantsReportDetails model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    custom_report_id: str | None = Field(default=None, alias="customReportId")
    "The custom report ID"
    name: str | None = Field(default=None, alias="name")
    "The custom report name"
    href: str | None = Field(default=None, alias="href")
    "The direct hyperlink to a resource"
    type_: Any | None = Field(default=None, alias="type")
    "The custom report type"
    scheduling: dict[str, Any] | None = Field(default=None, alias="scheduling")
    "Parameters responsible for defining the reporting period"
    files: list[dict[str, Any]] | None = Field(default=None, alias="files")
    "Files that have been generated for the given report"
    created_at: datetime | None = Field(default=None, alias="createdAt")
    "Custom report creation date"
    generated_at: datetime | None = Field(default=None, alias="generatedAt")
    "Custom report generation date"
    filters: dict[str, Any] | None = Field(default=None, alias="filters")
    "Filters used to narrow down the report data"


class WebinarStatistics(BaseModel):
    "WebinarStatistics model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    registrants: int = Field(alias="registrants")
    visitors: int = Field(alias="visitors")
    attendees: int = Field(alias="attendees")


class Website(BaseModel):
    "Website model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    website_id: str | None = Field(default=None, alias="websiteId")
    "The website ID"
    href: str | None = Field(default=None, alias="href")
    "Direct hyperlink to a resource"
    name: str | None = Field(default=None, alias="name")
    "The website name"
    status: WebsiteStatus | None = Field(default=None, alias="status")
    "The website status"
    domain_url: str | None = Field(default=None, alias="domainUrl")
    "The website domain"
    thumbnail_url: str | None = Field(default=None, alias="thumbnailUrl")
    "The URL of a website thumbnail"
    is_chats_enabled: Any | None = Field(default=None, alias="isChatsEnabled")
    "Chats is enabled on the website"
    created_at: datetime | None = Field(default=None, alias="createdAt")
    "The date (in GMT) the website was created"
    updated_at: datetime | None = Field(default=None, alias="updatedAt")
    "The date (in GMT) the website was updated"
    statistics: WebsiteStatistics | None = Field(default=None, alias="statistics")
    "The website statistics"


class WebsiteDetails(BaseModel):
    "WebsiteDetails model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    website_id: str | None = Field(default=None, alias="websiteId")
    "The website ID"
    href: str | None = Field(default=None, alias="href")
    "Direct hyperlink to a resource"
    name: str | None = Field(default=None, alias="name")
    "The website name"
    status: WebsiteDetailsStatus | None = Field(default=None, alias="status")
    "The website status"
    domain_url: str | None = Field(default=None, alias="domainUrl")
    "The website domain"
    thumbnail_url: str | None = Field(default=None, alias="thumbnailUrl")
    "The URL of a website thumbnail"
    is_chats_enabled: Any | None = Field(default=None, alias="isChatsEnabled")
    "Chats is enabled on the website"
    created_at: datetime | None = Field(default=None, alias="createdAt")
    "The date (in GMT) the website was created"
    updated_at: datetime | None = Field(default=None, alias="updatedAt")
    "The date (in GMT) the website was updated"
    statistics: WebsiteStatistics | None = Field(default=None, alias="statistics")
    "The website statistics"
    pages: list[WebsitePage] | None = Field(default=None, alias="pages")


class WebsitePage(BaseModel):
    "WebsitePage model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    uuid: str | None = Field(default=None, alias="uuid")
    "The website page ID"
    name: str | None = Field(default=None, alias="name")
    "The website page name"
    status: WebsitePageStatus | None = Field(default=None, alias="status")
    "The website page status"
    url: str | None = Field(default=None, alias="url")
    "Direct hyperlink to a resource"
    redirect_url: str | None = Field(default=None, alias="redirectUrl")
    "Direct hyperlink to a resource"
    created_at: datetime | None = Field(default=None, alias="createdAt")
    "The date (in GMT) the website page was created"


class WebsiteStatistics(BaseModel):
    "WebsiteStatistics model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    page_views: int | None = Field(default=None, alias="pageViews")
    "Number of page views"
    visits: int | None = Field(default=None, alias="visits")
    "Number of site visits"
    unique_visitors: int | None = Field(default=None, alias="uniqueVisitors")
    "Number of unique visitors"


class WebsiteStats(BaseModel):
    "WebsiteStats model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    website_id: str = Field(alias="websiteId")
    "The website ID"
    name: str | None = Field(default=None, alias="name")
    page_views: int | None = Field(default=None, alias="pageViews")
    "The number of page views"
    visits: int | None = Field(default=None, alias="visits")
    "The number of visits"
    unique_visitors: int | None = Field(default=None, alias="uniqueVisitors")
    "The number of unique visitors"
    thumbnail_url: str | None = Field(default=None, alias="thumbnailUrl")
    "Direct hyperlink to a resource"


class WeeklyReportScheduling(BaseModel):
    "WeeklyReportScheduling model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    frequency: Any | None = Field(default=None, alias="frequency")
    "The custom report frequency"
    one_time: dict[str, Any] | None = Field(default=None, alias="oneTime")
    "Field not applicable to the selected frequency"
    recurring: dict[str, Any] | None = Field(default=None, alias="recurring")
    "A field containing configuration parameters for recurring scheduling"


class Workflow(BaseModel):
    "Workflow model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    workflow_id: str = Field(alias="workflowId")
    "The workflow ID"
    name: str = Field(alias="name")
    status: WorkflowStatus = Field(alias="status")
    date_start: datetime | None = Field(default=None, alias="dateStart")
    date_stop: datetime | None = Field(default=None, alias="dateStop")
    subscriber_statistics: WorkflowSubscriberStatistics = Field(alias="subscriberStatistics")


class WorkflowSubscriberStatistics(BaseModel):
    "WorkflowSubscriberStatistics model."

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    completed_count: int = Field(alias="completedCount")
    "The number of subscribers that completed the workflow"
    in_progress_count: int = Field(alias="inProgressCount")
    "The number of subscribers that are in progress in the workflow"


# Every model above is now defined, so cross-references (including forward and
# self-references) can be resolved in one pass.
for _model_cls in list(globals().values()):
    if (
        isinstance(_model_cls, type)
        and issubclass(_model_cls, BaseModel)
        and _model_cls is not BaseModel
    ):
        _model_cls.model_rebuild(force=True)
