/** Resource-group properties attached to GetResponseClient. Generated from the spec's tags. */

import type { Core } from './core.js';
import {
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
  FormsResource,
  FormsAndPopupsResource,
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
  ProductVariantsResource,
  ProductsResource,
  RssNewslettersResource,
  SmsAutomationMessagesResource,
  SmsMessagesResource,
  SearchContactsResource,
  ShopsResource,
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
} from './resources/index.js';

/** One readonly resource-group property per API tag. */
export interface GeneratedResourceGroups {
  readonly abTests: AbTestsResource;
  readonly abTestsSubject: AbTestsSubjectResource;
  readonly accounts: AccountsResource;
  readonly addresses: AddressesResource;
  readonly autoresponders: AutorespondersResource;
  readonly campaignsLists: CampaignsListsResource;
  readonly carts: CartsResource;
  readonly categories: CategoriesResource;
  readonly clickTracks: ClickTracksResource;
  readonly contacts: ContactsResource;
  readonly customEvents: CustomEventsResource;
  readonly customFields: CustomFieldsResource;
  readonly customReports: CustomReportsResource;
  readonly ecommerce: EcommerceResource;
  readonly fileLibrary: FileLibraryResource;
  readonly formAndPopup: FormAndPopupResource;
  readonly forms: FormsResource;
  readonly formsAndPopups: FormsAndPopupsResource;
  readonly fromFields: FromFieldsResource;
  readonly gdprFields: GdprFieldsResource;
  readonly imports: ImportsResource;
  readonly landingPage: LandingPageResource;
  readonly landingPages: LandingPagesResource;
  readonly legacyForms: LegacyFormsResource;
  readonly legacyLandingPages: LegacyLandingPagesResource;
  readonly metaFields: MetaFieldsResource;
  readonly multimedia: MultimediaResource;
  readonly newsletters: NewslettersResource;
  readonly orders: OrdersResource;
  readonly predefinedFields: PredefinedFieldsResource;
  readonly productVariants: ProductVariantsResource;
  readonly products: ProductsResource;
  readonly rssNewsletters: RssNewslettersResource;
  readonly smsAutomationMessages: SmsAutomationMessagesResource;
  readonly smsMessages: SmsMessagesResource;
  readonly searchContacts: SearchContactsResource;
  readonly shops: ShopsResource;
  readonly sms: SmsResource;
  readonly subscriptionConfirmations: SubscriptionConfirmationsResource;
  readonly suppressions: SuppressionsResource;
  readonly tags: TagsResource;
  readonly taxes: TaxesResource;
  readonly tracking: TrackingResource;
  readonly transactionalEmails: TransactionalEmailsResource;
  readonly transactionalEmailsTemplates: TransactionalEmailsTemplatesResource;
  readonly webinars: WebinarsResource;
  readonly website: WebsiteResource;
  readonly websites: WebsitesResource;
  readonly workflows: WorkflowsResource;
}

/** Constructs one resource-group instance per tag, keyed by property name. */
export function createResourceGroups(core: Core): GeneratedResourceGroups {
  return {
    abTests: new AbTestsResource(core),
    abTestsSubject: new AbTestsSubjectResource(core),
    accounts: new AccountsResource(core),
    addresses: new AddressesResource(core),
    autoresponders: new AutorespondersResource(core),
    campaignsLists: new CampaignsListsResource(core),
    carts: new CartsResource(core),
    categories: new CategoriesResource(core),
    clickTracks: new ClickTracksResource(core),
    contacts: new ContactsResource(core),
    customEvents: new CustomEventsResource(core),
    customFields: new CustomFieldsResource(core),
    customReports: new CustomReportsResource(core),
    ecommerce: new EcommerceResource(core),
    fileLibrary: new FileLibraryResource(core),
    formAndPopup: new FormAndPopupResource(core),
    forms: new FormsResource(core),
    formsAndPopups: new FormsAndPopupsResource(core),
    fromFields: new FromFieldsResource(core),
    gdprFields: new GdprFieldsResource(core),
    imports: new ImportsResource(core),
    landingPage: new LandingPageResource(core),
    landingPages: new LandingPagesResource(core),
    legacyForms: new LegacyFormsResource(core),
    legacyLandingPages: new LegacyLandingPagesResource(core),
    metaFields: new MetaFieldsResource(core),
    multimedia: new MultimediaResource(core),
    newsletters: new NewslettersResource(core),
    orders: new OrdersResource(core),
    predefinedFields: new PredefinedFieldsResource(core),
    productVariants: new ProductVariantsResource(core),
    products: new ProductsResource(core),
    rssNewsletters: new RssNewslettersResource(core),
    smsAutomationMessages: new SmsAutomationMessagesResource(core),
    smsMessages: new SmsMessagesResource(core),
    searchContacts: new SearchContactsResource(core),
    shops: new ShopsResource(core),
    sms: new SmsResource(core),
    subscriptionConfirmations: new SubscriptionConfirmationsResource(core),
    suppressions: new SuppressionsResource(core),
    tags: new TagsResource(core),
    taxes: new TaxesResource(core),
    tracking: new TrackingResource(core),
    transactionalEmails: new TransactionalEmailsResource(core),
    transactionalEmailsTemplates: new TransactionalEmailsTemplatesResource(core),
    webinars: new WebinarsResource(core),
    website: new WebsiteResource(core),
    websites: new WebsitesResource(core),
    workflows: new WorkflowsResource(core),
  };
}
