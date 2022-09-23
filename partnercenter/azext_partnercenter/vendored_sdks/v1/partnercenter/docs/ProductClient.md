# partnercenter.ProductClient

All URIs are relative to *https://api.partner.microsoft.com/v1.0/ingestion*

Method | HTTP request | Description
------------- | ------------- | -------------
[**products_get**](ProductClient.md#products_get) | **GET** /products | Returns collection of products.
[**products_post**](ProductClient.md#products_post) | **POST** /products | Creates a Product
[**products_product_id_delete**](ProductClient.md#products_product_id_delete) | **DELETE** /products/{productID} | Deletes a product
[**products_product_id_get**](ProductClient.md#products_product_id_get) | **GET** /products/{productID} | Returns a product.
[**products_product_id_setup_get**](ProductClient.md#products_product_id_setup_get) | **GET** /products/{productID}/setup | Returns ProductSetup of a Product.
[**products_product_id_setup_post**](ProductClient.md#products_product_id_setup_post) | **POST** /products/{productID}/setup | Creates a ProductSetup [AzureProductSetup is allowed]


# **products_get**
> MicrosoftIngestionApiModelsCommonPagedCollectionMicrosoftIngestionApiModelsProductsBaseProduct products_get(authorization)

Returns collection of products.

Sample requests:        GET /products?$filter=ResourceType eq 'Application' or ResourceType eq 'SoftwareAsAService'       GET /products?$filter=ExternalIDs/Any(i:i/Type eq 'StoreID' and i/Value eq '{storeID}')      GET /products?$filter=ExternalIDs/Any(i:i/Type eq 'ExternalAzureProductID' and i/Value eq '{externalAzureProductID}')

### Example


```python
import time
import partnercenter
from ..api import product_client
from ..model.microsoft_ingestion_api_models_common_paged_collection_microsoft_ingestion_api_models_products_base_product import MicrosoftIngestionApiModelsCommonPagedCollectionMicrosoftIngestionApiModelsProductsBaseProduct
from pprint import pprint
# Defining the host is optional and defaults to https://api.partner.microsoft.com/v1.0/ingestion
# See configuration.py for a list of all supported configuration parameters.
configuration = partnercenter.Configuration(
    host = "https://api.partner.microsoft.com/v1.0/ingestion"
)


# Enter a context with an instance of the API client
with partnercenter.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = product_client.ProductClient(api_client)
    authorization = "Authorization_example" # str | User authorization
    filter = "$filter_example" # str | Filter for paged collection. Filter by ResourceType or ExternalIDs with operation eq is allowed. (optional)
    skip_token = "$skipToken_example" # str | Skip token for paged collection (optional)
    client_request_id = "Client-Request-ID_example" # str | ID of request provIDed by user (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns collection of products.
        api_response = api_instance.products_get(authorization)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling ProductClient->products_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns collection of products.
        api_response = api_instance.products_get(authorization, filter=filter, skip_token=skip_token, client_request_id=client_request_id)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling ProductClient->products_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| User authorization |
 **filter** | **str**| Filter for paged collection. Filter by ResourceType or ExternalIDs with operation eq is allowed. | [optional]
 **skip_token** | **str**| Skip token for paged collection | [optional]
 **client_request_id** | **str**| ID of request provIDed by user | [optional]

### Return type

[**MicrosoftIngestionApiModelsCommonPagedCollectionMicrosoftIngestionApiModelsProductsBaseProduct**](MicrosoftIngestionApiModelsCommonPagedCollectionMicrosoftIngestionApiModelsProductsBaseProduct.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Resource not available |  -  |
**409** | Conflict |  -  |
**429** | Request rate exceeds limit |  -  |
**0** | Unknown error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_post**
> MicrosoftIngestionApiModelsProductsAzureProduct products_post(authorization)

Creates a Product

Sample requests:                    POST /product                   {                       \"resourceType\": \"AzureThirdPartyVirtualMachine\",                       \"name\": \"testVm\",                       \"externalIDs\" : [                        {                           \"type\": \"AzureOfferID\",                           \"value\" : \"testOfferID\",                        }]                   }

### Example


```python
import time
import partnercenter
from ..api import product_client
from ..model.microsoft_ingestion_api_models_products_azure_product import MicrosoftIngestionApiModelsProductsAzureProduct
from pprint import pprint
# Defining the host is optional and defaults to https://api.partner.microsoft.com/v1.0/ingestion
# See configuration.py for a list of all supported configuration parameters.
configuration = partnercenter.Configuration(
    host = "https://api.partner.microsoft.com/v1.0/ingestion"
)


# Enter a context with an instance of the API client
with partnercenter.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = product_client.ProductClient(api_client)
    authorization = "Authorization_example" # str | User authorization
    client_request_id = "Client-Request-ID_example" # str | ID of request provIDed by user (optional)
    microsoft_ingestion_api_models_products_azure_product = MicrosoftIngestionApiModelsProductsAzureProduct(None) # MicrosoftIngestionApiModelsProductsAzureProduct | Request body of a Microsoft.Ingestion.Api.Models.Products.BaseProduct (optional)

    # example passing only required values which don't have defaults set
    try:
        # Creates a Product
        api_response = api_instance.products_post(authorization)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling ProductClient->products_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Creates a Product
        api_response = api_instance.products_post(authorization, client_request_id=client_request_id, microsoft_ingestion_api_models_products_azure_product=microsoft_ingestion_api_models_products_azure_product)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling ProductClient->products_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| User authorization |
 **client_request_id** | **str**| ID of request provIDed by user | [optional]
 **microsoft_ingestion_api_models_products_azure_product** | [**MicrosoftIngestionApiModelsProductsAzureProduct**](MicrosoftIngestionApiModelsProductsAzureProduct.md)| Request body of a Microsoft.Ingestion.Api.Models.Products.BaseProduct | [optional]

### Return type

[**MicrosoftIngestionApiModelsProductsAzureProduct**](MicrosoftIngestionApiModelsProductsAzureProduct.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Resource not available |  -  |
**405** | Method not allowed |  -  |
**409** | Conflict |  -  |
**429** | Request rate exceeds limit |  -  |
**0** | Unknown error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_product_id_delete**
> str products_product_id_delete(product_id, authorization)

Deletes a product

Sample requests:                    DELETE /products/{productID}

### Example


```python
import time
import partnercenter
from ..api import product_client
from pprint import pprint
# Defining the host is optional and defaults to https://api.partner.microsoft.com/v1.0/ingestion
# See configuration.py for a list of all supported configuration parameters.
configuration = partnercenter.Configuration(
    host = "https://api.partner.microsoft.com/v1.0/ingestion"
)


# Enter a context with an instance of the API client
with partnercenter.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = product_client.ProductClient(api_client)
    product_id = "productID_example" # str | ID of product
    authorization = "Authorization_example" # str | User authorization
    client_request_id = "Client-Request-ID_example" # str | ID of request provIDed by user (optional)

    # example passing only required values which don't have defaults set
    try:
        # Deletes a product
        api_response = api_instance.products_product_id_delete(product_id, authorization)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling ProductClient->products_product_id_delete: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Deletes a product
        api_response = api_instance.products_product_id_delete(product_id, authorization, client_request_id=client_request_id)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling ProductClient->products_product_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| ID of product |
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

# **products_product_id_get**
> MicrosoftIngestionApiModelsProductsAzureProduct products_product_id_get(product_id, authorization)

Returns a product.

Sample requests:                    GET /products/{productID}

### Example


```python
import time
import partnercenter
from ..api import product_client
from ..model.microsoft_ingestion_api_models_products_azure_product import MicrosoftIngestionApiModelsProductsAzureProduct
from pprint import pprint
# Defining the host is optional and defaults to https://api.partner.microsoft.com/v1.0/ingestion
# See configuration.py for a list of all supported configuration parameters.
configuration = partnercenter.Configuration(
    host = "https://api.partner.microsoft.com/v1.0/ingestion"
)


# Enter a context with an instance of the API client
with partnercenter.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = product_client.ProductClient(api_client)
    product_id = "productID_example" # str | ID of product
    authorization = "Authorization_example" # str | User authorization
    client_request_id = "Client-Request-ID_example" # str | ID of request provIDed by user (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a product.
        api_response = api_instance.products_product_id_get(product_id, authorization)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling ProductClient->products_product_id_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a product.
        api_response = api_instance.products_product_id_get(product_id, authorization, client_request_id=client_request_id)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling ProductClient->products_product_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| ID of product |
 **authorization** | **str**| User authorization |
 **client_request_id** | **str**| ID of request provIDed by user | [optional]

### Return type

[**MicrosoftIngestionApiModelsProductsAzureProduct**](MicrosoftIngestionApiModelsProductsAzureProduct.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Resource not available |  -  |
**409** | Conflict |  -  |
**429** | Request rate exceeds limit |  -  |
**0** | Unknown error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_product_id_setup_get**
> MicrosoftIngestionApiModelsProductsAzureProductSetup products_product_id_setup_get(product_id, authorization)

Returns ProductSetup of a Product.

Sample requests:                    GET /products/{productID}/setup

### Example


```python
import time
import partnercenter
from ..api import product_client
from ..model.microsoft_ingestion_api_models_products_azure_product_setup import MicrosoftIngestionApiModelsProductsAzureProductSetup
from pprint import pprint
# Defining the host is optional and defaults to https://api.partner.microsoft.com/v1.0/ingestion
# See configuration.py for a list of all supported configuration parameters.
configuration = partnercenter.Configuration(
    host = "https://api.partner.microsoft.com/v1.0/ingestion"
)


# Enter a context with an instance of the API client
with partnercenter.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = product_client.ProductClient(api_client)
    product_id = "productID_example" # str | ID of product
    authorization = "Authorization_example" # str | User authorization
    client_request_id = "Client-Request-ID_example" # str | ID of request provIDed by user (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns ProductSetup of a Product.
        api_response = api_instance.products_product_id_setup_get(product_id, authorization)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling ProductClient->products_product_id_setup_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns ProductSetup of a Product.
        api_response = api_instance.products_product_id_setup_get(product_id, authorization, client_request_id=client_request_id)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling ProductClient->products_product_id_setup_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| ID of product |
 **authorization** | **str**| User authorization |
 **client_request_id** | **str**| ID of request provIDed by user | [optional]

### Return type

[**MicrosoftIngestionApiModelsProductsAzureProductSetup**](MicrosoftIngestionApiModelsProductsAzureProductSetup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Resource not available |  -  |
**405** | Method not allowed |  -  |
**409** | Conflict |  -  |
**429** | Request rate exceeds limit |  -  |
**0** | Unknown error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_product_id_setup_post**
> MicrosoftIngestionApiModelsProductsAzureProductSetup products_product_id_setup_post(product_id, authorization)

Creates a ProductSetup [AzureProductSetup is allowed]

Sample requests:                    POST /product/{productID}/setup      {          \"resourceType\": \"AzureProductSetup\",          \"leadGenID\": \"testLeadGenID\"      }

### Example


```python
import time
import partnercenter
from ..api import product_client
from ..model.microsoft_ingestion_api_models_products_azure_product_setup import MicrosoftIngestionApiModelsProductsAzureProductSetup
from pprint import pprint
# Defining the host is optional and defaults to https://api.partner.microsoft.com/v1.0/ingestion
# See configuration.py for a list of all supported configuration parameters.
configuration = partnercenter.Configuration(
    host = "https://api.partner.microsoft.com/v1.0/ingestion"
)


# Enter a context with an instance of the API client
with partnercenter.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = product_client.ProductClient(api_client)
    product_id = "productID_example" # str | ID of product
    authorization = "Authorization_example" # str | User authorization
    client_request_id = "Client-Request-ID_example" # str | ID of request provIDed by user (optional)
    microsoft_ingestion_api_models_products_azure_product_setup = MicrosoftIngestionApiModelsProductsAzureProductSetup(
        resource_type="AzureProductSetup",
        selling_option="ListingOnly",
        call_to_action="free",
        trial_uri="trial_uri_example",
        enable_test_drive=True,
        test_drive_type="test_drive_type_example",
        channel_states=[
            MicrosoftIngestionApiModelsCommonTypeValuePair(
                type="type_example",
                value="value_example",
            ),
        ],
    ) # MicrosoftIngestionApiModelsProductsAzureProductSetup | Request body of a Microsoft.Ingestion.Api.Models.Products.BaseProductSetup (optional)

    # example passing only required values which don't have defaults set
    try:
        # Creates a ProductSetup [AzureProductSetup is allowed]
        api_response = api_instance.products_product_id_setup_post(product_id, authorization)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling ProductClient->products_product_id_setup_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Creates a ProductSetup [AzureProductSetup is allowed]
        api_response = api_instance.products_product_id_setup_post(product_id, authorization, client_request_id=client_request_id, microsoft_ingestion_api_models_products_azure_product_setup=microsoft_ingestion_api_models_products_azure_product_setup)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling ProductClient->products_product_id_setup_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| ID of product |
 **authorization** | **str**| User authorization |
 **client_request_id** | **str**| ID of request provIDed by user | [optional]
 **microsoft_ingestion_api_models_products_azure_product_setup** | [**MicrosoftIngestionApiModelsProductsAzureProductSetup**](MicrosoftIngestionApiModelsProductsAzureProductSetup.md)| Request body of a Microsoft.Ingestion.Api.Models.Products.BaseProductSetup | [optional]

### Return type

[**MicrosoftIngestionApiModelsProductsAzureProductSetup**](MicrosoftIngestionApiModelsProductsAzureProductSetup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Resource not available |  -  |
**405** | Method not allowed |  -  |
**409** | Conflict |  -  |
**429** | Request rate exceeds limit |  -  |
**0** | Unknown error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

