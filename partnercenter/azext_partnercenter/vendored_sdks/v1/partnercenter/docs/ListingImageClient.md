# partnercenter.ListingImageClient

All URIs are relative to *https://api.partner.microsoft.com/v1.0/ingestion*

Method | HTTP request | Description
------------- | ------------- | -------------
[**products_product_id_listings_listing_id_images_get**](ListingImageClient.md#products_product_id_listings_listing_id_images_get) | **GET** /products/{productID}/listings/{listingID}/images | Returns a paged collection of ListingImage resources
[**products_product_id_listings_listing_id_images_image_id_delete**](ListingImageClient.md#products_product_id_listings_listing_id_images_image_id_delete) | **DELETE** /products/{productID}/listings/{listingID}/images/{imageID} | Deletes a ListingImage resource
[**products_product_id_listings_listing_id_images_image_id_get**](ListingImageClient.md#products_product_id_listings_listing_id_images_image_id_get) | **GET** /products/{productID}/listings/{listingID}/images/{imageID} | Returns a ListingImage resource
[**products_product_id_listings_listing_id_images_image_id_put**](ListingImageClient.md#products_product_id_listings_listing_id_images_image_id_put) | **PUT** /products/{productID}/listings/{listingID}/images/{imageID} | Updates a ListingImage resource
[**products_product_id_listings_listing_id_images_post**](ListingImageClient.md#products_product_id_listings_listing_id_images_post) | **POST** /products/{productID}/listings/{listingID}/images | Creates a ListingImage resource


# **products_product_id_listings_listing_id_images_get**
> MicrosoftIngestionApiModelsCommonPagedCollectionMicrosoftIngestionApiModelsListingsListingImage products_product_id_listings_listing_id_images_get(product_id, listing_id, authorization)

Returns a paged collection of ListingImage resources

Sample request:                    GET /products/{productID}/listings/{listingID}/images                      returns all ListingImage resources for a given listing                    

### Example


```python
import time
import partnercenter
from ..api import listing_image_client
from ..model.microsoft_ingestion_api_models_common_paged_collection_microsoft_ingestion_api_models_listings_listing_image import MicrosoftIngestionApiModelsCommonPagedCollectionMicrosoftIngestionApiModelsListingsListingImage
from pprint import pprint
# Defining the host is optional and defaults to https://api.partner.microsoft.com/v1.0/ingestion
# See configuration.py for a list of all supported configuration parameters.
configuration = partnercenter.Configuration(
    host = "https://api.partner.microsoft.com/v1.0/ingestion"
)


# Enter a context with an instance of the API client
with partnercenter.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = listing_image_client.ListingImageClient(api_client)
    product_id = "productID_example" # str | ID of product
    listing_id = "listingID_example" # str | ID of listing
    authorization = "Authorization_example" # str | User authorization
    expand = "$expand_example" # str | Use $expand=FileSasUri to Include SAS URI in response (optional)
    client_request_id = "Client-Request-ID_example" # str | ID of request provIDed by user (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a paged collection of ListingImage resources
        api_response = api_instance.products_product_id_listings_listing_id_images_get(product_id, listing_id, authorization)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling ListingImageClient->products_product_id_listings_listing_id_images_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a paged collection of ListingImage resources
        api_response = api_instance.products_product_id_listings_listing_id_images_get(product_id, listing_id, authorization, expand=expand, client_request_id=client_request_id)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling ListingImageClient->products_product_id_listings_listing_id_images_get: %s\n" % e)
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

[**MicrosoftIngestionApiModelsCommonPagedCollectionMicrosoftIngestionApiModelsListingsListingImage**](MicrosoftIngestionApiModelsCommonPagedCollectionMicrosoftIngestionApiModelsListingsListingImage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a paged collection of ListingImage resources |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Resource not available |  -  |
**405** | Method not allowed |  -  |
**409** | Conflict |  -  |
**429** | Request rate exceeds limit |  -  |
**0** | Unknown error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_product_id_listings_listing_id_images_image_id_delete**
> str products_product_id_listings_listing_id_images_image_id_delete(product_id, listing_id, image_id, authorization)

Deletes a ListingImage resource

Sample request:                    DELETE /products/{productID}/listings/{listingID}/images/{imageID}

### Example


```python
import time
import partnercenter
from ..api import listing_image_client
from pprint import pprint
# Defining the host is optional and defaults to https://api.partner.microsoft.com/v1.0/ingestion
# See configuration.py for a list of all supported configuration parameters.
configuration = partnercenter.Configuration(
    host = "https://api.partner.microsoft.com/v1.0/ingestion"
)


# Enter a context with an instance of the API client
with partnercenter.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = listing_image_client.ListingImageClient(api_client)
    product_id = "productID_example" # str | ID of product
    listing_id = "listingID_example" # str | ID of listing
    image_id = "imageID_example" # str | ID of image
    authorization = "Authorization_example" # str | User authorization
    client_request_id = "Client-Request-ID_example" # str | ID of request provIDed by user (optional)

    # example passing only required values which don't have defaults set
    try:
        # Deletes a ListingImage resource
        api_response = api_instance.products_product_id_listings_listing_id_images_image_id_delete(product_id, listing_id, image_id, authorization)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling ListingImageClient->products_product_id_listings_listing_id_images_image_id_delete: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Deletes a ListingImage resource
        api_response = api_instance.products_product_id_listings_listing_id_images_image_id_delete(product_id, listing_id, image_id, authorization, client_request_id=client_request_id)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling ListingImageClient->products_product_id_listings_listing_id_images_image_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| ID of product |
 **listing_id** | **str**| ID of listing |
 **image_id** | **str**| ID of image |
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

# **products_product_id_listings_listing_id_images_image_id_get**
> MicrosoftIngestionApiModelsListingsListingImage products_product_id_listings_listing_id_images_image_id_get(product_id, listing_id, image_id, authorization)

Returns a ListingImage resource

Sample request:                    GET /products/{productID}/listings/{listingID}/images/{imageID}

### Example


```python
import time
import partnercenter
from ..api import listing_image_client
from ..model.microsoft_ingestion_api_models_listings_listing_image import MicrosoftIngestionApiModelsListingsListingImage
from pprint import pprint
# Defining the host is optional and defaults to https://api.partner.microsoft.com/v1.0/ingestion
# See configuration.py for a list of all supported configuration parameters.
configuration = partnercenter.Configuration(
    host = "https://api.partner.microsoft.com/v1.0/ingestion"
)


# Enter a context with an instance of the API client
with partnercenter.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = listing_image_client.ListingImageClient(api_client)
    product_id = "productID_example" # str | ID of product
    listing_id = "listingID_example" # str | ID of listing
    image_id = "imageID_example" # str | ID of image
    authorization = "Authorization_example" # str | User authorization
    expand = "$expand_example" # str | Use $expand=FileSasUri to Include SAS URI in response (optional)
    client_request_id = "Client-Request-ID_example" # str | ID of request provIDed by user (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a ListingImage resource
        api_response = api_instance.products_product_id_listings_listing_id_images_image_id_get(product_id, listing_id, image_id, authorization)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling ListingImageClient->products_product_id_listings_listing_id_images_image_id_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a ListingImage resource
        api_response = api_instance.products_product_id_listings_listing_id_images_image_id_get(product_id, listing_id, image_id, authorization, expand=expand, client_request_id=client_request_id)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling ListingImageClient->products_product_id_listings_listing_id_images_image_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| ID of product |
 **listing_id** | **str**| ID of listing |
 **image_id** | **str**| ID of image |
 **authorization** | **str**| User authorization |
 **expand** | **str**| Use $expand&#x3D;FileSasUri to Include SAS URI in response | [optional]
 **client_request_id** | **str**| ID of request provIDed by user | [optional]

### Return type

[**MicrosoftIngestionApiModelsListingsListingImage**](MicrosoftIngestionApiModelsListingsListingImage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a ListingImage resource |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Resource not available |  -  |
**405** | Method not allowed |  -  |
**409** | Conflict |  -  |
**429** | Request rate exceeds limit |  -  |
**0** | Unknown error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_product_id_listings_listing_id_images_image_id_put**
> MicrosoftIngestionApiModelsListingsListingImage products_product_id_listings_listing_id_images_image_id_put(product_id, listing_id, image_id, authorization)

Updates a ListingImage resource

Sample request:                    PUT /products/{productID}/listings/{listingID}/images/{imageID} [Body ListingImage]

### Example


```python
import time
import partnercenter
from ..api import listing_image_client
from ..model.microsoft_ingestion_api_models_listings_listing_image import MicrosoftIngestionApiModelsListingsListingImage
from pprint import pprint
# Defining the host is optional and defaults to https://api.partner.microsoft.com/v1.0/ingestion
# See configuration.py for a list of all supported configuration parameters.
configuration = partnercenter.Configuration(
    host = "https://api.partner.microsoft.com/v1.0/ingestion"
)


# Enter a context with an instance of the API client
with partnercenter.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = listing_image_client.ListingImageClient(api_client)
    product_id = "productID_example" # str | ID of product
    listing_id = "listingID_example" # str | ID of listing
    image_id = "imageID_example" # str | ID of image
    authorization = "Authorization_example" # str | User authorization
    client_request_id = "Client-Request-ID_example" # str | ID of request provIDed by user (optional)
    microsoft_ingestion_api_models_listings_listing_image = MicrosoftIngestionApiModelsListingsListingImage(None) # MicrosoftIngestionApiModelsListingsListingImage | Request body of a Microsoft.Ingestion.Api.Models.Listings.ListingImage (optional)

    # example passing only required values which don't have defaults set
    try:
        # Updates a ListingImage resource
        api_response = api_instance.products_product_id_listings_listing_id_images_image_id_put(product_id, listing_id, image_id, authorization)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling ListingImageClient->products_product_id_listings_listing_id_images_image_id_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Updates a ListingImage resource
        api_response = api_instance.products_product_id_listings_listing_id_images_image_id_put(product_id, listing_id, image_id, authorization, client_request_id=client_request_id, microsoft_ingestion_api_models_listings_listing_image=microsoft_ingestion_api_models_listings_listing_image)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling ListingImageClient->products_product_id_listings_listing_id_images_image_id_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| ID of product |
 **listing_id** | **str**| ID of listing |
 **image_id** | **str**| ID of image |
 **authorization** | **str**| User authorization |
 **client_request_id** | **str**| ID of request provIDed by user | [optional]
 **microsoft_ingestion_api_models_listings_listing_image** | [**MicrosoftIngestionApiModelsListingsListingImage**](MicrosoftIngestionApiModelsListingsListingImage.md)| Request body of a Microsoft.Ingestion.Api.Models.Listings.ListingImage | [optional]

### Return type

[**MicrosoftIngestionApiModelsListingsListingImage**](MicrosoftIngestionApiModelsListingsListingImage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns updated ListingImage resource |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Resource not available |  -  |
**405** | Method not allowed |  -  |
**409** | Conflict |  -  |
**429** | Request rate exceeds limit |  -  |
**0** | Unknown error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_product_id_listings_listing_id_images_post**
> MicrosoftIngestionApiModelsListingsListingImage products_product_id_listings_listing_id_images_post(product_id, listing_id, authorization)

Creates a ListingImage resource

Sample request:                    POST /products/{productID}/listings/{listingID}/images [Body ListingImage]

### Example


```python
import time
import partnercenter
from ..api import listing_image_client
from ..model.microsoft_ingestion_api_models_listings_listing_image import MicrosoftIngestionApiModelsListingsListingImage
from pprint import pprint
# Defining the host is optional and defaults to https://api.partner.microsoft.com/v1.0/ingestion
# See configuration.py for a list of all supported configuration parameters.
configuration = partnercenter.Configuration(
    host = "https://api.partner.microsoft.com/v1.0/ingestion"
)


# Enter a context with an instance of the API client
with partnercenter.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = listing_image_client.ListingImageClient(api_client)
    product_id = "productID_example" # str | ID of product
    listing_id = "listingID_example" # str | ID of listing
    authorization = "Authorization_example" # str | User authorization
    client_request_id = "Client-Request-ID_example" # str | ID of request provIDed by user (optional)
    microsoft_ingestion_api_models_listings_listing_image = MicrosoftIngestionApiModelsListingsListingImage(None) # MicrosoftIngestionApiModelsListingsListingImage | Request body of a Microsoft.Ingestion.Api.Models.Listings.ListingImage (optional)

    # example passing only required values which don't have defaults set
    try:
        # Creates a ListingImage resource
        api_response = api_instance.products_product_id_listings_listing_id_images_post(product_id, listing_id, authorization)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling ListingImageClient->products_product_id_listings_listing_id_images_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Creates a ListingImage resource
        api_response = api_instance.products_product_id_listings_listing_id_images_post(product_id, listing_id, authorization, client_request_id=client_request_id, microsoft_ingestion_api_models_listings_listing_image=microsoft_ingestion_api_models_listings_listing_image)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling ListingImageClient->products_product_id_listings_listing_id_images_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| ID of product |
 **listing_id** | **str**| ID of listing |
 **authorization** | **str**| User authorization |
 **client_request_id** | **str**| ID of request provIDed by user | [optional]
 **microsoft_ingestion_api_models_listings_listing_image** | [**MicrosoftIngestionApiModelsListingsListingImage**](MicrosoftIngestionApiModelsListingsListingImage.md)| Request body of a Microsoft.Ingestion.Api.Models.Listings.ListingImage | [optional]

### Return type

[**MicrosoftIngestionApiModelsListingsListingImage**](MicrosoftIngestionApiModelsListingsListingImage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Returns newly created ListingImage resource |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Resource not available |  -  |
**405** | Method not allowed |  -  |
**409** | Conflict |  -  |
**429** | Request rate exceeds limit |  -  |
**0** | Unknown error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

