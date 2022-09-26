# partnercenter.ListingVideoClient

All URIs are relative to *https://api.partner.microsoft.com/v1.0/ingestion*

Method | HTTP request | Description
------------- | ------------- | -------------
[**products_product_id_listings_listing_id_videos_get**](ListingVideoClient.md#products_product_id_listings_listing_id_videos_get) | **GET** /products/{productID}/listings/{listingID}/videos | Returns a paged collection of ListingVideo resources
[**products_product_id_listings_listing_id_videos_post**](ListingVideoClient.md#products_product_id_listings_listing_id_videos_post) | **POST** /products/{productID}/listings/{listingID}/videos | Creates a ListingVideo resource
[**products_product_id_listings_listing_id_videos_video_id_delete**](ListingVideoClient.md#products_product_id_listings_listing_id_videos_video_id_delete) | **DELETE** /products/{productID}/listings/{listingID}/videos/{videoID} | Deletes a ListingVideo resource
[**products_product_id_listings_listing_id_videos_video_id_get**](ListingVideoClient.md#products_product_id_listings_listing_id_videos_video_id_get) | **GET** /products/{productID}/listings/{listingID}/videos/{videoID} | Returns a ListingVideo resource
[**products_product_id_listings_listing_id_videos_video_id_put**](ListingVideoClient.md#products_product_id_listings_listing_id_videos_video_id_put) | **PUT** /products/{productID}/listings/{listingID}/videos/{videoID} | Updates a ListingVideo resource


# **products_product_id_listings_listing_id_videos_get**
> MicrosoftIngestionApiModelsCommonPagedCollectionMicrosoftIngestionApiModelsListingsListingVideo products_product_id_listings_listing_id_videos_get(product_id, listing_id, authorization)

Returns a paged collection of ListingVideo resources

Sample request:                    GET /products/{productID}/listings/{listingID}/videos                      =&gt; returns ListingVideo resources for a given language

### Example


```python
import time
import partnercenter
from ..api import listing_video_client
from ..model.microsoft_ingestion_api_models_common_paged_collection_microsoft_ingestion_api_models_listings_listing_video import MicrosoftIngestionApiModelsCommonPagedCollectionMicrosoftIngestionApiModelsListingsListingVideo
from pprint import pprint
# Defining the host is optional and defaults to https://api.partner.microsoft.com/v1.0/ingestion
# See configuration.py for a list of all supported configuration parameters.
configuration = partnercenter.Configuration(
    host = "https://api.partner.microsoft.com/v1.0/ingestion"
)


# Enter a context with an instance of the API client
with partnercenter.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = listing_video_client.ListingVideoClient(api_client)
    product_id = "productID_example" # str | ID of product
    listing_id = "listingID_example" # str | ID of listing
    authorization = "Authorization_example" # str | User authorization
    expand = "$expand_example" # str | Use $expand=FileSasUri to Include SAS URI in response (optional)
    client_request_id = "Client-Request-ID_example" # str | ID of request provIDed by user (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a paged collection of ListingVideo resources
        api_response = api_instance.products_product_id_listings_listing_id_videos_get(product_id, listing_id, authorization)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling ListingVideoClient->products_product_id_listings_listing_id_videos_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a paged collection of ListingVideo resources
        api_response = api_instance.products_product_id_listings_listing_id_videos_get(product_id, listing_id, authorization, expand=expand, client_request_id=client_request_id)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling ListingVideoClient->products_product_id_listings_listing_id_videos_get: %s\n" % e)
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

[**MicrosoftIngestionApiModelsCommonPagedCollectionMicrosoftIngestionApiModelsListingsListingVideo**](MicrosoftIngestionApiModelsCommonPagedCollectionMicrosoftIngestionApiModelsListingsListingVideo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a paged collection of ListingVideo resources |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Resource not available |  -  |
**405** | Method not allowed |  -  |
**409** | Conflict |  -  |
**429** | Request rate exceeds limit |  -  |
**0** | Unknown error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_product_id_listings_listing_id_videos_post**
> MicrosoftIngestionApiModelsListingsListingVideo products_product_id_listings_listing_id_videos_post(product_id, listing_id, authorization)

Creates a ListingVideo resource

Sample request:                    POST /products/{productID}/listings/{listingID}/videos   [Body ListingVideo]

### Example


```python
import time
import partnercenter
from ..api import listing_video_client
from ..model.microsoft_ingestion_api_models_listings_listing_video import MicrosoftIngestionApiModelsListingsListingVideo
from pprint import pprint
# Defining the host is optional and defaults to https://api.partner.microsoft.com/v1.0/ingestion
# See configuration.py for a list of all supported configuration parameters.
configuration = partnercenter.Configuration(
    host = "https://api.partner.microsoft.com/v1.0/ingestion"
)


# Enter a context with an instance of the API client
with partnercenter.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = listing_video_client.ListingVideoClient(api_client)
    product_id = "productID_example" # str | ID of product
    listing_id = "listingID_example" # str | ID of listing
    authorization = "Authorization_example" # str | User authorization
    client_request_id = "Client-Request-ID_example" # str | ID of request provIDed by user (optional)
    microsoft_ingestion_api_models_listings_listing_video = MicrosoftIngestionApiModelsListingsListingVideo(None) # MicrosoftIngestionApiModelsListingsListingVideo | Request body of a Microsoft.Ingestion.Api.Models.Listings.ListingVideo (optional)

    # example passing only required values which don't have defaults set
    try:
        # Creates a ListingVideo resource
        api_response = api_instance.products_product_id_listings_listing_id_videos_post(product_id, listing_id, authorization)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling ListingVideoClient->products_product_id_listings_listing_id_videos_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Creates a ListingVideo resource
        api_response = api_instance.products_product_id_listings_listing_id_videos_post(product_id, listing_id, authorization, client_request_id=client_request_id, microsoft_ingestion_api_models_listings_listing_video=microsoft_ingestion_api_models_listings_listing_video)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling ListingVideoClient->products_product_id_listings_listing_id_videos_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| ID of product |
 **listing_id** | **str**| ID of listing |
 **authorization** | **str**| User authorization |
 **client_request_id** | **str**| ID of request provIDed by user | [optional]
 **microsoft_ingestion_api_models_listings_listing_video** | [**MicrosoftIngestionApiModelsListingsListingVideo**](MicrosoftIngestionApiModelsListingsListingVideo.md)| Request body of a Microsoft.Ingestion.Api.Models.Listings.ListingVideo | [optional]

### Return type

[**MicrosoftIngestionApiModelsListingsListingVideo**](MicrosoftIngestionApiModelsListingsListingVideo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Returns newly created ListingVideo resource |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Resource not available |  -  |
**405** | Method not allowed |  -  |
**409** | Conflict |  -  |
**429** | Request rate exceeds limit |  -  |
**0** | Unknown error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_product_id_listings_listing_id_videos_video_id_delete**
> str products_product_id_listings_listing_id_videos_video_id_delete(product_id, listing_id, video_id, authorization)

Deletes a ListingVideo resource

Sample request:                    DELETE /products/{productID}/listings/{listingID}/videos/{videoID}

### Example


```python
import time
import partnercenter
from ..api import listing_video_client
from pprint import pprint
# Defining the host is optional and defaults to https://api.partner.microsoft.com/v1.0/ingestion
# See configuration.py for a list of all supported configuration parameters.
configuration = partnercenter.Configuration(
    host = "https://api.partner.microsoft.com/v1.0/ingestion"
)


# Enter a context with an instance of the API client
with partnercenter.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = listing_video_client.ListingVideoClient(api_client)
    product_id = "productID_example" # str | ID of product
    listing_id = "listingID_example" # str | ID of listing
    video_id = "videoID_example" # str | ID of ListingVideo
    authorization = "Authorization_example" # str | User authorization
    client_request_id = "Client-Request-ID_example" # str | ID of request provIDed by user (optional)

    # example passing only required values which don't have defaults set
    try:
        # Deletes a ListingVideo resource
        api_response = api_instance.products_product_id_listings_listing_id_videos_video_id_delete(product_id, listing_id, video_id, authorization)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling ListingVideoClient->products_product_id_listings_listing_id_videos_video_id_delete: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Deletes a ListingVideo resource
        api_response = api_instance.products_product_id_listings_listing_id_videos_video_id_delete(product_id, listing_id, video_id, authorization, client_request_id=client_request_id)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling ListingVideoClient->products_product_id_listings_listing_id_videos_video_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| ID of product |
 **listing_id** | **str**| ID of listing |
 **video_id** | **str**| ID of ListingVideo |
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

# **products_product_id_listings_listing_id_videos_video_id_get**
> MicrosoftIngestionApiModelsListingsListingVideo products_product_id_listings_listing_id_videos_video_id_get(product_id, listing_id, video_id, authorization)

Returns a ListingVideo resource

Sample request:                    GET /products/{productID}/listings/{listingID}/videos/{videoID}

### Example


```python
import time
import partnercenter
from ..api import listing_video_client
from ..model.microsoft_ingestion_api_models_listings_listing_video import MicrosoftIngestionApiModelsListingsListingVideo
from pprint import pprint
# Defining the host is optional and defaults to https://api.partner.microsoft.com/v1.0/ingestion
# See configuration.py for a list of all supported configuration parameters.
configuration = partnercenter.Configuration(
    host = "https://api.partner.microsoft.com/v1.0/ingestion"
)


# Enter a context with an instance of the API client
with partnercenter.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = listing_video_client.ListingVideoClient(api_client)
    product_id = "productID_example" # str | ID of product
    listing_id = "listingID_example" # str | ID of listing
    video_id = "videoID_example" # str | ID of Video
    authorization = "Authorization_example" # str | User authorization
    expand = "$expand_example" # str | Use $expand=FileSasUri to Include SAS URI in response (optional)
    client_request_id = "Client-Request-ID_example" # str | ID of request provIDed by user (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a ListingVideo resource
        api_response = api_instance.products_product_id_listings_listing_id_videos_video_id_get(product_id, listing_id, video_id, authorization)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling ListingVideoClient->products_product_id_listings_listing_id_videos_video_id_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a ListingVideo resource
        api_response = api_instance.products_product_id_listings_listing_id_videos_video_id_get(product_id, listing_id, video_id, authorization, expand=expand, client_request_id=client_request_id)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling ListingVideoClient->products_product_id_listings_listing_id_videos_video_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| ID of product |
 **listing_id** | **str**| ID of listing |
 **video_id** | **str**| ID of Video |
 **authorization** | **str**| User authorization |
 **expand** | **str**| Use $expand&#x3D;FileSasUri to Include SAS URI in response | [optional]
 **client_request_id** | **str**| ID of request provIDed by user | [optional]

### Return type

[**MicrosoftIngestionApiModelsListingsListingVideo**](MicrosoftIngestionApiModelsListingsListingVideo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns ListingVideo resource |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Resource not available |  -  |
**405** | Method not allowed |  -  |
**409** | Conflict |  -  |
**429** | Request rate exceeds limit |  -  |
**0** | Unknown error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_product_id_listings_listing_id_videos_video_id_put**
> MicrosoftIngestionApiModelsListingsListingVideo products_product_id_listings_listing_id_videos_video_id_put(product_id, listing_id, video_id, authorization)

Updates a ListingVideo resource

Sample request:                    PUT /products/{productID}/listings/{listingID}/videos/{videoID} [Body ListingVideo]

### Example


```python
import time
import partnercenter
from ..api import listing_video_client
from ..model.microsoft_ingestion_api_models_listings_listing_video import MicrosoftIngestionApiModelsListingsListingVideo
from pprint import pprint
# Defining the host is optional and defaults to https://api.partner.microsoft.com/v1.0/ingestion
# See configuration.py for a list of all supported configuration parameters.
configuration = partnercenter.Configuration(
    host = "https://api.partner.microsoft.com/v1.0/ingestion"
)


# Enter a context with an instance of the API client
with partnercenter.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = listing_video_client.ListingVideoClient(api_client)
    product_id = "productID_example" # str | ID of product
    listing_id = "listingID_example" # str | ID of listing
    video_id = "videoID_example" # str | ID of ListingVideo
    authorization = "Authorization_example" # str | User authorization
    client_request_id = "Client-Request-ID_example" # str | ID of request provIDed by user (optional)
    microsoft_ingestion_api_models_listings_listing_video = MicrosoftIngestionApiModelsListingsListingVideo(None) # MicrosoftIngestionApiModelsListingsListingVideo | Request body of a Microsoft.Ingestion.Api.Models.Listings.ListingVideo (optional)

    # example passing only required values which don't have defaults set
    try:
        # Updates a ListingVideo resource
        api_response = api_instance.products_product_id_listings_listing_id_videos_video_id_put(product_id, listing_id, video_id, authorization)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling ListingVideoClient->products_product_id_listings_listing_id_videos_video_id_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Updates a ListingVideo resource
        api_response = api_instance.products_product_id_listings_listing_id_videos_video_id_put(product_id, listing_id, video_id, authorization, client_request_id=client_request_id, microsoft_ingestion_api_models_listings_listing_video=microsoft_ingestion_api_models_listings_listing_video)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling ListingVideoClient->products_product_id_listings_listing_id_videos_video_id_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| ID of product |
 **listing_id** | **str**| ID of listing |
 **video_id** | **str**| ID of ListingVideo |
 **authorization** | **str**| User authorization |
 **client_request_id** | **str**| ID of request provIDed by user | [optional]
 **microsoft_ingestion_api_models_listings_listing_video** | [**MicrosoftIngestionApiModelsListingsListingVideo**](MicrosoftIngestionApiModelsListingsListingVideo.md)| Request body of a Microsoft.Ingestion.Api.Models.Listings.ListingVideo | [optional]

### Return type

[**MicrosoftIngestionApiModelsListingsListingVideo**](MicrosoftIngestionApiModelsListingsListingVideo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the updated ListingVideo resource |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Resource not available |  -  |
**405** | Method not allowed |  -  |
**409** | Conflict |  -  |
**429** | Request rate exceeds limit |  -  |
**0** | Unknown error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

