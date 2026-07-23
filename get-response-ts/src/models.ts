/**
 * Generated data models: every schema in the GetResponse OpenAPI spec.
 *
 * Enums are string-literal union types (simpler and tree-shakeable vs. a real
 * `enum`); models are plain interfaces keyed by the raw JSON wire name, so
 * (de)serialization is the identity function -- `response.json()` already
 * produces objects matching these shapes, and `JSON.stringify` on a value typed
 * as one of these interfaces produces valid wire JSON directly.
 *
 * This file is generated -- do not edit it directly.
 */

/** The message editor used for the A/B test */
export type AbtestsSubjectDetailsEditor =
  'html2' | 'custom' | 'text' | 'editor_v3' | 'getresponse' | 'legacy';

/** Tracking options enabled for the newsletter */
export type AbtestsSubjectDetailsFlagsItem =
  | 'clicktrack'
  | 'subscription_reminder'
  | 'openrate'
  | 'google_analytics'
  | 'manual_list'
  | 'custom_footer'
  | 'ecommerce_tracking';

/** A/B test stage */
export type AbtestsSubjectDetailsStage =
  'preparing' | 'testing' | 'finished' | 'sending_winner' | 'cancelled' | 'draft' | 'completed';

/** Newsletter status */
export type AbtestsSubjectDetailsStatus = 'active' | 'inactive' | 'deleted';

/** Tracking options enabled for the newsletter */
export type AbtestsSubjectListItemFlagsItem =
  | 'clicktrack'
  | 'subscription_reminder'
  | 'openrate'
  | 'google_analytics'
  | 'manual_list'
  | 'custom_footer'
  | 'ecommerce_tracking';

/** A/B test stage */
export type AbtestsSubjectListItemStage =
  'preparing' | 'testing' | 'finished' | 'sending_winner' | 'cancelled' | 'draft' | 'completed';

/** Newsletter status */
export type AbtestsSubjectListItemStatus = 'active' | 'inactive' | 'deleted';

/** Payment method */
export type AccountBillingPaymentMethod =
  | 'outside_system'
  | 'inside_system'
  | 'credit_card'
  | 'platnosci_pl'
  | 'direct_debit'
  | 'paypal'
  | 'yandex'
  | 'alipay'
  | 'alipay_mobile'
  | 'boleto'
  | 'ideal'
  | 'qiwi'
  | 'sofort'
  | 'webmoney';

/** Payment plan */
export type AccountBillingPaymentPlan = 'Free Trial' | 'Monthly' | '12 Months' | '24 Months';

/** Numbers of employees */
export type AccountNumberOfEmployees = '50' | '250' | '500' | 'more';

/** Account time notation */
export type AccountTimeFormat = '12h' | '24h';

/** AutoresponderDayConditionConditionType enum. */
export type AutoresponderDayConditionConditionType =
  | 'name'
  | 'email'
  | 'custom'
  | 'subscription_date'
  | 'subscription_method'
  | 'opened'
  | 'not_opened'
  | 'phase'
  | 'last_send_date'
  | 'last_click_date'
  | 'last_open_date'
  | 'webinar'
  | 'clicked'
  | 'not_clicked'
  | 'sent'
  | 'not_sent'
  | 'geo'
  | 'gdpr'
  | 'score'
  | 'engagement_score'
  | 'tag'
  | 'goal'
  | 'crm'
  | 'ecommerce_number_of_purchases'
  | 'ecommerce_total_spent'
  | 'ecommerce_product_purchased'
  | 'ecommerce_brand_purchased'
  | 'ecommerce_abandoned_cart'
  | 'sms_sent'
  | 'sms_link_clicked'
  | 'sms_link_not_clicked'
  | 'custom_event';

/** AutoresponderDayConditionOperatorType enum. */
export type AutoresponderDayConditionOperatorType = 'numeric_operator';

/** AutoresponderSendSettingsExcludedDaysOfWeekItem enum. */
export type AutoresponderSendSettingsExcludedDaysOfWeekItem =
  'Monday' | 'Tuesday' | 'Wednesday' | 'Thursday' | 'Friday' | 'Saturday' | 'Sunday';

/** When to send the message */
export type AutoresponderSendSettingsType = 'signup' | 'immediately' | 'delay' | 'custom';

/** The custom report type */
export type BaseCreateCustomReportType =
  | 'subscription_rejections'
  | 'message_stats'
  | 'unsubscribe_contacts_lists_report'
  | 'standard_subscriber_activity_report'
  | 'bounces'
  | 'account_summary_report'
  | 'user_activity'
  | 'list_summary_report'
  | 'isp_message_stats_report'
  | 'webinar_participants_report'
  | 'import_error_report'
  | 'message_clicks_report'
  | 'unconfirmed_contacts_stats_report'
  | 'transactional_email_bounce_report'
  | 'message_activity_report';

/** The DNS status for the user's private domain. Can be `null` if a private domain isn't assigned. */
export type BaseLandingPageUserDomainStatus = 'active' | 'inactive' | 'waiting';

/** The value type enumerable */
export type BaseMetaFieldValueType = 'string' | 'integer';

/** The recipient type. To send a text message to contacts in your list, select `contacts`. To message contacts who are not in any of your lists, select `importedNumbers` */
export type BaseSendSmsRecipientsType = 'contacts' | 'importedNumbers';

/** The MIME type for the confirmation message */
export type CampaignConfirmationMimeType = 'text/html' | 'text/plain' | 'combo';

/** What will happen after email confirmation. The values allowed include: hosted (the subscriber will stay on the default GetResponse website), customUrl (the subscriber will be redirected to a custom URL provided by the user). */
export type CampaignConfirmationRedirectType = 'hosted' | 'customUrl';

/** Single opt-in: confirmed opt-in disabled. Double opt-in: confirmed opt-in enabled. You can find more information [here](https://www.getresponse.com/resources/glossary/confirmed-opt-in.html) */
export type CampaignOptinTypesApi = 'single' | 'double';

/** Single opt-in: confirmed opt-in disabled. Double opt-in: confirmed opt-in enabled. You can find more information [here](https://www.getresponse.com/resources/glossary/confirmed-opt-in.html) */
export type CampaignOptinTypesEmail = 'single' | 'double';

/** Single opt-in: confirmed opt-in disabled. Double opt-in: confirmed opt-in enabled. You can find more information [here](https://www.getresponse.com/resources/glossary/confirmed-opt-in.html) */
export type CampaignOptinTypesImport = 'single';

/** Single opt-in: confirmed opt-in disabled. Double opt-in: confirmed opt-in enabled. You can find more information [here](https://www.getresponse.com/resources/glossary/confirmed-opt-in.html) */
export type CampaignOptinTypesWebform = 'single' | 'double';

/** Type of the resource that represents the message in the API */
export type ClickTrackMessageResourceType =
  'newsletters' | 'autoresponders' | 'rss-newsletters' | 'splittests' | 'sms';

/** The message type */
export type ClickTrackMessageType =
  'broadcast' | 'automation' | 'autoresponder' | 'rss' | 'splittest' | 'sms';

/** ConditionMessageOperatorOperatorType enum. */
export type ConditionMessageOperatorOperatorType = 'message_operator';

/** ConditionStringOperatorOperator enum. */
export type ConditionStringOperatorOperator =
  'is' | 'is_not' | 'contains' | 'not_contains' | 'starts' | 'ends' | 'not_starts' | 'not_ends';

/** ConditionStringOperatorOperatorType enum. */
export type ConditionStringOperatorOperatorType = 'string_operator';

/** ConditionTypeConditionType enum. */
export type ConditionTypeConditionType =
  | 'name'
  | 'email'
  | 'custom'
  | 'subscription_date'
  | 'subscription_method'
  | 'opened'
  | 'not_opened'
  | 'phase'
  | 'last_send_date'
  | 'last_click_date'
  | 'last_open_date'
  | 'webinar'
  | 'clicked'
  | 'not_clicked'
  | 'sent'
  | 'not_sent'
  | 'geo'
  | 'gdpr'
  | 'score'
  | 'engagement_score'
  | 'tag'
  | 'goal'
  | 'crm'
  | 'ecommerce_number_of_purchases'
  | 'ecommerce_total_spent'
  | 'ecommerce_product_purchased'
  | 'ecommerce_brand_purchased'
  | 'ecommerce_abandoned_cart'
  | 'sms_sent'
  | 'sms_link_clicked'
  | 'sms_link_not_clicked'
  | 'custom_event';

/** The type of activity */
export type ContactActivityActivity = 'send' | 'open' | 'click';

/** ContactActivityResourceResourceType enum. */
export type ContactActivityResourceResourceType =
  'newsletters' | 'splittests' | 'autoresponders' | 'rss-newsletters' | 'sms';

/** ContactDetailsOrigin enum. */
export type ContactDetailsOrigin =
  | 'import'
  | 'email'
  | 'www'
  | 'panel'
  | 'leads'
  | 'sale'
  | 'api'
  | 'survey'
  | 'iphone'
  | 'copy'
  | 'landing_page'
  | 'webinar'
  | 'website_builder_elegant'
  | 'chat'
  | 'course'
  | 'premium_newsletter';

/** ContactGeolocationContinentCode enum. */
export type ContactGeolocationContinentCode = 'OC' | 'AN' | 'SA' | 'NA' | 'AS' | 'EU' | 'AF';

/** ContactListElementOrigin enum. */
export type ContactListElementOrigin =
  | 'import'
  | 'email'
  | 'www'
  | 'panel'
  | 'leads'
  | 'sale'
  | 'api'
  | 'survey'
  | 'iphone'
  | 'copy'
  | 'landing_page'
  | 'webinar'
  | 'website_builder_elegant'
  | 'chat'
  | 'course'
  | 'premium_newsletter';

/** ContactOrigin enum. */
export type ContactOrigin =
  | 'import'
  | 'email'
  | 'www'
  | 'panel'
  | 'leads'
  | 'sale'
  | 'api'
  | 'survey'
  | 'iphone'
  | 'copy'
  | 'landing_page'
  | 'webinar'
  | 'website_builder_elegant'
  | 'chat'
  | 'course'
  | 'premium_newsletter';

/** The custom report type */
export type CreateAccountSummaryReportType =
  | 'subscription_rejections'
  | 'message_stats'
  | 'unsubscribe_contacts_lists_report'
  | 'standard_subscriber_activity_report'
  | 'bounces'
  | 'account_summary_report'
  | 'user_activity'
  | 'list_summary_report'
  | 'isp_message_stats_report'
  | 'webinar_participants_report'
  | 'import_error_report'
  | 'message_clicks_report'
  | 'unconfirmed_contacts_stats_report'
  | 'transactional_email_bounce_report'
  | 'message_activity_report';

/** The custom report type */
export type CreateBouncesReportType =
  | 'subscription_rejections'
  | 'message_stats'
  | 'unsubscribe_contacts_lists_report'
  | 'standard_subscriber_activity_report'
  | 'bounces'
  | 'account_summary_report'
  | 'user_activity'
  | 'list_summary_report'
  | 'isp_message_stats_report'
  | 'webinar_participants_report'
  | 'import_error_report'
  | 'message_clicks_report'
  | 'unconfirmed_contacts_stats_report'
  | 'transactional_email_bounce_report'
  | 'message_activity_report';

/** The custom report type */
export type CreateISPMessageStatsReportType =
  | 'subscription_rejections'
  | 'message_stats'
  | 'unsubscribe_contacts_lists_report'
  | 'standard_subscriber_activity_report'
  | 'bounces'
  | 'account_summary_report'
  | 'user_activity'
  | 'list_summary_report'
  | 'isp_message_stats_report'
  | 'webinar_participants_report'
  | 'import_error_report'
  | 'message_clicks_report'
  | 'unconfirmed_contacts_stats_report'
  | 'transactional_email_bounce_report'
  | 'message_activity_report';

/** The custom report type */
export type CreateImportErrorReportType =
  | 'subscription_rejections'
  | 'message_stats'
  | 'unsubscribe_contacts_lists_report'
  | 'standard_subscriber_activity_report'
  | 'bounces'
  | 'account_summary_report'
  | 'user_activity'
  | 'list_summary_report'
  | 'isp_message_stats_report'
  | 'webinar_participants_report'
  | 'import_error_report'
  | 'message_clicks_report'
  | 'unconfirmed_contacts_stats_report'
  | 'transactional_email_bounce_report'
  | 'message_activity_report';

/** The custom report type */
export type CreateListSummaryReportType =
  | 'subscription_rejections'
  | 'message_stats'
  | 'unsubscribe_contacts_lists_report'
  | 'standard_subscriber_activity_report'
  | 'bounces'
  | 'account_summary_report'
  | 'user_activity'
  | 'list_summary_report'
  | 'isp_message_stats_report'
  | 'webinar_participants_report'
  | 'import_error_report'
  | 'message_clicks_report'
  | 'unconfirmed_contacts_stats_report'
  | 'transactional_email_bounce_report'
  | 'message_activity_report';

/** The custom report type */
export type CreateMessageActivityReportType =
  | 'subscription_rejections'
  | 'message_stats'
  | 'unsubscribe_contacts_lists_report'
  | 'standard_subscriber_activity_report'
  | 'bounces'
  | 'account_summary_report'
  | 'user_activity'
  | 'list_summary_report'
  | 'isp_message_stats_report'
  | 'webinar_participants_report'
  | 'import_error_report'
  | 'message_clicks_report'
  | 'unconfirmed_contacts_stats_report'
  | 'transactional_email_bounce_report'
  | 'message_activity_report';

/** The custom report type */
export type CreateMessageClicksReportType =
  | 'subscription_rejections'
  | 'message_stats'
  | 'unsubscribe_contacts_lists_report'
  | 'standard_subscriber_activity_report'
  | 'bounces'
  | 'account_summary_report'
  | 'user_activity'
  | 'list_summary_report'
  | 'isp_message_stats_report'
  | 'webinar_participants_report'
  | 'import_error_report'
  | 'message_clicks_report'
  | 'unconfirmed_contacts_stats_report'
  | 'transactional_email_bounce_report'
  | 'message_activity_report';

/** The custom report type */
export type CreateMessageStatsReportType =
  | 'subscription_rejections'
  | 'message_stats'
  | 'unsubscribe_contacts_lists_report'
  | 'standard_subscriber_activity_report'
  | 'bounces'
  | 'account_summary_report'
  | 'user_activity'
  | 'list_summary_report'
  | 'isp_message_stats_report'
  | 'webinar_participants_report'
  | 'import_error_report'
  | 'message_clicks_report'
  | 'unconfirmed_contacts_stats_report'
  | 'transactional_email_bounce_report'
  | 'message_activity_report';

/** The custom report type */
export type CreateStandardSubscriberActivityReportType =
  | 'subscription_rejections'
  | 'message_stats'
  | 'unsubscribe_contacts_lists_report'
  | 'standard_subscriber_activity_report'
  | 'bounces'
  | 'account_summary_report'
  | 'user_activity'
  | 'list_summary_report'
  | 'isp_message_stats_report'
  | 'webinar_participants_report'
  | 'import_error_report'
  | 'message_clicks_report'
  | 'unconfirmed_contacts_stats_report'
  | 'transactional_email_bounce_report'
  | 'message_activity_report';

/** The custom report type */
export type CreateSubscriptionRejectionsReportType =
  | 'subscription_rejections'
  | 'message_stats'
  | 'unsubscribe_contacts_lists_report'
  | 'standard_subscriber_activity_report'
  | 'bounces'
  | 'account_summary_report'
  | 'user_activity'
  | 'list_summary_report'
  | 'isp_message_stats_report'
  | 'webinar_participants_report'
  | 'import_error_report'
  | 'message_clicks_report'
  | 'unconfirmed_contacts_stats_report'
  | 'transactional_email_bounce_report'
  | 'message_activity_report';

/** The custom report type */
export type CreateTransactionalEmailBounceReportType =
  | 'subscription_rejections'
  | 'message_stats'
  | 'unsubscribe_contacts_lists_report'
  | 'standard_subscriber_activity_report'
  | 'bounces'
  | 'account_summary_report'
  | 'user_activity'
  | 'list_summary_report'
  | 'isp_message_stats_report'
  | 'webinar_participants_report'
  | 'import_error_report'
  | 'message_clicks_report'
  | 'unconfirmed_contacts_stats_report'
  | 'transactional_email_bounce_report'
  | 'message_activity_report';

/** The message content type */
export type CreateTransactionalEmailContentType = 'direct' | 'template';

/** The custom report type */
export type CreateUnconfirmedContactsStatsReportType =
  | 'subscription_rejections'
  | 'message_stats'
  | 'unsubscribe_contacts_lists_report'
  | 'standard_subscriber_activity_report'
  | 'bounces'
  | 'account_summary_report'
  | 'user_activity'
  | 'list_summary_report'
  | 'isp_message_stats_report'
  | 'webinar_participants_report'
  | 'import_error_report'
  | 'message_clicks_report'
  | 'unconfirmed_contacts_stats_report'
  | 'transactional_email_bounce_report'
  | 'message_activity_report';

/** The custom report type */
export type CreateUnsubscribeContactsListsReportType =
  | 'subscription_rejections'
  | 'message_stats'
  | 'unsubscribe_contacts_lists_report'
  | 'standard_subscriber_activity_report'
  | 'bounces'
  | 'account_summary_report'
  | 'user_activity'
  | 'list_summary_report'
  | 'isp_message_stats_report'
  | 'webinar_participants_report'
  | 'import_error_report'
  | 'message_clicks_report'
  | 'unconfirmed_contacts_stats_report'
  | 'transactional_email_bounce_report'
  | 'message_activity_report';

/** The custom report type */
export type CreateUserActivityReportType =
  | 'subscription_rejections'
  | 'message_stats'
  | 'unsubscribe_contacts_lists_report'
  | 'standard_subscriber_activity_report'
  | 'bounces'
  | 'account_summary_report'
  | 'user_activity'
  | 'list_summary_report'
  | 'isp_message_stats_report'
  | 'webinar_participants_report'
  | 'import_error_report'
  | 'message_clicks_report'
  | 'unconfirmed_contacts_stats_report'
  | 'transactional_email_bounce_report'
  | 'message_activity_report';

/** The custom report type */
export type CreateWebinarParticipantsReportType =
  | 'subscription_rejections'
  | 'message_stats'
  | 'unsubscribe_contacts_lists_report'
  | 'standard_subscriber_activity_report'
  | 'bounces'
  | 'account_summary_report'
  | 'user_activity'
  | 'list_summary_report'
  | 'isp_message_stats_report'
  | 'webinar_participants_report'
  | 'import_error_report'
  | 'message_clicks_report'
  | 'unconfirmed_contacts_stats_report'
  | 'transactional_email_bounce_report'
  | 'message_activity_report';

/** CrmConditionConditionType enum. */
export type CrmConditionConditionType =
  | 'name'
  | 'email'
  | 'custom'
  | 'subscription_date'
  | 'subscription_method'
  | 'opened'
  | 'not_opened'
  | 'phase'
  | 'last_send_date'
  | 'last_click_date'
  | 'last_open_date'
  | 'webinar'
  | 'clicked'
  | 'not_clicked'
  | 'sent'
  | 'not_sent'
  | 'geo'
  | 'gdpr'
  | 'score'
  | 'engagement_score'
  | 'tag'
  | 'goal'
  | 'crm'
  | 'ecommerce_number_of_purchases'
  | 'ecommerce_total_spent'
  | 'ecommerce_product_purchased'
  | 'ecommerce_brand_purchased'
  | 'ecommerce_abandoned_cart'
  | 'sms_sent'
  | 'sms_link_clicked'
  | 'sms_link_not_clicked'
  | 'custom_event';

/** Type of attribute */
export type CustomEventAttributeDetailsType = 'string' | 'number' | 'datetime' | 'boolean';

/** Type of attribute */
export type CustomEventAttributeType = 'string' | 'number' | 'datetime' | 'boolean';

/** CustomEventConditionConditionType enum. */
export type CustomEventConditionConditionType =
  | 'name'
  | 'email'
  | 'custom'
  | 'subscription_date'
  | 'subscription_method'
  | 'opened'
  | 'not_opened'
  | 'phase'
  | 'last_send_date'
  | 'last_click_date'
  | 'last_open_date'
  | 'webinar'
  | 'clicked'
  | 'not_clicked'
  | 'sent'
  | 'not_sent'
  | 'geo'
  | 'gdpr'
  | 'score'
  | 'engagement_score'
  | 'tag'
  | 'goal'
  | 'crm'
  | 'ecommerce_number_of_purchases'
  | 'ecommerce_total_spent'
  | 'ecommerce_product_purchased'
  | 'ecommerce_brand_purchased'
  | 'ecommerce_abandoned_cart'
  | 'sms_sent'
  | 'sms_link_clicked'
  | 'sms_link_not_clicked'
  | 'custom_event';

/** Whether the custom event occurred or not */
export type CustomEventConditionOccurrence = 'occurred' | 'not_occurred';

/** CustomFieldConditionConditionType enum. */
export type CustomFieldConditionConditionType =
  | 'name'
  | 'email'
  | 'custom'
  | 'subscription_date'
  | 'subscription_method'
  | 'opened'
  | 'not_opened'
  | 'phase'
  | 'last_send_date'
  | 'last_click_date'
  | 'last_open_date'
  | 'webinar'
  | 'clicked'
  | 'not_clicked'
  | 'sent'
  | 'not_sent'
  | 'geo'
  | 'gdpr'
  | 'score'
  | 'engagement_score'
  | 'tag'
  | 'goal'
  | 'crm'
  | 'ecommerce_number_of_purchases'
  | 'ecommerce_total_spent'
  | 'ecommerce_product_purchased'
  | 'ecommerce_brand_purchased'
  | 'ecommerce_abandoned_cart'
  | 'sms_sent'
  | 'sms_link_clicked'
  | 'sms_link_not_clicked'
  | 'custom_event';

/** Depends on the type of custom field, read more in [custom field condition documentation in segments (search contacts) reference manual](https://apidocs.getresponse.com/v3/case-study/segments-manual#get-by-custom-fields-search-contacts) */
export type CustomFieldConditionOperatorType =
  'string_operator_list' | 'string_operator' | 'numeric_operator' | 'date_operator';

/** Allowed operators for `"operatorType":"date_operator"` */
export type CustomFieldDateOperatorEnum =
  'date_to' | 'date_from' | 'custom' | 'specific_date' | 'assigned' | 'not_assigned';

/** CustomFieldFormatEnum enum. */
export type CustomFieldFormatEnum =
  'text' | 'textarea' | 'radio' | 'checkbox' | 'single_select' | 'multi_select';

/** Allowed operators for `"operatorType":"numeric_operator"` */
export type CustomFieldNumericOperatorEnum =
  | 'numeric_lt'
  | 'numeric_gt'
  | 'numeric_eq'
  | 'numeric_not_eq'
  | 'numeric_lt_eq'
  | 'numeric_gt_eq'
  | "assigned'"
  | 'not_assigned';

/** Allowed operators for `"operatorType":"string_operator"` and `"operatorType":"string_operator_list"` */
export type CustomFieldStringOperatorEnum =
  | 'is'
  | 'is_not'
  | 'contains'
  | 'not_contains'
  | 'starts'
  | 'ends'
  | 'not_starts'
  | 'not_ends'
  | 'assigned'
  | 'not_assigned';

/** CustomFieldTypeEnum enum. */
export type CustomFieldTypeEnum =
  | 'string'
  | 'number'
  | 'date'
  | 'datetime'
  | 'country'
  | 'currency'
  | 'phone'
  | 'gender'
  | 'ip'
  | 'url';

/** Allowed values for `"operatorType":"date_operator"` with `"operator":"specific_date"` */
export type CustomFieldValueForOperatorTypeDateAndOperatorSpecificDate =
  | 'today'
  | 'yesterday'
  | 'last_7_days'
  | 'last_30_days'
  | 'last_n_days'
  | 'this_week'
  | 'last_week'
  | 'this_month'
  | 'last_month'
  | 'last_2_months';

/** Type of returning value, it returns `type` options extended by a `string` option if the `format` was not defined */
export type CustomFieldValueType =
  | 'string'
  | 'number'
  | 'date'
  | 'datetime'
  | 'country'
  | 'currency'
  | 'phone'
  | 'gender'
  | 'ip'
  | 'url';

/** CustomReportDaysOfWeekEnum enum. */
export type CustomReportDaysOfWeekEnum =
  'monday' | 'tuesday' | 'wednesday' | 'thursday' | 'friday' | 'saturday' | 'sunday';

/** CustomReportFileStatusesEnum enum. */
export type CustomReportFileStatusesEnum = 'pending' | 'in-progress' | 'ready' | 'error';

/** CustomReportFrequenciesEnum enum. */
export type CustomReportFrequenciesEnum = 'monthly' | 'weekly' | 'daily' | 'one_time';

/** CustomReportTypesEnum enum. */
export type CustomReportTypesEnum =
  | 'subscription_rejections'
  | 'message_stats'
  | 'unsubscribe_contacts_lists_report'
  | 'standard_subscriber_activity_report'
  | 'bounces'
  | 'account_summary_report'
  | 'user_activity'
  | 'list_summary_report'
  | 'isp_message_stats_report'
  | 'webinar_participants_report'
  | 'import_error_report'
  | 'message_clicks_report'
  | 'unconfirmed_contacts_stats_report'
  | 'transactional_email_bounce_report'
  | 'message_activity_report';

/** The message content type */
export type DirectContentContentType = 'direct' | 'template';

/** ECommerceAbandonedCartConditionConditionType enum. */
export type ECommerceAbandonedCartConditionConditionType =
  | 'name'
  | 'email'
  | 'custom'
  | 'subscription_date'
  | 'subscription_method'
  | 'opened'
  | 'not_opened'
  | 'phase'
  | 'last_send_date'
  | 'last_click_date'
  | 'last_open_date'
  | 'webinar'
  | 'clicked'
  | 'not_clicked'
  | 'sent'
  | 'not_sent'
  | 'geo'
  | 'gdpr'
  | 'score'
  | 'engagement_score'
  | 'tag'
  | 'goal'
  | 'crm'
  | 'ecommerce_number_of_purchases'
  | 'ecommerce_total_spent'
  | 'ecommerce_product_purchased'
  | 'ecommerce_brand_purchased'
  | 'ecommerce_abandoned_cart'
  | 'sms_sent'
  | 'sms_link_clicked'
  | 'sms_link_not_clicked'
  | 'custom_event';

/** Set a date range. For the date_from and last_n_days, custom field value is required. Examples can be found here: [API Docs](https://apidocs.getresponse.com/v3/case-study/segments-manual/#ecommerce-abandoned-cart-condition-type). */
export type ECommerceAbandonedCartConditionDateOperator =
  | 'date_from'
  | 'anytime'
  | 'never'
  | 'today'
  | 'yesterday'
  | 'last_n_days'
  | 'this_week'
  | 'last_week'
  | 'this_month'
  | 'last_month'
  | 'custom';

/** ECommerceBrandPurchasedConditionConditionType enum. */
export type ECommerceBrandPurchasedConditionConditionType =
  | 'name'
  | 'email'
  | 'custom'
  | 'subscription_date'
  | 'subscription_method'
  | 'opened'
  | 'not_opened'
  | 'phase'
  | 'last_send_date'
  | 'last_click_date'
  | 'last_open_date'
  | 'webinar'
  | 'clicked'
  | 'not_clicked'
  | 'sent'
  | 'not_sent'
  | 'geo'
  | 'gdpr'
  | 'score'
  | 'engagement_score'
  | 'tag'
  | 'goal'
  | 'crm'
  | 'ecommerce_number_of_purchases'
  | 'ecommerce_total_spent'
  | 'ecommerce_product_purchased'
  | 'ecommerce_brand_purchased'
  | 'ecommerce_abandoned_cart'
  | 'sms_sent'
  | 'sms_link_clicked'
  | 'sms_link_not_clicked'
  | 'custom_event';

/** ECommerceBrandPurchasedConditionOperator enum. */
export type ECommerceBrandPurchasedConditionOperator = 'is' | 'not_is';

/** ECommerceBrandPurchasedConditionOperatorType enum. */
export type ECommerceBrandPurchasedConditionOperatorType = 'equal_operator';

/** ECommerceNumberOfPurchasesConditionConditionType enum. */
export type ECommerceNumberOfPurchasesConditionConditionType =
  | 'name'
  | 'email'
  | 'custom'
  | 'subscription_date'
  | 'subscription_method'
  | 'opened'
  | 'not_opened'
  | 'phase'
  | 'last_send_date'
  | 'last_click_date'
  | 'last_open_date'
  | 'webinar'
  | 'clicked'
  | 'not_clicked'
  | 'sent'
  | 'not_sent'
  | 'geo'
  | 'gdpr'
  | 'score'
  | 'engagement_score'
  | 'tag'
  | 'goal'
  | 'crm'
  | 'ecommerce_number_of_purchases'
  | 'ecommerce_total_spent'
  | 'ecommerce_product_purchased'
  | 'ecommerce_brand_purchased'
  | 'ecommerce_abandoned_cart'
  | 'sms_sent'
  | 'sms_link_clicked'
  | 'sms_link_not_clicked'
  | 'custom_event';

/** ECommerceNumberOfPurchasesConditionOperator enum. */
export type ECommerceNumberOfPurchasesConditionOperator =
  'numeric_lt' | 'numeric_gt' | 'numeric_eq' | 'numeric_not_eq' | 'numeric_lt_eq' | 'numeric_gt_eq';

/** ECommerceNumberOfPurchasesConditionOperatorType enum. */
export type ECommerceNumberOfPurchasesConditionOperatorType = 'numeric_operator';

/** ECommerceProductPurchasedConditionConditionType enum. */
export type ECommerceProductPurchasedConditionConditionType =
  | 'name'
  | 'email'
  | 'custom'
  | 'subscription_date'
  | 'subscription_method'
  | 'opened'
  | 'not_opened'
  | 'phase'
  | 'last_send_date'
  | 'last_click_date'
  | 'last_open_date'
  | 'webinar'
  | 'clicked'
  | 'not_clicked'
  | 'sent'
  | 'not_sent'
  | 'geo'
  | 'gdpr'
  | 'score'
  | 'engagement_score'
  | 'tag'
  | 'goal'
  | 'crm'
  | 'ecommerce_number_of_purchases'
  | 'ecommerce_total_spent'
  | 'ecommerce_product_purchased'
  | 'ecommerce_brand_purchased'
  | 'ecommerce_abandoned_cart'
  | 'sms_sent'
  | 'sms_link_clicked'
  | 'sms_link_not_clicked'
  | 'custom_event';

/** ECommerceProductPurchasedConditionOperator enum. */
export type ECommerceProductPurchasedConditionOperator = 'is' | 'is_not';

/** ECommerceProductPurchasedConditionOperatorType enum. */
export type ECommerceProductPurchasedConditionOperatorType = 'equal_operator';

/** ECommerceTotalSpentConditionConditionType enum. */
export type ECommerceTotalSpentConditionConditionType =
  | 'name'
  | 'email'
  | 'custom'
  | 'subscription_date'
  | 'subscription_method'
  | 'opened'
  | 'not_opened'
  | 'phase'
  | 'last_send_date'
  | 'last_click_date'
  | 'last_open_date'
  | 'webinar'
  | 'clicked'
  | 'not_clicked'
  | 'sent'
  | 'not_sent'
  | 'geo'
  | 'gdpr'
  | 'score'
  | 'engagement_score'
  | 'tag'
  | 'goal'
  | 'crm'
  | 'ecommerce_number_of_purchases'
  | 'ecommerce_total_spent'
  | 'ecommerce_product_purchased'
  | 'ecommerce_brand_purchased'
  | 'ecommerce_abandoned_cart'
  | 'sms_sent'
  | 'sms_link_clicked'
  | 'sms_link_not_clicked'
  | 'custom_event';

/** ECommerceTotalSpentConditionOperator enum. */
export type ECommerceTotalSpentConditionOperator =
  'numeric_lt' | 'numeric_gt' | 'numeric_eq' | 'numeric_not_eq' | 'numeric_lt_eq' | 'numeric_gt_eq';

/** ECommerceTotalSpentConditionOperatorType enum. */
export type ECommerceTotalSpentConditionOperatorType = 'numeric_operator';

/** EmailConditionConditionType enum. */
export type EmailConditionConditionType =
  | 'name'
  | 'email'
  | 'custom'
  | 'subscription_date'
  | 'subscription_method'
  | 'opened'
  | 'not_opened'
  | 'phase'
  | 'last_send_date'
  | 'last_click_date'
  | 'last_open_date'
  | 'webinar'
  | 'clicked'
  | 'not_clicked'
  | 'sent'
  | 'not_sent'
  | 'geo'
  | 'gdpr'
  | 'score'
  | 'engagement_score'
  | 'tag'
  | 'goal'
  | 'crm'
  | 'ecommerce_number_of_purchases'
  | 'ecommerce_total_spent'
  | 'ecommerce_product_purchased'
  | 'ecommerce_brand_purchased'
  | 'ecommerce_abandoned_cart'
  | 'sms_sent'
  | 'sms_link_clicked'
  | 'sms_link_not_clicked'
  | 'custom_event';

/** EmailConditionOperator enum. */
export type EmailConditionOperator =
  'is' | 'is_not' | 'contains' | 'not_contains' | 'starts' | 'ends' | 'not_starts' | 'not_ends';

/** EmailConditionOperatorType enum. */
export type EmailConditionOperatorType = 'string_operator';

/** EngagementScoreConditionConditionType enum. */
export type EngagementScoreConditionConditionType =
  | 'name'
  | 'email'
  | 'custom'
  | 'subscription_date'
  | 'subscription_method'
  | 'opened'
  | 'not_opened'
  | 'phase'
  | 'last_send_date'
  | 'last_click_date'
  | 'last_open_date'
  | 'webinar'
  | 'clicked'
  | 'not_clicked'
  | 'sent'
  | 'not_sent'
  | 'geo'
  | 'gdpr'
  | 'score'
  | 'engagement_score'
  | 'tag'
  | 'goal'
  | 'crm'
  | 'ecommerce_number_of_purchases'
  | 'ecommerce_total_spent'
  | 'ecommerce_product_purchased'
  | 'ecommerce_brand_purchased'
  | 'ecommerce_abandoned_cart'
  | 'sms_sent'
  | 'sms_link_clicked'
  | 'sms_link_not_clicked'
  | 'custom_event';

/** The operator used in engagement score comparison */
export type EngagementScoreConditionOperator =
  'numeric_lt' | 'numeric_gt' | 'numeric_eq' | 'numeric_not_eq' | 'numeric_lt_eq' | 'numeric_gt_eq';

/** The file group */
export type FileGroup = 'audio' | 'video' | 'photo' | 'document';

/** FilePropertyName enum. */
export type FilePropertyName = 'width' | 'height';

/** FormDetailsStatus enum. */
export type FormDetailsStatus = 'published' | 'unpublished' | 'draft';

/** What to do when the address already exists in the campaign */
export type FormSettingsAlreadySubscribedType = 'stay_on_page' | 'default' | 'custom_url';

/** How to forward form data to a thank-you page. [Learn more](https://www.getresponse.com/help/building-contact-lists/forms-and-pop-ups/can-i-forward-subscriber-data-to-a-custom-thank-you-page.html). `null` means that the data forwarding is turned off. */
export type FormSettingsForwardDataRequestType = 'GET' | 'POST';

/** `single` - Single opt-in means that the contact will be added without confirming their subscription first. `double` - Double opt-in means that the contact will receive a subscription confirmation email. */
export type FormSettingsOptin = 'single' | 'double';

/** What should happen when a new contact subscribes via the form. */
export type FormSettingsThankYouType = 'stay_on_page' | 'default' | 'custom_url';

/** FormStatus enum. */
export type FormStatus = 'published' | 'unpublished' | 'draft';

/** FormVariantDetailsStatus enum. */
export type FormVariantDetailsStatus = 'published' | 'unpublished' | 'disabled';

/** Is this variant the winner in the A/B test */
export type FormVariantDetailsWinner = 'yes' | 'no';

/** FormVariantStatus enum. */
export type FormVariantStatus = 'published' | 'unpublished' | 'disabled';

/** GdprConditionConditionType enum. */
export type GdprConditionConditionType =
  | 'name'
  | 'email'
  | 'custom'
  | 'subscription_date'
  | 'subscription_method'
  | 'opened'
  | 'not_opened'
  | 'phase'
  | 'last_send_date'
  | 'last_click_date'
  | 'last_open_date'
  | 'webinar'
  | 'clicked'
  | 'not_clicked'
  | 'sent'
  | 'not_sent'
  | 'geo'
  | 'gdpr'
  | 'score'
  | 'engagement_score'
  | 'tag'
  | 'goal'
  | 'crm'
  | 'ecommerce_number_of_purchases'
  | 'ecommerce_total_spent'
  | 'ecommerce_product_purchased'
  | 'ecommerce_brand_purchased'
  | 'ecommerce_abandoned_cart'
  | 'sms_sent'
  | 'sms_link_clicked'
  | 'sms_link_not_clicked'
  | 'custom_event';

/** Specify whether you want to search for contacts who have given or not given consent. */
export type GdprConditionConsentStatus = 'given' | 'not_given';

/** GeolocationConditionConditionType enum. */
export type GeolocationConditionConditionType =
  | 'name'
  | 'email'
  | 'custom'
  | 'subscription_date'
  | 'subscription_method'
  | 'opened'
  | 'not_opened'
  | 'phase'
  | 'last_send_date'
  | 'last_click_date'
  | 'last_open_date'
  | 'webinar'
  | 'clicked'
  | 'not_clicked'
  | 'sent'
  | 'not_sent'
  | 'geo'
  | 'gdpr'
  | 'score'
  | 'engagement_score'
  | 'tag'
  | 'goal'
  | 'crm'
  | 'ecommerce_number_of_purchases'
  | 'ecommerce_total_spent'
  | 'ecommerce_product_purchased'
  | 'ecommerce_brand_purchased'
  | 'ecommerce_abandoned_cart'
  | 'sms_sent'
  | 'sms_link_clicked'
  | 'sms_link_not_clicked'
  | 'custom_event';

/** GeolocationConditionOperator enum. */
export type GeolocationConditionOperator =
  'is' | 'is_not' | 'contains' | 'not_contains' | 'starts' | 'ends' | 'not_starts' | 'not_ends';

/** GeolocationConditionOperatorType enum. */
export type GeolocationConditionOperatorType = 'string_operator';

/** Specify the search parameters */
export type GeolocationConditionScope =
  | 'country'
  | 'country_code'
  | 'region'
  | 'city'
  | 'longitude'
  | 'latitude'
  | 'postal_code'
  | 'dma_code';

/** GetAbTestSubjectListQueryStage enum. */
export type GetAbTestSubjectListQueryStage =
  'preparing' | 'testing' | 'finished' | 'sending-winner' | 'cancelled' | 'draft' | 'completed';

/** GetAutoresponderListQueryStatus enum. */
export type GetAutoresponderListQueryStatus = 'enabled' | 'disabled';

/** GetAutoresponderStatisticsCollectionQueryGroupBy enum. */
export type GetAutoresponderStatisticsCollectionQueryGroupBy = 'total' | 'hour' | 'day' | 'month';

/** GetAutoresponderThumbnailSize enum. */
export type GetAutoresponderThumbnailSize = 'default' | 'small';

/** GetCampaignStatisticsBalanceQueryGroupBy enum. */
export type GetCampaignStatisticsBalanceQueryGroupBy = 'hour' | 'day' | 'month' | 'total';

/** GetCampaignStatisticsListSizeQueryGroupBy enum. */
export type GetCampaignStatisticsListSizeQueryGroupBy = 'hour' | 'day' | 'month' | 'total';

/** GetCampaignStatisticsLocationsQueryGroupBy enum. */
export type GetCampaignStatisticsLocationsQueryGroupBy = 'hour' | 'day' | 'month' | 'total';

/** GetCampaignStatisticsOriginsQueryGroupBy enum. */
export type GetCampaignStatisticsOriginsQueryGroupBy = 'hour' | 'day' | 'month' | 'total';

/** GetCampaignStatisticsRemovalsQueryGroupBy enum. */
export type GetCampaignStatisticsRemovalsQueryGroupBy = 'hour' | 'day' | 'month' | 'total';

/** GetCampaignStatisticsSubscriptionsQueryGroupBy enum. */
export type GetCampaignStatisticsSubscriptionsQueryGroupBy = 'hour' | 'day' | 'month' | 'total';

/** GetContactListQueryOrigin enum. */
export type GetContactListQueryOrigin =
  | 'import'
  | 'email'
  | 'www'
  | 'panel'
  | 'leads'
  | 'sale'
  | 'api'
  | 'survey'
  | 'iphone'
  | 'copy'
  | 'landing_page'
  | 'webinar'
  | 'website_builder_elegant'
  | 'chat'
  | 'course'
  | 'premium_newsletter';

/** GetFormListQueryStatus enum. */
export type GetFormListQueryStatus = 'enabled' | 'disabled' | 'published' | 'unpublished' | 'draft';

/** GetLpsGeneralPerformanceStatsQueryDevice enum. */
export type GetLpsGeneralPerformanceStatsQueryDevice = 'desktop' | 'mobile';

/** GetLpsListQueryStatus enum. */
export type GetLpsListQueryStatus = 'published' | 'unpublished';

/** GetNewsletterActivitiesQueryActivity enum. */
export type GetNewsletterActivitiesQueryActivity = 'send' | 'open' | 'click';

/** GetNewsletterListQueryStatus enum. */
export type GetNewsletterListQueryStatus = 'enabled' | 'disabled';

/** GetNewsletterListQueryType enum. */
export type GetNewsletterListQueryType = 'draft' | 'broadcast' | 'splittest' | 'automation';

/** GetNewsletterStatisticsCollectionQueryGroupBy enum. */
export type GetNewsletterStatisticsCollectionQueryGroupBy = 'total' | 'hour' | 'day' | 'month';

/** GetNewsletterThumbnailSize enum. */
export type GetNewsletterThumbnailSize = 'default' | 'small';

/** GetPopupGeneralPerformanceQueryDevice enum. */
export type GetPopupGeneralPerformanceQueryDevice = 'desktop' | 'mobile';

/** GetPopupsListQueryStatus enum. */
export type GetPopupsListQueryStatus = 'published' | 'unpublished';

/** GetRssNewsletterStatisticsCollectionQueryGroupBy enum. */
export type GetRssNewsletterStatisticsCollectionQueryGroupBy = 'total' | 'hour' | 'day' | 'month';

/** GetRssNewslettersListQueryStatus enum. */
export type GetRssNewslettersListQueryStatus = 'enabled' | 'disabled';

/** GetSingleAutoresponderStatisticsQueryGroupBy enum. */
export type GetSingleAutoresponderStatisticsQueryGroupBy = 'total' | 'hour' | 'day' | 'month';

/** GetSingleNewsletterStatisticsQueryGroupBy enum. */
export type GetSingleNewsletterStatisticsQueryGroupBy = 'total' | 'hour' | 'day' | 'month';

/** GetSingleRssNewsletterStatisticsCollectionQueryGroupBy enum. */
export type GetSingleRssNewsletterStatisticsCollectionQueryGroupBy =
  'total' | 'hour' | 'day' | 'month';

/** GetSmsListQuerySendingStatus enum. */
export type GetSmsListQuerySendingStatus = 'scheduled' | 'sending' | 'sent';

/** GetSmsListQueryType enum. */
export type GetSmsListQueryType = 'sms' | 'draft';

/** GetSplittestListQueryStatus enum. */
export type GetSplittestListQueryStatus = 'active' | 'inactive';

/** GetTransactionalEmailsStatisticsQueryGroupBy enum. */
export type GetTransactionalEmailsStatisticsQueryGroupBy = 'total' | 'day';

/** GetWbeGeneralPerformanceStatsQueryDevice enum. */
export type GetWbeGeneralPerformanceStatsQueryDevice = 'desktop' | 'mobile';

/** GetWebinarListQueryStatus enum. */
export type GetWebinarListQueryStatus = 'upcoming' | 'finished' | 'published' | 'unpublished';

/** GetWebinarListQueryType enum. */
export type GetWebinarListQueryType = 'all' | 'live' | 'on_demand';

/** GetWebsitesListQueryStatus enum. */
export type GetWebsitesListQueryStatus = 'published' | 'unpublished';

/** GoalConditionConditionType enum. */
export type GoalConditionConditionType =
  | 'name'
  | 'email'
  | 'custom'
  | 'subscription_date'
  | 'subscription_method'
  | 'opened'
  | 'not_opened'
  | 'phase'
  | 'last_send_date'
  | 'last_click_date'
  | 'last_open_date'
  | 'webinar'
  | 'clicked'
  | 'not_clicked'
  | 'sent'
  | 'not_sent'
  | 'geo'
  | 'gdpr'
  | 'score'
  | 'engagement_score'
  | 'tag'
  | 'goal'
  | 'crm'
  | 'ecommerce_number_of_purchases'
  | 'ecommerce_total_spent'
  | 'ecommerce_product_purchased'
  | 'ecommerce_brand_purchased'
  | 'ecommerce_abandoned_cart'
  | 'sms_sent'
  | 'sms_link_clicked'
  | 'sms_link_not_clicked'
  | 'custom_event';

/** The relational and existence operator. For the relational operator, the value field is required. */
export type GoalConditionOperator =
  | 'numeric_lt'
  | 'numeric_gt'
  | 'numeric_eq'
  | 'numeric_not_eq'
  | 'numeric_lt_eq'
  | 'numeric_gt_eq'
  | 'assigned'
  | 'not_assigned';

/** GoalConditionOperatorType enum. */
export type GoalConditionOperatorType = 'numeric_operator';

/** File extension */
export type ImageDetailsExtension = 'jpg' | 'gif' | 'png' | 'jpeg' | 'bmp';

/** ImportStatus enum. */
export type ImportStatus =
  'uploaded' | 'review' | 'approved' | 'rejected' | 'finished' | 'canceled' | 'to_review';

/** To entirely prevent your page content from being listed in the Google web index, even if other sites link to it use a noindex meta tag */
export type LandingPageMetaNoindex = 'yes' | 'no';

/** The opt-in type (double or single) */
export type LandingPageOptin = 'single' | 'double';

/** What should happen after a contact subscribes */
export type LandingPageThankYouPageType = 'stay_on_page' | 'default' | 'custom_url';

/** The DNS status for the user's private domain. Can be `null` if a private domain isn't assigned. */
export type LandingPageUserDomainStatus = 'active' | 'inactive' | 'waiting';

/** LastClickDateConditionConditionType enum. */
export type LastClickDateConditionConditionType =
  | 'name'
  | 'email'
  | 'custom'
  | 'subscription_date'
  | 'subscription_method'
  | 'opened'
  | 'not_opened'
  | 'phase'
  | 'last_send_date'
  | 'last_click_date'
  | 'last_open_date'
  | 'webinar'
  | 'clicked'
  | 'not_clicked'
  | 'sent'
  | 'not_sent'
  | 'geo'
  | 'gdpr'
  | 'score'
  | 'engagement_score'
  | 'tag'
  | 'goal'
  | 'crm'
  | 'ecommerce_number_of_purchases'
  | 'ecommerce_total_spent'
  | 'ecommerce_product_purchased'
  | 'ecommerce_brand_purchased'
  | 'ecommerce_abandoned_cart'
  | 'sms_sent'
  | 'sms_link_clicked'
  | 'sms_link_not_clicked'
  | 'custom_event';

/** LastClickDateConditionOperator enum. */
export type LastClickDateConditionOperator = 'date_to' | 'date_from' | 'specific_date' | 'custom';

/** LastClickDateConditionOperatorType enum. */
export type LastClickDateConditionOperatorType = 'date_operator';

/** LastOpenDateConditionConditionType enum. */
export type LastOpenDateConditionConditionType =
  | 'name'
  | 'email'
  | 'custom'
  | 'subscription_date'
  | 'subscription_method'
  | 'opened'
  | 'not_opened'
  | 'phase'
  | 'last_send_date'
  | 'last_click_date'
  | 'last_open_date'
  | 'webinar'
  | 'clicked'
  | 'not_clicked'
  | 'sent'
  | 'not_sent'
  | 'geo'
  | 'gdpr'
  | 'score'
  | 'engagement_score'
  | 'tag'
  | 'goal'
  | 'crm'
  | 'ecommerce_number_of_purchases'
  | 'ecommerce_total_spent'
  | 'ecommerce_product_purchased'
  | 'ecommerce_brand_purchased'
  | 'ecommerce_abandoned_cart'
  | 'sms_sent'
  | 'sms_link_clicked'
  | 'sms_link_not_clicked'
  | 'custom_event';

/** LastOpenDateConditionOperator enum. */
export type LastOpenDateConditionOperator = 'date_to' | 'date_from' | 'specific_date' | 'custom';

/** LastOpenDateConditionOperatorType enum. */
export type LastOpenDateConditionOperatorType = 'date_operator';

/** LastSendDateConditionConditionType enum. */
export type LastSendDateConditionConditionType =
  | 'name'
  | 'email'
  | 'custom'
  | 'subscription_date'
  | 'subscription_method'
  | 'opened'
  | 'not_opened'
  | 'phase'
  | 'last_send_date'
  | 'last_click_date'
  | 'last_open_date'
  | 'webinar'
  | 'clicked'
  | 'not_clicked'
  | 'sent'
  | 'not_sent'
  | 'geo'
  | 'gdpr'
  | 'score'
  | 'engagement_score'
  | 'tag'
  | 'goal'
  | 'crm'
  | 'ecommerce_number_of_purchases'
  | 'ecommerce_total_spent'
  | 'ecommerce_product_purchased'
  | 'ecommerce_brand_purchased'
  | 'ecommerce_abandoned_cart'
  | 'sms_sent'
  | 'sms_link_clicked'
  | 'sms_link_not_clicked'
  | 'custom_event';

/** LastSendDateConditionOperator enum. */
export type LastSendDateConditionOperator = 'date_to' | 'date_from' | 'specific_date' | 'custom';

/** LastSendDateConditionOperatorType enum. */
export type LastSendDateConditionOperatorType = 'date_operator';

/** LinkClickedConditionConditionType enum. */
export type LinkClickedConditionConditionType =
  | 'name'
  | 'email'
  | 'custom'
  | 'subscription_date'
  | 'subscription_method'
  | 'opened'
  | 'not_opened'
  | 'phase'
  | 'last_send_date'
  | 'last_click_date'
  | 'last_open_date'
  | 'webinar'
  | 'clicked'
  | 'not_clicked'
  | 'sent'
  | 'not_sent'
  | 'geo'
  | 'gdpr'
  | 'score'
  | 'engagement_score'
  | 'tag'
  | 'goal'
  | 'crm'
  | 'ecommerce_number_of_purchases'
  | 'ecommerce_total_spent'
  | 'ecommerce_product_purchased'
  | 'ecommerce_brand_purchased'
  | 'ecommerce_abandoned_cart'
  | 'sms_sent'
  | 'sms_link_clicked'
  | 'sms_link_not_clicked'
  | 'custom_event';

/** LinkClickedConditionOperatorType enum. */
export type LinkClickedConditionOperatorType = 'message_operator';

/** LinkNotClickedConditionConditionType enum. */
export type LinkNotClickedConditionConditionType =
  | 'name'
  | 'email'
  | 'custom'
  | 'subscription_date'
  | 'subscription_method'
  | 'opened'
  | 'not_opened'
  | 'phase'
  | 'last_send_date'
  | 'last_click_date'
  | 'last_open_date'
  | 'webinar'
  | 'clicked'
  | 'not_clicked'
  | 'sent'
  | 'not_sent'
  | 'geo'
  | 'gdpr'
  | 'score'
  | 'engagement_score'
  | 'tag'
  | 'goal'
  | 'crm'
  | 'ecommerce_number_of_purchases'
  | 'ecommerce_total_spent'
  | 'ecommerce_product_purchased'
  | 'ecommerce_brand_purchased'
  | 'ecommerce_abandoned_cart'
  | 'sms_sent'
  | 'sms_link_clicked'
  | 'sms_link_not_clicked'
  | 'custom_event';

/** It allows you to set a date range. For some of them `value` will be required. Examples can be found here: [API Docs](https://apidocs.getresponse.com/v3/case-study/segments-manual#not-opened-action). */
export type LinkNotClickedConditionDateOperator =
  | 'date_from'
  | 'never'
  | 'today'
  | 'yesterday'
  | 'last_7_days'
  | 'last_30_days'
  | 'last_n_days'
  | 'this_week'
  | 'this_month';

/** LinkNotClickedConditionOperatorType enum. */
export type LinkNotClickedConditionOperatorType = 'complex_message_operator';

/** The landing page status */
export type LpsDetailsStatus = 'published' | 'unpublished';

/** The landing page status */
export type LpsListItemStatus = 'published' | 'unpublished';

/** The status of a page associated with the landing page (i.e., 404 page or thank you page) */
export type LpsPageStatus = 'active' | 'inactive';

/** The landing page status */
export type LpsStatus = 'published' | 'unpublished';

/** MessageActivityReportActivityTypesEnum enum. */
export type MessageActivityReportActivityTypesEnum = 'click' | 'open' | 'send';

/** Indicates how the message was created: `custom` means a custom-made message, `text` means plain text content, `getresponse` means that the message was created using the GetResponse editor. */
export type MessageEditorEnum = 'custom' | 'text' | 'getresponse' | 'legacy' | 'html2';

/** MessageFlagsArrayItem enum. */
export type MessageFlagsArrayItem = 'openrate' | 'clicktrack' | 'google_analytics';

/** MessageNotSentConditionConditionType enum. */
export type MessageNotSentConditionConditionType =
  | 'name'
  | 'email'
  | 'custom'
  | 'subscription_date'
  | 'subscription_method'
  | 'opened'
  | 'not_opened'
  | 'phase'
  | 'last_send_date'
  | 'last_click_date'
  | 'last_open_date'
  | 'webinar'
  | 'clicked'
  | 'not_clicked'
  | 'sent'
  | 'not_sent'
  | 'geo'
  | 'gdpr'
  | 'score'
  | 'engagement_score'
  | 'tag'
  | 'goal'
  | 'crm'
  | 'ecommerce_number_of_purchases'
  | 'ecommerce_total_spent'
  | 'ecommerce_product_purchased'
  | 'ecommerce_brand_purchased'
  | 'ecommerce_abandoned_cart'
  | 'sms_sent'
  | 'sms_link_clicked'
  | 'sms_link_not_clicked'
  | 'custom_event';

/** MessageNotSentConditionOperatorType enum. */
export type MessageNotSentConditionOperatorType = 'message_operator';

/** MessageSentConditionConditionType enum. */
export type MessageSentConditionConditionType =
  | 'name'
  | 'email'
  | 'custom'
  | 'subscription_date'
  | 'subscription_method'
  | 'opened'
  | 'not_opened'
  | 'phase'
  | 'last_send_date'
  | 'last_click_date'
  | 'last_open_date'
  | 'webinar'
  | 'clicked'
  | 'not_clicked'
  | 'sent'
  | 'not_sent'
  | 'geo'
  | 'gdpr'
  | 'score'
  | 'engagement_score'
  | 'tag'
  | 'goal'
  | 'crm'
  | 'ecommerce_number_of_purchases'
  | 'ecommerce_total_spent'
  | 'ecommerce_product_purchased'
  | 'ecommerce_brand_purchased'
  | 'ecommerce_abandoned_cart'
  | 'sms_sent'
  | 'sms_link_clicked'
  | 'sms_link_not_clicked'
  | 'custom_event';

/** MessageSentConditionOperatorType enum. */
export type MessageSentConditionOperatorType = 'message_operator';

/** The type of message. */
export type MessageTypeOperator = 'autoresponder' | 'newsletter' | 'splittest' | 'automation';

/** The value type enumerable */
export type MetaFieldValueType = 'string' | 'integer';

/** NameConditionConditionType enum. */
export type NameConditionConditionType =
  | 'name'
  | 'email'
  | 'custom'
  | 'subscription_date'
  | 'subscription_method'
  | 'opened'
  | 'not_opened'
  | 'phase'
  | 'last_send_date'
  | 'last_click_date'
  | 'last_open_date'
  | 'webinar'
  | 'clicked'
  | 'not_clicked'
  | 'sent'
  | 'not_sent'
  | 'geo'
  | 'gdpr'
  | 'score'
  | 'engagement_score'
  | 'tag'
  | 'goal'
  | 'crm'
  | 'ecommerce_number_of_purchases'
  | 'ecommerce_total_spent'
  | 'ecommerce_product_purchased'
  | 'ecommerce_brand_purchased'
  | 'ecommerce_abandoned_cart'
  | 'sms_sent'
  | 'sms_link_clicked'
  | 'sms_link_not_clicked'
  | 'custom_event';

/** NameConditionOperator enum. */
export type NameConditionOperator =
  'is' | 'is_not' | 'contains' | 'not_contains' | 'starts' | 'ends' | 'not_starts' | 'not_ends';

/** NameConditionOperatorType enum. */
export type NameConditionOperatorType = 'string_operator';

/** Tracking options enabled for the newsletter */
export type NewAbtestsSubjectFlagsItem = 'clicktrack' | 'google_analytics' | 'ecommerce_tracking';

/** NewContactOrigin enum. */
export type NewContactOrigin =
  | 'import'
  | 'email'
  | 'www'
  | 'panel'
  | 'leads'
  | 'sale'
  | 'api'
  | 'survey'
  | 'iphone'
  | 'copy'
  | 'landing_page'
  | 'webinar'
  | 'website_builder_elegant'
  | 'chat'
  | 'course'
  | 'premium_newsletter';

/** Type of returning value, it returns `type` options extended by a `string` option if the `format` was not defined */
export type NewCustomFieldValueType =
  | 'string'
  | 'number'
  | 'date'
  | 'datetime'
  | 'country'
  | 'currency'
  | 'phone'
  | 'gender'
  | 'ip'
  | 'url';

/** How the message was created: `editor_v3` - created by GetResponse editor, `text` means plain text content, `html` means custom HTML content, `getresponse` is a deprecated, legacy GetResponse editor. */
export type NewMessageEditorEnumOutput = 'editor_v3' | 'getresponse' | 'text' | 'html';

/** The value type enumerable */
export type NewMetaFieldValueType = 'string' | 'integer';

/** The newsletter type */
export type NewNewsletterType = 'broadcast' | 'draft';

/** Match 'any' (`or` value) or 'all' (`and` value) of the following conditions */
export type NewSearchContactsSectionLogicOperator = 'or' | 'and';

/** NewSearchContactsSubscribersTypeItem enum. */
export type NewSearchContactsSubscribersTypeItem = 'subscribed';

/** The type of activity */
export type NewsletterActivityActivity = 'send' | 'open' | 'click';

/** The newsletter type */
export type NewsletterDetailsType = 'broadcast' | 'draft';

/** The newsletter type */
export type NewsletterListElementType = 'broadcast' | 'draft';

/** The newsletter type */
export type NewsletterType = 'broadcast' | 'draft';

/** NotOpenedConditionConditionType enum. */
export type NotOpenedConditionConditionType =
  | 'name'
  | 'email'
  | 'custom'
  | 'subscription_date'
  | 'subscription_method'
  | 'opened'
  | 'not_opened'
  | 'phase'
  | 'last_send_date'
  | 'last_click_date'
  | 'last_open_date'
  | 'webinar'
  | 'clicked'
  | 'not_clicked'
  | 'sent'
  | 'not_sent'
  | 'geo'
  | 'gdpr'
  | 'score'
  | 'engagement_score'
  | 'tag'
  | 'goal'
  | 'crm'
  | 'ecommerce_number_of_purchases'
  | 'ecommerce_total_spent'
  | 'ecommerce_product_purchased'
  | 'ecommerce_brand_purchased'
  | 'ecommerce_abandoned_cart'
  | 'sms_sent'
  | 'sms_link_clicked'
  | 'sms_link_not_clicked'
  | 'custom_event';

/** It allows you to set a date range. For some of them `value` will be required. Examples can be found here: [API Docs](https://apidocs.getresponse.com/v3/case-study/segments-manual#not-opened-action). */
export type NotOpenedConditionDateOperator =
  | 'date_from'
  | 'never'
  | 'today'
  | 'yesterday'
  | 'last_7_days'
  | 'last_30_days'
  | 'last_n_days'
  | 'this_week'
  | 'this_month';

/** NotOpenedConditionOperatorType enum. */
export type NotOpenedConditionOperatorType = 'complex_message_operator';

/** OpenedConditionConditionType enum. */
export type OpenedConditionConditionType =
  | 'name'
  | 'email'
  | 'custom'
  | 'subscription_date'
  | 'subscription_method'
  | 'opened'
  | 'not_opened'
  | 'phase'
  | 'last_send_date'
  | 'last_click_date'
  | 'last_open_date'
  | 'webinar'
  | 'clicked'
  | 'not_clicked'
  | 'sent'
  | 'not_sent'
  | 'geo'
  | 'gdpr'
  | 'score'
  | 'engagement_score'
  | 'tag'
  | 'goal'
  | 'crm'
  | 'ecommerce_number_of_purchases'
  | 'ecommerce_total_spent'
  | 'ecommerce_product_purchased'
  | 'ecommerce_brand_purchased'
  | 'ecommerce_abandoned_cart'
  | 'sms_sent'
  | 'sms_link_clicked'
  | 'sms_link_not_clicked'
  | 'custom_event';

/** OpenedConditionOperatorType enum. */
export type OpenedConditionOperatorType = 'message_operator';

/** The form or popup status */
export type PopupDetailsStatus = 'published' | 'unpublished';

/** The form or popup type */
export type PopupDetailsType = 'popup' | 'inline';

/** The form or popup status */
export type PopupListItemStatus = 'published' | 'unpublished';

/** The form or popup type */
export type PopupListItemType = 'popup' | 'inline';

/** The relational operators. */
export type RelationalNumericOperatorEnum =
  'numeric_lt' | 'numeric_gt' | 'numeric_eq' | 'numeric_not_eq' | 'numeric_lt_eq' | 'numeric_gt_eq';

/** The filter settings for an RSS post */
export type RssNewsletterListSendAsapSettingsFilter = 'recent' | 'engaged' | 'shared' | 'commented';

/** The filter settings for an RSS post */
export type RssNewsletterListSendDailySettingsFilter =
  'recent' | 'engaged' | 'shared' | 'commented';

/** The filter settings for an RSS post */
export type RssNewsletterListSendMonthlySettingsFilter =
  'recent' | 'engaged' | 'shared' | 'commented';

/** The filter settings for an RSS post */
export type RssNewsletterListSendWeeklySettingsFilter =
  'recent' | 'engaged' | 'shared' | 'commented';

/** The day of the week when the message should be sent */
export type RssNewsletterListSendWeeklySettingsSendAtWeekDay =
  'Monday' | 'Tuesday' | 'Wednesday' | 'Thursday' | 'Friday' | 'Saturday' | 'Sunday';

/** The filter settings for an RSS post */
export type RssNewsletterSendAsapSettingsFilter = 'recent' | 'engaged' | 'shared' | 'commented';

/** The filter settings for an RSS post */
export type RssNewsletterSendDailySettingsFilter = 'recent' | 'engaged' | 'shared' | 'commented';

/** The filter settings for an RSS post */
export type RssNewsletterSendMonthlySettingsFilter = 'recent' | 'engaged' | 'shared' | 'commented';

/** The filter settings for an RSS post */
export type RssNewsletterSendSettingsDetailsFilter = 'recent' | 'engaged' | 'shared' | 'commented';

/** The filter settings for an RSS post */
export type RssNewsletterSendSettingsListingFilter = 'recent' | 'engaged' | 'shared' | 'commented';

/** The filter settings for an RSS post */
export type RssNewsletterSendWeeklySettingsFilter = 'recent' | 'engaged' | 'shared' | 'commented';

/** The day of the week when the message should be sent */
export type RssNewsletterSendWeeklySettingsSendAtWeekDay =
  'Monday' | 'Tuesday' | 'Wednesday' | 'Thursday' | 'Friday' | 'Saturday' | 'Sunday';

/** ScoringConditionConditionType enum. */
export type ScoringConditionConditionType =
  | 'name'
  | 'email'
  | 'custom'
  | 'subscription_date'
  | 'subscription_method'
  | 'opened'
  | 'not_opened'
  | 'phase'
  | 'last_send_date'
  | 'last_click_date'
  | 'last_open_date'
  | 'webinar'
  | 'clicked'
  | 'not_clicked'
  | 'sent'
  | 'not_sent'
  | 'geo'
  | 'gdpr'
  | 'score'
  | 'engagement_score'
  | 'tag'
  | 'goal'
  | 'crm'
  | 'ecommerce_number_of_purchases'
  | 'ecommerce_total_spent'
  | 'ecommerce_product_purchased'
  | 'ecommerce_brand_purchased'
  | 'ecommerce_abandoned_cart'
  | 'sms_sent'
  | 'sms_link_clicked'
  | 'sms_link_not_clicked'
  | 'custom_event';

/** The relational operator. Required for the operatorType=numeric_operator. */
export type ScoringConditionOperator =
  'numeric_lt' | 'numeric_gt' | 'numeric_eq' | 'numeric_not_eq' | 'numeric_lt_eq' | 'numeric_gt_eq';

/** ScoringConditionOperatorType enum. */
export type ScoringConditionOperatorType = 'numeric_operator' | 'not_exists';

/** SearchContactSectionLogicOperator enum. */
export type SearchContactSectionLogicOperator = 'and' | 'or';

/** SearchContactSectionSubscriberCycleItem enum. */
export type SearchContactSectionSubscriberCycleItem =
  'receiving_autoresponder' | 'not_receiving_autoresponder';

/** Matches the matching period */
export type SearchContactSectionSubscriptionDate =
  | 'all_time'
  | 'today'
  | 'yesterday'
  | 'last_7_days'
  | 'last_30_days'
  | 'this_week'
  | 'last_week'
  | 'this_month'
  | 'last_month'
  | 'last_2_months'
  | 'custom';

/** Match 'any' (`or` value) or 'all' (`and` value) of the following conditions */
export type SearchContactsBySearchFormSectionLogicOperator = 'or' | 'and';

/** SearchContactsBySearchFormSubscribersTypeItem enum. */
export type SearchContactsBySearchFormSubscribersTypeItem =
  'subscribed' | 'undelivered' | 'removed' | 'unconfirmed';

/** Match 'any' (`or` value) or 'all' (`and` value) of the following conditions */
export type SearchContactsConditionsDetailsSectionLogicOperator = 'or' | 'and';

/** Match 'any' (`or` value) or 'all' (`and` value) of the following conditions */
export type SearchContactsDetailsSectionLogicOperator = 'or' | 'and';

/** SearchContactsDetailsSubscribersTypeItem enum. */
export type SearchContactsDetailsSubscribersTypeItem = 'subscribed';

/** SearchedContactDetailsOrigin enum. */
export type SearchedContactDetailsOrigin =
  | 'import'
  | 'email'
  | 'www'
  | 'panel'
  | 'leads'
  | 'sale'
  | 'api'
  | 'forward'
  | 'survey'
  | 'iphone'
  | 'copy'
  | 'landing_page'
  | 'webinar'
  | 'course'
  | 'premium_newsletter';

/** SearchedContactDetailsReason enum. */
export type SearchedContactDetailsReason =
  | 'api'
  | 'automation'
  | 'blacklisted'
  | 'bounce'
  | 'cleaner'
  | 'complaint'
  | 'support'
  | 'unsubscribe'
  | 'user';

/** SectionAllTimeSubscriptionDateLogicOperator enum. */
export type SectionAllTimeSubscriptionDateLogicOperator = 'and' | 'or';

/** SectionAllTimeSubscriptionDateSubscriberCycleItem enum. */
export type SectionAllTimeSubscriptionDateSubscriberCycleItem =
  'receiving_autoresponder' | 'not_receiving_autoresponder';

/** Matches the matching period */
export type SectionAllTimeSubscriptionDateSubscriptionDate =
  | 'all_time'
  | 'today'
  | 'yesterday'
  | 'last_7_days'
  | 'last_30_days'
  | 'this_week'
  | 'last_week'
  | 'this_month'
  | 'last_month'
  | 'last_2_months'
  | 'custom';

/** SectionCustomSubscriptionDateLogicOperator enum. */
export type SectionCustomSubscriptionDateLogicOperator = 'and' | 'or';

/** SectionCustomSubscriptionDateSubscriberCycleItem enum. */
export type SectionCustomSubscriptionDateSubscriberCycleItem =
  'receiving_autoresponder' | 'not_receiving_autoresponder';

/** Matches the matching period */
export type SectionCustomSubscriptionDateSubscriptionDate =
  | 'all_time'
  | 'today'
  | 'yesterday'
  | 'last_7_days'
  | 'last_30_days'
  | 'this_week'
  | 'last_week'
  | 'this_month'
  | 'last_month'
  | 'last_2_months'
  | 'custom';

/** SectionLast2MonthsSubscriptionDateLogicOperator enum. */
export type SectionLast2MonthsSubscriptionDateLogicOperator = 'and' | 'or';

/** SectionLast2MonthsSubscriptionDateSubscriberCycleItem enum. */
export type SectionLast2MonthsSubscriptionDateSubscriberCycleItem =
  'receiving_autoresponder' | 'not_receiving_autoresponder';

/** Matches the matching period */
export type SectionLast2MonthsSubscriptionDateSubscriptionDate =
  | 'all_time'
  | 'today'
  | 'yesterday'
  | 'last_7_days'
  | 'last_30_days'
  | 'this_week'
  | 'last_week'
  | 'this_month'
  | 'last_month'
  | 'last_2_months'
  | 'custom';

/** SectionLast30DaysSubscriptionDateLogicOperator enum. */
export type SectionLast30DaysSubscriptionDateLogicOperator = 'and' | 'or';

/** SectionLast30DaysSubscriptionDateSubscriberCycleItem enum. */
export type SectionLast30DaysSubscriptionDateSubscriberCycleItem =
  'receiving_autoresponder' | 'not_receiving_autoresponder';

/** Matches the matching period */
export type SectionLast30DaysSubscriptionDateSubscriptionDate =
  | 'all_time'
  | 'today'
  | 'yesterday'
  | 'last_7_days'
  | 'last_30_days'
  | 'this_week'
  | 'last_week'
  | 'this_month'
  | 'last_month'
  | 'last_2_months'
  | 'custom';

/** SectionLast7DaysSubscriptionDateLogicOperator enum. */
export type SectionLast7DaysSubscriptionDateLogicOperator = 'and' | 'or';

/** SectionLast7DaysSubscriptionDateSubscriberCycleItem enum. */
export type SectionLast7DaysSubscriptionDateSubscriberCycleItem =
  'receiving_autoresponder' | 'not_receiving_autoresponder';

/** Matches the matching period */
export type SectionLast7DaysSubscriptionDateSubscriptionDate =
  | 'all_time'
  | 'today'
  | 'yesterday'
  | 'last_7_days'
  | 'last_30_days'
  | 'this_week'
  | 'last_week'
  | 'this_month'
  | 'last_month'
  | 'last_2_months'
  | 'custom';

/** SectionLastMonthSubscriptionDateLogicOperator enum. */
export type SectionLastMonthSubscriptionDateLogicOperator = 'and' | 'or';

/** SectionLastMonthSubscriptionDateSubscriberCycleItem enum. */
export type SectionLastMonthSubscriptionDateSubscriberCycleItem =
  'receiving_autoresponder' | 'not_receiving_autoresponder';

/** Matches the matching period */
export type SectionLastMonthSubscriptionDateSubscriptionDate =
  | 'all_time'
  | 'today'
  | 'yesterday'
  | 'last_7_days'
  | 'last_30_days'
  | 'this_week'
  | 'last_week'
  | 'this_month'
  | 'last_month'
  | 'last_2_months'
  | 'custom';

/** SectionLastWeekSubscriptionDateLogicOperator enum. */
export type SectionLastWeekSubscriptionDateLogicOperator = 'and' | 'or';

/** SectionLastWeekSubscriptionDateSubscriberCycleItem enum. */
export type SectionLastWeekSubscriptionDateSubscriberCycleItem =
  'receiving_autoresponder' | 'not_receiving_autoresponder';

/** Matches the matching period */
export type SectionLastWeekSubscriptionDateSubscriptionDate =
  | 'all_time'
  | 'today'
  | 'yesterday'
  | 'last_7_days'
  | 'last_30_days'
  | 'this_week'
  | 'last_week'
  | 'this_month'
  | 'last_month'
  | 'last_2_months'
  | 'custom';

/** SectionThisMonthSubscriptionDateLogicOperator enum. */
export type SectionThisMonthSubscriptionDateLogicOperator = 'and' | 'or';

/** SectionThisMonthSubscriptionDateSubscriberCycleItem enum. */
export type SectionThisMonthSubscriptionDateSubscriberCycleItem =
  'receiving_autoresponder' | 'not_receiving_autoresponder';

/** Matches the matching period */
export type SectionThisMonthSubscriptionDateSubscriptionDate =
  | 'all_time'
  | 'today'
  | 'yesterday'
  | 'last_7_days'
  | 'last_30_days'
  | 'this_week'
  | 'last_week'
  | 'this_month'
  | 'last_month'
  | 'last_2_months'
  | 'custom';

/** SectionThisWeekSubscriptionDateLogicOperator enum. */
export type SectionThisWeekSubscriptionDateLogicOperator = 'and' | 'or';

/** SectionThisWeekSubscriptionDateSubscriberCycleItem enum. */
export type SectionThisWeekSubscriptionDateSubscriberCycleItem =
  'receiving_autoresponder' | 'not_receiving_autoresponder';

/** Matches the matching period */
export type SectionThisWeekSubscriptionDateSubscriptionDate =
  | 'all_time'
  | 'today'
  | 'yesterday'
  | 'last_7_days'
  | 'last_30_days'
  | 'this_week'
  | 'last_week'
  | 'this_month'
  | 'last_month'
  | 'last_2_months'
  | 'custom';

/** SectionTodaySubscriptionDateLogicOperator enum. */
export type SectionTodaySubscriptionDateLogicOperator = 'and' | 'or';

/** SectionTodaySubscriptionDateSubscriberCycleItem enum. */
export type SectionTodaySubscriptionDateSubscriberCycleItem =
  'receiving_autoresponder' | 'not_receiving_autoresponder';

/** Matches the matching period */
export type SectionTodaySubscriptionDateSubscriptionDate =
  | 'all_time'
  | 'today'
  | 'yesterday'
  | 'last_7_days'
  | 'last_30_days'
  | 'this_week'
  | 'last_week'
  | 'this_month'
  | 'last_month'
  | 'last_2_months'
  | 'custom';

/** SectionYesterdaySubscriptionDateLogicOperator enum. */
export type SectionYesterdaySubscriptionDateLogicOperator = 'and' | 'or';

/** SectionYesterdaySubscriptionDateSubscriberCycleItem enum. */
export type SectionYesterdaySubscriptionDateSubscriberCycleItem =
  'receiving_autoresponder' | 'not_receiving_autoresponder';

/** Matches the matching period */
export type SectionYesterdaySubscriptionDateSubscriptionDate =
  | 'all_time'
  | 'today'
  | 'yesterday'
  | 'last_7_days'
  | 'last_30_days'
  | 'this_week'
  | 'last_week'
  | 'this_month'
  | 'last_month'
  | 'last_2_months'
  | 'custom';

/** The recipient type. To send a text message to contacts in your list, select `contacts`. To message contacts who are not in any of your lists, select `importedNumbers` */
export type SendSmsToContactsRecipientsType = 'contacts' | 'importedNumbers';

/** The recipient type. To send a text message to contacts in your list, select `contacts`. To message contacts who are not in any of your lists, select `importedNumbers` */
export type SendSmsToImportedNumbersRecipientsType = 'contacts' | 'importedNumbers';

/** The status of of the automated SMS message */
export type SmsAutomationDetailsStatus = 'ready' | 'in_use';

/** The status of of the automated SMS message */
export type SmsAutomationListItemStatus = 'ready' | 'in_use';

/** Type of SMS message recipients */
export type SmsDetailsRecipientsType = 'contacts' | 'importedNumbers';

/** The SMS message type */
export type SmsDetailsType = 'sms' | 'draft';

/** SmsLinkClickedConditionConditionType enum. */
export type SmsLinkClickedConditionConditionType =
  | 'name'
  | 'email'
  | 'custom'
  | 'subscription_date'
  | 'subscription_method'
  | 'opened'
  | 'not_opened'
  | 'phase'
  | 'last_send_date'
  | 'last_click_date'
  | 'last_open_date'
  | 'webinar'
  | 'clicked'
  | 'not_clicked'
  | 'sent'
  | 'not_sent'
  | 'geo'
  | 'gdpr'
  | 'score'
  | 'engagement_score'
  | 'tag'
  | 'goal'
  | 'crm'
  | 'ecommerce_number_of_purchases'
  | 'ecommerce_total_spent'
  | 'ecommerce_product_purchased'
  | 'ecommerce_brand_purchased'
  | 'ecommerce_abandoned_cart'
  | 'sms_sent'
  | 'sms_link_clicked'
  | 'sms_link_not_clicked'
  | 'custom_event';

/** SmsLinkNotClickedConditionConditionType enum. */
export type SmsLinkNotClickedConditionConditionType =
  | 'name'
  | 'email'
  | 'custom'
  | 'subscription_date'
  | 'subscription_method'
  | 'opened'
  | 'not_opened'
  | 'phase'
  | 'last_send_date'
  | 'last_click_date'
  | 'last_open_date'
  | 'webinar'
  | 'clicked'
  | 'not_clicked'
  | 'sent'
  | 'not_sent'
  | 'geo'
  | 'gdpr'
  | 'score'
  | 'engagement_score'
  | 'tag'
  | 'goal'
  | 'crm'
  | 'ecommerce_number_of_purchases'
  | 'ecommerce_total_spent'
  | 'ecommerce_product_purchased'
  | 'ecommerce_brand_purchased'
  | 'ecommerce_abandoned_cart'
  | 'sms_sent'
  | 'sms_link_clicked'
  | 'sms_link_not_clicked'
  | 'custom_event';

/** Type of SMS message recipients */
export type SmsListItemRecipientsType = 'contacts' | 'importedNumbers';

/** The SMS message type */
export type SmsListItemType = 'sms' | 'draft';

/** SmsSenderNameStatusesEnum enum. */
export type SmsSenderNameStatusesEnum = 'pending' | 'active' | 'rejected';

/** SmsSentConditionConditionType enum. */
export type SmsSentConditionConditionType =
  | 'name'
  | 'email'
  | 'custom'
  | 'subscription_date'
  | 'subscription_method'
  | 'opened'
  | 'not_opened'
  | 'phase'
  | 'last_send_date'
  | 'last_click_date'
  | 'last_open_date'
  | 'webinar'
  | 'clicked'
  | 'not_clicked'
  | 'sent'
  | 'not_sent'
  | 'geo'
  | 'gdpr'
  | 'score'
  | 'engagement_score'
  | 'tag'
  | 'goal'
  | 'crm'
  | 'ecommerce_number_of_purchases'
  | 'ecommerce_total_spent'
  | 'ecommerce_product_purchased'
  | 'ecommerce_brand_purchased'
  | 'ecommerce_abandoned_cart'
  | 'sms_sent'
  | 'sms_link_clicked'
  | 'sms_link_not_clicked'
  | 'custom_event';

/** Specify the delivery status. Omit this field if the delivery status is not relevant. */
export type SmsSentConditionDeliveryStatus = 'delivered' | 'undelivered' | 'any';

/** SortOrderEnum enum. */
export type SortOrderEnum = 'ASC' | 'DESC';

/** The specific date. */
export type SpecificDateEnum =
  | 'today'
  | 'yesterday'
  | 'last_7_days'
  | 'last_30_days'
  | 'last_n_days'
  | 'this_week'
  | 'last_week'
  | 'this_month'
  | 'last_month';

/** The method of choosing the winning A/B test */
export type SplittestChooseWinning = 'automatic' | 'manual';

/** The status of the newsletter */
export type SplittestNewsletterStatus = 'sampled' | 'chosen' | 'rejected';

/** A/B test stage */
export type SplittestStage =
  | 'queued'
  | 'schedule_sampling'
  | 'evaluate_sampling'
  | 'choose_winning'
  | 'schedule_winning'
  | 'send_winning'
  | 'canceled_queued'
  | 'canceled_sampling'
  | 'canceled_winning'
  | 'incomplete'
  | 'finished';

/** A/B test status */
export type SplittestStatus = 'active' | 'inactive';

/** A/B test type */
export type SplittestType = 'content' | 'subject' | 'day' | 'hour' | 'from_field';

/** A/B test winning criteria */
export type SplittestWinningCriteria = 'open' | 'click';

/** StatusEnum enum. */
export type StatusEnum = 'enabled' | 'disabled';

/** StringBooleanEnum enum. */
export type StringBooleanEnum = 'true' | 'false';

/** SubscribersTypeEnumForSearchingSubscribersTypeItem enum. */
export type SubscribersTypeEnumForSearchingSubscribersTypeItem =
  'subscribed' | 'undelivered' | 'removed' | 'unconfirmed';

/** SubscribersTypeEnumForSegmentsSubscribersTypeItem enum. */
export type SubscribersTypeEnumForSegmentsSubscribersTypeItem = 'subscribed';

/** SubscriptionDateConditionConditionType enum. */
export type SubscriptionDateConditionConditionType =
  | 'name'
  | 'email'
  | 'custom'
  | 'subscription_date'
  | 'subscription_method'
  | 'opened'
  | 'not_opened'
  | 'phase'
  | 'last_send_date'
  | 'last_click_date'
  | 'last_open_date'
  | 'webinar'
  | 'clicked'
  | 'not_clicked'
  | 'sent'
  | 'not_sent'
  | 'geo'
  | 'gdpr'
  | 'score'
  | 'engagement_score'
  | 'tag'
  | 'goal'
  | 'crm'
  | 'ecommerce_number_of_purchases'
  | 'ecommerce_total_spent'
  | 'ecommerce_product_purchased'
  | 'ecommerce_brand_purchased'
  | 'ecommerce_abandoned_cart'
  | 'sms_sent'
  | 'sms_link_clicked'
  | 'sms_link_not_clicked'
  | 'custom_event';

/** SubscriptionDateConditionOperator enum. */
export type SubscriptionDateConditionOperator =
  'date_to' | 'date_from' | 'specific_date' | 'custom';

/** SubscriptionDateConditionOperatorType enum. */
export type SubscriptionDateConditionOperatorType = 'date_operator';

/** SubscriptionMethodConditionConditionType enum. */
export type SubscriptionMethodConditionConditionType =
  | 'name'
  | 'email'
  | 'custom'
  | 'subscription_date'
  | 'subscription_method'
  | 'opened'
  | 'not_opened'
  | 'phase'
  | 'last_send_date'
  | 'last_click_date'
  | 'last_open_date'
  | 'webinar'
  | 'clicked'
  | 'not_clicked'
  | 'sent'
  | 'not_sent'
  | 'geo'
  | 'gdpr'
  | 'score'
  | 'engagement_score'
  | 'tag'
  | 'goal'
  | 'crm'
  | 'ecommerce_number_of_purchases'
  | 'ecommerce_total_spent'
  | 'ecommerce_product_purchased'
  | 'ecommerce_brand_purchased'
  | 'ecommerce_abandoned_cart'
  | 'sms_sent'
  | 'sms_link_clicked'
  | 'sms_link_not_clicked'
  | 'custom_event';

/** SubscriptionMethodConditionMethod enum. */
export type SubscriptionMethodConditionMethod =
  | 'webform'
  | 'import'
  | 'landing_page'
  | 'api'
  | 'email'
  | 'panel'
  | 'mobile'
  | 'survey'
  | 'sales'
  | 'copy'
  | 'leads'
  | 'webinar'
  | 'chat'
  | 'website_builder_elegant'
  | 'course'
  | 'premium_newsletter';

/** The property required for the webform subscription method. If it equals webforms, webformsv2 or popups, additonal property value is needed. */
export type SubscriptionMethodConditionWebformType = 'all' | 'webforms' | 'webformsv2' | 'popups';

/** TagConditionConditionType enum. */
export type TagConditionConditionType =
  | 'name'
  | 'email'
  | 'custom'
  | 'subscription_date'
  | 'subscription_method'
  | 'opened'
  | 'not_opened'
  | 'phase'
  | 'last_send_date'
  | 'last_click_date'
  | 'last_open_date'
  | 'webinar'
  | 'clicked'
  | 'not_clicked'
  | 'sent'
  | 'not_sent'
  | 'geo'
  | 'gdpr'
  | 'score'
  | 'engagement_score'
  | 'tag'
  | 'goal'
  | 'crm'
  | 'ecommerce_number_of_purchases'
  | 'ecommerce_total_spent'
  | 'ecommerce_product_purchased'
  | 'ecommerce_brand_purchased'
  | 'ecommerce_abandoned_cart'
  | 'sms_sent'
  | 'sms_link_clicked'
  | 'sms_link_not_clicked'
  | 'custom_event';

/** This operator verifies whether the property you are looking for exists or not */
export type TagConditionOperator = 'exists' | 'not_exists';

/** The operator for the existence of a property */
export type TagConditionOperatorType = 'exists';

/** The message content type */
export type TemplateContentContentType = 'direct' | 'template';

/** TransactionalEmailRecipientDetailsStatus enum. */
export type TransactionalEmailRecipientDetailsStatus =
  'unknown' | 'sent' | 'rejected' | 'opened' | 'bounced' | 'reported_spam';

/** TransactionalEmailRecipientStatus enum. */
export type TransactionalEmailRecipientStatus =
  'unknown' | 'sent' | 'rejected' | 'opened' | 'bounced' | 'reported_spam';

/** TransactionalEmailRecipientToStatus enum. */
export type TransactionalEmailRecipientToStatus =
  'unknown' | 'sent' | 'rejected' | 'opened' | 'bounced' | 'reported_spam';

/** UpdateAccountBlocklistAdditionalFlags enum. */
export type UpdateAccountBlocklistAdditionalFlags = 'add' | 'delete' | 'noResponse';

/** Numbers of employees */
export type UpdateAccountNumberOfEmployees = '50' | '250' | '500' | 'more';

/** Account time notation */
export type UpdateAccountTimeFormat = '12h' | '24h';

/** UpdateCampaignBlocklistAdditionalFlags enum. */
export type UpdateCampaignBlocklistAdditionalFlags = 'add' | 'delete' | 'noResponse';

/** UpdateContactOrigin enum. */
export type UpdateContactOrigin =
  | 'import'
  | 'email'
  | 'www'
  | 'panel'
  | 'leads'
  | 'sale'
  | 'api'
  | 'survey'
  | 'iphone'
  | 'copy'
  | 'landing_page'
  | 'webinar'
  | 'website_builder_elegant'
  | 'chat'
  | 'course'
  | 'premium_newsletter';

/** The value type enumerable */
export type UpdateMetaFieldValueType = 'string' | 'integer';

/** Match 'any' (`or` value) or 'all' (`and` value) of the following conditions */
export type UpdateSearchContactsSectionLogicOperator = 'or' | 'and';

/** UpdateSearchContactsSubscribersTypeItem enum. */
export type UpdateSearchContactsSubscribersTypeItem = 'subscribed';

/** An 'incomplete' status means that the workflow is a 'draft' in the web panel */
export type UpdateWorkflowStatus = 'active' | 'inactive' | 'incomplete';

/** WebinarConditionConditionType enum. */
export type WebinarConditionConditionType =
  | 'name'
  | 'email'
  | 'custom'
  | 'subscription_date'
  | 'subscription_method'
  | 'opened'
  | 'not_opened'
  | 'phase'
  | 'last_send_date'
  | 'last_click_date'
  | 'last_open_date'
  | 'webinar'
  | 'clicked'
  | 'not_clicked'
  | 'sent'
  | 'not_sent'
  | 'geo'
  | 'gdpr'
  | 'score'
  | 'engagement_score'
  | 'tag'
  | 'goal'
  | 'crm'
  | 'ecommerce_number_of_purchases'
  | 'ecommerce_total_spent'
  | 'ecommerce_product_purchased'
  | 'ecommerce_brand_purchased'
  | 'ecommerce_abandoned_cart'
  | 'sms_sent'
  | 'sms_link_clicked'
  | 'sms_link_not_clicked'
  | 'custom_event';

/** WebinarConditionContactType enum. */
export type WebinarConditionContactType = 'host' | 'listener' | 'presenter' | 'registrant' | 'all';

/** WebinarConditionWebinarCondition enum. */
export type WebinarConditionWebinarCondition = 'participated' | 'not_participated';

/** WebinarStatus enum. */
export type WebinarStatus = 'upcoming' | 'finished' | 'published' | 'unpublished';

/** The webinar type */
export type WebinarType = 'all' | 'live' | 'on_demand';

/** The website status */
export type WebsiteDetailsStatus = 'published' | 'unpublished';

/** The website page status */
export type WebsitePageStatus = 'active' | 'inactive';

/** The website status */
export type WebsiteStatus = 'published' | 'unpublished';

/** WorkflowStatus enum. */
export type WorkflowStatus = 'active' | 'inactive' | 'incomplete';

/** AbtestsSubject model. */
export interface AbtestsSubject {
  /** A/B test ID */
  abTestId?: string;
  /** A/B test name */
  name?: string;
  /** List linked to A/B test */
  campaign?: Record<string, unknown>;
  /** Newsletter's From" address" */
  fromField?: Record<string, unknown>;
  /** Newsletter's reply-to address */
  replyTo?: Record<string, unknown>;
}

/** AbtestsSubjectDetails model. */
export interface AbtestsSubjectDetails {
  /** A/B test ID */
  abTestId?: string;
  /** A/B test name */
  name?: string;
  /** List linked to A/B test */
  campaign?: Record<string, unknown>;
  /** Newsletter's From" address" */
  fromField?: Record<string, unknown>;
  /** Newsletter's reply-to address */
  replyTo?: Record<string, unknown>;
  /** Newsletter status */
  status?: AbtestsSubjectDetailsStatus;
  /** A/B test stage */
  stage?: AbtestsSubjectDetailsStage;
  /** The A/B test delivery settings */
  deliverySettings?: Record<string, unknown>;
  flags?: AbtestsSubjectDetailsFlagsItem[];
  /** Date the A/B test was created on (ISO 8601 date-time string) */
  createdOn?: string;
  /** Date A/B test was updated on (ISO 8601 date-time string) */
  updatedOn?: string;
  /** Direct hyperlink to a resource */
  href?: string;
  /** Date the winning message was sent on (ISO 8601 date-time string) */
  winnerSendingStart?: string;
  /** The statistics of A/B test */
  statistics?: Record<string, unknown>;
  variants?: Record<string, unknown>[];
  /** The send settings for the A/B test */
  sendSettings?: Record<string, unknown>;
  /** The message editor used for the A/B test */
  editor?: AbtestsSubjectDetailsEditor;
  content?: MessageContent;
}

/** AbtestsSubjectListItem model. */
export interface AbtestsSubjectListItem {
  /** A/B test ID */
  abTestId?: string;
  /** A/B test name */
  name?: string;
  /** List linked to A/B test */
  campaign?: Record<string, unknown>;
  /** Newsletter's From" address" */
  fromField?: Record<string, unknown>;
  /** Newsletter's reply-to address */
  replyTo?: Record<string, unknown>;
  /** Newsletter status */
  status?: AbtestsSubjectListItemStatus;
  /** A/B test stage */
  stage?: AbtestsSubjectListItemStage;
  /** The A/B test delivery settings */
  deliverySettings?: Record<string, unknown>;
  flags?: AbtestsSubjectListItemFlagsItem[];
  /** Date the A/B test was created on (ISO 8601 date-time string) */
  createdOn?: string;
  /** Date A/B test was updated on (ISO 8601 date-time string) */
  updatedOn?: string;
  /** Direct hyperlink to a resource */
  href?: string;
}

/** AbtestsSubjectStatistics model. */
export interface AbtestsSubjectStatistics {
  /** The total number of delivered messages */
  delivered?: number;
  /** Percentage of messages that were opened */
  openRate?: number;
  /** Percentage of messages links that were clicked */
  clickRate?: number;
}

/** Account model. */
export interface Account {
  /** Account ID */
  accountId?: string;
  /** Email */
  email?: string;
  countryCode?: unknown;
  industryTag?: unknown;
  timeZone?: unknown;
  /** Direct URL to resource */
  href?: string;
  /** First name */
  firstName?: string;
  /** Last name */
  lastName?: string;
  /** Company name */
  companyName?: string;
  /** Phone number */
  phone?: string;
  /** State */
  state?: string;
  /** City */
  city?: string;
  /** Street */
  street?: string;
  /** ZIP Code */
  zipCode?: string;
  /** Numbers of employees */
  numberOfEmployees?: AccountNumberOfEmployees;
  /** Account time notation */
  timeFormat?: AccountTimeFormat;
}

/** AccountBadgeDetails model. */
export interface AccountBadgeDetails {
  /** Current badge status */
  status?: StatusEnum;
}

/** AccountBilling model. */
export interface AccountBilling {
  /** Billing plan maximum list size */
  listSize?: string;
  /** Payment plan */
  paymentPlan?: AccountBillingPaymentPlan;
  /** Subscription price */
  subscriptionPrice?: number;
  /** Subscription reneval date (ISO 8601 date-time string) */
  renewalDate?: string;
  /** Currency code compliant with ISO-4217 */
  currencyCode?: string;
  /** Account balance */
  accountBalance?: string;
  /** Price */
  price?: number;
  /** Payment method */
  paymentMethod?: AccountBillingPaymentMethod;
  creditCard?: Record<string, unknown>;
  /** Addons */
  addons?: Record<string, unknown>[];
}

/** AccountDetailsCountryCode model. */
export interface AccountDetailsCountryCode {
  /** Country code ID */
  countryCodeId?: string;
  /** Country code */
  countryCode?: string;
}

/** AccountSummaryReportDetails model. */
export interface AccountSummaryReportDetails {
  /** The custom report ID */
  customReportId?: string;
  /** The custom report name */
  name?: string;
  /** The direct hyperlink to a resource */
  href?: string;
  /** The custom report type */
  type?: unknown;
  /** Parameters responsible for defining the reporting period */
  scheduling?: Record<string, unknown>;
  /** Files that have been generated for the given report */
  files?: Record<string, unknown>[];
  /** Custom report creation date (ISO 8601 date-time string) */
  createdAt?: string;
  /** Custom report generation date (ISO 8601 date-time string) */
  generatedAt?: string;
  /** Filters used to narrow down the report data */
  filters?: Record<string, unknown>;
}

/** AccountsLoginHistoryListElement model. */
export interface AccountsLoginHistoryListElement {
  /** Login time (ISO 8601 date-time string) */
  loginTime?: string;
  /** Logout time (ISO 8601 date-time string) */
  logoutTime?: string;
  /** Login was successful */
  isSuccessful?: unknown;
  /** IP address */
  ip?: string;
}

/** Address model. */
export interface Address {
  /** The creation date (ISO 8601 date-time string) */
  createdOn?: string;
  /** The date of the last update (ISO 8601 date-time string) */
  updatedOn?: string;
  addressId?: string;
  /** Direct hyperlink to a resource */
  href?: string;
  /** The country code (ISO 3166-1 alpha-3) */
  countryCode?: string;
  /** The country name, based on `countryCode` */
  countryName?: string;
  name?: string;
  firstName?: string;
  lastName?: string;
  /** Address line 1 */
  address1?: string;
  /** Address line 2 */
  address2?: string;
  city?: string;
  /** The ZIP/postal code, free text */
  zip?: string;
  province?: string;
  /** The province code, free text */
  provinceCode?: string;
  /** The phone number, free text */
  phone?: string;
  /** The company name, free text */
  company?: string;
}

/** Autoresponder model. */
export interface Autoresponder {
  /** The autoresponder ID */
  autoresponderId?: string;
  /** Direct hyperlink to a resource */
  href?: string;
  /** The autoresponder name */
  name?: string;
  /** The autoresponder message subject */
  subject?: string;
  /** The campaign ID. The system will assign the autoresponder to a default campaign if you don't provide a specific campaign ID. */
  campaignId?: string;
  /** The autoresponder status */
  status?: unknown;
  /** The from email address used for the message */
  fromField?: unknown;
  /** The email that will be used as a reply-to address */
  replyTo?: unknown;
  content?: MessageContent;
  flags?: MessageFlagsArrayItem[];
  /** The conditions that will trigger the autoresponder */
  triggerSettings?: unknown;
  /** The autoresponder statistics summary */
  statistics?: Record<string, unknown>;
  /** The creation date (ISO 8601 date-time string) */
  createdOn?: string;
}

/** To find the autoresponder cycle day of a contact. */
export interface AutoresponderDayCondition {
  conditionType: AutoresponderDayConditionConditionType;
  operatorType: AutoresponderDayConditionOperatorType;
  operator: Record<string, unknown>;
  /** The autoresponder cycle day value. The field is prohibited for the operators assigned and not_assigned. */
  value?: number;
}

/** AutoresponderDetails model. */
export interface AutoresponderDetails {
  /** The autoresponder ID */
  autoresponderId?: string;
  /** Direct hyperlink to a resource */
  href?: string;
  /** The autoresponder name */
  name?: string;
  /** The autoresponder message subject */
  subject?: string;
  /** The campaign ID. The system will assign the autoresponder to a default campaign if you don't provide a specific campaign ID. */
  campaignId?: string;
  /** The autoresponder status */
  status?: unknown;
  /** The from email address used for the message */
  fromField?: unknown;
  /** The email that will be used as a reply-to address */
  replyTo?: unknown;
  content?: MessageContent;
  flags?: MessageFlagsArrayItem[];
  /** The conditions that will trigger the autoresponder */
  triggerSettings?: unknown;
  /** The autoresponder statistics summary */
  statistics?: Record<string, unknown>;
  /** The creation date (ISO 8601 date-time string) */
  createdOn?: string;
  /** The list of tracked links */
  clickTracks?: ClickTrack[];
  /** The autoresponder campaign (list) */
  campaign?: unknown;
  editor?: unknown;
  sendSettings?: Record<string, unknown>;
}

/** AutoresponderSendCustomSettings model. */
export interface AutoresponderSendCustomSettings {
  type: AutoresponderSendSettingsType;
  timeTravel?: string;
  excludedDaysOfWeek?: AutoresponderSendSettingsExcludedDaysOfWeekItem[];
  externalLexpad?: ExternalLexpad;
  sendAtHour: number;
}

/** AutoresponderSendDelaySettings model. */
export interface AutoresponderSendDelaySettings {
  type: AutoresponderSendSettingsType;
  timeTravel?: string;
  excludedDaysOfWeek?: AutoresponderSendSettingsExcludedDaysOfWeekItem[];
  externalLexpad?: ExternalLexpad;
  delayInHours: number;
}

/** AutoresponderSendImmediatelySettings model. */
export interface AutoresponderSendImmediatelySettings {
  type: AutoresponderSendSettingsType;
  timeTravel?: string;
  excludedDaysOfWeek?: AutoresponderSendSettingsExcludedDaysOfWeekItem[];
  externalLexpad?: ExternalLexpad;
}

/** How the message will be delivered to the subscriber */
export interface AutoresponderSendSettingsInput {
  type: AutoresponderSendSettingsType;
  timeTravel?: string;
  excludedDaysOfWeek?: AutoresponderSendSettingsExcludedDaysOfWeekItem[];
  externalLexpad?: ExternalLexpad;
}

/** How the message will be delivered to the subscriber */
export interface AutoresponderSendSettingsOutput {
  type?: AutoresponderSendSettingsType;
  timeTravel?: string;
  excludedDaysOfWeek?: AutoresponderSendSettingsExcludedDaysOfWeekItem[];
  delayInHours?: number;
  sendAtHour?: number;
  recurrence?: unknown;
}

/** AutoresponderSendSignupSettings model. */
export interface AutoresponderSendSignupSettings {
  type: AutoresponderSendSettingsType;
  timeTravel?: string;
  excludedDaysOfWeek?: AutoresponderSendSettingsExcludedDaysOfWeekItem[];
  externalLexpad?: ExternalLexpad;
}

/** The conditions that will trigger the autoresponder */
export interface AutoresponderTriggerSettings {
  /** The trigger type */
  type?: string;
  /** For onday type the day of the autoresponder cycle in the 0-9999 format */
  dayOfCycle?: number;
  autoresponder?: string;
  newsletter?: string;
  clickTrackId?: string;
  goal?: string;
  custom?: string;
  newCustomValue?: string;
  action?: string;
  selectedCampaigns?: unknown;
  selectedSegments?: unknown;
}

/** BaseCampaign model. */
export interface BaseCampaign {
  /** Unique identifier of the campaign (contact list) */
  campaignId?: string;
  /** The campaign (list) name. * You can use each list name just once in your account. * The name must be between 3-64 characters. * All alphabets supported by GetResponse, including right-to-left ones, are allowed. * You can use upper and lower case letters, numbers, spaces and special characters apart from the ones listed below. * You can’t use emojis and the following special characters: `/`, `\`, `@`, and `[` or `]`. */
  name?: string;
  /** Tech name is a unique internal ID of a list used for [FTP imports](https://www.getresponse.com/help/how-to-import-files-via-ftp.html) (available in GetResponse MAX accounts only) */
  techName?: string;
  /** The campaign language code according to ISO 639-1, plus: zt - Chinese (Traditional), fs - Afghan Persian (Dari), md - Moldavian */
  languageCode?: string;
  /** Is the campaign default */
  isDefault?: unknown;
  /** The date of creation (ISO 8601 date-time string) */
  createdOn?: string;
  /** Direct hyperlink to a resource */
  href?: string;
}

/** BaseCategory model. */
export interface BaseCategory {
  /** The category ID */
  categoryId?: string;
  /** Direct hyperlink to a resource */
  href?: string;
  /** The name of the category */
  name?: string;
  /** The parent category ID */
  parentId?: string;
  /** This is a default category */
  isDefault?: boolean;
  /** The external URL to the category */
  url?: string;
  /** The external ID is the identifying string or number of the category given by another software */
  externalId?: string;
}

/** BaseCreateCustomReport model. */
export interface BaseCreateCustomReport {
  /** The custom report name */
  name: string;
  /** The custom report type */
  type: BaseCreateCustomReportType;
  /** Parameters responsible for defining the reporting period */
  scheduling: Record<string, unknown>;
}

/** BaseFile model. */
export interface BaseFile {
  /** The file name */
  name?: string;
  /** The file extension */
  extension?: string;
  /** The folder where the file is stored */
  folder?: Record<string, unknown>;
}

/** BaseLandingPage model. */
export interface BaseLandingPage {
  /** The landing page ID */
  landingPageId?: string;
  /** Direct hyperlink to a resource */
  href?: string;
  /** The landing page meta title property */
  metaTitle?: string;
  /** The domain where the landing page is hosted */
  domain?: string;
  /** The subdomain where the landing page is assigned */
  subdomain?: string;
  /** The private domain provided by the user */
  userDomain?: string;
  /** The private domain path provided by the user */
  userDomainPath?: string;
  /** The campaign to which the landing page is linked */
  campaign?: unknown;
  /** The landing page status */
  status?: unknown;
  /** The DNS status for the user's private domain. Can be `null` if a private domain isn't assigned. */
  userDomainStatus?: BaseLandingPageUserDomainStatus;
  /** Does the landing page have AB testing (variants) enabled */
  testAB?: unknown;
  /** The creation date (ISO 8601 date-time string) */
  createdOn?: string;
  /** The date of the last page update (ISO 8601 date-time string) */
  updatedOn?: string;
}

/** BaseMetaField model. */
export interface BaseMetaField {
  /** Direct hyperlink to a resource */
  href?: string;
  /** The meta field ID */
  metaFieldId?: string;
  /** The meta field name */
  name?: string;
  /** The meta field value */
  value?: string;
  /** The value type enumerable */
  valueType?: BaseMetaFieldValueType;
  /** The meta field description */
  description?: string;
}

/** BaseProductVariant model. */
export interface BaseProductVariant {
  /** The product ID */
  variantId?: string;
  /** Direct hyperlink to a resource */
  href?: string;
  /** The product name */
  name?: string;
  /** The external URL to the product variant */
  url?: string;
  /** The stock-keeping unit of a variant. Must be unique within the product */
  sku?: string;
  /** The price */
  price?: number;
  /** The price including tax */
  priceTax?: number;
  /** The price before the change */
  previousPrice?: number;
  /** The price before the change including tax */
  previousPriceTax?: number;
  /** The quantity of variant items */
  quantity?: number;
  /** The position of a variant */
  position?: number;
  /** The barcode of a variant */
  barcode?: string;
  /** The external ID is the identifying string or number of the variant given by another software */
  externalId?: string;
  /** The description of a variant */
  description?: string;
  images?: NewProductVariantImage[];
  metaFields?: NewMetaField[];
  taxes?: NewTax[];
}

/** The short description of a saved search. */
export interface BaseSearchContacts {
  /** The unique search-contact identifier */
  searchContactId?: string;
  /** The unique name of search-contact */
  name?: string;
  /** The UTC date time format ISO 8601, e.g. 2018-04-10T10:02:57+0000 (ISO 8601 date-time string) */
  createdOn?: string;
  /** Direct hyperlink to a resource */
  href?: string;
}

/** BaseSearchContactsDetails model. */
export interface BaseSearchContactsDetails {
  /** The unique search-contact identifier */
  searchContactId: string;
  /** The unique name of search-contact */
  name?: string;
  /** The UTC date time format ISO 8601, e.g. 2018-04-10T10:02:57+0000 (ISO 8601 date-time string) */
  createdOn?: string;
  /** Direct hyperlink to a resource */
  href?: string;
}

/** BaseSendSms model. */
export interface BaseSendSms {
  /** The SMS message name */
  name: string;
  /** The SMS message content */
  content: string;
  /** The recipient type. To send a text message to contacts in your list, select `contacts`. To message contacts who are not in any of your lists, select `importedNumbers` */
  recipientsType: BaseSendSmsRecipientsType;
}

/** BaseSuppression model. */
export interface BaseSuppression {
  /** The name of the suppression list */
  name?: string;
  masks?: string[];
}

/** BaseTag model. */
export interface BaseTag {
  /** The tag name */
  name?: string;
  /** The tag color (deprecated) */
  color?: string;
}

/** BaseTax model. */
export interface BaseTax {
  /** The tax ID */
  taxId?: string;
  /** Direct hyperlink to a resource */
  href?: string;
  /** The tax name */
  name?: string;
  /** The rate value */
  rate?: number;
}

/** Blocklist model. */
export interface Blocklist {
  masks?: string[];
}

/** BouncesReportDetails model. */
export interface BouncesReportDetails {
  /** The custom report ID */
  customReportId?: string;
  /** The custom report name */
  name?: string;
  /** The direct hyperlink to a resource */
  href?: string;
  /** The custom report type */
  type?: unknown;
  /** Parameters responsible for defining the reporting period */
  scheduling?: Record<string, unknown>;
  /** Files that have been generated for the given report */
  files?: Record<string, unknown>[];
  /** Custom report creation date (ISO 8601 date-time string) */
  createdAt?: string;
  /** Custom report generation date (ISO 8601 date-time string) */
  generatedAt?: string;
  /** Filters used to narrow down the report data */
  filters?: Record<string, unknown>;
}

/** Callback model. */
export interface Callback {
  /** URL to use to post notifications */
  url?: unknown;
  actions?: CallbackActions;
}

/** CallbackActions model. */
export interface CallbackActions {
  /** Is `open` callback enabled */
  open?: boolean;
  /** Is `click` callback enabled */
  click?: boolean;
  /** Is `subscribe` callback enabled */
  subscribe?: boolean;
  /** Is `unsubscribe` callback enabled */
  unsubscribe?: boolean;
  /** Is `survey` callback enabled */
  survey?: boolean;
}

/** Campaign model. */
export interface Campaign {
  /** Unique identifier of the campaign (contact list) */
  campaignId?: string;
  /** The campaign (list) name. * You can use each list name just once in your account. * The name must be between 3-64 characters. * All alphabets supported by GetResponse, including right-to-left ones, are allowed. * You can use upper and lower case letters, numbers, spaces and special characters apart from the ones listed below. * You can’t use emojis and the following special characters: `/`, `\`, `@`, and `[` or `]`. */
  name: string;
  /** Tech name is a unique internal ID of a list used for [FTP imports](https://www.getresponse.com/help/how-to-import-files-via-ftp.html) (available in GetResponse MAX accounts only) */
  techName?: string;
  /** The campaign language code according to ISO 639-1, plus: zt - Chinese (Traditional), fs - Afghan Persian (Dari), md - Moldavian */
  languageCode?: string;
  /** Is the campaign default */
  isDefault?: unknown;
  /** The date of creation (ISO 8601 date-time string) */
  createdOn?: string;
  /** Direct hyperlink to a resource */
  href?: string;
  postal?: CampaignPostal;
  confirmation?: CampaignConfirmation;
  optinTypes?: CampaignOptinTypes;
  subscriptionNotifications?: CampaignSubscriptionNotifications;
  profile?: CampaignProfile;
}

/** CampaignAdditionalProperties model. */
export interface CampaignAdditionalProperties {
  postal?: CampaignPostal;
  confirmation?: CampaignConfirmation;
  optinTypes?: CampaignOptinTypes;
  subscriptionNotifications?: CampaignSubscriptionNotifications;
  profile?: CampaignProfile;
}

/** CampaignConfirmation model. */
export interface CampaignConfirmation {
  fromField?: FromFieldReference;
  /** What will happen after email confirmation. The values allowed include: hosted (the subscriber will stay on the default GetResponse website), customUrl (the subscriber will be redirected to a custom URL provided by the user). */
  redirectType?: CampaignConfirmationRedirectType;
  /** The MIME type for the confirmation message */
  mimeType?: CampaignConfirmationMimeType;
  /** Required if the redirectType is customUrl. The URL a subscriber will be redirected to if the redirectType is set to customUrl. */
  redirectUrl?: string;
  replyTo?: FromFieldReference;
  /** The subscription confirmation body ID */
  subscriptionConfirmationBodyId?: string;
  /** Subscription confirmation subject ID */
  subscriptionConfirmationSubjectId?: string;
}

/** CampaignListElement model. */
export interface CampaignListElement {
  /** Unique identifier of the campaign (contact list) */
  campaignId?: string;
  /** The campaign (list) name. * You can use each list name just once in your account. * The name must be between 3-64 characters. * All alphabets supported by GetResponse, including right-to-left ones, are allowed. * You can use upper and lower case letters, numbers, spaces and special characters apart from the ones listed below. * You can’t use emojis and the following special characters: `/`, `\`, `@`, and `[` or `]`. */
  name?: string;
  /** Tech name is a unique internal ID of a list used for [FTP imports](https://www.getresponse.com/help/how-to-import-files-via-ftp.html) (available in GetResponse MAX accounts only) */
  techName?: string;
  /** The campaign language code according to ISO 639-1, plus: zt - Chinese (Traditional), fs - Afghan Persian (Dari), md - Moldavian */
  languageCode?: string;
  /** Is the campaign default */
  isDefault?: unknown;
  /** The date of creation (ISO 8601 date-time string) */
  createdOn?: string;
  /** Direct hyperlink to a resource */
  href?: string;
  /** It's the same as the campaign name, kept for compatibility reasons */
  description?: string;
}

/** CampaignListSizesStatisticsElement model. */
export interface CampaignListSizesStatisticsElement {
  /** The total amount of subscribers for a given datetime and grouping */
  totalSubscribers?: number;
  /** The amount of subscribers added since the previous statistics frame */
  addedSubscribers?: number;
  /** The amount of subscribers removed since the previous statistics frame */
  removedSubscribers?: number;
  /** The statistics frame timestamp. The value depends on the groupBy parameter. For the hour, use datetime in the format YYYY-mm-dd HH:mm:ss; for the day, use date in the format YYYY-mm-dd; for the month, use a string in the format YYYY-mm; and for the total, use the string total. */
  createdOn?: string;
}

/** CampaignOptinTypes model. */
export interface CampaignOptinTypes {
  /** Single opt-in: confirmed opt-in disabled. Double opt-in: confirmed opt-in enabled. You can find more information [here](https://www.getresponse.com/resources/glossary/confirmed-opt-in.html) */
  email?: CampaignOptinTypesEmail;
  /** Single opt-in: confirmed opt-in disabled. Double opt-in: confirmed opt-in enabled. You can find more information [here](https://www.getresponse.com/resources/glossary/confirmed-opt-in.html) */
  api?: CampaignOptinTypesApi;
  /** Single opt-in: confirmed opt-in disabled. Double opt-in: confirmed opt-in enabled. You can find more information [here](https://www.getresponse.com/resources/glossary/confirmed-opt-in.html) */
  import?: CampaignOptinTypesImport;
  /** Single opt-in: confirmed opt-in disabled. Double opt-in: confirmed opt-in enabled. You can find more information [here](https://www.getresponse.com/resources/glossary/confirmed-opt-in.html) */
  webform?: CampaignOptinTypesWebform;
}

/** CampaignPostal model. */
export interface CampaignPostal {
  /** Should the postal address be included in all message footers for this campaign (mandatory for Canada and the US) */
  addPostalToMessages?: unknown;
  /** The city, free-text */
  city?: string;
  /** The company name, free-text */
  companyName?: string;
  /** The country name, free-text */
  country?: string;
  /** How the postal address will display in messages. The available fields include: [[name]], [[address]], [[city]], [[state]] [[zip]], [[country]] */
  design?: string;
  /** The state, free-text */
  state?: string;
  /** The street, free-text */
  street?: string;
  /** The ZIP code */
  zipCode?: string;
}

/** CampaignProfile model. */
export interface CampaignProfile {
  /** The campaign description */
  description?: string;
  /** The industry tag ID */
  industryTagId?: string;
  /** The logo URL */
  logo?: string;
  /** The logo link URL */
  logoLinkUrl?: string;
  /** The profile title */
  title?: string;
}

/** CampaignReference model. */
export interface CampaignReference {
  /** Campaign ID */
  campaignId: string;
  /** Direct hyperlink to a resource */
  href?: string;
  /** The campaign name */
  name?: string;
}

/** CampaignSubscriptionNotifications model. */
export interface CampaignSubscriptionNotifications {
  /** Are notifications enabled. Possible values include: enabled, disabled. */
  status?: unknown;
  recipients?: FromFieldReference[];
}

/** CampaignSubscriptionStatisticsItem model. */
export interface CampaignSubscriptionStatisticsItem {
  import?: number;
  email?: number;
  www?: number;
  panel?: number;
  leads?: number;
  sale?: number;
  api?: number;
  forward?: number;
  survey?: number;
  mobile?: number;
  copy?: number;
  landing_page?: number;
  webinar?: number;
  premium_newsletter?: number;
  course?: number;
  website_buider_elegant?: number;
  chat?: number;
  summary?: number;
}

/** Cart model. */
export interface Cart {
  /** The creation date (ISO 8601 date-time string) */
  createdOn?: string;
  /** The date of the last update (ISO 8601 date-time string) */
  updatedOn?: string;
  /** The contact ID */
  cartId?: string;
  /** Direct hyperlink to a resource */
  href?: string;
  /** The ID of the contact that the cart belongs to. You must first create the contact using POST /v3/contacts, or if it already exists, using GET /v3/contacts */
  contactId?: string;
  /** The total cart price, tax excluded */
  totalPrice?: number;
  /** The total cart price, tax included */
  totalTaxPrice?: number;
  /** The currency code (ISO 4217) */
  currency?: string;
  selectedVariants?: NewCartSelectedProductVariant[];
  /** The external ID is the identifying string or number of the cart, given by another software */
  externalId?: string;
  /** The external cart URL */
  cartUrl?: string;
}

/** Category model. */
export interface Category {
  /** The category ID */
  categoryId?: string;
  /** Direct hyperlink to a resource */
  href?: string;
  /** The name of the category */
  name?: string;
  /** The parent category ID */
  parentId?: string;
  /** This is a default category */
  isDefault?: boolean;
  /** The external URL to the category */
  url?: string;
  /** The external ID is the identifying string or number of the category given by another software */
  externalId?: string;
  /** The creation date (ISO 8601 date-time string) */
  createdOn?: string;
  /** The date of the last update (ISO 8601 date-time string) */
  updatedOn?: string;
}

/** ChooseWinnerAbtestsSubject model. */
export interface ChooseWinnerAbtestsSubject {
  /** The message variant ID. A variant identifier from https://apireference.getresponse.com/#operation/getAbtestsSubjectById. */
  variantId: string;
}

/** ClickTrack model. */
export interface ClickTrack {
  clickTrackId?: string;
  /** The tracked link */
  url?: string;
  /** The tracked link name */
  name?: string;
  /** The number of clicks on a link in a message */
  amount?: string;
}

/** The source message reference for a click track */
export interface ClickTrackMessage {
  /** The ID identifying message resource */
  resourceId?: string;
  /** The message type */
  type?: ClickTrackMessageType;
  /** The message creation date (ISO 8601 date-time string) */
  createdOn?: string;
  /** Type of the resource that represents the message in the API */
  resourceType?: ClickTrackMessageResourceType;
  /** Direct URL to the resource that represents the message */
  href?: string;
}

/** ClickTrackResource model. */
export interface ClickTrackResource {
  clickTrackId?: string;
  /** The name (label) of a click track */
  name?: string;
  /** The link URL of a click track */
  url?: string;
  /** The number of clicks counted for a click track */
  clicks?: number;
  message?: ClickTrackMessage;
  /** Direct hyperlink to a resource */
  href?: string;
}

/** The operator allows searching by message type. */
export interface ConditionMessageOperator {
  operatorType: ConditionMessageOperatorOperatorType;
  operator: MessageTypeOperator;
  /** The identifier of a selected resource: autoresponder, newsletter, split test or automation message */
  value: string;
}

/** ConditionStringOperator model. */
export interface ConditionStringOperator {
  operatorType: ConditionStringOperatorOperatorType;
  operator: ConditionStringOperatorOperator;
  value: string;
}

/** ConditionType model. */
export interface ConditionType {
  conditionType: ConditionTypeConditionType;
}

/** Contact model. */
export interface Contact {
  contactId: string;
  name?: string;
  origin?: ContactOrigin;
  /** The time zone of a contact, uses the time zone database format (https://www.iana.org/time-zones) */
  timeZone?: string;
  activities?: string;
  /** ISO 8601 date-time string. */
  changedOn?: string;
  /** ISO 8601 date-time string. */
  createdOn?: string;
  campaign?: CampaignReference;
  email: string;
  /** The day on which the contact is in the Autoresponder cycle. `null` indicates the contacts is not in the cycle. */
  dayOfCycle?: string;
  /** Contact scoring, pass null to remove the score from a contact */
  scoring?: number;
  /** Engagement Score is a feature that presents a visual estimate of a contact's engagement with mailings. The score is based on the contact's interactions with your e-mails. Via API, it's returned in the form of numbers ranging from 1 (Not Engaged) to 5 (Highly Engaged). */
  engagementScore?: number;
  /** Direct hyperlink to a resource */
  href: string;
}

/** ContactActivity model. */
export interface ContactActivity {
  /** The type of activity */
  activity?: ContactActivityActivity;
  subject?: string;
  /** The activity date (ISO 8601 date-time string) */
  createdOn?: string;
  /** This is only available for the `send` activity. It includes a link to the message preview */
  previewUrl?: string;
  resource?: ContactActivityResource;
  /** This is only available for the `click` activity. It includes the clicked link data */
  clickTrack?: ContactActivityClickTrack;
}

/** ContactActivityClickTrack model. */
export interface ContactActivityClickTrack {
  /** The click tracking ID */
  id?: string;
  /** The name of the clicked link */
  name?: string;
  /** The URL of the clicked link */
  url?: string;
}

/** ContactActivityResource model. */
export interface ContactActivityResource {
  resourceId?: string;
  resourceType?: ContactActivityResourceResourceType;
  /** Direct hyperlink to a resource */
  href?: string;
}

/** ContactConsent model. */
export interface ContactConsent {
  /** The unique identifier of the consent field. */
  consentId?: string;
  /** The name of the consent field. */
  name?: string;
  /** The actual text content of the consent field. */
  content?: string;
  /** Information whether the consent field is currently granted (true) or not (false). */
  isGranted?: boolean;
  /** The history of changes to the consent field text. */
  history?: ContactConsentHistoryItem[];
}

/** ContactConsentHistoryItem model. */
export interface ContactConsentHistoryItem {
  /** The text content of the consent field. */
  content?: string;
  /** Information whether the consent field was granted. */
  wasGranted?: boolean;
  /** The date and time when the consent field status was declared by the contact (ISO 8601). (ISO 8601 date-time string) */
  declaredAt?: string;
  /** The date and time when this consent field version was created (ISO 8601). (ISO 8601 date-time string) */
  createdAt?: string;
}

/** ContactCustomField model. */
export interface ContactCustomField {
  customFieldId?: string;
  values?: string[];
}

/** ContactCustomFieldValue model. */
export interface ContactCustomFieldValue {
  /** Custom field ID */
  customFieldId: string;
  name: string;
  value: string[];
  values: string[];
  type: string;
  fieldType?: string;
  valueType?: string;
}

/** ContactDetails model. */
export interface ContactDetails {
  contactId: string;
  name?: string;
  origin?: ContactDetailsOrigin;
  /** The time zone of a contact, uses the time zone database format (https://www.iana.org/time-zones) */
  timeZone?: string;
  activities?: string;
  /** ISO 8601 date-time string. */
  changedOn?: string;
  /** ISO 8601 date-time string. */
  createdOn?: string;
  campaign?: CampaignReference;
  email: string;
  /** The day on which the contact is in the Autoresponder cycle. `null` indicates the contacts is not in the cycle. */
  dayOfCycle?: string;
  /** Contact scoring, pass null to remove the score from a contact */
  scoring?: number;
  /** Engagement Score is a feature that presents a visual estimate of a contact's engagement with mailings. The score is based on the contact's interactions with your e-mails. Via API, it's returned in the form of numbers ranging from 1 (Not Engaged) to 5 (Highly Engaged). */
  engagementScore?: number;
  /** Direct hyperlink to a resource */
  href: string;
  note?: string;
  /** The contact's IP address. IPv4 and IPv6 formats are accepted. */
  ipAddress?: string;
  geolocation?: ContactGeolocation;
  /** The list of contact tags, limited to 500 tags. */
  tags?: ContactTag[];
  customFieldValues?: ContactCustomFieldValue[];
}

/** ContactGeolocation model. */
export interface ContactGeolocation {
  latitude?: string;
  longitude?: string;
  continentCode?: ContactGeolocationContinentCode;
  /** The country code, compliant with ISO 3166-1 alpha-2 */
  countryCode?: string;
  region?: string;
  postalCode?: string;
  dmaCode?: string;
  city?: string;
}

/** ContactListElement model. */
export interface ContactListElement {
  contactId: string;
  name?: string;
  origin?: ContactListElementOrigin;
  /** The time zone of a contact, uses the time zone database format (https://www.iana.org/time-zones) */
  timeZone?: string;
  activities?: string;
  /** ISO 8601 date-time string. */
  changedOn?: string;
  /** ISO 8601 date-time string. */
  createdOn?: string;
  campaign?: CampaignReference;
  email: string;
  /** The day on which the contact is in the Autoresponder cycle. `null` indicates the contacts is not in the cycle. */
  dayOfCycle?: string;
  /** Contact scoring, pass null to remove the score from a contact */
  scoring?: number;
  /** Engagement Score is a feature that presents a visual estimate of a contact's engagement with mailings. The score is based on the contact's interactions with your e-mails. Via API, it's returned in the form of numbers ranging from 1 (Not Engaged) to 5 (Highly Engaged). */
  engagementScore?: number;
  /** Direct hyperlink to a resource */
  href: string;
  note?: string;
  /** The contact's IP address. IPv4 and IPv6 formats are accepted. */
  ipAddress?: string;
}

/** ContactTag model. */
export interface ContactTag {
  tagId?: string;
  name?: string;
  href?: string;
  color?: string;
}

/** CreateAccountSummaryReport model. */
export interface CreateAccountSummaryReport {
  /** The custom report name */
  name: string;
  /** The custom report type */
  type: CreateAccountSummaryReportType;
  /** Parameters responsible for defining the reporting period */
  scheduling: Record<string, unknown>;
}

/** CreateAndUpdate model. */
export interface CreateAndUpdate {
  /** The creation date (ISO 8601 date-time string) */
  createdOn?: string;
  /** The date of the last update (ISO 8601 date-time string) */
  updatedOn?: string;
}

/** CreateBouncesReport model. */
export interface CreateBouncesReport {
  /** The custom report name */
  name: string;
  /** The custom report type */
  type: CreateBouncesReportType;
  /** Parameters responsible for defining the reporting period */
  scheduling: Record<string, unknown>;
}

/** CreateISPMessageStatsReport model. */
export interface CreateISPMessageStatsReport {
  /** The custom report name */
  name: string;
  /** The custom report type */
  type: CreateISPMessageStatsReportType;
  /** Parameters responsible for defining the reporting period */
  scheduling: Record<string, unknown>;
}

/** CreateImportErrorReport model. */
export interface CreateImportErrorReport {
  /** The custom report name */
  name: string;
  /** The custom report type */
  type: CreateImportErrorReportType;
  /** Parameters responsible for defining the reporting period */
  scheduling: Record<string, unknown>;
}

/** CreateListSummaryReport model. */
export interface CreateListSummaryReport {
  /** The custom report name */
  name: string;
  /** The custom report type */
  type: CreateListSummaryReportType;
  /** Parameters responsible for defining the reporting period */
  scheduling: Record<string, unknown>;
}

/** CreateMessageActivityReport model. */
export interface CreateMessageActivityReport {
  /** The custom report name */
  name: string;
  /** The custom report type */
  type: CreateMessageActivityReportType;
  /** Parameters responsible for defining the reporting period */
  scheduling: Record<string, unknown>;
  /** Filters used to narrow down the report data */
  filters: Record<string, unknown>;
}

/** CreateMessageActivityReportFilters model. */
export interface CreateMessageActivityReportFilters {
  /** Filters used to narrow down the report data */
  filters: Record<string, unknown>;
}

/** CreateMessageClicksReport model. */
export interface CreateMessageClicksReport {
  /** The custom report name */
  name: string;
  /** The custom report type */
  type: CreateMessageClicksReportType;
  /** Parameters responsible for defining the reporting period */
  scheduling: Record<string, unknown>;
}

/** CreateMessageStatsReport model. */
export interface CreateMessageStatsReport {
  /** The custom report name */
  name: string;
  /** The custom report type */
  type: CreateMessageStatsReportType;
  /** Parameters responsible for defining the reporting period */
  scheduling: Record<string, unknown>;
}

/** CreateMultimedia model. */
export interface CreateMultimedia {
  file?: string;
}

/** CreateStandardSubscriberActivityReport model. */
export interface CreateStandardSubscriberActivityReport {
  /** The custom report name */
  name: string;
  /** The custom report type */
  type: CreateStandardSubscriberActivityReportType;
  /** Parameters responsible for defining the reporting period */
  scheduling: Record<string, unknown>;
}

/** CreateSubscriptionRejectionsReport model. */
export interface CreateSubscriptionRejectionsReport {
  /** The custom report name */
  name: string;
  /** The custom report type */
  type: CreateSubscriptionRejectionsReportType;
  /** Parameters responsible for defining the reporting period */
  scheduling: Record<string, unknown>;
}

/** CreateTransactionalEmail model. */
export interface CreateTransactionalEmail {
  /** The 'From' address ID to be used as the message sender */
  fromField: unknown;
  /** The 'From' address ID to be used as the Reply-to */
  replyTo?: unknown;
  /** The tag ID used for statistical data collection */
  tag?: unknown;
  recipients: TransactionalEmailRecipients;
  /** The message content type */
  contentType: CreateTransactionalEmailContentType;
}

/** CreateTransactionalEmailBounceReport model. */
export interface CreateTransactionalEmailBounceReport {
  /** The custom report name */
  name: string;
  /** The custom report type */
  type: CreateTransactionalEmailBounceReportType;
  /** Parameters responsible for defining the reporting period */
  scheduling: Record<string, unknown>;
}

/** CreateTransactionalEmailTemplate model. */
export interface CreateTransactionalEmailTemplate {
  /** The template subject */
  subject: string;
  content?: TransactionalEmailTemplateContent;
}

/** CreateUnconfirmedContactsStatsReport model. */
export interface CreateUnconfirmedContactsStatsReport {
  /** The custom report name */
  name: string;
  /** The custom report type */
  type: CreateUnconfirmedContactsStatsReportType;
  /** Parameters responsible for defining the reporting period */
  scheduling: Record<string, unknown>;
}

/** CreateUnsubscribeContactsListsReport model. */
export interface CreateUnsubscribeContactsListsReport {
  /** The custom report name */
  name: string;
  /** The custom report type */
  type: CreateUnsubscribeContactsListsReportType;
  /** Parameters responsible for defining the reporting period */
  scheduling: Record<string, unknown>;
}

/** CreateUserActivityReport model. */
export interface CreateUserActivityReport {
  /** The custom report name */
  name: string;
  /** The custom report type */
  type: CreateUserActivityReportType;
  /** Parameters responsible for defining the reporting period */
  scheduling: Record<string, unknown>;
}

/** CreateWebinarParticipantsReport model. */
export interface CreateWebinarParticipantsReport {
  /** The custom report name */
  name: string;
  /** The custom report type */
  type: CreateWebinarParticipantsReportType;
  /** Parameters responsible for defining the reporting period */
  scheduling: Record<string, unknown>;
}

/** This makes it possible to search contacts by CRM conditions. */
export interface CrmCondition {
  conditionType: CrmConditionConditionType;
  /** The pipeline identifier */
  pipelineScope: string;
  stageScope: Record<string, unknown>;
}

/** CustomDateRange model. */
export interface CustomDateRange {
  /** The UTC date format (ISO 8601 date-time string) */
  from: string;
  /** The UTC date format (ISO 8601 date-time string) */
  to: string;
}

/** CustomEvent model. */
export interface CustomEvent {
  /** Unique name of custom event */
  name: string;
  /** Optional collection of attributes */
  attributes: CustomEventAttributeDetails[];
}

/** CustomEventAttribute model. */
export interface CustomEventAttribute {
  /** Unique name of attribute */
  name: string;
  /** Type of attribute */
  type: CustomEventAttributeType;
}

/** CustomEventAttributeDetails model. */
export interface CustomEventAttributeDetails {
  /** Unique name of attribute */
  name: string;
  /** Type of attribute */
  type: CustomEventAttributeDetailsType;
  customEventAttributeId: string;
}

/** Search contacts for which an custom event occurred / not occurred */
export interface CustomEventCondition {
  conditionType: CustomEventConditionConditionType;
  /** The custom event identifier */
  customEventId: string;
  /** Whether the custom event occurred or not */
  occurrence: CustomEventConditionOccurrence;
  /** Show contacts for which a custom event occurred / not occurred in certain date range */
  dateOperator: Record<string, unknown>;
  /** The operators `date_to`, `date_from`, and `customDate` require you to provide, respectively, a date, datetime, or a time interval. */
  date?: Record<string, unknown>;
}

/** CustomEventDetails model. */
export interface CustomEventDetails {
  /** Unique name of custom event */
  name: string;
  /** Optional collection of attributes */
  attributes: CustomEventAttributeDetails[];
  /** The custom event ID */
  customEventId: string;
  /** Date of creation custom event definition (ISO 8601 date-time string) */
  createdOn: string;
  /** Direct hyperlink to a resource */
  href?: string;
}

/** CustomField model. */
export interface CustomField {
  /** Custom field ID */
  customFieldId?: string;
  /** Direct hyperlink to a resource */
  href?: string;
  /** The name of the custom field. It must meet the following requirements: * be unique * use only lowercase letters, underscores and digits * not be equal to one of the merge words used in messages, i.e. `name, email, twitter, facebook, buzz, myspace, linkedin, digg, googleplus, pinterest, responder, campaign, change`. */
  name?: string;
  /** The custom field `type` accepts the following values: * `string` - input for a string value * `number` - input for a numeric value * `date` - input for a date * `datetime` - input for date and time * `country` - input for a country * `currency` - input for a currency, allows all ISO 4217 currency codes * `phone` - input for a phone number * `gender` - input for gender, allows `Male`, `Female` or `Prefer not to say` * `ip` - input for an IP address * `url` - input for a URL. */
  type?: unknown;
  /** Type of returning value, it returns `type` options extended by a `string` option if the `format` was not defined */
  valueType?: CustomFieldValueType;
  /** The custom field `format` accepts following values: * `text` - text input (doesn't require values in the `values` field, you can pass empty array) * `textarea` - textarea input (doesn't require values in the `values` field, you can pass empty array) * `radio` - radio input (requires at least 2 values in the `values` field) * `checkbox` - checkbox input (doesn't require values in the `values` field, you can pass empty array) * `single_select` - single select input (requires at least 2 values in the `values` field) * `multi_select` - multi select input (requires at least 2 values in the `values` field). */
  format?: unknown;
  /** Returns the same as `format` */
  fieldType?: string;
  /** Whether the custom field is visible to contacts */
  hidden?: unknown;
  /** The list of assigned default values, starting from zero depending on the custom field format. (Please see description). */
  values?: string[];
}

/** Search a contact by custom fields. */
export interface CustomFieldCondition {
  conditionType: CustomFieldConditionConditionType;
  /** Depends on the type of custom field, read more in [custom field condition documentation in segments (search contacts) reference manual](https://apidocs.getresponse.com/v3/case-study/segments-manual#get-by-custom-fields-search-contacts) */
  operatorType: CustomFieldConditionOperatorType;
  /** Depends on selected `"operatorType"`, read more in [custom field condition documentation in segments (search contacts) reference manual](https://apidocs.getresponse.com/v3/case-study/segments-manual#get-by-custom-fields-search-contacts) */
  operator: Record<string, unknown>;
  /** Depends on selected `"operator"` and `"operatorType"`, read more in [custom field condition documentation in segments (search contacts) reference manual](https://apidocs.getresponse.com/v3/case-study/segments-manual#get-by-custom-fields-search-contacts) */
  value?: Record<string, unknown>;
  /** The identifier of the custom field, read more in [custom field condition documentation in segments (search contacts) reference manual](https://apidocs.getresponse.com/v3/case-study/segments-manual#get-by-custom-fields-search-contacts) */
  scope: string;
  /** Required only when `"value":"last_n_days"`, read more in [custom field condition documentation in segments (search contacts) reference manual](https://apidocs.getresponse.com/v3/case-study/segments-manual#get-by-custom-fields-search-contacts) */
  numberOfDays?: number;
  /** Flag determines if current day will be included into chosen range. This flag can be used with `last_n_days`. */
  includeCurrentPeriod?: boolean;
}

/** CustomFieldReference model. */
export interface CustomFieldReference {
  customFieldId?: string;
  /** The name of the custom field. It must meet the following requirements: * be unique * use only lowercase letters, underscores and digits: [a-z0-9_]{1,128} * not be equal to one of the merge words used in messages, i.e. `name`, `email`, `twitter`, `facebook`, `buzz`, `myspace`, `linkedin`, `digg`, `googleplus`, `pinterest`, `responder`, `campaign`, `change`. */
  name?: string;
  /** The list of assigned default values, starting from zero depending on the custom field format. (Please see description). */
  values?: string[];
}

/** CustomFieldResponse model. */
export interface CustomFieldResponse {
  /** Custom field ID */
  customFieldId?: string;
  /** Direct hyperlink to a resource */
  href?: string;
  /** The name of the custom field */
  name?: string;
  type?: unknown;
  /** Type of returning value, it returns `type` options extended by a `string` option if the `format` was not defined */
  valueType?: string;
  format?: unknown;
  /** Returns the same as `format` */
  fieldType?: string;
  /** Whether the custom field is visible to contacts */
  hidden?: unknown;
  /** The list of assigned default values, starting from zero depending on the custom field format. (Please see description). */
  values?: string[];
}

/** CustomReport model. */
export interface CustomReport {
  /** The custom report ID */
  customReportId?: string;
  /** The custom report name */
  name?: string;
  /** The direct hyperlink to a resource */
  href?: string;
  /** The custom report frequency */
  frequency?: unknown;
  /** ISO 8601 date-time string. */
  createdAt?: string;
  /** ISO 8601 date-time string. */
  generatedAt?: string;
}

/** CustomReportDetails model. */
export interface CustomReportDetails {
  /** The custom report ID */
  customReportId?: string;
  /** The custom report name */
  name?: string;
  /** The direct hyperlink to a resource */
  href?: string;
  /** The custom report type */
  type?: unknown;
  /** Parameters responsible for defining the reporting period */
  scheduling?: Record<string, unknown>;
  /** Files that have been generated for the given report */
  files?: Record<string, unknown>[];
  /** Custom report creation date (ISO 8601 date-time string) */
  createdAt?: string;
  /** Custom report generation date (ISO 8601 date-time string) */
  generatedAt?: string;
}

/** CustomReportFilterActivityType model. */
export interface CustomReportFilterActivityType {
  /** Types of activities included in the report */
  activityType: unknown[];
}

/** CustomReportFilterMessageId model. */
export interface CustomReportFilterMessageId {
  /** Message IDs included in the report */
  messageId: string[];
}

/** CustomReportScheduling model. */
export interface CustomReportScheduling {
  /** The custom report frequency */
  frequency?: unknown;
}

/** DailyReportScheduling model. */
export interface DailyReportScheduling {
  /** The custom report frequency */
  frequency?: unknown;
  /** Field not applicable to the selected frequency */
  oneTime?: Record<string, unknown>;
  /** A field containing configuration parameters for recurring scheduling */
  recurring?: Record<string, unknown>;
}

/** DirectContent model. */
export interface DirectContent {
  /** The 'From' address ID to be used as the message sender */
  fromField: unknown;
  /** The 'From' address ID to be used as the Reply-to */
  replyTo?: unknown;
  /** The tag ID used for statistical data collection */
  tag?: unknown;
  recipients: TransactionalEmailRecipients;
  /** The message content type */
  contentType: DirectContentContentType;
  subject?: string;
  attachments?: TransactionalEmailAttachment[];
  /** The message content. At least one field is required. The maximum combined size of plain text and HTML is 16MB */
  content: Record<string, unknown>;
}

/** Search contacts by abandoned cart. */
export interface ECommerceAbandonedCartCondition {
  conditionType: ECommerceAbandonedCartConditionConditionType;
  /** Limit the searched shops */
  shopScope: Record<string, unknown>;
  /** Limit search by cart value */
  cartValue: Record<string, unknown>;
  /** Set a date range. For the date_from and last_n_days, custom field value is required. Examples can be found here: [API Docs](https://apidocs.getresponse.com/v3/case-study/segments-manual/#ecommerce-abandoned-cart-condition-type). */
  dateOperator: ECommerceAbandonedCartConditionDateOperator;
  /** This field is required only for `date_from` and `last_n_days` date operators. */
  value?: Record<string, unknown>;
  /** Flag determines if current day will be included into chosen range. This flag can be used with `last_n_days`. */
  includeCurrentPeriod?: boolean;
  /** Date interval string compliant with ISO 8601, supported format: <start_date>/<end_date>, allowed only for `custom` date operator */
  range?: unknown;
}

/** Search contacts by brand purchased. */
export interface ECommerceBrandPurchasedCondition {
  conditionType: ECommerceBrandPurchasedConditionConditionType;
  /** The shop identifier */
  scope: string;
  operatorType: ECommerceBrandPurchasedConditionOperatorType;
  operator: ECommerceBrandPurchasedConditionOperator;
  value: string;
}

/** Search contacts by the number of purchases. */
export interface ECommerceNumberOfPurchasesCondition {
  conditionType: ECommerceNumberOfPurchasesConditionConditionType;
  operatorType: ECommerceNumberOfPurchasesConditionOperatorType;
  operator: ECommerceNumberOfPurchasesConditionOperator;
  /** The condition limiting the searched shop */
  scope: Record<string, unknown>;
  value: number;
  /** Limit search by date range */
  date: Record<string, unknown>;
}

/** Search the product purchased. */
export interface ECommerceProductPurchasedCondition {
  conditionType: ECommerceProductPurchasedConditionConditionType;
  /** Limit the searched shops */
  shopScope: Record<string, unknown>;
  /** The product category */
  categoryScope: Record<string, unknown>;
  operatorType: ECommerceProductPurchasedConditionOperatorType;
  operator: ECommerceProductPurchasedConditionOperator;
  productScope: Record<string, unknown>;
  /** Set a date range. For the date_from and date_to, custom field value is required. */
  dateOperator: Record<string, unknown>;
  /** This field stores the date or time interval for the `date_to`, `date_from`, or `custom` date operator */
  value?: Record<string, unknown>;
  /** Number of days, required for the `last_n_days` date operator */
  numberOfDays?: number;
  /** Flag determines if current day will be included into chosen range. This flag is required for `last_n_days` date operator. Can be used with `last_7_days` and `last_30_days` date operators */
  includeCurrentPeriod?: boolean;
}

/** Search contacts by total spent. */
export interface ECommerceTotalSpentCondition {
  conditionType: ECommerceTotalSpentConditionConditionType;
  operatorType: ECommerceTotalSpentConditionOperatorType;
  operator: ECommerceTotalSpentConditionOperator;
  /** The condition limiting the searched shop */
  scope: Record<string, unknown>;
  value: number;
  /** The currency code according to ISO 4217, i.e. USD, GBP, PLN */
  currency: string;
  /** Limit search by date range */
  date: Record<string, unknown>;
}

/** EmailCondition model. */
export interface EmailCondition {
  conditionType: EmailConditionConditionType;
  operatorType: EmailConditionOperatorType;
  operator: EmailConditionOperator;
  value: string;
}

/** EmptyReportFilters model. */
export interface EmptyReportFilters {
  /** Filters used to narrow down the report data */
  filters?: Record<string, unknown>;
}

/** Search contacts by their engagement score */
export interface EngagementScoreCondition {
  conditionType: EngagementScoreConditionConditionType;
  /** The operator used in engagement score comparison */
  operator: EngagementScoreConditionOperator;
  /** The condition value */
  value: number;
}

/** ErrorResponse model. */
export interface ErrorResponse {
  /** HTTP response code */
  httpStatus: number;
  /** API error code */
  code: number;
  /** API error code description */
  codeDescription: string;
  /** Error message */
  message: string;
  /** URL to error description in the API Docs */
  moreInfo: string;
  context: Record<string, unknown>;
  /** UUID of the error response */
  uuid: string;
}

/** External Lexpad settings for the message, read more: [External Lexpad](https://apidocs.getresponse.com/v3/dynamic-content/external-lexpad) */
export interface ExternalLexpad {
  /** URL to the endpoint that will provide data for External Lexpad */
  dataSourceUrl: string;
  /** Token that will be sent in `X-Auth-Token` header to authenticate the requests made to the endpoint */
  dataSourceToken?: string;
}

/** FacebookPixel model. */
export interface FacebookPixel {
  name?: string;
  pixelId?: string;
}

/** File model. */
export interface File {
  /** The file name */
  name?: string;
  /** The file extension */
  extension?: string;
  /** The folder where the file is stored */
  folder?: Record<string, unknown>;
  /** The file ID */
  fileId: string;
  /** The file size */
  fileSize?: number;
  group?: FileGroup;
  /** The direct URL to the file thumbnail */
  thumbnail?: string;
  /** The direct URL to resource */
  url?: string;
  /** The file properties (available only for the `photos` group) */
  properties?: FileProperty[];
  /** The creation date (ISO 8601 date-time string) */
  createdOn?: string;
  /** Direct hyperlink to a resource */
  href?: string;
}

/** FileProperty model. */
export interface FileProperty {
  name: FilePropertyName;
  value: Record<string, unknown>;
}

/** Folder model. */
export interface Folder {
  /** The folder ID */
  folderId: string;
  /** The folder name */
  name?: string;
  /** The size of all files in the directory */
  size?: number;
  /** The creation date (ISO 8601 date-time string) */
  createdOn?: string;
}

/** FolderShort model. */
export interface FolderShort {
  /** The folder ID */
  folderId: string;
}

/** Form model. */
export interface Form {
  formId?: string;
  /** Same as `formId` */
  webformId?: string;
  name?: string;
  /** Direct hyperlink to a resource */
  href?: string;
  /** Indicates if the form has variants (A/B tests) */
  hasVariants?: boolean;
  /** The URL to a JavaScript file of the form. This is used to embed the form within a web page. */
  scriptUrl?: string;
  status?: FormStatus;
  /** ISO 8601 date-time string. */
  createdOn?: string;
  statistics?: FormStatistics;
  campaign?: CampaignReference;
}

/** FormDetails model. */
export interface FormDetails {
  formId?: string;
  /** Same as `formId` */
  webformId?: string;
  name?: string;
  /** Direct hyperlink to a resource */
  href?: string;
  /** Indicates if the form has variants (A/B tests) */
  hasVariants?: boolean;
  /** The URL to a JavaScript file of the form. This is used to embed the form within a web page. */
  scriptUrl?: string;
  status?: FormDetailsStatus;
  /** ISO 8601 date-time string. */
  createdOn?: string;
  statistics?: FormStatistics;
  campaign?: CampaignReference;
  settings?: FormSettings;
  variants?: FormVariant[];
}

/** FormSettings model. */
export interface FormSettings {
  /** `single` - Single opt-in means that the contact will be added without confirming their subscription first. `double` - Double opt-in means that the contact will receive a subscription confirmation email. */
  optin?: FormSettingsOptin;
  /** The contact who subscribed via this form will be added to the selected day in the autoresponder cycle. If null, the contact won't be added to the cycle. */
  phase?: number;
  /** What should happen when a new contact subscribes via the form. */
  thankYouType?: FormSettingsThankYouType;
  /** The URL used to redirect the newly subscribed contacts when they complete this form. Used if `thankYouType` is `custom_url`. */
  thankYouUrl?: string;
  /** What to do when the address already exists in the campaign */
  alreadySubscribedType?: FormSettingsAlreadySubscribedType;
  /** The URL used to redirect the already subscribed contacts when they complete this form. Used if `alreadySubscribedType` is `custom_url`. */
  alreadySubscribedUrl?: string;
  /** Is captcha enabled for the form */
  secondStageCaptcha?: StringBooleanEnum;
  /** How to forward form data to a thank-you page. [Learn more](https://www.getresponse.com/help/building-contact-lists/forms-and-pop-ups/can-i-forward-subscriber-data-to-a-custom-thank-you-page.html). `null` means that the data forwarding is turned off. */
  forwardDataRequestType?: FormSettingsForwardDataRequestType;
  /** Subscribers added via this form will have this custom field set with a value passed in `trackingCustomFieldValue` */
  trackingCustomField?: CustomFieldReference;
  /** See the `trackingCustomField` description */
  trackingCustomFieldValue?: string;
}

/** FormStatistics model. */
export interface FormStatistics {
  /** The total number of form visitors */
  visitors?: number;
  /** The number of unique form visitors */
  uniqueVisitors?: number;
  /** The number of visitors that subscribed using this form */
  subscribed?: number;
  /** The ratio of `subscribed` to `visitors` */
  subscriptionRate?: number;
}

/** FormVariant model. */
export interface FormVariant {
  /** The index of variants */
  variant?: string;
  variantName?: string;
  /** Is this variant the winner in the A/B test */
  winner?: StringBooleanEnum;
  status?: FormVariantStatus;
  /** ISO 8601 date-time string. */
  createdOn?: string;
  statistics?: FormStatistics;
}

/** FormVariantDetails model. */
export interface FormVariantDetails {
  formId?: string;
  /** Same as `formId` */
  webformId?: string;
  /** The index of variants */
  variant?: string;
  variantName?: string;
  /** Is this variant the winner in the A/B test */
  winner?: FormVariantDetailsWinner;
  status?: FormVariantDetailsStatus;
  /** ISO 8601 date-time string. */
  createdOn?: string;
  /** The total number of form visitors */
  numberOfVisitors?: number;
  /** The number of unique form visitors */
  numberOfUniqueVisitors?: number;
  /** The number of visitors who subscribed through this form */
  numberOfSubscribers?: number;
  /** The ratio of `numberOfSubscribers` to `numberOfVisitors` */
  subscriptionRate?: number;
}

/** FromField model. */
export interface FromField {
  /** The 'From' address ID */
  fromFieldId?: string;
  /** Direct hyperlink to a resource */
  href?: string;
  /** The email address */
  email?: string;
  /** Email address used to send message. */
  rewrittenEmail?: string;
  /** The name connected to the email address */
  name?: string;
  /** Flag if the 'From' address is active */
  isActive?: unknown;
  /** Flag if the 'From' address is default for the account */
  isDefault?: unknown;
  /** The creation date (ISO 8601 date-time string) */
  createdOn?: string;
  domain?: Record<string, unknown>;
}

/** FromFieldReference model. */
export interface FromFieldReference {
  /** The 'From' address ID */
  fromFieldId: string;
  /** Direct hyperlink to a resource */
  href?: string;
}

/** GDPRField model. */
export interface GDPRField {
  gdprFieldId?: string;
  /** The name of the GDPR field */
  name?: string;
  /** ISO 8601 date-time string. */
  createdOn?: string;
  /** The direct hyperlink to the resource */
  href?: string;
}

/** GDPRFieldDetails model. */
export interface GDPRFieldDetails {
  gdprFieldId?: string;
  /** The name of the GDPR field */
  name?: string;
  /** ISO 8601 date-time string. */
  createdOn?: string;
  /** The direct hyperlink to the resource */
  href?: string;
  latestVersion?: GDPRFieldLatestVersion;
}

/** GDPRFieldLatestVersion model. */
export interface GDPRFieldLatestVersion {
  gdprFieldVersionId?: string;
  /** The content of the GDPR field */
  content?: string;
  /** ISO 8601 date-time string. */
  createdOn?: string;
}

/** Find contacts based on whether they have given or not given specific consents. */
export interface GdprCondition {
  conditionType: GdprConditionConditionType;
  /** The ID of the consent field. You can retrieve it using [this API call](https://apireference.getresponse.com/#operation/getGDPRFieldList). */
  gdprFieldId: string;
  /** Specify whether you want to search for contacts who have given or not given consent. */
  consentStatus: GdprConditionConsentStatus;
  /** Specify when consent was given or not given. Not providing this field is equivalent to using the `anytime` operator. */
  consentDate?: Record<string, unknown>;
}

/** GeneralPerformanceStats model. */
export interface GeneralPerformanceStats {
  /** Statistics currency */
  currency?: string;
  /** Order statistics */
  order?: Record<string, unknown>;
  /** Revenue statistics */
  revenue?: Record<string, unknown>;
}

/** Search contacts by geolocation. */
export interface GeolocationCondition {
  conditionType: GeolocationConditionConditionType;
  operatorType: GeolocationConditionOperatorType;
  operator: GeolocationConditionOperator;
  value: string;
  /** Specify the search parameters */
  scope: GeolocationConditionScope;
}

/** Search contacts by a defined goal. */
export interface GoalCondition {
  conditionType: GoalConditionConditionType;
  operatorType: GoalConditionOperatorType;
  /** The relational and existence operator. For the relational operator, the value field is required. */
  operator: GoalConditionOperator;
  /** The value to be compared for the relational operator. For the assigned, the not_assigned operator field is prohibited. */
  value?: number;
  /** The goal identifier */
  scope: string;
}

/** ImageDetails model. */
export interface ImageDetails {
  /** Image ID */
  imageId?: string;
  /** URL from which image was downloaded */
  originalImageUrl?: string;
  /** Size in bytes */
  size?: string;
  /** Original name */
  name?: string;
  /** Thumbnail URL */
  thumbnailUrl?: string;
  /** Asset URL */
  url?: string;
  /** File extension */
  extension?: ImageDetailsExtension;
}

/** Import model. */
export interface Import {
  /** The import ID */
  importId?: string;
  campaign?: CampaignReference;
  status?: ImportStatus;
  /** The import statistics */
  statistics?: ImportStatistics;
  /** The detailed import error statistics */
  errorStatistics?: ImportErrorStatistics;
  /** ISO 8601 date-time string. */
  createdOn?: string;
  /** ISO 8601 date-time string. */
  finishedOn?: string;
  /** Direct hyperlink to a resource */
  href?: string;
}

/** ImportErrorReportDetails model. */
export interface ImportErrorReportDetails {
  /** The custom report ID */
  customReportId?: string;
  /** The custom report name */
  name?: string;
  /** The direct hyperlink to a resource */
  href?: string;
  /** The custom report type */
  type?: unknown;
  /** Parameters responsible for defining the reporting period */
  scheduling?: Record<string, unknown>;
  /** Files that have been generated for the given report */
  files?: Record<string, unknown>[];
  /** Custom report creation date (ISO 8601 date-time string) */
  createdAt?: string;
  /** Custom report generation date (ISO 8601 date-time string) */
  generatedAt?: string;
  /** Filters used to narrow down the report data */
  filters?: Record<string, unknown>;
}

/** ImportErrorStatistics model. */
export interface ImportErrorStatistics {
  /** The number of contacts with a syntax error */
  syntaxErrors?: number;
  /** The number of contacts already in queue */
  alreadyInQueue?: number;
  /** The number of contacts with invalid domains */
  invalidDomains?: number;
  /** The number of blocked contacts */
  blacklist?: number;
  /** The number of contacts rejected for policy reasons */
  policyFailures?: number;
  /** The number of contacts rejected because of mismatched criteria, [learn more](https://www.getresponse.com/help/managing-contacts/working-with-contact-lists/where-can-i-find-import-statistics.html#what-do-the-numbers-for-uploaded-approved-and-import-errors-mean) */
  mismatchedCriteria?: number;
}

/** ImportStatistics model. */
export interface ImportStatistics {
  /** The number of uploaded contacts */
  uploaded: number;
  /** The number of invalid contacts */
  invalid: number;
  /** The number of updated contacts */
  updated: number;
  /** The number of added contacts */
  addedToList: number;
}

/** IndustryTag model. */
export interface IndustryTag {
  /** Industry tag ID */
  industryTagId: string;
  name?: string;
  description?: string;
}

/** IndustryTagId model. */
export interface IndustryTagId {
  /** Industry tag ID */
  industryTagId?: string;
}

/** IndustryTagProperties model. */
export interface IndustryTagProperties {
  name?: string;
  description?: string;
}

/** IspMessageStatsReportDetails model. */
export interface IspMessageStatsReportDetails {
  /** The custom report ID */
  customReportId?: string;
  /** The custom report name */
  name?: string;
  /** The direct hyperlink to a resource */
  href?: string;
  /** The custom report type */
  type?: unknown;
  /** Parameters responsible for defining the reporting period */
  scheduling?: Record<string, unknown>;
  /** Files that have been generated for the given report */
  files?: Record<string, unknown>[];
  /** Custom report creation date (ISO 8601 date-time string) */
  createdAt?: string;
  /** Custom report generation date (ISO 8601 date-time string) */
  generatedAt?: string;
  /** Filters used to narrow down the report data */
  filters?: Record<string, unknown>;
}

/** LandingPage model. */
export interface LandingPage {
  /** The landing page ID */
  landingPageId?: string;
  /** Direct hyperlink to a resource */
  href?: string;
  /** The landing page meta title property */
  metaTitle?: string;
  /** The domain where the landing page is hosted */
  domain?: string;
  /** The subdomain where the landing page is assigned */
  subdomain?: string;
  /** The private domain provided by the user */
  userDomain?: string;
  /** The private domain path provided by the user */
  userDomainPath?: string;
  /** The campaign to which the landing page is linked */
  campaign?: unknown;
  /** The landing page status */
  status?: unknown;
  /** The DNS status for the user's private domain. Can be `null` if a private domain isn't assigned. */
  userDomainStatus?: LandingPageUserDomainStatus;
  /** Does the landing page have AB testing (variants) enabled */
  testAB?: unknown;
  /** The creation date (ISO 8601 date-time string) */
  createdOn?: string;
  /** The date of the last page update (ISO 8601 date-time string) */
  updatedOn?: string;
  /** The landing page meta description property */
  metaDescription?: string;
  /** To entirely prevent your page content from being listed in the Google web index, even if other sites link to it use a noindex meta tag */
  metaNoindex?: LandingPageMetaNoindex;
  /** Contacts subscribed via the landing page will be added to the autoresponder cycle. `Null` if contacts shouldn't be added to the cycle. */
  dayOfCycle?: number;
  /** The opt-in type (double or single) */
  optin?: LandingPageOptin;
  /** The favicon URL. Can be `null` if a favicon isn't present */
  favicoUrl?: string;
  /** What should happen after a contact subscribes */
  thankYouPageType?: LandingPageThankYouPageType;
  /** The `thank-you` page URL. Can be empty if a custom thank-you page isn't being used */
  thankYouPageUrl?: string;
  /** The landing page URL */
  url?: string;
  variants?: LandingPageVariant[];
}

/** LandingPageVariant model. */
export interface LandingPageVariant {
  /** The landing page variant ID. */
  variantId?: string;
  /** The variant index. */
  variant?: string;
  winner?: boolean;
  visitors?: string;
  uniqueVisitors?: string;
  subscribed?: string;
}

/** This is used to find the last time when a contact clicked a message. */
export interface LastClickDateCondition {
  conditionType: LastClickDateConditionConditionType;
  operatorType: LastClickDateConditionOperatorType;
  operator: LastClickDateConditionOperator;
  value: Record<string, unknown>;
}

/** Search the last time when a contact opened a message. */
export interface LastOpenDateCondition {
  conditionType: LastOpenDateConditionConditionType;
  operatorType: LastOpenDateConditionOperatorType;
  operator: LastOpenDateConditionOperator;
  value: Record<string, unknown>;
}

/** Search the last time when an email message was sent to a contact. */
export interface LastSendDateCondition {
  conditionType: LastSendDateConditionConditionType;
  operatorType: LastSendDateConditionOperatorType;
  operator: LastSendDateConditionOperator;
  value: Record<string, unknown>;
}

/** LegacyForm model. */
export interface LegacyForm {
  /** The webform (Legacy Form) ID */
  webformId?: string;
  name?: string;
  /** Direct hyperlink to a resource */
  href?: string;
  /** The URL of the script that displays the Legacy Form */
  scriptUrl?: string;
  status?: StatusEnum;
  /** The modification date (ISO 8601 date-time string) */
  modifiedOn?: string;
  statistics?: LegacyFormStatistics;
  campaign?: CampaignReference;
}

/** LegacyFormStatistics model. */
export interface LegacyFormStatistics {
  /** The number of Legacy Form views */
  opened?: number;
  /** The number of contacts that subscribed using this Legacy Form */
  subscribed?: number;
}

/** Search contacts that clicked on a link. */
export interface LinkClickedCondition {
  conditionType: LinkClickedConditionConditionType;
  operatorType: LinkClickedConditionOperatorType;
  operator: MessageTypeOperator;
  /** The message identifier */
  scope: string;
  clickTrackId: Record<string, unknown>;
}

/** Search contacts that didn't click a link. */
export interface LinkNotClickedCondition {
  conditionType: LinkNotClickedConditionConditionType;
  operatorType: LinkNotClickedConditionOperatorType;
  operator: Record<string, unknown>;
  /** It allows you to set a date range. For some of them `value` will be required. Examples can be found here: [API Docs](https://apidocs.getresponse.com/v3/case-study/segments-manual#not-opened-action). */
  dateOperator: LinkNotClickedConditionDateOperator;
  /** This field is required only for `date_from` and `last_n_days` date operators. */
  value?: Record<string, unknown>;
  /** Flag determines if current day will be included into chosen range. This flag can be used with `last_7_days`, `last_30_days`, `last_n_days`. */
  includeCurrentPeriod?: boolean;
  /** The message identifier. This field is prohibited for the 'all' operator. */
  scope?: string;
  /** The click track identifier */
  clickTrackId?: Record<string, unknown>;
}

/** ListSummaryReportDetails model. */
export interface ListSummaryReportDetails {
  /** The custom report ID */
  customReportId?: string;
  /** The custom report name */
  name?: string;
  /** The direct hyperlink to a resource */
  href?: string;
  /** The custom report type */
  type?: unknown;
  /** Parameters responsible for defining the reporting period */
  scheduling?: Record<string, unknown>;
  /** Files that have been generated for the given report */
  files?: Record<string, unknown>[];
  /** Custom report creation date (ISO 8601 date-time string) */
  createdAt?: string;
  /** Custom report generation date (ISO 8601 date-time string) */
  generatedAt?: string;
  /** Filters used to narrow down the report data */
  filters?: Record<string, unknown>;
}

/** Lps model. */
export interface Lps {
  /** The landing page ID */
  lpsId?: string;
  /** Direct hyperlink to a resource */
  href?: string;
  /** The landing page name */
  name?: string;
  /** The landing page status */
  status?: LpsStatus;
  /** The landing page domain */
  domainUrl?: string;
  /** The URL of a landing page thumbnail */
  thumbnailUrl?: string;
  /** Chats is enabled on the landing page */
  isChatsEnabled?: unknown;
  /** The date (in GMT) the landing page was created (ISO 8601 date-time string) */
  createdAt?: string;
  /** The date (in GMT) the landing page was updated (ISO 8601 date-time string) */
  updatedAt?: string;
  /** The landing page statistics */
  statistics?: LpsListItemStatistics;
}

/** LpsDetails model. */
export interface LpsDetails {
  /** The landing page ID */
  lpsId?: string;
  /** Direct hyperlink to a resource */
  href?: string;
  /** The landing page name */
  name?: string;
  /** The landing page status */
  status?: LpsDetailsStatus;
  /** The landing page domain */
  domainUrl?: string;
  /** The URL of a landing page thumbnail */
  thumbnailUrl?: string;
  /** Chats is enabled on the landing page */
  isChatsEnabled?: unknown;
  /** The date (in GMT) the landing page was created (ISO 8601 date-time string) */
  createdAt?: string;
  /** The date (in GMT) the landing page was updated (ISO 8601 date-time string) */
  updatedAt?: string;
  /** The total number of times your landing page was viewed or refreshed */
  pageViews?: number;
  /** The number of browsing sessions initiated on your landing page */
  visits?: number;
  /** The number of people who visited your landing page */
  uniqueVisitors?: number;
  pages?: LpsPage[];
}

/** LpsDetailsStatistics model. */
export interface LpsDetailsStatistics {
  /** The total number of times your landing page was viewed or refreshed */
  pageViews?: number;
  /** The number of browsing sessions initiated on your landing page */
  visits?: number;
  /** The number of people who visited your landing page */
  uniqueVisitors?: number;
}

/** LpsListItem model. */
export interface LpsListItem {
  /** The landing page ID */
  lpsId?: string;
  /** Direct hyperlink to a resource */
  href?: string;
  /** The landing page name */
  name?: string;
  /** The landing page status */
  status?: LpsListItemStatus;
  /** The landing page domain */
  domainUrl?: string;
  /** The URL of a landing page thumbnail */
  thumbnailUrl?: string;
  /** Chats is enabled on the landing page */
  isChatsEnabled?: unknown;
  /** The date (in GMT) the landing page was created (ISO 8601 date-time string) */
  createdAt?: string;
  /** The date (in GMT) the landing page was updated (ISO 8601 date-time string) */
  updatedAt?: string;
}

/** LpsListItemStatistics model. */
export interface LpsListItemStatistics {
  /** The number of browsing sessions initiated on your landing page */
  visits?: number;
  /** Number of leads */
  leads?: number;
  /** The number of leads divided by the number of visitors, shown as a percentage */
  subscriptionRate?: number;
}

/** LpsPage model. */
export interface LpsPage {
  /** The ID of a page associated with the landing page (i.e., 404 page and thank you page) */
  uuid?: string;
  /** The name of a page associated with the landing page (i.e., 404 page and thank you page) */
  name?: string;
  /** The status of a page associated with the landing page (i.e., 404 page or thank you page) */
  status?: LpsPageStatus;
  /** Direct hyperlink to a resource */
  url?: string;
  /** Direct hyperlink to a resource */
  redirectUrl?: string;
  /** The date (in GMT) a page associated with the landing page (i.e., 404 page or thank you page) was created (ISO 8601 date-time string) */
  createdAt?: string;
}

/** LpsStats model. */
export interface LpsStats {
  /** The landing page ID */
  lpsId: string;
  name?: string;
  /** The total number of times your landing page was viewed or refreshed */
  pageViews?: number;
  /** The number of browsing sessions initiated on your landing page */
  visits?: number;
  /** The number of people who visited your landing page */
  uniqueVisitors?: number;
  /** Direct hyperlink to a resource */
  thumbnailUrl?: string;
}

/** MessageActivityReportDetails model. */
export interface MessageActivityReportDetails {
  /** The custom report ID */
  customReportId?: string;
  /** The custom report name */
  name?: string;
  /** The direct hyperlink to a resource */
  href?: string;
  /** The custom report type */
  type?: unknown;
  /** Parameters responsible for defining the reporting period */
  scheduling?: Record<string, unknown>;
  /** Files that have been generated for the given report */
  files?: Record<string, unknown>[];
  /** Custom report creation date (ISO 8601 date-time string) */
  createdAt?: string;
  /** Custom report generation date (ISO 8601 date-time string) */
  generatedAt?: string;
  /** Filters used to narrow down the report data */
  filters?: Record<string, unknown>;
}

/** MessageActivityReportFilters model. */
export interface MessageActivityReportFilters {
  /** Filters used to narrow down the report data */
  filters?: Record<string, unknown>;
}

/** MessageClicksReportDetails model. */
export interface MessageClicksReportDetails {
  /** The custom report ID */
  customReportId?: string;
  /** The custom report name */
  name?: string;
  /** The direct hyperlink to a resource */
  href?: string;
  /** The custom report type */
  type?: unknown;
  /** Parameters responsible for defining the reporting period */
  scheduling?: Record<string, unknown>;
  /** Files that have been generated for the given report */
  files?: Record<string, unknown>[];
  /** Custom report creation date (ISO 8601 date-time string) */
  createdAt?: string;
  /** Custom report generation date (ISO 8601 date-time string) */
  generatedAt?: string;
  /** Filters used to narrow down the report data */
  filters?: Record<string, unknown>;
}

/** The message content. */
export interface MessageContent {
  /** The message content in HTML */
  html?: string;
  /** The plain text equivalent of the message content */
  plain?: string;
}

/** Search contacts who didn't receive a certain message. */
export interface MessageNotSentCondition {
  conditionType: MessageNotSentConditionConditionType;
  operatorType: MessageNotSentConditionOperatorType;
  operator: MessageTypeOperator;
  /** The message identifier */
  value: string;
}

/** Search contacts who received a certain message. */
export interface MessageSentCondition {
  conditionType: MessageSentConditionConditionType;
  operatorType: MessageSentConditionOperatorType;
  operator: MessageTypeOperator;
  /** The message identifier */
  value: string;
}

/** MessageStatisticsListElement model. */
export interface MessageStatisticsListElement {
  /** The statistics time frame in the ISO 8601 datetime format with duration interval */
  timeInterval?: string;
  sent?: number;
  totalOpened?: number;
  totalHumanOpened?: number;
  uniqueOpened?: number;
  uniqueHumanOpened?: number;
  totalClicked?: number;
  totalHumanClicked?: number;
  uniqueClicked?: number;
  uniqueHumanClicked?: number;
  goals?: number;
  uniqueGoals?: number;
  forwarded?: number;
  unsubscribed?: number;
  bounced?: number;
  complaints?: number;
}

/** MessageStatsReportDetails model. */
export interface MessageStatsReportDetails {
  /** The custom report ID */
  customReportId?: string;
  /** The custom report name */
  name?: string;
  /** The direct hyperlink to a resource */
  href?: string;
  /** The custom report type */
  type?: unknown;
  /** Parameters responsible for defining the reporting period */
  scheduling?: Record<string, unknown>;
  /** Files that have been generated for the given report */
  files?: Record<string, unknown>[];
  /** Custom report creation date (ISO 8601 date-time string) */
  createdAt?: string;
  /** Custom report generation date (ISO 8601 date-time string) */
  generatedAt?: string;
  /** Filters used to narrow down the report data */
  filters?: Record<string, unknown>;
}

/** MetaField model. */
export interface MetaField {
  /** Direct hyperlink to a resource */
  href?: string;
  /** The meta field ID */
  metaFieldId?: string;
  /** The meta field name */
  name?: string;
  /** The meta field value */
  value?: string;
  /** The value type enumerable */
  valueType?: MetaFieldValueType;
  /** The meta field description */
  description?: string;
  /** The creation date (ISO 8601 date-time string) */
  createdOn?: string;
  /** The date of the last update (ISO 8601 date-time string) */
  updatedOn?: string;
}

/** MonthlyReportScheduling model. */
export interface MonthlyReportScheduling {
  /** The custom report frequency */
  frequency?: unknown;
  /** Field not applicable to the selected frequency */
  oneTime?: Record<string, unknown>;
  /** A field containing configuration parameters for recurring scheduling */
  recurring?: Record<string, unknown>;
}

/** NameCondition model. */
export interface NameCondition {
  conditionType: NameConditionConditionType;
  operatorType: NameConditionOperatorType;
  operator: NameConditionOperator;
  value: string;
}

/** NewAbtestsSubject model. */
export interface NewAbtestsSubject {
  /** A/B test ID */
  abTestId?: string;
  /** A/B test name */
  name: string;
  /** List linked to A/B test */
  campaign: CampaignReference;
  /** Newsletter's From" address" */
  fromField: FromFieldReference;
  /** Newsletter's reply-to address */
  replyTo?: FromFieldReference;
  /** The A/B test delivery settings */
  deliverySettings: Record<string, unknown>;
  flags?: NewAbtestsSubjectFlagsItem[];
  /** Message variants. Please note, the number of subject variants should be between 2 and 5 */
  variants: string[];
  /** The send settings for the A/B test */
  sendSettings: Record<string, unknown>;
  content: MessageContent;
}

/** NewAddress model. */
export interface NewAddress {
  /** The creation date (ISO 8601 date-time string) */
  createdOn?: string;
  /** The date of the last update (ISO 8601 date-time string) */
  updatedOn?: string;
  addressId?: string;
  /** Direct hyperlink to a resource */
  href?: string;
  /** The country code (ISO 3166-1 alpha-3) */
  countryCode: string;
  /** The country name, based on `countryCode` */
  countryName?: string;
  name: string;
  firstName?: string;
  lastName?: string;
  /** Address line 1 */
  address1?: string;
  /** Address line 2 */
  address2?: string;
  city?: string;
  /** The ZIP/postal code, free text */
  zip?: string;
  province?: string;
  /** The province code, free text */
  provinceCode?: string;
  /** The phone number, free text */
  phone?: string;
  /** The company name, free text */
  company?: string;
}

/** NewAutoresponder model. */
export interface NewAutoresponder {
  /** The autoresponder ID */
  autoresponderId?: string;
  /** Direct hyperlink to a resource */
  href?: string;
  /** The autoresponder name */
  name?: string;
  /** The autoresponder message subject */
  subject: string;
  /** The campaign ID. The system will assign the autoresponder to a default campaign if you don't provide a specific campaign ID. */
  campaignId?: string;
  /** The autoresponder status */
  status: unknown;
  /** The from email address used for the message */
  fromField?: unknown;
  /** The email that will be used as a reply-to address */
  replyTo?: unknown;
  content: MessageContent;
  flags?: MessageFlagsArrayItem[];
  /** The conditions that will trigger the autoresponder */
  triggerSettings: unknown;
  /** The autoresponder statistics summary */
  statistics?: Record<string, unknown>;
  /** The creation date (ISO 8601 date-time string) */
  createdOn?: string;
  /** How the message will be delivered to the subscriber */
  sendSettings: AutoresponderSendSettingsInput;
}

/** NewCampaign model. */
export interface NewCampaign {
  /** Unique identifier of the campaign (contact list) */
  campaignId?: string;
  /** The campaign (list) name. * You can use each list name just once in your account. * The name must be between 3-64 characters. * All alphabets supported by GetResponse, including right-to-left ones, are allowed. * You can use upper and lower case letters, numbers, spaces and special characters apart from the ones listed below. * You can’t use emojis and the following special characters: `/`, `\`, `@`, and `[` or `]`. */
  name: string;
  /** Tech name is a unique internal ID of a list used for [FTP imports](https://www.getresponse.com/help/how-to-import-files-via-ftp.html) (available in GetResponse MAX accounts only) */
  techName?: string;
  /** The campaign language code according to ISO 639-1, plus: zt - Chinese (Traditional), fs - Afghan Persian (Dari), md - Moldavian */
  languageCode?: string;
  /** Is the campaign default */
  isDefault?: unknown;
  /** The date of creation (ISO 8601 date-time string) */
  createdOn?: string;
  /** Direct hyperlink to a resource */
  href?: string;
  postal?: CampaignPostal;
  confirmation?: CampaignConfirmation;
  optinTypes?: CampaignOptinTypes;
  subscriptionNotifications?: CampaignSubscriptionNotifications;
  profile?: CampaignProfile;
}

/** NewCart model. */
export interface NewCart {
  /** The creation date (ISO 8601 date-time string) */
  createdOn?: string;
  /** The date of the last update (ISO 8601 date-time string) */
  updatedOn?: string;
  /** The contact ID */
  cartId?: string;
  /** Direct hyperlink to a resource */
  href?: string;
  /** The ID of the contact that the cart belongs to. You must first create the contact using POST /v3/contacts, or if it already exists, using GET /v3/contacts */
  contactId: string;
  /** The total cart price, tax excluded */
  totalPrice: number;
  /** The total cart price, tax included */
  totalTaxPrice?: number;
  /** The currency code (ISO 4217) */
  currency: string;
  selectedVariants: NewCartSelectedProductVariant[];
  /** The external ID is the identifying string or number of the cart, given by another software */
  externalId?: string;
  /** The external cart URL */
  cartUrl?: string;
}

/** NewCartSelectedProductVariant model. */
export interface NewCartSelectedProductVariant {
  /** The ID of a selected variant. You must first create a variant using: `POST` [Create product](https://apireference.getresponse.com/#operation/createProduct) `POST` [Create product variant](https://apireference.getresponse.com/#operation/createProductVariant) or get ID from variants created already: `GET` [Get a list of product variants](https://apireference.getresponse.com/#operation/getProductVariantList) */
  variantId: string;
  /** The quantity */
  quantity: number;
  /** The price, tax excluded */
  price: number;
  /** The price, tax included */
  priceTax: number;
  /** Direct hyperlink to a resource */
  href?: string;
}

/** NewCategory model. */
export interface NewCategory {
  /** The category ID */
  categoryId?: string;
  /** Direct hyperlink to a resource */
  href?: string;
  /** The name of the category */
  name: string;
  /** The parent category ID */
  parentId?: string;
  /** This is a default category */
  isDefault?: boolean;
  /** The external URL to the category */
  url?: string;
  /** The external ID is the identifying string or number of the category given by another software */
  externalId?: string;
  /** The creation date (ISO 8601 date-time string) */
  createdOn?: string;
  /** The date of the last update (ISO 8601 date-time string) */
  updatedOn?: string;
}

/** NewContact model. */
export interface NewContact {
  contactId: string;
  name?: string;
  origin?: NewContactOrigin;
  /** The time zone of a contact, uses the time zone database format (https://www.iana.org/time-zones) */
  timeZone?: string;
  activities?: string;
  /** ISO 8601 date-time string. */
  changedOn?: string;
  /** ISO 8601 date-time string. */
  createdOn?: string;
  campaign: CampaignReference;
  email: string;
  /** The day on which the contact is in the Autoresponder cycle. `null` indicates the contacts is not in the cycle. */
  dayOfCycle?: string;
  /** Contact scoring, pass null to remove the score from a contact */
  scoring?: number;
  /** Engagement Score is a feature that presents a visual estimate of a contact's engagement with mailings. The score is based on the contact's interactions with your e-mails. Via API, it's returned in the form of numbers ranging from 1 (Not Engaged) to 5 (Highly Engaged). */
  engagementScore?: number;
  /** Direct hyperlink to a resource */
  href: string;
  /** The contact's IP address. IPv4 and IPv6 formats are accepted. */
  ipAddress?: string;
  tags?: NewContactTag[];
  customFieldValues?: NewContactCustomFieldValue[];
}

/** NewContactCustomFieldValue model. */
export interface NewContactCustomFieldValue {
  /** Custom field ID */
  customFieldId: string;
  value: string[];
}

/** NewContactCustomFieldValues model. */
export interface NewContactCustomFieldValues {
  customFieldValues?: NewContactCustomFieldValue[];
}

/** NewContactTag model. */
export interface NewContactTag {
  tagId: string;
}

/** NewContactTags model. */
export interface NewContactTags {
  tags?: NewContactTag[];
}

/** NewCustomEvent model. */
export interface NewCustomEvent {
  /** Unique name of custom event */
  name: string;
  /** Optional collection of attributes */
  attributes: CustomEventAttributeDetails[];
}

/** NewCustomField model. */
export interface NewCustomField {
  /** Custom field ID */
  customFieldId?: string;
  /** Direct hyperlink to a resource */
  href?: string;
  /** The name of the custom field. It must meet the following requirements: * be unique * use only lowercase letters, underscores and digits * not be equal to one of the merge words used in messages, i.e. `name, email, twitter, facebook, buzz, myspace, linkedin, digg, googleplus, pinterest, responder, campaign, change`. */
  name: string;
  /** The custom field `type` accepts the following values: * `string` - input for a string value * `number` - input for a numeric value * `date` - input for a date * `datetime` - input for date and time * `country` - input for a country * `currency` - input for a currency, allows all ISO 4217 currency codes * `phone` - input for a phone number * `gender` - input for gender, allows `Male`, `Female` or `Prefer not to say` * `ip` - input for an IP address * `url` - input for a URL. */
  type: unknown;
  /** Type of returning value, it returns `type` options extended by a `string` option if the `format` was not defined */
  valueType?: NewCustomFieldValueType;
  /** The custom field `format` accepts following values: * `text` - text input (doesn't require values in the `values` field, you can pass empty array) * `textarea` - textarea input (doesn't require values in the `values` field, you can pass empty array) * `radio` - radio input (requires at least 2 values in the `values` field) * `checkbox` - checkbox input (doesn't require values in the `values` field, you can pass empty array) * `single_select` - single select input (requires at least 2 values in the `values` field) * `multi_select` - multi select input (requires at least 2 values in the `values` field). */
  format: unknown;
  /** Returns the same as `format` */
  fieldType?: string;
  /** Whether the custom field is visible to contacts */
  hidden: unknown;
  /** The list of assigned default values, starting from zero depending on the custom field format. (Please see description). */
  values: string[];
}

/** NewFile model. */
export interface NewFile {
  /** The file name */
  name: string;
  /** The file extension */
  extension: string;
  /** The folder where the file is stored */
  folder: Record<string, unknown>;
  /** The base64 encoded file content */
  content: string;
}

/** NewFolder model. */
export interface NewFolder {
  /** The folder name */
  name: string;
}

/** NewFromField model. */
export interface NewFromField {
  /** The email address */
  email: string;
  /** The name connected to the email address */
  name: string;
}

/** NewImport model. */
export interface NewImport {
  /** The ID of the destination campaign (list) */
  campaignId: string;
  /** Mapping definition for such contact properties as email address, name, or custom fields. It's the equivalent of column headers in a CSV file used to import contacts in a GetResponse account. The `email` value is required. For custom fields, provide only custom fields name in the mapping. Include their values in the corresponding field in the contact array */
  fieldMapping: string[];
  /** Container for a contact definition. Include the values defined in the `fieldMapping` array */
  contacts: string[][];
}

/** NewMetaField model. */
export interface NewMetaField {
  /** Direct hyperlink to a resource */
  href?: string;
  /** The meta field ID */
  metaFieldId?: string;
  /** The meta field name */
  name: string;
  /** The meta field value */
  value: string;
  /** The value type enumerable */
  valueType: NewMetaFieldValueType;
  /** The meta field description */
  description?: string;
}

/** NewNewsletter model. */
export interface NewNewsletter {
  content: MessageContent;
  flags?: MessageFlagsArrayItem[];
  /** The newsletter name */
  name?: string;
  /** The newsletter type */
  type?: NewNewsletterType;
  /** The message subject */
  subject: string;
  /** The 'From' email address used for the message */
  fromField: unknown;
  /** The email that will be used as the reply-to address */
  replyTo?: unknown;
  /** The newsletter must be assigned to a campaign */
  campaign: unknown;
  /** The newsletter attachments. The size of all attachments combined can't exceed 400KB */
  attachments?: NewsletterAttachment[];
  /** How the message will be delivered to the subscriber. You can specify multiple parameters. Then the system uses AND logic. */
  sendSettings: unknown;
}

/** NewOrder model. */
export interface NewOrder {
  /** The order ID */
  orderId?: string;
  /** Direct hyperlink to a resource */
  href?: string;
  /** Create a contact by using `POST /v3/contacts`. Or, if the contact already exists, using `GET /v3/contacts` */
  contactId: string;
  /** The external URL for an order */
  orderUrl?: string;
  /** The external ID is the identifying string or number of the order given by another software */
  externalId?: string;
  /** The total price of an order */
  totalPrice: number;
  /** The total price tax of an order */
  totalPriceTax?: number;
  /** The order currency code (ISO 4217) */
  currency: string;
  /** The status value */
  status?: string;
  /** Create a cart by using `POST /v3/shops/{shopId}/carts` */
  cartId?: string;
  /** The order description */
  description?: string;
  /** The shipping price for an order */
  shippingPrice?: number;
  /** The shipping address for an order */
  shippingAddress?: unknown;
  /** The billing status of an order */
  billingStatus?: string;
  /** The billing address for an order */
  billingAddress?: unknown;
  /** The exact time an order was made (ISO 8601 date-time string) */
  processedAt?: string;
  metaFields?: NewMetaField[];
  selectedVariants: NewSelectedProductVariant[];
}

/** NewPredefinedField model. */
export interface NewPredefinedField {
  predefinedFieldId?: string;
  /** Direct hyperlink to a resource */
  href?: string;
  name: string;
  value: string;
  campaign: CampaignReference;
}

/** NewProduct model. */
export interface NewProduct {
  /** The creation date (ISO 8601 date-time string) */
  createdOn?: string;
  /** The date of the last update (ISO 8601 date-time string) */
  updatedOn?: string;
  /** The product ID */
  productId?: string;
  /** Direct hyperlink to a resource */
  href?: string;
  /** The product name */
  name: string;
  /** The product type */
  type?: string;
  /** The external URL for the product */
  url?: string;
  /** The product vendor */
  vendor?: string;
  /** The external ID is the identifying string or number of the product given by another software */
  externalId?: string;
  categories?: NewProductCategory[];
  variants: NewProductVariant[];
  metaFields?: NewMetaField[];
}

/** NewProductCategory model. */
export interface NewProductCategory {
  /** The category ID */
  categoryId?: string;
  /** Direct hyperlink to a resource */
  href?: string;
  /** The name of the category */
  name: string;
  /** The parent category ID */
  parentId?: string;
  /** This is a default category */
  isDefault?: boolean;
  /** The external URL to the category */
  url?: string;
  /** The external ID is the identifying string or number of the category given by another software */
  externalId?: string;
}

/** NewProductVariant model. */
export interface NewProductVariant {
  /** The product ID */
  variantId?: string;
  /** Direct hyperlink to a resource */
  href?: string;
  /** The product name */
  name: string;
  /** The external URL to the product variant */
  url?: string;
  /** The stock-keeping unit of a variant. Must be unique within the product */
  sku: string;
  /** The price */
  price: number;
  /** The price including tax */
  priceTax: number;
  /** The price before the change */
  previousPrice?: number;
  /** The price before the change including tax */
  previousPriceTax?: number;
  /** The quantity of variant items */
  quantity?: number;
  /** The position of a variant */
  position?: number;
  /** The barcode of a variant */
  barcode?: string;
  /** The external ID is the identifying string or number of the variant given by another software */
  externalId?: string;
  /** The description of a variant */
  description?: string;
  images?: NewProductVariantImage[];
  metaFields?: NewMetaField[];
  taxes?: NewTax[];
}

/** NewProductVariantImage model. */
export interface NewProductVariantImage {
  /** The image ID */
  imageId?: string;
  /** Direct hyperlink to a resource */
  href?: string;
  /** The source URL of an image */
  src: string;
  /** The position of an image */
  position: number;
}

/** NewRssNewsletter model. */
export interface NewRssNewsletter {
  /** The RSS newsletter ID */
  rssNewsletterId: string;
  /** Direct hyperlink to a resource */
  href: string;
  /** The URL for the RSS Feed */
  rssFeedUrl: string;
  /** The RSS message subject */
  subject: string;
  /** How your newsletters will be seen inside the application */
  name?: string;
  /** The status of the RSS newsletter */
  status: unknown;
  editor?: unknown;
  /** The 'From' email address used for the message */
  fromField: unknown;
  /** The email that will be used as a reply-to address */
  replyTo?: unknown;
  content: MessageContent;
  /** How the message will be delivered to the subscriber */
  sendSettings: unknown;
  /** The creation date (ISO 8601 date-time string) */
  createdOn?: string;
  flags?: MessageFlagsArrayItem[];
}

/** New search contacts. */
export interface NewSearchContacts {
  /** Only one subscription status */
  subscribersType?: NewSearchContactsSubscribersTypeItem[];
  /** Match 'any' (`or` value) or 'all' (`and` value) of the following conditions */
  sectionLogicOperator: NewSearchContactsSectionLogicOperator;
  section: SearchContactSection[];
  /** The unique search-contact identifier */
  searchContactId?: string;
  /** The unique name of search-contact */
  name: string;
  /** The UTC date time format ISO 8601, e.g. 2018-04-10T10:02:57+0000 (ISO 8601 date-time string) */
  createdOn?: string;
  /** Direct hyperlink to a resource */
  href?: string;
}

/** NewSelectedProductVariant model. */
export interface NewSelectedProductVariant {
  /** Direct hyperlink to a resource */
  href?: string;
  /** The ID of a selected variant. You must first create a variant using: `POST` [Create product](https://apireference.getresponse.com/#operation/createProduct) `POST` [Create product variant](https://apireference.getresponse.com/#operation/createProductVariant) or get ID from variants created already: `GET` [Get a list of product variants](https://apireference.getresponse.com/#operation/getProductVariantList) */
  variantId: string;
  /** The product variant price */
  price: number;
  /** The product variant price tax */
  priceTax?: number;
  /** The product variant quantity */
  quantity: number;
  taxes?: NewTax[];
}

/** NewShop model. */
export interface NewShop {
  /** The creation date (ISO 8601 date-time string) */
  createdOn?: string;
  /** The date of the last update (ISO 8601 date-time string) */
  updatedOn?: string;
  /** The shop ID */
  shopId?: string;
  /** Direct hyperlink to a resource */
  href?: string;
  /** The shop name */
  name: string;
  /** The language locale (ISO 639-1) */
  locale: string;
  /** The currency code (ISO 4217) */
  currency: string;
}

/** NewSuppression model. */
export interface NewSuppression {
  /** The name of the suppression list */
  name: string;
  masks?: string[];
}

/** NewTag model. */
export interface NewTag {
  /** The tag name */
  name: string;
  /** The tag color (deprecated) */
  color?: string;
}

/** NewTax model. */
export interface NewTax {
  /** The tax ID */
  taxId?: string;
  /** Direct hyperlink to a resource */
  href?: string;
  /** The tax name */
  name: string;
  /** The rate value */
  rate: number;
}

/** NewTransactionalEmailTag model. */
export interface NewTransactionalEmailTag {
  tagId: string;
}

/** Newsletter model. */
export interface Newsletter {
  /** The newsletter ID */
  newsletterId: string;
  /** Direct hyperlink to a resource */
  href: string;
  /** The newsletter name */
  name?: string;
  /** The newsletter type */
  type?: NewsletterType;
  /** The newsletter status */
  status?: unknown;
  /** This describes how the content of the message was created */
  editor?: unknown;
  /** The message subject */
  subject?: string;
  /** The 'From' email address used for the message */
  fromField?: unknown;
  /** The email that will be used as the reply-to address */
  replyTo?: unknown;
  /** The newsletter must be assigned to a campaign */
  campaign?: unknown;
  /** The scheduled send date and time for the newsletter in the ISO 8601 format. (ISO 8601 date-time string) */
  sendOn?: string;
  /** The newsletter attachments. The size of all attachments combined can't exceed 400KB */
  attachments?: NewsletterAttachment[];
  /** How the message will be delivered to the subscriber. You can specify multiple parameters. Then the system uses AND logic. */
  sendSettings?: unknown;
  /** The sending metrics */
  sendMetrics?: Record<string, unknown>;
  /** The creation date (ISO 8601 date-time string) */
  createdOn?: string;
}

/** NewsletterActivity model. */
export interface NewsletterActivity {
  /** The type of activity */
  activity?: NewsletterActivityActivity;
  /** The date when activity occurred (ISO 8601 date-time string) */
  createdOn?: string;
  /** The contact ID */
  contact?: unknown;
}

/** NewsletterActivityContactReference model. */
export interface NewsletterActivityContactReference {
  /** Unique identifier of the contact. You can retrieve this ID from the [list of contacts](https://apireference.getresponse.com/#operation/getContactList) field: contactId */
  contactId?: string;
  /** The contact email */
  email?: string;
  /** Direct hyperlink to a resource */
  href?: string;
}

/** NewsletterAttachment model. */
export interface NewsletterAttachment {
  /** The file name */
  fileName?: string;
  /** The base64 encoded file content */
  content?: string;
  /** The file mime type */
  mimeType?: string;
}

/** NewsletterDetails model. */
export interface NewsletterDetails {
  /** The newsletter ID */
  newsletterId: string;
  /** Direct hyperlink to a resource */
  href: string;
  /** The newsletter name */
  name?: string;
  /** The newsletter type */
  type?: NewsletterDetailsType;
  /** The newsletter status */
  status?: unknown;
  /** This describes how the content of the message was created */
  editor?: unknown;
  /** The message subject */
  subject?: string;
  /** The 'From' email address used for the message */
  fromField?: unknown;
  /** The email that will be used as the reply-to address */
  replyTo?: unknown;
  /** The newsletter must be assigned to a campaign */
  campaign?: unknown;
  /** The scheduled send date and time for the newsletter in the ISO 8601 format. (ISO 8601 date-time string) */
  sendOn?: string;
  /** The newsletter attachments. The size of all attachments combined can't exceed 400KB */
  attachments?: NewsletterAttachment[];
  /** How the message will be delivered to the subscriber. You can specify multiple parameters. Then the system uses AND logic. */
  sendSettings?: unknown;
  /** The sending metrics */
  sendMetrics?: Record<string, unknown>;
  /** The creation date (ISO 8601 date-time string) */
  createdOn?: string;
  content?: MessageContent;
  /** The list of tracked links */
  clickTracks?: ClickTrack[];
  flags?: MessageFlagsArrayItem[];
}

/** NewsletterListElement model. */
export interface NewsletterListElement {
  /** The newsletter ID */
  newsletterId: string;
  /** Direct hyperlink to a resource */
  href: string;
  /** The newsletter name */
  name?: string;
  /** The newsletter type */
  type?: NewsletterListElementType;
  /** The newsletter status */
  status?: unknown;
  /** This describes how the content of the message was created */
  editor?: unknown;
  /** The message subject */
  subject?: string;
  /** The newsletter must be assigned to a campaign */
  campaign?: unknown;
  /** The scheduled send date and time for the newsletter in the ISO 8601 format. (ISO 8601 date-time string) */
  sendOn?: string;
  /** How the message will be delivered to the subscriber. You can specify multiple parameters. Then the system uses AND logic. */
  sendSettings?: unknown;
  /** The sending metrics */
  sendMetrics?: Record<string, unknown>;
  /** The creation date (ISO 8601 date-time string) */
  createdOn?: string;
  flags?: string;
}

/** NewsletterSendSettingsDetails model. */
export interface NewsletterSendSettingsDetails {
  /** The list of selected campaigns */
  selectedCampaigns?: unknown;
  /** The list of selected segments */
  selectedSegments?: unknown;
  /** The list of selected suppressions (suppressions exclude contacts) */
  selectedSuppressions?: unknown;
  /** The list of excluded campaigns */
  excludedCampaigns?: unknown;
  /** The list of excluded segments */
  excludedSegments?: unknown;
  /** The list of selected contacts */
  selectedContacts?: unknown;
  /** Use the time travel functionality. This means that the system will match the scheduled sending hour for the message to the time zone of each recipient. As a result, sending may take up to 24 hours. */
  timeTravel?: unknown;
  /** Use the perfect timing functionality */
  perfectTiming?: unknown;
  /** External Lexpad settings for the message, read more: [External Lexpad](https://apidocs.getresponse.com/v3/dynamic-content/external-lexpad) */
  externalLexpad?: Record<string, unknown>;
  /** The scheduled send date and time for the newsletter. **Please note:** To send your message immediately, omit the `sendOn` section */
  sendOn?: Record<string, unknown>;
}

/** NewsletterSendSettingsListing model. */
export interface NewsletterSendSettingsListing {
  /** Use the time travel functionality. This means that the system will match the scheduled sending hour for the message to the time zone of each recipient. As a result, sending may take up to 24 hours. */
  timeTravel?: unknown;
  /** Use the perfect timing functionality */
  perfectTiming?: unknown;
}

/** Search contacts who didn't open a message. */
export interface NotOpenedCondition {
  conditionType: NotOpenedConditionConditionType;
  operatorType: NotOpenedConditionOperatorType;
  /** Specifies the type of message to search for */
  operator: Record<string, unknown>;
  /** The message identifier. Required only for the operator different from 'all'. */
  scope?: string;
  /** It allows you to set a date range. For some of them `value` will be required. Examples can be found here: [API Docs](https://apidocs.getresponse.com/v3/case-study/segments-manual#not-opened-action). */
  dateOperator: NotOpenedConditionDateOperator;
  /** This field is required only for `date_from` and `last_n_days` date operators. */
  value?: Record<string, unknown>;
  /** Flag determines if current day will be included into chosen range. This flag can be used with `last_7_days`, `last_30_days`, `last_n_days`. */
  includeCurrentPeriod?: boolean;
}

/** OneTimeReportScheduling model. */
export interface OneTimeReportScheduling {
  /** The custom report frequency */
  frequency?: unknown;
  /** A field containing configuration parameters for one-time scheduling */
  oneTime?: Record<string, unknown>;
  /** Field not applicable to the selected frequency */
  recurring?: Record<string, unknown>;
}

/** OneTimeScheduling model. */
export interface OneTimeScheduling {
  /** A field containing configuration parameters for one-time scheduling */
  oneTime?: Record<string, unknown>;
  /** Field not applicable to the selected frequency */
  recurring?: Record<string, unknown>;
}

/** Search contacts who did open a message. */
export interface OpenedCondition {
  conditionType: OpenedConditionConditionType;
  operatorType: OpenedConditionOperatorType;
  operator: MessageTypeOperator;
  /** The identifier of a selected resource: autoresponder, newsletter, split test or automation message */
  value: string;
}

/** Order model. */
export interface Order {
  /** The order ID */
  orderId?: string;
  /** Direct hyperlink to a resource */
  href?: string;
  /** Create a contact by using `POST /v3/contacts`. Or, if the contact already exists, using `GET /v3/contacts` */
  contactId?: string;
  /** The external URL for an order */
  orderUrl?: string;
  /** The external ID is the identifying string or number of the order given by another software */
  externalId?: string;
  /** The total price of an order */
  totalPrice?: number;
  /** The total price tax of an order */
  totalPriceTax?: number;
  /** The order currency code (ISO 4217) */
  currency?: string;
  /** The status value */
  status?: string;
  /** Create a cart by using `POST /v3/shops/{shopId}/carts` */
  cartId?: string;
  /** The order description */
  description?: string;
  /** The shipping price for an order */
  shippingPrice?: number;
  /** The shipping address for an order */
  shippingAddress?: unknown;
  /** The billing status of an order */
  billingStatus?: string;
  /** The billing address for an order */
  billingAddress?: unknown;
  /** The exact time an order was made (ISO 8601 date-time string) */
  processedAt?: string;
  metaFields?: NewMetaField[];
}

/** OrderResponse model. */
export interface OrderResponse {
  /** The order ID */
  orderId?: string;
  /** Direct hyperlink to a resource */
  href?: string;
  /** Create a contact by using `POST /v3/contacts`. Or, if the contact already exists, using `GET /v3/contacts` */
  contactId?: string;
  /** The external URL for an order */
  orderUrl?: string;
  /** The external ID is the identifying string or number of the order given by another software */
  externalId?: string;
  /** The total price of an order */
  totalPrice?: number;
  /** The total price tax of an order */
  totalPriceTax?: number;
  /** The order currency code (ISO 4217) */
  currency?: string;
  /** The status value */
  status?: string;
  /** Create a cart by using `POST /v3/shops/{shopId}/carts` */
  cartId?: string;
  /** The order description */
  description?: string;
  /** The shipping price for an order */
  shippingPrice?: number;
  /** The shipping address for an order */
  shippingAddress?: unknown;
  /** The billing status of an order */
  billingStatus?: string;
  /** The billing address for an order */
  billingAddress?: unknown;
  /** The exact time an order was made (ISO 8601 date-time string) */
  processedAt?: string;
  metaFields?: NewMetaField[];
  selectedVariants?: OrderSelectedProductVariant[];
}

/** OrderSelectedProductVariant model. */
export interface OrderSelectedProductVariant {
  /** Direct hyperlink to a resource */
  href?: string;
  /** The ID of a selected variant. You must first create a variant using: `POST` [Create product](https://apireference.getresponse.com/#operation/createProduct) `POST` [Create product variant](https://apireference.getresponse.com/#operation/createProductVariant) or get ID from variants created already: `GET` [Get a list of product variants](https://apireference.getresponse.com/#operation/getProductVariantList) */
  variantId: string;
  /** The product variant price */
  price: number;
  /** The product variant price tax */
  priceTax?: number;
  /** The product variant quantity */
  quantity: number;
  taxes?: NewTax[];
  categories?: BaseCategory[];
}

/** PopupDetails model. */
export interface PopupDetails {
  /** The form or popup ID */
  popupId?: string;
  /** Direct hyperlink to a resource */
  href?: string;
  /** The form or popup name */
  name?: string;
  /** The form or popup status */
  status?: PopupDetailsStatus;
  /** The form or popup type */
  type?: PopupDetailsType;
  /** Direct hyperlink to a resource */
  thumbnailUrl?: string;
  /** The date (in GMT) the form or popup was created. Shown in format `ISO 8601` without timezone offset e.g. `2024-01-01T10:35:00`. (ISO 8601 date-time string) */
  createdAt?: string;
  /** The date (in GMT) the form or popup was updated. Shown in format `ISO 8601` without timezone offset e.g. `2024-01-10T10:00:00`. (ISO 8601 date-time string) */
  updatedAt?: string;
}

/** PopupGeneralPerformanceStats model. */
export interface PopupGeneralPerformanceStats {
  /** The form or popup ID */
  popupId: string;
  /** The total number of times your popup was viewed by website visitors */
  views?: number;
  /** The number of clicks */
  clicks?: number;
  /** The number of clicks divided by the number of views, shown as a percentage */
  ctr?: number;
  /** The number of leads */
  leads?: number;
}

/** PopupListItem model. */
export interface PopupListItem {
  /** The form or popup ID */
  popupId?: string;
  /** Direct hyperlink to a resource */
  href?: string;
  /** The form or popup name */
  name?: string;
  /** The form or popup status */
  status?: PopupListItemStatus;
  /** The form or popup type */
  type?: PopupListItemType;
  /** The date (in GMT) the form or popup was created. Shown in format `ISO 8601` without timezone offset e.g. `2024-01-01T10:35:00`. (ISO 8601 date-time string) */
  createdAt?: string;
  /** The date (in GMT) the form or popup was updated. Shown in format `ISO 8601` without timezone offset e.g. `2024-01-10T10:00:00`. (ISO 8601 date-time string) */
  updatedAt?: string;
  /** The landing page statistics */
  statistics?: PopupListItemStatistics;
}

/** PopupListItemStatistics model. */
export interface PopupListItemStatistics {
  /** The total number of times your popup was viewed by website visitors */
  views?: number;
  /** The total number of visitors */
  uniqueVisitors?: number;
  /** The number of leads */
  leads?: number;
  /** The number of clicks divided by the number of views, shown as a percentage */
  ctr?: number;
}

/** PredefinedField model. */
export interface PredefinedField {
  predefinedFieldId?: string;
  /** Direct hyperlink to a resource */
  href?: string;
  name?: string;
  value?: string;
  campaign?: CampaignReference;
}

/** The predefined field details. */
export interface PredefinedFieldDetails {
  predefinedFieldId?: string;
  /** Direct hyperlink to a resource */
  href?: string;
  name?: string;
  value?: string;
  campaign?: CampaignReference;
}

/** Product model. */
export interface Product {
  /** The creation date (ISO 8601 date-time string) */
  createdOn?: string;
  /** The date of the last update (ISO 8601 date-time string) */
  updatedOn?: string;
  /** The product ID */
  productId?: string;
  /** Direct hyperlink to a resource */
  href?: string;
  /** The product name */
  name?: string;
  /** The product type */
  type?: string;
  /** The external URL for the product */
  url?: string;
  /** The product vendor */
  vendor?: string;
  /** The external ID is the identifying string or number of the product given by another software */
  externalId?: string;
  categories?: NewProductCategory[];
  variants?: NewProductVariant[];
  metaFields?: NewMetaField[];
}

/** ProductCategory model. */
export interface ProductCategory {
  /** The category ID */
  categoryId?: string;
  /** Direct hyperlink to a resource */
  href?: string;
  /** The name of the category */
  name?: string;
  /** The parent category ID */
  parentId?: string;
  /** This is a default category */
  isDefault?: boolean;
  /** The external URL to the category */
  url?: string;
  /** The external ID is the identifying string or number of the category given by another software */
  externalId?: string;
  /** The creation date (ISO 8601 date-time string) */
  createdOn?: string;
  /** The date of the last update (ISO 8601 date-time string) */
  updatedOn?: string;
}

/** ProductVariant model. */
export interface ProductVariant {
  /** The product ID */
  variantId?: string;
  /** Direct hyperlink to a resource */
  href?: string;
  /** The product name */
  name?: string;
  /** The external URL to the product variant */
  url?: string;
  /** The stock-keeping unit of a variant. Must be unique within the product */
  sku?: string;
  /** The price */
  price?: number;
  /** The price including tax */
  priceTax?: number;
  /** The price before the change */
  previousPrice?: number;
  /** The price before the change including tax */
  previousPriceTax?: number;
  /** The quantity of variant items */
  quantity?: number;
  /** The position of a variant */
  position?: number;
  /** The barcode of a variant */
  barcode?: string;
  /** The external ID is the identifying string or number of the variant given by another software */
  externalId?: string;
  /** The description of a variant */
  description?: string;
  images?: NewProductVariantImage[];
  metaFields?: NewMetaField[];
  taxes?: NewTax[];
  /** The creation date (ISO 8601 date-time string) */
  createdOn?: string;
  /** The date of the last update (ISO 8601 date-time string) */
  updatedOn?: string;
}

/** Quota model. */
export interface Quota {
  /** The total size of available storage space */
  limit?: number;
  /** The currently used storage space */
  usage?: number;
}

/** RecurringScheduling model. */
export interface RecurringScheduling {
  /** Field not applicable to the selected frequency */
  oneTime?: Record<string, unknown>;
  /** A field containing configuration parameters for recurring scheduling */
  recurring?: Record<string, unknown>;
}

/** RevenueStatistics model. */
export interface RevenueStatistics {
  /** Statistics currency */
  currency?: string;
  timeSeries?: Record<string, unknown>[];
}

/** RssNewsletter model. */
export interface RssNewsletter {
  /** The RSS newsletter ID */
  rssNewsletterId: string;
  /** Direct hyperlink to a resource */
  href: string;
  /** The URL for the RSS Feed */
  rssFeedUrl?: string;
  /** The RSS message subject */
  subject?: string;
  /** How your newsletters will be seen inside the application */
  name?: string;
  /** The status of the RSS newsletter */
  status?: unknown;
  editor?: unknown;
  /** The 'From' email address used for the message */
  fromField?: unknown;
  /** The email that will be used as a reply-to address */
  replyTo?: unknown;
  content?: MessageContent;
  /** How the message will be delivered to the subscriber */
  sendSettings?: unknown;
  /** The creation date (ISO 8601 date-time string) */
  createdOn?: string;
}

/** RssNewsletterDetails model. */
export interface RssNewsletterDetails {
  /** The RSS newsletter ID */
  rssNewsletterId: string;
  /** Direct hyperlink to a resource */
  href: string;
  /** The URL for the RSS Feed */
  rssFeedUrl?: string;
  /** The RSS message subject */
  subject?: string;
  /** How your newsletters will be seen inside the application */
  name?: string;
  /** The status of the RSS newsletter */
  status?: unknown;
  editor?: unknown;
  /** The 'From' email address used for the message */
  fromField?: unknown;
  /** The email that will be used as a reply-to address */
  replyTo?: unknown;
  content?: MessageContent;
  /** How the message will be delivered to the subscriber */
  sendSettings?: unknown;
  /** The creation date (ISO 8601 date-time string) */
  createdOn?: string;
  /** The list of tracked links */
  clickTracks?: ClickTrack[];
  flags?: MessageFlagsArrayItem[];
}

/** RssNewsletterListItem model. */
export interface RssNewsletterListItem {
  /** The RSS newsletter ID */
  rssNewsletterId: string;
  /** Direct hyperlink to a resource */
  href: string;
  /** The URL for the RSS Feed */
  rssFeedUrl?: string;
  /** The RSS message subject */
  subject?: string;
  /** How your newsletters will be seen inside the application */
  name?: string;
  /** The status of the RSS newsletter */
  status?: unknown;
  editor?: unknown;
  /** The 'From' email address used for the message */
  fromField?: unknown;
  /** The email that will be used as a reply-to address */
  replyTo?: unknown;
  content?: MessageContent;
  /** How the message will be delivered to the subscriber */
  sendSettings?: unknown;
  /** The creation date (ISO 8601 date-time string) */
  createdOn?: string;
  flags?: string;
}

/** RssNewsletterListSendAsapSettings model. */
export interface RssNewsletterListSendAsapSettings {
  /** When to send the message */
  frequency: string;
  /** The filter settings for an RSS post */
  filter: RssNewsletterListSendAsapSettingsFilter;
  /** How many articles to display in a list */
  maxArticles?: number;
  selectedCampaigns?: unknown;
  selectedSegments?: unknown;
  selectedSuppressions?: unknown;
  excludedCampaigns?: unknown;
  excludedSegments?: unknown;
}

/** RssNewsletterListSendDailySettings model. */
export interface RssNewsletterListSendDailySettings {
  /** When to send the message */
  frequency: string;
  /** The filter settings for an RSS post */
  filter: RssNewsletterListSendDailySettingsFilter;
  /** How many articles to display in a list */
  maxArticles?: number;
  selectedCampaigns?: unknown;
  selectedSegments?: unknown;
  selectedSuppressions?: unknown;
  excludedCampaigns?: unknown;
  excludedSegments?: unknown;
  /** The hour when the message should be sent */
  sendAtHour: number;
}

/** RssNewsletterListSendMonthlySettings model. */
export interface RssNewsletterListSendMonthlySettings {
  /** When to send the message */
  frequency: string;
  /** The filter settings for an RSS post */
  filter: RssNewsletterListSendMonthlySettingsFilter;
  /** How many articles to display in a list */
  maxArticles?: number;
  selectedCampaigns?: unknown;
  selectedSegments?: unknown;
  selectedSuppressions?: unknown;
  excludedCampaigns?: unknown;
  excludedSegments?: unknown;
  /** The hour when the message should be sent */
  sendAtHour: number;
  /** The day of the month when the message should be sent or 31 representing last day of month */
  sendAtMonthDay: number;
}

/** RssNewsletterListSendWeeklySettings model. */
export interface RssNewsletterListSendWeeklySettings {
  /** When to send the message */
  frequency: string;
  /** The filter settings for an RSS post */
  filter: RssNewsletterListSendWeeklySettingsFilter;
  /** How many articles to display in a list */
  maxArticles?: number;
  selectedCampaigns?: unknown;
  selectedSegments?: unknown;
  selectedSuppressions?: unknown;
  excludedCampaigns?: unknown;
  excludedSegments?: unknown;
  /** The hour when the message should be sent */
  sendAtHour: number;
  /** The day of the week when the message should be sent */
  sendAtWeekDay: RssNewsletterListSendWeeklySettingsSendAtWeekDay;
}

/** RssNewsletterListing model. */
export interface RssNewsletterListing {
  /** The RSS newsletter ID */
  rssNewsletterId: string;
  /** Direct hyperlink to a resource */
  href: string;
  /** The URL for the RSS Feed */
  rssFeedUrl?: string;
  /** The RSS message subject */
  subject?: string;
  /** How your newsletters will be seen inside the application */
  name?: string;
  /** The status of the RSS newsletter */
  status?: unknown;
  editor?: unknown;
  /** The 'From' email address used for the message */
  fromField?: unknown;
  /** The email that will be used as a reply-to address */
  replyTo?: unknown;
  content?: MessageContent;
  /** How the message will be delivered to the subscriber */
  sendSettings?: unknown;
  /** The creation date (ISO 8601 date-time string) */
  createdOn?: string;
}

/** RssNewsletterSendAsapSettings model. */
export interface RssNewsletterSendAsapSettings {
  /** When to send the message */
  frequency: string;
  /** The filter settings for an RSS post */
  filter: RssNewsletterSendAsapSettingsFilter;
  /** How many articles to display in a list */
  maxArticles?: number;
  selectedCampaigns?: unknown;
  selectedSegments?: unknown;
  selectedSuppressions?: unknown;
  excludedCampaigns?: unknown;
  excludedSegments?: unknown;
  selectedContacts?: unknown;
}

/** RssNewsletterSendDailySettings model. */
export interface RssNewsletterSendDailySettings {
  /** When to send the message */
  frequency: string;
  /** The filter settings for an RSS post */
  filter: RssNewsletterSendDailySettingsFilter;
  /** How many articles to display in a list */
  maxArticles?: number;
  selectedCampaigns?: unknown;
  selectedSegments?: unknown;
  selectedSuppressions?: unknown;
  excludedCampaigns?: unknown;
  excludedSegments?: unknown;
  selectedContacts?: unknown;
  /** The hour when the message should be sent */
  sendAtHour: number;
}

/** RssNewsletterSendMonthlySettings model. */
export interface RssNewsletterSendMonthlySettings {
  /** When to send the message */
  frequency: string;
  /** The filter settings for an RSS post */
  filter: RssNewsletterSendMonthlySettingsFilter;
  /** How many articles to display in a list */
  maxArticles?: number;
  selectedCampaigns?: unknown;
  selectedSegments?: unknown;
  selectedSuppressions?: unknown;
  excludedCampaigns?: unknown;
  excludedSegments?: unknown;
  selectedContacts?: unknown;
  /** The hour when the message should be sent */
  sendAtHour: number;
  /** The day of the month when the message should be sent or 31 representing last day of month */
  sendAtMonthDay: Record<string, unknown>;
}

/** RssNewsletterSendSettingsDetails model. */
export interface RssNewsletterSendSettingsDetails {
  /** When to send the message */
  frequency: string;
  /** The filter settings for an RSS post */
  filter: RssNewsletterSendSettingsDetailsFilter;
  /** How many articles to display in a list */
  maxArticles?: number;
  selectedCampaigns?: unknown;
  selectedSegments?: unknown;
  selectedSuppressions?: unknown;
  excludedCampaigns?: unknown;
  excludedSegments?: unknown;
  selectedContacts?: unknown;
}

/** RssNewsletterSendSettingsListing model. */
export interface RssNewsletterSendSettingsListing {
  /** When to send the message */
  frequency: string;
  /** The filter settings for an RSS post */
  filter: RssNewsletterSendSettingsListingFilter;
  /** How many articles to display in a list */
  maxArticles?: number;
  selectedCampaigns?: unknown;
  selectedSegments?: unknown;
  selectedSuppressions?: unknown;
  excludedCampaigns?: unknown;
  excludedSegments?: unknown;
}

/** RssNewsletterSendWeeklySettings model. */
export interface RssNewsletterSendWeeklySettings {
  /** When to send the message */
  frequency: string;
  /** The filter settings for an RSS post */
  filter: RssNewsletterSendWeeklySettingsFilter;
  /** How many articles to display in a list */
  maxArticles?: number;
  selectedCampaigns?: unknown;
  selectedSegments?: unknown;
  selectedSuppressions?: unknown;
  excludedCampaigns?: unknown;
  excludedSegments?: unknown;
  selectedContacts?: unknown;
  /** The hour when the message should be sent */
  sendAtHour: number;
  /** The day of the week when the message should be sent */
  sendAtWeekDay: RssNewsletterSendWeeklySettingsSendAtWeekDay;
}

/** Search contacts by scoring. */
export interface ScoringCondition {
  conditionType: ScoringConditionConditionType;
  operatorType: ScoringConditionOperatorType;
  /** The relational operator. Required for the operatorType=numeric_operator. */
  operator?: ScoringConditionOperator;
  /** This field is required for the relational operator, and prohibited for the not_exists operator type */
  value?: number;
}

/** SearchContactSection model. */
export interface SearchContactSection {
  /** An array of campaign identifiers */
  campaignIdsList: string[];
  logicOperator: SearchContactSectionLogicOperator;
  /** Defining whether or not a subscriber is in an autoresponder cycle */
  subscriberCycle: SearchContactSectionSubscriberCycleItem[];
  /** One of the search contact conditions */
  conditions?: ConditionType[];
  /** Matches the matching period */
  subscriptionDate: SearchContactSectionSubscriptionDate;
}

/** SearchContactsBySearchForm model. */
export interface SearchContactsBySearchForm {
  /** Only one subscription status */
  subscribersType: SearchContactsBySearchFormSubscribersTypeItem[];
  /** Match 'any' (`or` value) or 'all' (`and` value) of the following conditions */
  sectionLogicOperator: SearchContactsBySearchFormSectionLogicOperator;
  section: SearchContactSection[];
}

/** SearchContactsConditionsDetails model. */
export interface SearchContactsConditionsDetails {
  /** Match 'any' (`or` value) or 'all' (`and` value) of the following conditions */
  sectionLogicOperator: SearchContactsConditionsDetailsSectionLogicOperator;
  section: SearchContactSection[];
}

/** Search contact details. */
export interface SearchContactsDetails {
  /** Only one subscription status */
  subscribersType?: SearchContactsDetailsSubscribersTypeItem[];
  /** Match 'any' (`or` value) or 'all' (`and` value) of the following conditions */
  sectionLogicOperator: SearchContactsDetailsSectionLogicOperator;
  section: SearchContactSection[];
  /** The unique search-contact identifier */
  searchContactId: string;
  /** The unique name of search-contact */
  name: string;
  /** The UTC date time format ISO 8601, e.g. 2018-04-10T10:02:57+0000 (ISO 8601 date-time string) */
  createdOn: string;
  /** Direct hyperlink to a resource */
  href: string;
}

/** SearchedContactDetails model. */
export interface SearchedContactDetails {
  /** The contact identifier */
  contactId?: string;
  /** The contact description */
  name?: string;
  email?: string;
  origin?: SearchedContactDetailsOrigin;
  dayOfCycle?: string;
  /** ISO 8601 date-time string. */
  createdOn?: string;
  campaign?: CampaignReference;
  score?: string;
  reason?: SearchedContactDetailsReason;
  /** ISO 8601 date-time string. */
  deletedOn?: string;
}

/** SectionAllTimeSubscriptionDate model. */
export interface SectionAllTimeSubscriptionDate {
  /** An array of campaign identifiers */
  campaignIdsList: string[];
  logicOperator: SectionAllTimeSubscriptionDateLogicOperator;
  /** Defining whether or not a subscriber is in an autoresponder cycle */
  subscriberCycle: SectionAllTimeSubscriptionDateSubscriberCycleItem[];
  /** One of the search contact conditions */
  conditions?: ConditionType[];
  /** Matches the matching period */
  subscriptionDate: SectionAllTimeSubscriptionDateSubscriptionDate;
}

/** SectionCustomSubscriptionDate model. */
export interface SectionCustomSubscriptionDate {
  /** An array of campaign identifiers */
  campaignIdsList: string[];
  logicOperator: SectionCustomSubscriptionDateLogicOperator;
  /** Defining whether or not a subscriber is in an autoresponder cycle */
  subscriberCycle: SectionCustomSubscriptionDateSubscriberCycleItem[];
  /** One of the search contact conditions */
  conditions?: ConditionType[];
  /** Matches the matching period */
  subscriptionDate: SectionCustomSubscriptionDateSubscriptionDate;
  customDate: CustomDateRange;
}

/** SectionLast2MonthsSubscriptionDate model. */
export interface SectionLast2MonthsSubscriptionDate {
  /** An array of campaign identifiers */
  campaignIdsList: string[];
  logicOperator: SectionLast2MonthsSubscriptionDateLogicOperator;
  /** Defining whether or not a subscriber is in an autoresponder cycle */
  subscriberCycle: SectionLast2MonthsSubscriptionDateSubscriberCycleItem[];
  /** One of the search contact conditions */
  conditions?: ConditionType[];
  /** Matches the matching period */
  subscriptionDate: SectionLast2MonthsSubscriptionDateSubscriptionDate;
}

/** SectionLast30DaysSubscriptionDate model. */
export interface SectionLast30DaysSubscriptionDate {
  /** An array of campaign identifiers */
  campaignIdsList: string[];
  logicOperator: SectionLast30DaysSubscriptionDateLogicOperator;
  /** Defining whether or not a subscriber is in an autoresponder cycle */
  subscriberCycle: SectionLast30DaysSubscriptionDateSubscriberCycleItem[];
  /** One of the search contact conditions */
  conditions?: ConditionType[];
  /** Matches the matching period */
  subscriptionDate: SectionLast30DaysSubscriptionDateSubscriptionDate;
}

/** SectionLast7DaysSubscriptionDate model. */
export interface SectionLast7DaysSubscriptionDate {
  /** An array of campaign identifiers */
  campaignIdsList: string[];
  logicOperator: SectionLast7DaysSubscriptionDateLogicOperator;
  /** Defining whether or not a subscriber is in an autoresponder cycle */
  subscriberCycle: SectionLast7DaysSubscriptionDateSubscriberCycleItem[];
  /** One of the search contact conditions */
  conditions?: ConditionType[];
  /** Matches the matching period */
  subscriptionDate: SectionLast7DaysSubscriptionDateSubscriptionDate;
}

/** SectionLastMonthSubscriptionDate model. */
export interface SectionLastMonthSubscriptionDate {
  /** An array of campaign identifiers */
  campaignIdsList: string[];
  logicOperator: SectionLastMonthSubscriptionDateLogicOperator;
  /** Defining whether or not a subscriber is in an autoresponder cycle */
  subscriberCycle: SectionLastMonthSubscriptionDateSubscriberCycleItem[];
  /** One of the search contact conditions */
  conditions?: ConditionType[];
  /** Matches the matching period */
  subscriptionDate: SectionLastMonthSubscriptionDateSubscriptionDate;
}

/** SectionLastWeekSubscriptionDate model. */
export interface SectionLastWeekSubscriptionDate {
  /** An array of campaign identifiers */
  campaignIdsList: string[];
  logicOperator: SectionLastWeekSubscriptionDateLogicOperator;
  /** Defining whether or not a subscriber is in an autoresponder cycle */
  subscriberCycle: SectionLastWeekSubscriptionDateSubscriberCycleItem[];
  /** One of the search contact conditions */
  conditions?: ConditionType[];
  /** Matches the matching period */
  subscriptionDate: SectionLastWeekSubscriptionDateSubscriptionDate;
}

/** SectionThisMonthSubscriptionDate model. */
export interface SectionThisMonthSubscriptionDate {
  /** An array of campaign identifiers */
  campaignIdsList: string[];
  logicOperator: SectionThisMonthSubscriptionDateLogicOperator;
  /** Defining whether or not a subscriber is in an autoresponder cycle */
  subscriberCycle: SectionThisMonthSubscriptionDateSubscriberCycleItem[];
  /** One of the search contact conditions */
  conditions?: ConditionType[];
  /** Matches the matching period */
  subscriptionDate: SectionThisMonthSubscriptionDateSubscriptionDate;
}

/** SectionThisWeekSubscriptionDate model. */
export interface SectionThisWeekSubscriptionDate {
  /** An array of campaign identifiers */
  campaignIdsList: string[];
  logicOperator: SectionThisWeekSubscriptionDateLogicOperator;
  /** Defining whether or not a subscriber is in an autoresponder cycle */
  subscriberCycle: SectionThisWeekSubscriptionDateSubscriberCycleItem[];
  /** One of the search contact conditions */
  conditions?: ConditionType[];
  /** Matches the matching period */
  subscriptionDate: SectionThisWeekSubscriptionDateSubscriptionDate;
}

/** SectionTodaySubscriptionDate model. */
export interface SectionTodaySubscriptionDate {
  /** An array of campaign identifiers */
  campaignIdsList: string[];
  logicOperator: SectionTodaySubscriptionDateLogicOperator;
  /** Defining whether or not a subscriber is in an autoresponder cycle */
  subscriberCycle: SectionTodaySubscriptionDateSubscriberCycleItem[];
  /** One of the search contact conditions */
  conditions?: ConditionType[];
  /** Matches the matching period */
  subscriptionDate: SectionTodaySubscriptionDateSubscriptionDate;
}

/** SectionYesterdaySubscriptionDate model. */
export interface SectionYesterdaySubscriptionDate {
  /** An array of campaign identifiers */
  campaignIdsList: string[];
  logicOperator: SectionYesterdaySubscriptionDateLogicOperator;
  /** Defining whether or not a subscriber is in an autoresponder cycle */
  subscriberCycle: SectionYesterdaySubscriptionDateSubscriberCycleItem[];
  /** One of the search contact conditions */
  conditions?: ConditionType[];
  /** Matches the matching period */
  subscriptionDate: SectionYesterdaySubscriptionDateSubscriptionDate;
}

/** SendNewsletterDraft model. */
export interface SendNewsletterDraft {
  /** The message identifier (equals to newsletterId) */
  messageId: string;
  /** How the message will be delivered to the subscriber */
  sendSettings: unknown;
}

/** SendSmsToContacts model. */
export interface SendSmsToContacts {
  /** The SMS message name */
  name: string;
  /** The SMS message content */
  content: string;
  /** The recipient type. To send a text message to contacts in your list, select `contacts`. To message contacts who are not in any of your lists, select `importedNumbers` */
  recipientsType: SendSmsToContactsRecipientsType;
  /** How the message will be delivered to the subscriber */
  sendSettings: Record<string, unknown>;
}

/** SendSmsToImportedNumbers model. */
export interface SendSmsToImportedNumbers {
  /** The SMS message name */
  name: string;
  /** The SMS message content */
  content: string;
  /** The recipient type. To send a text message to contacts in your list, select `contacts`. To message contacts who are not in any of your lists, select `importedNumbers` */
  recipientsType: SendSmsToImportedNumbersRecipientsType;
  /** How the message will be delivered to the subscriber */
  sendSettings: Record<string, unknown>;
}

/** SendingLimitsListItem model. */
export interface SendingLimitsListItem {
  /** Time frame, measured in seconds */
  timeFrame?: number;
  /** The number of email sends available within a given time frame */
  limit?: number;
  /** The number of email sends used within the given time frame */
  used?: number;
}

/** Shop model. */
export interface Shop {
  /** The creation date (ISO 8601 date-time string) */
  createdOn?: string;
  /** The date of the last update (ISO 8601 date-time string) */
  updatedOn?: string;
  /** The shop ID */
  shopId?: string;
  /** Direct hyperlink to a resource */
  href?: string;
  /** The shop name */
  name?: string;
  /** The language locale (ISO 639-1) */
  locale?: string;
  /** The currency code (ISO 4217) */
  currency?: string;
}

/** ShopDetails model. */
export interface ShopDetails {
  /** The creation date (ISO 8601 date-time string) */
  createdOn?: string;
  /** The date of the last update (ISO 8601 date-time string) */
  updatedOn?: string;
  /** The shop ID */
  shopId?: string;
  /** Direct hyperlink to a resource */
  href?: string;
  /** The shop name */
  name?: string;
  /** The language locale (ISO 639-1) */
  locale?: string;
  /** The currency code (ISO 4217) */
  currency?: string;
  /** Amount of products in the shop */
  productCount?: number;
  /** Total revenue from purchased products */
  productRevenue?: number;
  /** The revenue currency code (ISO 4217) */
  revenueCurrency?: string;
}

/** SmsAutomationDetails model. */
export interface SmsAutomationDetails {
  /** The automated SMS message ID */
  smsId: string;
  /** Direct hyperlink to a resource */
  href?: string;
  /** The automated SMS message name */
  name?: string;
  /** The campaign the SMS message is in */
  campaign?: unknown;
  /** The date the automated SMS message was last modified on, shown in `ISO 8601` date and time format. e.g. `2022-04-10T10:02:57+0000` (ISO 8601 date-time string) */
  modifiedOn?: string;
  /** The status of of the automated SMS message */
  status?: SmsAutomationDetailsStatus;
  /** Automate SMS message statistics */
  statistics?: unknown;
  /** The name of the sender of the automated SMS message */
  senderName?: string;
  /** Information is the automated SMS message contains links */
  hasLinks?: boolean;
  /** Details of the workflows in which the given automated SMS is used */
  workflows?: unknown[];
  /** Details of links attached to automated SMS message */
  clickTracks?: unknown[];
  /** The automated SMS message content */
  content?: string;
}

/** SmsAutomationListItem model. */
export interface SmsAutomationListItem {
  /** The automated SMS message ID */
  smsId: string;
  /** Direct hyperlink to a resource */
  href?: string;
  /** The automated SMS message name */
  name?: string;
  /** The campaign the SMS message is in */
  campaign?: unknown;
  /** The date the automated SMS message was last modified on, shown in `ISO 8601` date and time format. e.g. `2022-04-10T10:02:57+0000` (ISO 8601 date-time string) */
  modifiedOn?: string;
  /** The status of of the automated SMS message */
  status?: SmsAutomationListItemStatus;
  /** Automate SMS message statistics */
  statistics?: unknown;
  /** The name of the sender of the automated SMS message */
  senderName?: string;
  /** Information is the automated SMS message contains links */
  hasLinks?: boolean;
}

/** SmsDetails model. */
export interface SmsDetails {
  /** The SMS message ID */
  smsId?: string;
  /** Direct hyperlink to a resource */
  href?: string;
  /** The SMS message name */
  name?: string;
  /** The SMS message campaign */
  campaign?: unknown;
  /** The date the SMS message was last modified on, shown in `ISO 8601` date and time format. e.g. `2022-04-10T10:02:57+0000` (ISO 8601 date-time string) */
  modifiedOn?: string;
  /** The SMS message type */
  type?: SmsDetailsType;
  /** SMS message send date details */
  sendOn?: Record<string, unknown>;
  /** Type of SMS message recipients */
  recipientsType?: SmsDetailsRecipientsType;
  /** The SMS message sender name */
  senderName?: string;
  /** The SMS message content */
  content?: string;
  /** Information about sending process */
  sendMetrics?: Record<string, unknown>;
  /** Message statistics */
  statistics?: unknown;
  /** How the message will be delivered to the subscriber */
  sendSettings?: Record<string, unknown>;
  /** Details of links attached to SMS message. Maximum 20 links will be returned. */
  clickTracks?: unknown[];
}

/** Find contacts who clicked a link from an SMS */
export interface SmsLinkClickedCondition {
  conditionType: SmsLinkClickedConditionConditionType;
  /** The SMS message ID */
  smsId: string;
  /** The click track ID */
  clickTrackId: string;
}

/** Find contacts who didn't click a link from an SMS */
export interface SmsLinkNotClickedCondition {
  conditionType: SmsLinkNotClickedConditionConditionType;
  /** The SMS message ID */
  smsId: string;
  /** The click track ID */
  clickTrackId: string;
}

/** SmsListItem model. */
export interface SmsListItem {
  /** The SMS message ID */
  smsId?: string;
  /** Direct hyperlink to a resource */
  href?: string;
  /** The SMS message name */
  name?: string;
  /** The SMS message campaign */
  campaign?: unknown;
  /** The date the SMS message was last modified on, shown in `ISO 8601` date and time format. e.g. `2022-04-10T10:02:57+0000` (ISO 8601 date-time string) */
  modifiedOn?: string;
  /** The SMS message type */
  type?: SmsListItemType;
  /** SMS message send date details */
  sendOn?: Record<string, unknown>;
  /** Type of SMS message recipients */
  recipientsType?: SmsListItemRecipientsType;
  /** The SMS message sender name */
  senderName?: string;
  /** The SMS message content */
  content?: string;
  /** Information about sending process */
  sendMetrics?: Record<string, unknown>;
  /** Message statistics */
  statistics?: unknown;
}

/** SmsSenderName model. */
export interface SmsSenderName {
  /** The sender name id */
  senderNameId?: string;
  /** The sender name */
  name?: string;
  /** Status of the sender name */
  status?: unknown;
  /** Is the sender name default */
  isDefault?: boolean;
}

/** Find contacts who were sent an SMS */
export interface SmsSentCondition {
  conditionType: SmsSentConditionConditionType;
  /** The SMS message ID */
  smsId: string;
  /** Specify the delivery status. Omit this field if the delivery status is not relevant. */
  deliveryStatus?: SmsSentConditionDeliveryStatus;
}

/** SmsStats model. */
export interface SmsStats {
  /** The SMS message ID */
  smsId: string;
  /** The number of SMS messages sent */
  totalSms?: number;
  /** The number of recipients */
  totalRecipients?: number;
  /** The number of link clicks from an SMS message */
  totalClicks?: number;
  /** The number of total unique link clicks from an SMS message */
  totalUniqueClicks?: number;
  /** The number of opt-outs from an SMS message */
  totalUnsubscribes?: number;
  /** The number of delivered SMS messages */
  totalDelivered?: number;
  /** Cost details of a specific SMS */
  totalPrice?: Record<string, unknown>;
  /** Link details */
  link?: Record<string, unknown>;
  /** SMS message statistics per country */
  countryStatistics?: Record<string, unknown>;
}

/** Splittest model. */
export interface Splittest {
  /** A/B test ID */
  splittestId?: string;
  /** Direct hyperlink to a resource */
  href?: string;
  /** A/B test name */
  name?: string;
  /** A/B test campaign */
  campaign?: CampaignReference;
  /** A/B test status */
  status?: SplittestStatus;
  /** A/B test winning criteria */
  winningCriteria?: SplittestWinningCriteria;
  /** A/B test wining target */
  winningTarget?: string;
  /** A/B test stage */
  stage?: SplittestStage;
  /** A/B test type */
  type?: SplittestType;
  /** A/B test sample percentage */
  samplingPercentage?: string;
  /** A/B test sampling time in seconds */
  samplingTime?: string;
  /** The method of choosing the winning A/B test */
  chooseWinning?: SplittestChooseWinning;
  /** The open rate of the winning A/B test */
  winningScoreOpens?: string;
  /** The click rate of the winning A/B test */
  winningScoreClicks?: string;
  /** The delivery rate of the winning A/B test */
  winningDelivered?: string;
  /** The date for wchich the winning A/B test was scheduled (ISO 8601 date-time string) */
  winningScheduleOn?: string;
  /** The date of the next step in the A/B test (ISO 8601 date-time string) */
  nextStepOn?: string;
  /** The date when the A/B test was skipped (ISO 8601 date-time string) */
  evaluationSkippedOn?: string;
  /** The date when the A/B test was canceled (ISO 8601 date-time string) */
  canceledOn?: string;
  /** The date when the A/B test was created (ISO 8601 date-time string) */
  createdOn?: string;
  /** The newsletters that are associated with the A/B test */
  newsletters?: SplittestNewsletter[];
  /** The send settings for the A/B test */
  sendSettings?: Record<string, unknown>;
}

/** SplittestNewsletter model. */
export interface SplittestNewsletter {
  /** The newsletter ID */
  newsletterId?: string;
  /** The direct newsletter URL */
  href?: string;
  /** The newsletter name */
  name?: string;
  /** The newsletter subject */
  subject?: string;
  /** The \"From\" address for the newsletter */
  fromField?: FromFieldReference;
  /** The status of the newsletter */
  status?: SplittestNewsletterStatus;
  /** The date when the newsletter was sent (ISO 8601 date-time string) */
  sendOn?: string;
  /** The newsletter sample targets */
  samplingTargets?: string;
  /** The newsletter sample delivery */
  samplingDelivered?: string;
  /** The newsletter open rate */
  scoreOpens?: string;
  /** The newsletter click rate */
  scoreClicks?: string;
}

/** StandardSubscriberActivityReportDetails model. */
export interface StandardSubscriberActivityReportDetails {
  /** The custom report ID */
  customReportId?: string;
  /** The custom report name */
  name?: string;
  /** The direct hyperlink to a resource */
  href?: string;
  /** The custom report type */
  type?: unknown;
  /** Parameters responsible for defining the reporting period */
  scheduling?: Record<string, unknown>;
  /** Files that have been generated for the given report */
  files?: Record<string, unknown>[];
  /** Custom report creation date (ISO 8601 date-time string) */
  createdAt?: string;
  /** Custom report generation date (ISO 8601 date-time string) */
  generatedAt?: string;
  /** Filters used to narrow down the report data */
  filters?: Record<string, unknown>;
}

/** SubscribersTypeEnumForSearching model. */
export interface SubscribersTypeEnumForSearching {
  /** Only one subscription status */
  subscribersType?: SubscribersTypeEnumForSearchingSubscribersTypeItem[];
}

/** SubscribersTypeEnumForSegments model. */
export interface SubscribersTypeEnumForSegments {
  /** Only one subscription status */
  subscribersType?: SubscribersTypeEnumForSegmentsSubscribersTypeItem[];
}

/** SubscriptionConfirmationBody model. */
export interface SubscriptionConfirmationBody {
  /** Subscription confirmation subject ID */
  subscriptionConfirmationBodyId?: string;
  /** Name */
  name?: string;
  /** Plain text content equivalent of confirmation message */
  contentPlain?: string;
  /** HTML content of confirmation message */
  contentHtml?: string;
}

/** SubscriptionConfirmationSubject model. */
export interface SubscriptionConfirmationSubject {
  /** Subscription confirmation subject ID */
  subscriptionConfirmationSubjectId?: string;
  /** Subject */
  subject?: string;
  /** Is private */
  isPrivate?: unknown;
}

/** Use this to find a contact by subscription date, use. */
export interface SubscriptionDateCondition {
  conditionType: SubscriptionDateConditionConditionType;
  operatorType: SubscriptionDateConditionOperatorType;
  operator: SubscriptionDateConditionOperator;
  value: Record<string, unknown>;
}

/** The subscription method. */
export interface SubscriptionMethodCondition {
  conditionType: SubscriptionMethodConditionConditionType;
  method: SubscriptionMethodConditionMethod;
  /** The property required for the webform subscription method. If it equals webforms, webformsv2 or popups, additonal property value is needed. */
  webformType?: SubscriptionMethodConditionWebformType;
  /** The field required for `import`, `landing_page`, `webinar` and `website_builder_elegant`, optional for the `webform` method */
  value?: Record<string, unknown>;
}

/** SubscriptionRejectionsReportDetails model. */
export interface SubscriptionRejectionsReportDetails {
  /** The custom report ID */
  customReportId?: string;
  /** The custom report name */
  name?: string;
  /** The direct hyperlink to a resource */
  href?: string;
  /** The custom report type */
  type?: unknown;
  /** Parameters responsible for defining the reporting period */
  scheduling?: Record<string, unknown>;
  /** Files that have been generated for the given report */
  files?: Record<string, unknown>[];
  /** Custom report creation date (ISO 8601 date-time string) */
  createdAt?: string;
  /** Custom report generation date (ISO 8601 date-time string) */
  generatedAt?: string;
  /** Filters used to narrow down the report data */
  filters?: Record<string, unknown>;
}

/** Suppression model. */
export interface Suppression {
  /** The suppression ID */
  suppressionId: string;
  /** The suppression name */
  name?: string;
  /** Created on DateTime in the ISO8601 format (ISO 8601 date-time string) */
  createdOn?: string;
  /** Direct hyperlink to a resource */
  href?: string;
}

/** SuppressionDetails model. */
export interface SuppressionDetails {
  /** The suppression ID */
  suppressionId: string;
  /** The name of the suppression list */
  name?: string;
  /** Created on DateTime in the ISO8601 format (ISO 8601 date-time string) */
  createdOn?: string;
  /** Direct hyperlink to a resource */
  href?: string;
  masks?: string[];
}

/** Tag model. */
export interface Tag {
  /** The tag name */
  name?: string;
  /** The tag color (deprecated) */
  color?: string;
  /** The tag ID */
  tagId?: string;
  /** The direct hyperlink to a resource */
  href?: string;
  /** ISO 8601 date-time string. */
  createdAt?: string;
}

/** Search contacts by tag. */
export interface TagCondition {
  conditionType: TagConditionConditionType;
  /** The operator for the existence of a property */
  operatorType: TagConditionOperatorType;
  /** This operator verifies whether the property you are looking for exists or not */
  operator: TagConditionOperator;
  /** The tag identifier */
  value: string;
}

/** TagDetails model. */
export interface TagDetails {
  /** The tag name */
  name?: string;
  /** The tag color (deprecated) */
  color?: string;
  /** The tag ID. */
  tagId?: string;
  /** ISO 8601 date-time string. */
  createdAt?: string;
}

/** Tax model. */
export interface Tax {
  /** The tax ID */
  taxId?: string;
  /** Direct hyperlink to a resource */
  href?: string;
  /** The tax name */
  name?: string;
  /** The rate value */
  rate?: number;
  /** The creation date (ISO 8601 date-time string) */
  createdOn?: string;
  /** The date of the last update (ISO 8601 date-time string) */
  updatedOn?: string;
}

/** TemplateContent model. */
export interface TemplateContent {
  /** The 'From' address ID to be used as the message sender */
  fromField: unknown;
  /** The 'From' address ID to be used as the Reply-to */
  replyTo?: unknown;
  /** The tag ID used for statistical data collection */
  tag?: unknown;
  recipients: TransactionalEmailRecipients;
  /** The message content type */
  contentType: TemplateContentContentType;
  attachments?: TransactionalEmailAttachment[];
  /** The message template. At least templateId is required */
  template: Record<string, unknown>;
}

/** TimeZone model. */
export interface TimeZone {
  /** Time zone ID: [Link to resource](https://apireference.getresponse.com/#operation/getTimezones) */
  timeZoneId: number;
}

/** Timezone model. */
export interface Timezone {
  timezoneId: number;
  /** Time zone name as defined by https://en.wikipedia.org/wiki/List_of_tz_database_time_zones */
  name?: string;
  offset?: string;
  country?: string;
}

/** TimezoneCountry model. */
export interface TimezoneCountry {
  country?: string;
}

/** TimezoneId model. */
export interface TimezoneId {
  timezoneId?: number;
}

/** TimezoneName model. */
export interface TimezoneName {
  /** Time zone name as defined by https://en.wikipedia.org/wiki/List_of_tz_database_time_zones */
  name?: string;
}

/** TimezoneOffset model. */
export interface TimezoneOffset {
  offset?: string;
}

/** Tracking model. */
export interface Tracking {
  grid?: string;
  snippet?: string;
  snippetV2?: string;
}

/** TransactionalEmail model. */
export interface TransactionalEmail {
  transactionalEmailId?: string;
}

/** TransactionalEmailAttachment model. */
export interface TransactionalEmailAttachment {
  /** The attachment file name */
  fileName: string;
  /** The MIME attachment type */
  mimeType: string;
  /** The base64-encoded attachment */
  content: string;
}

/** TransactionalEmailBounceReportDetails model. */
export interface TransactionalEmailBounceReportDetails {
  /** The custom report ID */
  customReportId?: string;
  /** The custom report name */
  name?: string;
  /** The direct hyperlink to a resource */
  href?: string;
  /** The custom report type */
  type?: unknown;
  /** Parameters responsible for defining the reporting period */
  scheduling?: Record<string, unknown>;
  /** Files that have been generated for the given report */
  files?: Record<string, unknown>[];
  /** Custom report creation date (ISO 8601 date-time string) */
  createdAt?: string;
  /** Custom report generation date (ISO 8601 date-time string) */
  generatedAt?: string;
  /** Filters used to narrow down the report data */
  filters?: Record<string, unknown>;
}

/** TransactionalEmailContent model. */
export interface TransactionalEmailContent {
  subject?: string;
  attachments?: TransactionalEmailAttachment[];
  /** The message content. At least one field is required. The maximum combined size of plain text and HTML is 16MB */
  content: Record<string, unknown>;
}

/** TransactionalEmailDetails model. */
export interface TransactionalEmailDetails {
  transactionalEmailId: string;
  /** The 'From' address ID to be used as the message sender */
  fromField: unknown;
  /** The 'From' address ID to be used as the Reply-to */
  replyTo?: unknown;
  subject: string;
  /** The tag ID used for statistical data collection */
  tag?: unknown;
  recipients: unknown;
  /** Direct hyperlink to a resource */
  href?: string;
}

/** TransactionalEmailListElement model. */
export interface TransactionalEmailListElement {
  transactionalEmailId: string;
  fromField: FromFieldReference;
  recipients: unknown;
  subject: string;
  tag?: TransactionalEmailTag;
  /** Direct hyperlink to a resource */
  href?: string;
}

/** TransactionalEmailRecipient model. */
export interface TransactionalEmailRecipient {
  email: string;
  name?: string;
  status?: TransactionalEmailRecipientStatus;
}

/** TransactionalEmailRecipientClickedLink model. */
export interface TransactionalEmailRecipientClickedLink {
  url?: string;
  /** ISO 8601 date-time string. */
  clickedOn?: string;
}

/** TransactionalEmailRecipientDetails model. */
export interface TransactionalEmailRecipientDetails {
  email: string;
  name?: string;
  status?: TransactionalEmailRecipientDetailsStatus;
  statuses?: TransactionalEmailRecipientStatuses;
  clickedLinks?: TransactionalEmailRecipientClickedLink[];
}

/** TransactionalEmailRecipientSentOnStatus model. */
export interface TransactionalEmailRecipientSentOnStatus {
  /** ISO 8601 date-time string. */
  sentOn?: string;
}

/** TransactionalEmailRecipientStatuses model. */
export interface TransactionalEmailRecipientStatuses {
  /** ISO 8601 date-time string. */
  sentOn?: string;
  /** ISO 8601 date-time string. */
  rejectedOn?: string;
  /** ISO 8601 date-time string. */
  openedOn?: string;
  /** ISO 8601 date-time string. */
  bouncedOn?: string;
  /** ISO 8601 date-time string. */
  complainedOn?: string;
}

/** TransactionalEmailRecipientTo model. */
export interface TransactionalEmailRecipientTo {
  email: string;
  name?: string;
  status?: TransactionalEmailRecipientToStatus;
  /** The first time this address appeared in your system (ISO 8601 date-time string) */
  validSince?: string;
}

/** A field containing the message recipients. You can enter up to 8 recipients. */
export interface TransactionalEmailRecipients {
  to: TransactionalEmailRecipientTo;
  cc?: TransactionalEmailRecipient[];
  bcc?: TransactionalEmailRecipient[];
}

/** TransactionalEmailRecipientsDetails model. */
export interface TransactionalEmailRecipientsDetails {
  to: TransactionalEmailRecipientDetails;
  cc?: TransactionalEmailRecipientDetails[];
  bcc?: TransactionalEmailRecipientDetails[];
}

/** TransactionalEmailStatistics model. */
export interface TransactionalEmailStatistics {
  /** The statistics time frame in the ISO 8601 date format with duration interval */
  timeFrame?: string;
  sent?: number;
  opened?: number;
  bounced?: number;
  complaint?: number;
  clicks?: number;
}

/** TransactionalEmailTag model. */
export interface TransactionalEmailTag {
  tagId: string;
}

/** The template content */
export interface TransactionalEmailTemplate {
  attachments?: TransactionalEmailAttachment[];
  /** The message template. At least templateId is required */
  template: Record<string, unknown>;
}

/** The template content. At least one field is required */
export interface TransactionalEmailTemplateContent {
  /** The plain text equivalent of template content */
  plain?: string;
  /** The template content in HTML */
  html?: string;
}

/** TransactionalEmailsTemplateDetails model. */
export interface TransactionalEmailsTemplateDetails {
  /** Transactional email template ID */
  templateId?: string;
  /** Direct hyperlink to a resource */
  href?: string;
  /** The template subject */
  subject?: string;
  /** The creation date (ISO 8601 date-time string) */
  createdOn?: string;
  /** The date of the last template update (ISO 8601 date-time string) */
  updatedOn?: string;
  /** The Editor type */
  editor?: unknown;
  content?: TransactionalEmailTemplateContent;
}

/** TransactionalEmailsTemplateListElement model. */
export interface TransactionalEmailsTemplateListElement {
  /** Transactional email template ID */
  templateId?: string;
  /** Direct hyperlink to a resource */
  href?: string;
  /** The template subject */
  subject?: string;
  /** The creation date (ISO 8601 date-time string) */
  createdOn?: string;
  /** The date of the last template update (ISO 8601 date-time string) */
  updatedOn?: string;
  /** The Editor type */
  editor?: unknown;
}

/** TriggerCustomEvent model. */
export interface TriggerCustomEvent {
  /** The name of custom event. Custom event with this name must already exist */
  name: string;
  /** The contact ID */
  contactId: string;
  /** The attributes for the trigger */
  attributes?: TriggerCustomEventAttribute[];
}

/** TriggerCustomEventAttribute model. */
export interface TriggerCustomEventAttribute {
  /** The name of the attribute. It must be already defined for the custom event */
  name: string;
  value: Record<string, unknown>;
}

/** UnconfirmedContactsStatsReportDetails model. */
export interface UnconfirmedContactsStatsReportDetails {
  /** The custom report ID */
  customReportId?: string;
  /** The custom report name */
  name?: string;
  /** The direct hyperlink to a resource */
  href?: string;
  /** The custom report type */
  type?: unknown;
  /** Parameters responsible for defining the reporting period */
  scheduling?: Record<string, unknown>;
  /** Files that have been generated for the given report */
  files?: Record<string, unknown>[];
  /** Custom report creation date (ISO 8601 date-time string) */
  createdAt?: string;
  /** Custom report generation date (ISO 8601 date-time string) */
  generatedAt?: string;
  /** Filters used to narrow down the report data */
  filters?: Record<string, unknown>;
}

/** UnsubscribeContactsListsReportDetails model. */
export interface UnsubscribeContactsListsReportDetails {
  /** The custom report ID */
  customReportId?: string;
  /** The custom report name */
  name?: string;
  /** The direct hyperlink to a resource */
  href?: string;
  /** The custom report type */
  type?: unknown;
  /** Parameters responsible for defining the reporting period */
  scheduling?: Record<string, unknown>;
  /** Files that have been generated for the given report */
  files?: Record<string, unknown>[];
  /** Custom report creation date (ISO 8601 date-time string) */
  createdAt?: string;
  /** Custom report generation date (ISO 8601 date-time string) */
  generatedAt?: string;
  /** Filters used to narrow down the report data */
  filters?: Record<string, unknown>;
}

/** UpdateAccount model. */
export interface UpdateAccount {
  /** Account ID */
  accountId?: string;
  /** Email */
  email?: string;
  countryCode?: unknown;
  industryTag?: unknown;
  timeZone?: unknown;
  /** Direct URL to resource */
  href?: string;
  /** First name */
  firstName?: string;
  /** Last name */
  lastName?: string;
  /** Company name */
  companyName?: string;
  /** Phone number */
  phone?: string;
  /** State */
  state?: string;
  /** City */
  city?: string;
  /** Street */
  street?: string;
  /** ZIP Code */
  zipCode?: string;
  /** Numbers of employees */
  numberOfEmployees?: UpdateAccountNumberOfEmployees;
  /** Account time notation */
  timeFormat?: UpdateAccountTimeFormat;
}

/** UpdateAddress model. */
export interface UpdateAddress {
  /** The creation date (ISO 8601 date-time string) */
  createdOn?: string;
  /** The date of the last update (ISO 8601 date-time string) */
  updatedOn?: string;
  addressId?: string;
  /** Direct hyperlink to a resource */
  href?: string;
  /** The country code (ISO 3166-1 alpha-3) */
  countryCode?: string;
  /** The country name, based on `countryCode` */
  countryName?: string;
  name?: string;
  firstName?: string;
  lastName?: string;
  /** Address line 1 */
  address1?: string;
  /** Address line 2 */
  address2?: string;
  city?: string;
  /** The ZIP/postal code, free text */
  zip?: string;
  province?: string;
  /** The province code, free text */
  provinceCode?: string;
  /** The phone number, free text */
  phone?: string;
  /** The company name, free text */
  company?: string;
}

/** UpdateAutoresponder model. */
export interface UpdateAutoresponder {
  /** The autoresponder ID */
  autoresponderId?: string;
  /** Direct hyperlink to a resource */
  href?: string;
  /** The autoresponder name */
  name?: string;
  /** The autoresponder message subject */
  subject?: string;
  /** The campaign ID. The system will assign the autoresponder to a default campaign if you don't provide a specific campaign ID. */
  campaignId?: string;
  /** The autoresponder status */
  status?: unknown;
  /** The from email address used for the message */
  fromField?: unknown;
  /** The email that will be used as a reply-to address */
  replyTo?: unknown;
  content?: MessageContent;
  flags?: MessageFlagsArrayItem[];
  /** The conditions that will trigger the autoresponder */
  triggerSettings?: unknown;
  /** The autoresponder statistics summary */
  statistics?: Record<string, unknown>;
  /** The creation date (ISO 8601 date-time string) */
  createdOn?: string;
  /** How the message will be delivered to the subscriber */
  sendSettings?: AutoresponderSendSettingsInput;
}

/** UpdateBlocklist model. */
export interface UpdateBlocklist {
  masks: string[];
}

/** UpdateCallbacks model. */
export interface UpdateCallbacks {
  /** URL to use to post notifications, required if callbacks are not yet enabled */
  url?: string;
  actions?: CallbackActions;
}

/** UpdateCampaign model. */
export interface UpdateCampaign {
  /** Unique identifier of the campaign (contact list) */
  campaignId?: string;
  /** The campaign (list) name. * You can use each list name just once in your account. * The name must be between 3-64 characters. * All alphabets supported by GetResponse, including right-to-left ones, are allowed. * You can use upper and lower case letters, numbers, spaces and special characters apart from the ones listed below. * You can’t use emojis and the following special characters: `/`, `\`, `@`, and `[` or `]`. */
  name: string;
  /** Tech name is a unique internal ID of a list used for [FTP imports](https://www.getresponse.com/help/how-to-import-files-via-ftp.html) (available in GetResponse MAX accounts only) */
  techName?: string;
  /** The campaign language code according to ISO 639-1, plus: zt - Chinese (Traditional), fs - Afghan Persian (Dari), md - Moldavian */
  languageCode?: string;
  /** Is the campaign default */
  isDefault?: unknown;
  /** The date of creation (ISO 8601 date-time string) */
  createdOn?: string;
  /** Direct hyperlink to a resource */
  href?: string;
  postal?: CampaignPostal;
  confirmation?: CampaignConfirmation;
  optinTypes?: CampaignOptinTypes;
  subscriptionNotifications?: CampaignSubscriptionNotifications;
  profile?: CampaignProfile;
}

/** UpdateCart model. */
export interface UpdateCart {
  /** The creation date (ISO 8601 date-time string) */
  createdOn?: string;
  /** The date of the last update (ISO 8601 date-time string) */
  updatedOn?: string;
  /** The contact ID */
  cartId?: string;
  /** Direct hyperlink to a resource */
  href?: string;
  /** The ID of the contact that the cart belongs to. You must first create the contact using POST /v3/contacts, or if it already exists, using GET /v3/contacts */
  contactId?: string;
  /** The total cart price, tax excluded */
  totalPrice?: number;
  /** The total cart price, tax included */
  totalTaxPrice?: number;
  /** The currency code (ISO 4217) */
  currency?: string;
  selectedVariants?: NewCartSelectedProductVariant[];
  /** The external ID is the identifying string or number of the cart, given by another software */
  externalId?: string;
  /** The external cart URL */
  cartUrl?: string;
}

/** UpdateContact model. */
export interface UpdateContact {
  contactId?: string;
  name?: string;
  origin?: UpdateContactOrigin;
  /** The time zone of a contact, uses the time zone database format (https://www.iana.org/time-zones) */
  timeZone?: string;
  activities?: string;
  /** ISO 8601 date-time string. */
  changedOn?: string;
  /** ISO 8601 date-time string. */
  createdOn?: string;
  campaign?: Record<string, unknown>;
  email?: string;
  /** The day on which the contact is in the Autoresponder cycle. `null` indicates the contacts is not in the cycle. */
  dayOfCycle?: string;
  /** Contact scoring, pass null to remove the score from a contact */
  scoring?: number;
  /** Engagement Score is a feature that presents a visual estimate of a contact's engagement with mailings. The score is based on the contact's interactions with your e-mails. Via API, it's returned in the form of numbers ranging from 1 (Not Engaged) to 5 (Highly Engaged). */
  engagementScore?: number;
  /** Direct hyperlink to a resource */
  href?: string;
  note?: string;
  tags?: NewContactTag[];
  customFieldValues?: NewContactCustomFieldValue[];
}

/** UpdateCustomEvent model. */
export interface UpdateCustomEvent {
  /** Unique name of custom event */
  name: string;
  /** Optional collection of attributes */
  attributes: CustomEventAttributeDetails[];
}

/** UpdateCustomField model. */
export interface UpdateCustomField {
  /** Whether the custom field is visible to contacts */
  hidden: unknown;
  /** The list of assigned values (zero or more - depending on the custom field type. Please see description) */
  values: string[];
}

/** UpdateMetaField model. */
export interface UpdateMetaField {
  /** Direct hyperlink to a resource */
  href?: string;
  /** The meta field ID */
  metaFieldId?: string;
  /** The meta field name */
  name?: string;
  /** The meta field value */
  value?: string;
  /** The value type enumerable */
  valueType?: UpdateMetaFieldValueType;
  /** The meta field description */
  description?: string;
  /** The creation date (ISO 8601 date-time string) */
  createdOn?: string;
  /** The date of the last update (ISO 8601 date-time string) */
  updatedOn?: string;
}

/** UpdateOrder model. */
export interface UpdateOrder {
  /** The order ID */
  orderId?: string;
  /** Direct hyperlink to a resource */
  href?: string;
  /** Create a contact by using `POST /v3/contacts`. Or, if the contact already exists, using `GET /v3/contacts` */
  contactId?: string;
  /** The external URL for an order */
  orderUrl?: string;
  /** The external ID is the identifying string or number of the order given by another software */
  externalId?: string;
  /** The total price of an order */
  totalPrice?: number;
  /** The total price tax of an order */
  totalPriceTax?: number;
  /** The order currency code (ISO 4217) */
  currency?: string;
  /** The status value */
  status?: string;
  /** Create a cart by using `POST /v3/shops/{shopId}/carts` */
  cartId?: string;
  /** The order description */
  description?: string;
  /** The shipping price for an order */
  shippingPrice?: number;
  /** The shipping address for an order */
  shippingAddress?: unknown;
  /** The billing status of an order */
  billingStatus?: string;
  /** The billing address for an order */
  billingAddress?: unknown;
  /** The exact time an order was made (ISO 8601 date-time string) */
  processedAt?: string;
  metaFields?: NewMetaField[];
}

/** UpdatePredefinedField model. */
export interface UpdatePredefinedField {
  value: string;
}

/** UpdateProduct model. */
export interface UpdateProduct {
  /** The creation date (ISO 8601 date-time string) */
  createdOn?: string;
  /** The date of the last update (ISO 8601 date-time string) */
  updatedOn?: string;
  /** The product ID */
  productId?: string;
  /** Direct hyperlink to a resource */
  href?: string;
  /** The product name */
  name?: string;
  /** The product type */
  type?: string;
  /** The external URL for the product */
  url?: string;
  /** The product vendor */
  vendor?: string;
  /** The external ID is the identifying string or number of the product given by another software */
  externalId?: string;
  categories?: NewProductCategory[];
  variants?: NewProductVariant[];
  metaFields?: NewMetaField[];
}

/** UpdateProductVariant model. */
export interface UpdateProductVariant {
  /** The product ID */
  variantId?: string;
  /** Direct hyperlink to a resource */
  href?: string;
  /** The product name */
  name?: string;
  /** The external URL to the product variant */
  url?: string;
  /** The stock-keeping unit of a variant. Must be unique within the product */
  sku?: string;
  /** The price */
  price?: number;
  /** The price including tax */
  priceTax?: number;
  /** The price before the change */
  previousPrice?: number;
  /** The price before the change including tax */
  previousPriceTax?: number;
  /** The quantity of variant items */
  quantity?: number;
  /** The position of a variant */
  position?: number;
  /** The barcode of a variant */
  barcode?: string;
  /** The external ID is the identifying string or number of the variant given by another software */
  externalId?: string;
  /** The description of a variant */
  description?: string;
  images?: NewProductVariantImage[];
  metaFields?: NewMetaField[];
  taxes?: NewTax[];
  /** The creation date (ISO 8601 date-time string) */
  createdOn?: string;
  /** The date of the last update (ISO 8601 date-time string) */
  updatedOn?: string;
}

/** UpdateRssNewsletter model. */
export interface UpdateRssNewsletter {
  /** The RSS newsletter ID */
  rssNewsletterId: string;
  /** Direct hyperlink to a resource */
  href: string;
  /** The URL for the RSS Feed */
  rssFeedUrl?: string;
  /** The RSS message subject */
  subject?: string;
  /** How your newsletters will be seen inside the application */
  name?: string;
  /** The status of the RSS newsletter */
  status?: unknown;
  editor?: unknown;
  /** The 'From' email address used for the message */
  fromField?: unknown;
  /** The email that will be used as a reply-to address */
  replyTo?: unknown;
  content?: MessageContent;
  /** How the message will be delivered to the subscriber */
  sendSettings?: unknown;
  /** The creation date (ISO 8601 date-time string) */
  createdOn?: string;
  flags?: MessageFlagsArrayItem[];
}

/** New search contacts. */
export interface UpdateSearchContacts {
  /** Only one subscription status */
  subscribersType?: UpdateSearchContactsSubscribersTypeItem[];
  /** Match 'any' (`or` value) or 'all' (`and` value) of the following conditions */
  sectionLogicOperator: UpdateSearchContactsSectionLogicOperator;
  section: SearchContactSection[];
  /** The unique search-contact identifier */
  searchContactId?: string;
  /** The unique name of search-contact */
  name: string;
  /** The UTC date time format ISO 8601, e.g. 2018-04-10T10:02:57+0000 (ISO 8601 date-time string) */
  createdOn?: string;
  /** Direct hyperlink to a resource */
  href?: string;
}

/** UpdateShop model. */
export interface UpdateShop {
  /** The creation date (ISO 8601 date-time string) */
  createdOn?: string;
  /** The date of the last update (ISO 8601 date-time string) */
  updatedOn?: string;
  /** The shop ID */
  shopId?: string;
  /** Direct hyperlink to a resource */
  href?: string;
  /** The shop name */
  name?: string;
  /** The language locale (ISO 639-1) */
  locale?: string;
  /** The currency code (ISO 4217) */
  currency?: string;
}

/** UpdateSuppression model. */
export interface UpdateSuppression {
  /** The name of the suppression list */
  name: string;
  masks: string[];
}

/** UpdateTag model. */
export interface UpdateTag {
  /** The tag name */
  name: string;
  /** The tag color (deprecated) */
  color?: string;
}

/** UpdateTax model. */
export interface UpdateTax {
  /** The tax ID */
  taxId?: string;
  /** Direct hyperlink to a resource */
  href?: string;
  /** The tax name */
  name?: string;
  /** The rate value */
  rate?: number;
}

/** UpdateWorkflow model. */
export interface UpdateWorkflow {
  /** An 'incomplete' status means that the workflow is a 'draft' in the web panel */
  status: UpdateWorkflowStatus;
}

/** UpsertContactCustomFields model. */
export interface UpsertContactCustomFields {
  customFieldValues: NewContactCustomFieldValue[];
}

/** UpsertContactTags model. */
export interface UpsertContactTags {
  tags: NewContactTag[];
}

/** This method assigns metafields. It doesn't unassign or delete them. */
export interface UpsertMetaField {
  metaFields: UpsertSingleMetaField[];
}

/** This method makes it possible to assign product categories, and to set a default product category. It doesn't remove or unassign product categories. */
export interface UpsertProductCategory {
  categories: UpsertSingleProductCategory[];
}

/** UpsertSingleMetaField model. */
export interface UpsertSingleMetaField {
  /** MetaField ID */
  metaFieldId: string;
}

/** UpsertSingleProductCategory model. */
export interface UpsertSingleProductCategory {
  /** The category ID */
  categoryId: string;
  /** This is a default category */
  isDefault?: boolean;
}

/** UserActivityReportDetails model. */
export interface UserActivityReportDetails {
  /** The custom report ID */
  customReportId?: string;
  /** The custom report name */
  name?: string;
  /** The direct hyperlink to a resource */
  href?: string;
  /** The custom report type */
  type?: unknown;
  /** Parameters responsible for defining the reporting period */
  scheduling?: Record<string, unknown>;
  /** Files that have been generated for the given report */
  files?: Record<string, unknown>[];
  /** Custom report creation date (ISO 8601 date-time string) */
  createdAt?: string;
  /** Custom report generation date (ISO 8601 date-time string) */
  generatedAt?: string;
  /** Filters used to narrow down the report data */
  filters?: Record<string, unknown>;
}

/** Webinar model. */
export interface Webinar {
  webinarId?: string;
  /** Direct hyperlink to a resource */
  href?: string;
  /** ISO 8601 date-time string. */
  createdOn?: string;
  /** ISO 8601 date-time string. */
  startsOn?: string;
  /** The URL to the webinar room */
  webinarUrl?: string;
  status?: WebinarStatus;
  /** The webinar type */
  type?: WebinarType;
  campaigns?: CampaignReference[];
  /** The list of invitation messages */
  newsletters?: WebinarNewsletter[];
  statistics?: WebinarStatistics;
}

/** Search contacts that have participated/not participated in a specific webinar as a host/listener/presenter/registrant/any user. */
export interface WebinarCondition {
  conditionType: WebinarConditionConditionType;
  /** The identifier of a webinar */
  scope: string;
  webinarCondition: WebinarConditionWebinarCondition;
  contactType: WebinarConditionContactType;
}

/** WebinarNewsletter model. */
export interface WebinarNewsletter {
  /** The ID of the webinar invitation message */
  newsletterId: string;
  /** Direct hyperlink to a resource */
  href: string;
}

/** WebinarParticipantsReportDetails model. */
export interface WebinarParticipantsReportDetails {
  /** The custom report ID */
  customReportId?: string;
  /** The custom report name */
  name?: string;
  /** The direct hyperlink to a resource */
  href?: string;
  /** The custom report type */
  type?: unknown;
  /** Parameters responsible for defining the reporting period */
  scheduling?: Record<string, unknown>;
  /** Files that have been generated for the given report */
  files?: Record<string, unknown>[];
  /** Custom report creation date (ISO 8601 date-time string) */
  createdAt?: string;
  /** Custom report generation date (ISO 8601 date-time string) */
  generatedAt?: string;
  /** Filters used to narrow down the report data */
  filters?: Record<string, unknown>;
}

/** WebinarStatistics model. */
export interface WebinarStatistics {
  registrants: number;
  visitors: number;
  attendees: number;
}

/** Website model. */
export interface Website {
  /** The website ID */
  websiteId?: string;
  /** Direct hyperlink to a resource */
  href?: string;
  /** The website name */
  name?: string;
  /** The website status */
  status?: WebsiteStatus;
  /** The website domain */
  domainUrl?: string;
  /** The URL of a website thumbnail */
  thumbnailUrl?: string;
  /** Chats is enabled on the website */
  isChatsEnabled?: unknown;
  /** The date (in GMT) the website was created (ISO 8601 date-time string) */
  createdAt?: string;
  /** The date (in GMT) the website was updated (ISO 8601 date-time string) */
  updatedAt?: string;
  /** The website statistics */
  statistics?: WebsiteStatistics;
}

/** WebsiteDetails model. */
export interface WebsiteDetails {
  /** The website ID */
  websiteId?: string;
  /** Direct hyperlink to a resource */
  href?: string;
  /** The website name */
  name?: string;
  /** The website status */
  status?: WebsiteDetailsStatus;
  /** The website domain */
  domainUrl?: string;
  /** The URL of a website thumbnail */
  thumbnailUrl?: string;
  /** Chats is enabled on the website */
  isChatsEnabled?: unknown;
  /** The date (in GMT) the website was created (ISO 8601 date-time string) */
  createdAt?: string;
  /** The date (in GMT) the website was updated (ISO 8601 date-time string) */
  updatedAt?: string;
  /** The website statistics */
  statistics?: WebsiteStatistics;
  pages?: WebsitePage[];
}

/** WebsitePage model. */
export interface WebsitePage {
  /** The website page ID */
  uuid?: string;
  /** The website page name */
  name?: string;
  /** The website page status */
  status?: WebsitePageStatus;
  /** Direct hyperlink to a resource */
  url?: string;
  /** Direct hyperlink to a resource */
  redirectUrl?: string;
  /** The date (in GMT) the website page was created (ISO 8601 date-time string) */
  createdAt?: string;
}

/** WebsiteStatistics model. */
export interface WebsiteStatistics {
  /** Number of page views */
  pageViews?: number;
  /** Number of site visits */
  visits?: number;
  /** Number of unique visitors */
  uniqueVisitors?: number;
}

/** WebsiteStats model. */
export interface WebsiteStats {
  /** The website ID */
  websiteId: string;
  name?: string;
  /** The number of page views */
  pageViews?: number;
  /** The number of visits */
  visits?: number;
  /** The number of unique visitors */
  uniqueVisitors?: number;
  /** Direct hyperlink to a resource */
  thumbnailUrl?: string;
}

/** WeeklyReportScheduling model. */
export interface WeeklyReportScheduling {
  /** The custom report frequency */
  frequency?: unknown;
  /** Field not applicable to the selected frequency */
  oneTime?: Record<string, unknown>;
  /** A field containing configuration parameters for recurring scheduling */
  recurring?: Record<string, unknown>;
}

/** Workflow model. */
export interface Workflow {
  /** The workflow ID */
  workflowId: string;
  name: string;
  status: WorkflowStatus;
  /** ISO 8601 date-time string. */
  dateStart?: string;
  /** ISO 8601 date-time string. */
  dateStop?: string;
  subscriberStatistics: WorkflowSubscriberStatistics;
}

/** WorkflowSubscriberStatistics model. */
export interface WorkflowSubscriberStatistics {
  /** The number of subscribers that completed the workflow */
  completedCount: number;
  /** The number of subscribers that are in progress in the workflow */
  inProgressCount: number;
}
