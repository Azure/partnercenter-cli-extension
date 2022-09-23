# partnercenter.ListingClient

All URIs are relative to *https://api.partner.microsoft.com/v1.0/ingestion*

Method | HTTP request | Description
------------- | ------------- | -------------
[**products_product_id_listings_create_with_instance_id_instance_i_dinstance_id_post**](ListingClient.md#products_product_id_listings_create_with_instance_id_instance_i_dinstance_id_post) | **POST** /products/{productID}/listings/createWithInstanceID(instanceID&#x3D;{instanceID}) | Creates a Listing resource
[**products_product_id_listings_get_by_instance_id_instance_i_dinstance_id_get**](ListingClient.md#products_product_id_listings_get_by_instance_id_instance_i_dinstance_id_get) | **GET** /products/{productID}/listings/getByInstanceID(instanceID&#x3D;{instanceID}) | Returns a paged collection of Listing resources
[**products_product_id_listings_listing_id_delete**](ListingClient.md#products_product_id_listings_listing_id_delete) | **DELETE** /products/{productID}/listings/{listingID} | Deletes Listing resource
[**products_product_id_listings_listing_id_get**](ListingClient.md#products_product_id_listings_listing_id_get) | **GET** /products/{productID}/listings/{listingID} | Returns Listing resource
[**products_product_id_listings_listing_id_put**](ListingClient.md#products_product_id_listings_listing_id_put) | **PUT** /products/{productID}/listings/{listingID} | Updates Listing resource


# **products_product_id_listings_create_with_instance_id_instance_i_dinstance_id_post**
> MicrosoftIngestionApiModelsListingsAzureListing products_product_id_listings_create_with_instance_id_instance_i_dinstance_id_post(product_id, instance_id, authorization)

Creates a Listing resource

Sample request:                   POST /products/{productID}/listings/createWithInstanceID(instanceID={instanceID}) [Body Listing]

### Example


```python
import time
import partnercenter
from ..api import listing_client
from ..model.microsoft_ingestion_api_models_listings_azure_listing import MicrosoftIngestionApiModelsListingsAzureListing
from pprint import pprint
# Defining the host is optional and defaults to https://api.partner.microsoft.com/v1.0/ingestion
# See configuration.py for a list of all supported configuration parameters.
configuration = partnercenter.Configuration(
    host = "https://api.partner.microsoft.com/v1.0/ingestion"
)


# Enter a context with an instance of the API client
with partnercenter.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = listing_client.ListingClient(api_client)
    product_id = "productID_example" # str | ID of product
    instance_id = "instanceID_example" # str | Resource instance ID
    authorization = "Authorization_example" # str | User authorization
    client_request_id = "Client-Request-ID_example" # str | ID of request provIDed by user (optional)
    microsoft_ingestion_api_models_listings_azure_listing = MicrosoftIngestionApiModelsListingsAzureListing(None) # MicrosoftIngestionApiModelsListingsAzureListing | Request body of a base Listing (optional)

    # example passing only required values which don't have defaults set
    try:
        # Creates a Listing resource
        api_response = api_instance.products_product_id_listings_create_with_instance_id_instance_i_dinstance_id_post(product_id, instance_id, authorization)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling ListingClient->products_product_id_listings_create_with_instance_id_instance_i_dinstance_id_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Creates a Listing resource
        api_response = api_instance.products_product_id_listings_create_with_instance_id_instance_i_dinstance_id_post(product_id, instance_id, authorization, client_request_id=client_request_id, microsoft_ingestion_api_models_listings_azure_listing=microsoft_ingestion_api_models_listings_azure_listing)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling ListingClient->products_product_id_listings_create_with_instance_id_instance_i_dinstance_id_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| ID of product |
 **instance_id** | **str**| Resource instance ID |
 **authorization** | **str**| User authorization |
 **client_request_id** | **str**| ID of request provIDed by user | [optional]
 **microsoft_ingestion_api_models_listings_azure_listing** | [**MicrosoftIngestionApiModelsListingsAzureListing**](MicrosoftIngestionApiModelsListingsAzureListing.md)| Request body of a base Listing | [optional]

### Return type

[**MicrosoftIngestionApiModelsListingsAzureListing**](MicrosoftIngestionApiModelsListingsAzureListing.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The created BaseListing resource |  * Request-ID - ID of request generated by service <br>  * ETag - ETag of returned resource <br>  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Resource not available |  -  |
**405** | Method not allowed |  -  |
**409** | Conflict |  -  |
**429** | Request rate exceeds limit |  -  |
**0** | Unknown error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_product_id_listings_get_by_instance_id_instance_i_dinstance_id_get**
> MicrosoftIngestionApiModelsCommonPagedCollectionMicrosoftIngestionApiModelsListingsBaseListing products_product_id_listings_get_by_instance_id_instance_i_dinstance_id_get(product_id, instance_id, authorization)

Returns a paged collection of Listing resources

Sample request:                   GET /products/{productID}/listings/getByInstanceID(instanceID={instanceID})

### Example


```python
import time
import partnercenter
from ..api import listing_client
from ..model.microsoft_ingestion_api_models_common_paged_collection_microsoft_ingestion_api_models_listings_base_listing import MicrosoftIngestionApiModelsCommonPagedCollectionMicrosoftIngestionApiModelsListingsBaseListing
from pprint import pprint
# Defining the host is optional and defaults to https://api.partner.microsoft.com/v1.0/ingestion
# See configuration.py for a list of all supported configuration parameters.
configuration = partnercenter.Configuration(
    host = "https://api.partner.microsoft.com/v1.0/ingestion"
)


# Enter a context with an instance of the API client
with partnercenter.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = listing_client.ListingClient(api_client)
    product_id = "productID_example" # str | ID of product
    instance_id = "instanceID_example" # str | Resource instance ID
    authorization = "Authorization_example" # str | User authorization
    client_request_id = "Client-Request-ID_example" # str | ID of request provIDed by user (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a paged collection of Listing resources
        api_response = api_instance.products_product_id_listings_get_by_instance_id_instance_i_dinstance_id_get(product_id, instance_id, authorization)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling ListingClient->products_product_id_listings_get_by_instance_id_instance_i_dinstance_id_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a paged collection of Listing resources
        api_response = api_instance.products_product_id_listings_get_by_instance_id_instance_i_dinstance_id_get(product_id, instance_id, authorization, client_request_id=client_request_id)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling ListingClient->products_product_id_listings_get_by_instance_id_instance_i_dinstance_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| ID of product |
 **instance_id** | **str**| Resource instance ID |
 **authorization** | **str**| User authorization |
 **client_request_id** | **str**| ID of request provIDed by user | [optional]

### Return type

[**MicrosoftIngestionApiModelsCommonPagedCollectionMicrosoftIngestionApiModelsListingsBaseListing**](MicrosoftIngestionApiModelsCommonPagedCollectionMicrosoftIngestionApiModelsListingsBaseListing.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A PagedCollection of BaseListing resource |  * Request-ID - ID of request generated by service <br>  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Resource not available |  -  |
**405** | Method not allowed |  -  |
**409** | Conflict |  -  |
**429** | Request rate exceeds limit |  -  |
**0** | Unknown error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_product_id_listings_listing_id_delete**
> products_product_id_listings_listing_id_delete(product_id, listing_id, authorization)

Deletes Listing resource

Sample request:                    DELETE /products/{productID}/listings/{listingID}

### Example


```python
import time
import partnercenter
from ..api import listing_client
from pprint import pprint
# Defining the host is optional and defaults to https://api.partner.microsoft.com/v1.0/ingestion
# See configuration.py for a list of all supported configuration parameters.
configuration = partnercenter.Configuration(
    host = "https://api.partner.microsoft.com/v1.0/ingestion"
)


# Enter a context with an instance of the API client
with partnercenter.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = listing_client.ListingClient(api_client)
    product_id = "productID_example" # str | ID of product
    listing_id = "listingID_example" # str | ID of listing
    authorization = "Authorization_example" # str | User authorization
    client_request_id = "Client-Request-ID_example" # str | ID of request provIDed by user (optional)

    # example passing only required values which don't have defaults set
    try:
        # Deletes Listing resource
        api_instance.products_product_id_listings_listing_id_delete(product_id, listing_id, authorization)
    except partnercenter.ApiException as e:
        print("Exception when calling ListingClient->products_product_id_listings_listing_id_delete: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Deletes Listing resource
        api_instance.products_product_id_listings_listing_id_delete(product_id, listing_id, authorization, client_request_id=client_request_id)
    except partnercenter.ApiException as e:
        print("Exception when calling ListingClient->products_product_id_listings_listing_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| ID of product |
 **listing_id** | **str**| ID of listing |
 **authorization** | **str**| User authorization |
 **client_request_id** | **str**| ID of request provIDed by user | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Deletes Listing resource |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Resource not available |  -  |
**405** | Method not allowed |  -  |
**409** | Conflict |  -  |
**429** | Request rate exceeds limit |  -  |
**0** | Unknown error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_product_id_listings_listing_id_get**
> MicrosoftIngestionApiModelsListingsAzureListing products_product_id_listings_listing_id_get(product_id, listing_id, authorization)

Returns Listing resource

Sample request:                   GET /products/{productID}/listings/{listingID}

### Example


```python
import time
import partnercenter
from ..api import listing_client
from ..model.microsoft_ingestion_api_models_listings_azure_listing import MicrosoftIngestionApiModelsListingsAzureListing
from pprint import pprint
# Defining the host is optional and defaults to https://api.partner.microsoft.com/v1.0/ingestion
# See configuration.py for a list of all supported configuration parameters.
configuration = partnercenter.Configuration(
    host = "https://api.partner.microsoft.com/v1.0/ingestion"
)


# Enter a context with an instance of the API client
with partnercenter.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = listing_client.ListingClient(api_client)
    product_id = "productID_example" # str | ID of product
    listing_id = "listingID_example" # str | ID of listing
    authorization = "Authorization_example" # str | User authorization
    client_request_id = "Client-Request-ID_example" # str | ID of request provIDed by user (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns Listing resource
        api_response = api_instance.products_product_id_listings_listing_id_get(product_id, listing_id, authorization)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling ListingClient->products_product_id_listings_listing_id_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns Listing resource
        api_response = api_instance.products_product_id_listings_listing_id_get(product_id, listing_id, authorization, client_request_id=client_request_id)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling ListingClient->products_product_id_listings_listing_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| ID of product |
 **listing_id** | **str**| ID of listing |
 **authorization** | **str**| User authorization |
 **client_request_id** | **str**| ID of request provIDed by user | [optional]

### Return type

[**MicrosoftIngestionApiModelsListingsAzureListing**](MicrosoftIngestionApiModelsListingsAzureListing.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns Azure Listing resource |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Resource not available |  -  |
**429** | Request rate exceeds limit |  -  |
**0** | Unknown error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_product_id_listings_listing_id_put**
> MicrosoftIngestionApiModelsListingsAzureListing products_product_id_listings_listing_id_put(product_id, listing_id, authorization)

Updates Listing resource

Sample request:                    PUT /products/{productID}/listings/{listingID [Body Listing]  

### Example


```python
import time
import partnercenter
from ..api import listing_client
from ..model.microsoft_ingestion_api_models_listings_azure_listing import MicrosoftIngestionApiModelsListingsAzureListing
from pprint import pprint
# Defining the host is optional and defaults to https://api.partner.microsoft.com/v1.0/ingestion
# See configuration.py for a list of all supported configuration parameters.
configuration = partnercenter.Configuration(
    host = "https://api.partner.microsoft.com/v1.0/ingestion"
)


# Enter a context with an instance of the API client
with partnercenter.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = listing_client.ListingClient(api_client)
    product_id = "productID_example" # str | ID of product
    listing_id = "listingID_example" # str | ID of listing
    authorization = "Authorization_example" # str | User authorization
    client_request_id = "Client-Request-ID_example" # str | ID of request provIDed by user (optional)
    microsoft_ingestion_api_models_listings_azure_listing = MicrosoftIngestionApiModelsListingsAzureListing(None) # MicrosoftIngestionApiModelsListingsAzureListing | Request body of a Microsoft.Ingestion.Api.Models.Listings.BaseListing (optional)

    # example passing only required values which don't have defaults set
    try:
        # Updates Listing resource
        api_response = api_instance.products_product_id_listings_listing_id_put(product_id, listing_id, authorization)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling ListingClient->products_product_id_listings_listing_id_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Updates Listing resource
        api_response = api_instance.products_product_id_listings_listing_id_put(product_id, listing_id, authorization, client_request_id=client_request_id, microsoft_ingestion_api_models_listings_azure_listing=microsoft_ingestion_api_models_listings_azure_listing)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling ListingClient->products_product_id_listings_listing_id_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| ID of product |
 **listing_id** | **str**| ID of listing |
 **authorization** | **str**| User authorization |
 **client_request_id** | **str**| ID of request provIDed by user | [optional]
 **microsoft_ingestion_api_models_listings_azure_listing** | [**MicrosoftIngestionApiModelsListingsAzureListing**](MicrosoftIngestionApiModelsListingsAzureListing.md)| Request body of a Microsoft.Ingestion.Api.Models.Listings.BaseListing | [optional]

### Return type

[**MicrosoftIngestionApiModelsListingsAzureListing**](MicrosoftIngestionApiModelsListingsAzureListing.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns updated Listing resource |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Resource not available |  -  |
**405** | Method not allowed |  -  |
**409** | Conflict |  -  |
**429** | Request rate exceeds limit |  -  |
**0** | Unknown error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

