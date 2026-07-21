/** Operations tagged 'Addresses' in the GetResponse API. */

import type { Core } from '../core.js';
import type * as M from '../models.js';

export class AddressesResource {
  constructor(private readonly core: Core) {}

  /** Create address */
  readonly createAddress = async (body: M.NewAddress, signal?: AbortSignal): Promise<M.Address> => {
    return this.core.request<M.Address>('POST', '/addresses', {
      body,
      signal,
    });
  };

  /** Delete address */
  readonly deleteAddress = async (addressId: string, signal?: AbortSignal): Promise<void> => {
    return this.core.request<void>('DELETE', '/addresses/{addressId}', {
      pathParams: { addressId: addressId },
      signal,
    });
  };

  /** Get an address by ID */
  readonly getAddress = async (
    addressId: string,
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
    },
    signal?: AbortSignal,
  ): Promise<M.Address> => {
    return this.core.request<M.Address>('GET', '/addresses/{addressId}', {
      pathParams: { addressId: addressId },
      query: params ? { fields: params.fields } : undefined,
      signal,
    });
  };

  /** Sending a **GET** request to this URL returns collection of address resources. You can narrow down the list of resources by passing proper query parameters (the list of which you can find below in the request params section). You can basically search by: * name * firstName * lastName * address1 * address2 * city * zip * province * provinceCode * phone * company * createdOn The `name` field can be a pattern and we'll try to match this phrase. You can specify which page of the results you want and how many results per page to display. You can also specify the sort-order using one or more of the allowed fields (listed below in the request params section). Last but not least, you can even specify which fields from a resource you want to get. If you pass the param `fields` with the list of fields (separated by a comma [,]) we'll return the list of resources with only those fields (we'll always add a resource ID to ensure that you can use that data later on) You can filter the resource using criteria specified as `query[*]`. You can provide multiple criteria, to use AND logic. You can sort the resource using parameters specified as `sort[*]`. You can specify multiple fields to sort by. */
  readonly getAddressList = async (
    params?: {
      /** List of fields that should be returned. Id is always returned. Fields should be separated by comma */
      fields?: string;
      /** Page number */
      page?: number;
      /** Requested number of results per page */
      perPage?: number;
      /** Search addresses by address1 field */
      queryAddress1?: string;
      /** Search addresses by address2 field */
      queryAddress2?: string;
      /** Search addresses by city */
      queryCity?: string;
      /** Search addresses by company */
      queryCompany?: string;
      /** Search addresses created from this date */
      queryCreatedOnFrom?: string;
      /** Search addresses created to this date */
      queryCreatedOnTo?: string;
      /** Search addresses by first name */
      queryFirstName?: string;
      /** Search addresses by last name */
      queryLastName?: string;
      /** Search addresses by name */
      queryName?: string;
      /** Search addresses by phone */
      queryPhone?: string;
      /** Search addresses by province code */
      queryProvinceCode?: string;
      /** Search addresses by province */
      queryProvince?: string;
      /** Search addresses by ZIP */
      queryZip?: string;
      /** Sort by date */
      sortCreatedOn?: M.SortOrderEnum;
    },
    signal?: AbortSignal,
  ): Promise<M.Address[]> => {
    return this.core.request<M.Address[]>('GET', '/addresses', {
      query: params
        ? {
            'query[name]': params.queryName,
            'query[firstName]': params.queryFirstName,
            'query[lastName]': params.queryLastName,
            'query[address1]': params.queryAddress1,
            'query[address2]': params.queryAddress2,
            'query[city]': params.queryCity,
            'query[zip]': params.queryZip,
            'query[province]': params.queryProvince,
            'query[provinceCode]': params.queryProvinceCode,
            'query[phone]': params.queryPhone,
            'query[company]': params.queryCompany,
            'query[createdOn][from]': params.queryCreatedOnFrom,
            'query[createdOn][to]': params.queryCreatedOnTo,
            'sort[createdOn]': params.sortCreatedOn,
            fields: params.fields,
            perPage: params.perPage,
            page: params.page,
          }
        : undefined,
      signal,
    });
  };

  /** Update an existing address. You should send only those fields that need to be changed. The rest of the properties will stay the same. */
  readonly updateAddress = async (
    addressId: string,
    body: M.UpdateAddress,
    signal?: AbortSignal,
  ): Promise<M.Address> => {
    return this.core.request<M.Address>('POST', '/addresses/{addressId}', {
      pathParams: { addressId: addressId },
      body,
      signal,
    });
  };
}
