# partnercenter.ListingAssetClient

All URIs are relative to *https://api.partner.microsoft.com/v1.0/ingestion*

Method | HTTP request | Description
------------- | ------------- | -------------
[**products_product_id_listings_listing_id_assets_asset_id_delete**](ListingAssetClient.md#products_product_id_listings_listing_id_assets_asset_id_delete) | **DELETE** /products/{productID}/listings/{listingID}/assets/{assetID} | Deletes a ListingAsset resource
[**products_product_id_listings_listing_id_assets_asset_id_get**](ListingAssetClient.md#products_product_id_listings_listing_id_assets_asset_id_get) | **GET** /products/{productID}/listings/{listingID}/assets/{assetID} | Returns a ListingAsset resource
[**products_product_id_listings_listing_id_assets_asset_id_put**](ListingAssetClient.md#products_product_id_listings_listing_id_assets_asset_id_put) | **PUT** /products/{productID}/listings/{listingID}/assets/{assetID} | Updates a ListingImage resource
[**products_product_id_listings_listing_id_assets_get**](ListingAssetClient.md#products_product_id_listings_listing_id_assets_get) | **GET** /products/{productID}/listings/{listingID}/assets | Returns a paged collection of ListingAsset resources
[**products_product_id_listings_listing_id_assets_post**](ListingAssetClient.md#products_product_id_listings_listing_id_assets_post) | **POST** /products/{productID}/listings/{listingID}/assets | Creates a ListingAsset resource


# **products_product_id_listings_listing_id_assets_asset_id_delete**
> str products_product_id_listings_listing_id_assets_asset_id_delete(product_id, listing_id, asset_id, authorization)

Deletes a ListingAsset resource

Sample request:                    DELETE /products/{productID}/listings/{listingID}/assets/{assetID}

### Example


```python
import time
import partnercenter
from ..api import listing_asset_client
from pprint import pprint
# Defining the host is optional and defaults to https://api.partner.microsoft.com/v1.0/ingestion
# See configuration.py for a list of all supported configuration parameters.
configuration = partnercenter.Configuration(
    host = "https://api.partner.microsoft.com/v1.0/ingestion"
)


# Enter a context with an instance of the API client
with partnercenter.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = listing_asset_client.ListingAssetClient(api_client)
    product_id = "productID_example" # str | ID of product
    listing_id = "listingID_example" # str | ID of listing
    asset_id = "assetID_example" # str | ID of asset
    authorization = "Authorization_example" # str | User authorization
    client_request_id = "Client-Request-ID_example" # str | ID of request provIDed by user (optional)

    # example passing only required values which don't have defaults set
    try:
        # Deletes a ListingAsset resource
        api_response = api_instance.products_product_id_listings_listing_id_assets_asset_id_delete(product_id, listing_id, asset_id, authorization)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling ListingAssetClient->products_product_id_listings_listing_id_assets_asset_id_delete: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Deletes a ListingAsset resource
        api_response = api_instance.products_product_id_listings_listing_id_assets_asset_id_delete(product_id, listing_id, asset_id, authorization, client_request_id=client_request_id)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling ListingAssetClient->products_product_id_listings_listing_id_assets_asset_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| ID of product |
 **listing_id** | **str**| ID of listing |
 **asset_id** | **str**| ID of asset |
 **authorization** | **str**| User authorization |
 **client_request_id** | **str**| ID of request provIDed by user | [optional]

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Resource not available |  -  |
**405** | Method not allowed |  -  |
**409** | Conflict |  -  |
**429** | Request rate exceeds limit |  -  |
**0** | Unknown error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_product_id_listings_listing_id_assets_asset_id_get**
> MicrosoftIngestionApiModelsListingsListingAsset products_product_id_listings_listing_id_assets_asset_id_get(product_id, listing_id, asset_id, authorization)

Returns a ListingAsset resource

Sample request:                    GET /products/{productID}/listings/{listingID}/assets/{assetID}

### Example


```python
import time
import partnercenter
from ..api import listing_asset_client
from ..model.microsoft_ingestion_api_models_listings_listing_asset import MicrosoftIngestionApiModelsListingsListingAsset
from pprint import pprint
# Defining the host is optional and defaults to https://api.partner.microsoft.com/v1.0/ingestion
# See configuration.py for a list of all supported configuration parameters.
configuration = partnercenter.Configuration(
    host = "https://api.partner.microsoft.com/v1.0/ingestion"
)


# Enter a context with an instance of the API client
with partnercenter.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = listing_asset_client.ListingAssetClient(api_client)
    product_id = "productID_example" # str | ID of product
    listing_id = "listingID_example" # str | ID of listing
    asset_id = "assetID_example" # str | ID of asset
    authorization = "Authorization_example" # str | User authorization
    expand = "$expand_example" # str | Use $expand=FileSasUri to Include SAS URI in response (optional)
    client_request_id = "Client-Request-ID_example" # str | ID of request provIDed by user (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a ListingAsset resource
        api_response = api_instance.products_product_id_listings_listing_id_assets_asset_id_get(product_id, listing_id, asset_id, authorization)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling ListingAssetClient->products_product_id_listings_listing_id_assets_asset_id_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a ListingAsset resource
        api_response = api_instance.products_product_id_listings_listing_id_assets_asset_id_get(product_id, listing_id, asset_id, authorization, expand=expand, client_request_id=client_request_id)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling ListingAssetClient->products_product_id_listings_listing_id_assets_asset_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| ID of product |
 **listing_id** | **str**| ID of listing |
 **asset_id** | **str**| ID of asset |
 **authorization** | **str**| User authorization |
 **expand** | **str**| Use $expand&#x3D;FileSasUri to Include SAS URI in response | [optional]
 **client_request_id** | **str**| ID of request provIDed by user | [optional]

### Return type

[**MicrosoftIngestionApiModelsListingsListingAsset**](MicrosoftIngestionApiModelsListingsListingAsset.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a ListingAsset resource |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Resource not available |  -  |
**405** | Method not allowed |  -  |
**409** | Conflict |  -  |
**429** | Request rate exceeds limit |  -  |
**0** | Unknown error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_product_id_listings_listing_id_assets_asset_id_put**
> MicrosoftIngestionApiModelsListingsListingAsset products_product_id_listings_listing_id_assets_asset_id_put(product_id, listing_id, asset_id, authorization)

Updates a ListingImage resource

Sample request:                    PUT /products/{productID}/listings/{listingID}/assets/{assetID} [Body ListingImage]

### Example


```python
import time
import partnercenter
from ..api import listing_asset_client
from ..model.microsoft_ingestion_api_models_listings_listing_asset import MicrosoftIngestionApiModelsListingsListingAsset
from pprint import pprint
# Defining the host is optional and defaults to https://api.partner.microsoft.com/v1.0/ingestion
# See configuration.py for a list of all supported configuration parameters.
configuration = partnercenter.Configuration(
    host = "https://api.partner.microsoft.com/v1.0/ingestion"
)


# Enter a context with an instance of the API client
with partnercenter.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = listing_asset_client.ListingAssetClient(api_client)
    product_id = "productID_example" # str | ID of product
    listing_id = "listingID_example" # str | ID of listing
    asset_id = "assetID_example" # str | ID of asset
    authorization = "Authorization_example" # str | User authorization
    client_request_id = "Client-Request-ID_example" # str | ID of request provIDed by user (optional)
    microsoft_ingestion_api_models_listings_listing_asset = MicrosoftIngestionApiModelsListingsListingAsset(None) # MicrosoftIngestionApiModelsListingsListingAsset | Request body of a Microsoft.Ingestion.Api.Models.Listings.ListingAsset (optional)

    # example passing only required values which don't have defaults set
    try:
        # Updates a ListingImage resource
        api_response = api_instance.products_product_id_listings_listing_id_assets_asset_id_put(product_id, listing_id, asset_id, authorization)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling ListingAssetClient->products_product_id_listings_listing_id_assets_asset_id_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Updates a ListingImage resource
        api_response = api_instance.products_product_id_listings_listing_id_assets_asset_id_put(product_id, listing_id, asset_id, authorization, client_request_id=client_request_id, microsoft_ingestion_api_models_listings_listing_asset=microsoft_ingestion_api_models_listings_listing_asset)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling ListingAssetClient->products_product_id_listings_listing_id_assets_asset_id_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| ID of product |
 **listing_id** | **str**| ID of listing |
 **asset_id** | **str**| ID of asset |
 **authorization** | **str**| User authorization |
 **client_request_id** | **str**| ID of request provIDed by user | [optional]
 **microsoft_ingestion_api_models_listings_listing_asset** | [**MicrosoftIngestionApiModelsListingsListingAsset**](MicrosoftIngestionApiModelsListingsListingAsset.md)| Request body of a Microsoft.Ingestion.Api.Models.Listings.ListingAsset | [optional]

### Return type

[**MicrosoftIngestionApiModelsListingsListingAsset**](MicrosoftIngestionApiModelsListingsListingAsset.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns updated ListingAsset resource |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Resource not available |  -  |
**405** | Method not allowed |  -  |
**409** | Conflict |  -  |
**429** | Request rate exceeds limit |  -  |
**0** | Unknown error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_product_id_listings_listing_id_assets_get**
> MicrosoftIngestionApiModelsCommonPagedCollectionMicrosoftIngestionApiModelsListingsListingAsset products_product_id_listings_listing_id_assets_get(product_id, listing_id, authorization)

Returns a paged collection of ListingAsset resources

Sample request:                    GET /products/{productID}/listings/{listingID}/assets                      =&gt; returns all ListingAsset resources for a given listingID

### Example


```python
import time
import partnercenter
from ..api import listing_asset_client
from ..model.microsoft_ingestion_api_models_common_paged_collection_microsoft_ingestion_api_models_listings_listing_asset import MicrosoftIngestionApiModelsCommonPagedCollectionMicrosoftIngestionApiModelsListingsListingAsset
from pprint import pprint
# Defining the host is optional and defaults to https://api.partner.microsoft.com/v1.0/ingestion
# See configuration.py for a list of all supported configuration parameters.
configuration = partnercenter.Configuration(
    host = "https://api.partner.microsoft.com/v1.0/ingestion"
)


# Enter a context with an instance of the API client
with partnercenter.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = listing_asset_client.ListingAssetClient(api_client)
    product_id = "productID_example" # str | ID of product
    listing_id = "listingID_example" # str | ID of listing
    authorization = "Authorization_example" # str | User authorization
    expand = "$expand_example" # str | Use $expand=FileSasUri to Include SAS URI in response (optional)
    client_request_id = "Client-Request-ID_example" # str | ID of request provIDed by user (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a paged collection of ListingAsset resources
        api_response = api_instance.products_product_id_listings_listing_id_assets_get(product_id, listing_id, authorization)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling ListingAssetClient->products_product_id_listings_listing_id_assets_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a paged collection of ListingAsset resources
        api_response = api_instance.products_product_id_listings_listing_id_assets_get(product_id, listing_id, authorization, expand=expand, client_request_id=client_request_id)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling ListingAssetClient->products_product_id_listings_listing_id_assets_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| ID of product |
 **listing_id** | **str**| ID of listing |
 **authorization** | **str**| User authorization |
 **expand** | **str**| Use $expand&#x3D;FileSasUri to Include SAS URI in response | [optional]
 **client_request_id** | **str**| ID of request provIDed by user | [optional]

### Return type

[**MicrosoftIngestionApiModelsCommonPagedCollectionMicrosoftIngestionApiModelsListingsListingAsset**](MicrosoftIngestionApiModelsCommonPagedCollectionMicrosoftIngestionApiModelsListingsListingAsset.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a paged collection of ListingAsset resources |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Resource not available |  -  |
**429** | Request rate exceeds limit |  -  |
**0** | Unknown error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_product_id_listings_listing_id_assets_post**
> MicrosoftIngestionApiModelsListingsListingAsset products_product_id_listings_listing_id_assets_post(product_id, listing_id, authorization)

Creates a ListingAsset resource

Sample request:                    POST /products/{productID}/listings/{listingID}/assets/{assetID} [Body ListingAsset]

### Example


```python
import time
import partnercenter
from ..api import listing_asset_client
from ..model.microsoft_ingestion_api_models_listings_listing_asset import MicrosoftIngestionApiModelsListingsListingAsset
from pprint import pprint
# Defining the host is optional and defaults to https://api.partner.microsoft.com/v1.0/ingestion
# See configuration.py for a list of all supported configuration parameters.
configuration = partnercenter.Configuration(
    host = "https://api.partner.microsoft.com/v1.0/ingestion"
)


# Enter a context with an instance of the API client
with partnercenter.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = listing_asset_client.ListingAssetClient(api_client)
    product_id = "productID_example" # str | ID of product
    listing_id = "listingID_example" # str | ID of listing
    authorization = "Authorization_example" # str | User authorization
    client_request_id = "Client-Request-ID_example" # str | ID of request provIDed by user (optional)
    microsoft_ingestion_api_models_listings_listing_asset = MicrosoftIngestionApiModelsListingsListingAsset(None) # MicrosoftIngestionApiModelsListingsListingAsset | Request body of a Microsoft.Ingestion.Api.Models.Listings.ListingAsset (optional)

    # example passing only required values which don't have defaults set
    try:
        # Creates a ListingAsset resource
        api_response = api_instance.products_product_id_listings_listing_id_assets_post(product_id, listing_id, authorization)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling ListingAssetClient->products_product_id_listings_listing_id_assets_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Creates a ListingAsset resource
        api_response = api_instance.products_product_id_listings_listing_id_assets_post(product_id, listing_id, authorization, client_request_id=client_request_id, microsoft_ingestion_api_models_listings_listing_asset=microsoft_ingestion_api_models_listings_listing_asset)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling ListingAssetClient->products_product_id_listings_listing_id_assets_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| ID of product |
 **listing_id** | **str**| ID of listing |
 **authorization** | **str**| User authorization |
 **client_request_id** | **str**| ID of request provIDed by user | [optional]
 **microsoft_ingestion_api_models_listings_listing_asset** | [**MicrosoftIngestionApiModelsListingsListingAsset**](MicrosoftIngestionApiModelsListingsListingAsset.md)| Request body of a Microsoft.Ingestion.Api.Models.Listings.ListingAsset | [optional]

### Return type

[**MicrosoftIngestionApiModelsListingsListingAsset**](MicrosoftIngestionApiModelsListingsListingAsset.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Returns newly created ListingAsset resource |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Resource not available |  -  |
**405** | Method not allowed |  -  |
**409** | Conflict |  -  |
**429** | Request rate exceeds limit |  -  |
**0** | Unknown error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

