/** Root client: auth, one property per resource-group tag, and pagination. */

import { Core, DEFAULT_BASE_URL, type FetchFn } from './core.js';
import type { RateLimitOptions } from './ratelimit.js';
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

/** Constructor options for {@link GetResponseClient}. */
export interface GetResponseClientOptions {
  /** API key: sent as `X-Auth-Token: api-key <apiKey>`. Mutually exclusive with `accessToken`. */
  apiKey?: string;
  /** OAuth2 bearer token: sent as `Authorization: Bearer <accessToken>`. */
  accessToken?: string;
  /** API base URL. Defaults to the standard GetResponse endpoint (see also the MAX US/PL constants in `core.ts`). */
  baseUrl?: string;
  /** Per-request timeout in milliseconds. Defaults to 30000. */
  timeoutMs?: number;
  /** Inject a custom `fetch` implementation (used by the test suite). Defaults to the global `fetch`. */
  fetch?: FetchFn;
  /** Opt-in client-side rate limiting; disabled unless provided. */
  rateLimit?: RateLimitOptions;
}

/** Async, fully-typed GetResponse v3 API client; one property per resource-group tag. */
export class GetResponseClient {
  private readonly core: Core;

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

  constructor(options: GetResponseClientOptions = {}) {
    const {
      apiKey,
      accessToken,
      baseUrl = DEFAULT_BASE_URL,
      timeoutMs = 30_000,
      fetch: fetchImpl,
      rateLimit,
    } = options;
    if ((apiKey === undefined) === (accessToken === undefined)) {
      throw new Error('Provide exactly one of `apiKey` or `accessToken`.');
    }
    const authHeader: Record<string, string> =
      apiKey !== undefined
        ? { 'X-Auth-Token': `api-key ${apiKey}` }
        : { Authorization: `Bearer ${accessToken}` };
    this.core = new Core({ baseUrl, authHeader, timeoutMs, fetch: fetchImpl, rateLimit });
    this.abTests = new AbTestsResource(this.core);
    this.abTestsSubject = new AbTestsSubjectResource(this.core);
    this.accounts = new AccountsResource(this.core);
    this.addresses = new AddressesResource(this.core);
    this.autoresponders = new AutorespondersResource(this.core);
    this.campaignsLists = new CampaignsListsResource(this.core);
    this.carts = new CartsResource(this.core);
    this.categories = new CategoriesResource(this.core);
    this.clickTracks = new ClickTracksResource(this.core);
    this.contacts = new ContactsResource(this.core);
    this.customEvents = new CustomEventsResource(this.core);
    this.customFields = new CustomFieldsResource(this.core);
    this.customReports = new CustomReportsResource(this.core);
    this.ecommerce = new EcommerceResource(this.core);
    this.fileLibrary = new FileLibraryResource(this.core);
    this.formAndPopup = new FormAndPopupResource(this.core);
    this.forms = new FormsResource(this.core);
    this.formsAndPopups = new FormsAndPopupsResource(this.core);
    this.fromFields = new FromFieldsResource(this.core);
    this.gdprFields = new GdprFieldsResource(this.core);
    this.imports = new ImportsResource(this.core);
    this.landingPage = new LandingPageResource(this.core);
    this.landingPages = new LandingPagesResource(this.core);
    this.legacyForms = new LegacyFormsResource(this.core);
    this.legacyLandingPages = new LegacyLandingPagesResource(this.core);
    this.metaFields = new MetaFieldsResource(this.core);
    this.multimedia = new MultimediaResource(this.core);
    this.newsletters = new NewslettersResource(this.core);
    this.orders = new OrdersResource(this.core);
    this.predefinedFields = new PredefinedFieldsResource(this.core);
    this.productVariants = new ProductVariantsResource(this.core);
    this.products = new ProductsResource(this.core);
    this.rssNewsletters = new RssNewslettersResource(this.core);
    this.smsAutomationMessages = new SmsAutomationMessagesResource(this.core);
    this.smsMessages = new SmsMessagesResource(this.core);
    this.searchContacts = new SearchContactsResource(this.core);
    this.shops = new ShopsResource(this.core);
    this.sms = new SmsResource(this.core);
    this.subscriptionConfirmations = new SubscriptionConfirmationsResource(this.core);
    this.suppressions = new SuppressionsResource(this.core);
    this.tags = new TagsResource(this.core);
    this.taxes = new TaxesResource(this.core);
    this.tracking = new TrackingResource(this.core);
    this.transactionalEmails = new TransactionalEmailsResource(this.core);
    this.transactionalEmailsTemplates = new TransactionalEmailsTemplatesResource(this.core);
    this.webinars = new WebinarsResource(this.core);
    this.website = new WebsiteResource(this.core);
    this.websites = new WebsitesResource(this.core);
    this.workflows = new WorkflowsResource(this.core);
  }

  /**
   * Walk every page of a `list`/`get*List` resource method, yielding items one by one.
   *
   * GetResponse also reports `TotalCount`/`CurrentPage`/`TotalPages` response headers, but
   * resource methods only return typed bodies (no header access), so this walks by page
   * length instead: it stops once a page comes back empty or shorter than `perPage`.
   */
  async *paginate<T>(
    listMethod: (
      params: Record<string, unknown> & { page?: number; perPage?: number },
      signal?: AbortSignal,
    ) => Promise<T[]>,
    options: { perPage?: number; params?: Record<string, unknown>; signal?: AbortSignal } = {},
  ): AsyncGenerator<T, void, void> {
    const perPage = options.perPage ?? 100;
    let page = 1;
    for (;;) {
      const items = await listMethod({ ...options.params, page, perPage }, options.signal);
      if (items.length === 0) return;
      yield* items;
      if (items.length < perPage) return;
      page += 1;
    }
  }
}
