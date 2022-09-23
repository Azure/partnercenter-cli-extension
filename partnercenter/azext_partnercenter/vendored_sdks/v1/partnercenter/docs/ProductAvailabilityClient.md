# partnercenter.ProductAvailabilityClient

All URIs are relative to *https://api.partner.microsoft.com/v1.0/ingestion*

Method | HTTP request | Description
------------- | ------------- | -------------
[**products_product_id_product_availabilities_get_by_instance_id_instance_i_dinstance_id_get**](ProductAvailabilityClient.md#products_product_id_product_availabilities_get_by_instance_id_instance_i_dinstance_id_get) | **GET** /products/{productID}/productAvailabilities/getByInstanceID(instanceID&#x3D;{instanceID}) | Returns a paged collection of ProductAvailability resource for Product
[**products_product_id_productavailabilities_get**](ProductAvailabilityClient.md#products_product_id_productavailabilities_get) | **GET** /products/{productID}/productavailabilities | Returns a paged collection of ProductAvailability resource for Product
[**products_product_id_productavailabilities_post**](ProductAvailabilityClient.md#products_product_id_productavailabilities_post) | **POST** /products/{productID}/productavailabilities | Create ProductAvailability resource for Product
[**products_product_id_productavailabilities_product_availability_id_get**](ProductAvailabilityClient.md#products_product_id_productavailabilities_product_availability_id_get) | **GET** /products/{productID}/productavailabilities/{productAvailabilityID} | Returns ProductAvailability resource for Product
[**products_product_id_productavailabilities_product_availability_id_put**](ProductAvailabilityClient.md#products_product_id_productavailabilities_product_availability_id_put) | **PUT** /products/{productID}/productavailabilities/{productAvailabilityID} | Update ProductAvailability resource for Product


# **products_product_id_product_availabilities_get_by_instance_id_instance_i_dinstance_id_get**
> MicrosoftIngestionApiModelsCommonPagedCollectionMicrosoftIngestionApiModelsAvailabilitiesProductAvailability products_product_id_product_availabilities_get_by_instance_id_instance_i_dinstance_id_get(product_id, instance_id, authorization)

Returns a paged collection of ProductAvailability resource for Product

Sample request:                   GET /products/{productID}/productAvailabilities/getByInstanceID(instanceID={instanceID})

### Example


```python
import time
import partnercenter
from ..api import product_availability_client
from ..model.microsoft_ingestion_api_models_common_paged_collection_microsoft_ingestion_api_models_availabilities_product_availability import MicrosoftIngestionApiModelsCommonPagedCollectionMicrosoftIngestionApiModelsAvailabilitiesProductAvailability
from pprint import pprint
# Defining the host is optional and defaults to https://api.partner.microsoft.com/v1.0/ingestion
# See configuration.py for a list of all supported configuration parameters.
configuration = partnercenter.Configuration(
    host = "https://api.partner.microsoft.com/v1.0/ingestion"
)


# Enter a context with an instance of the API client
with partnercenter.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = product_availability_client.ProductAvailabilityClient(api_client)
    product_id = "productID_example" # str | ID of product
    instance_id = "instanceID_example" # str | Resource instance ID
    authorization = "Authorization_example" # str | User authorization
    client_request_id = "Client-Request-ID_example" # str | ID of request provIDed by user (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a paged collection of ProductAvailability resource for Product
        api_response = api_instance.products_product_id_product_availabilities_get_by_instance_id_instance_i_dinstance_id_get(product_id, instance_id, authorization)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling ProductAvailabilityClient->products_product_id_product_availabilities_get_by_instance_id_instance_i_dinstance_id_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a paged collection of ProductAvailability resource for Product
        api_response = api_instance.products_product_id_product_availabilities_get_by_instance_id_instance_i_dinstance_id_get(product_id, instance_id, authorization, client_request_id=client_request_id)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling ProductAvailabilityClient->products_product_id_product_availabilities_get_by_instance_id_instance_i_dinstance_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| ID of product |
 **instance_id** | **str**| Resource instance ID |
 **authorization** | **str**| User authorization |
 **client_request_id** | **str**| ID of request provIDed by user | [optional]

### Return type

[**MicrosoftIngestionApiModelsCommonPagedCollectionMicrosoftIngestionApiModelsAvailabilitiesProductAvailability**](MicrosoftIngestionApiModelsCommonPagedCollectionMicrosoftIngestionApiModelsAvailabilitiesProductAvailability.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A PagedCollection of ProductAvailability |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Resource not available |  -  |
**429** | Request rate exceeds limit |  -  |
**0** | Unknown error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_product_id_productavailabilities_get**
> MicrosoftIngestionApiModelsCommonPagedCollectionMicrosoftIngestionApiModelsAvailabilitiesProductAvailability products_product_id_productavailabilities_get(product_id, authorization)

Returns a paged collection of ProductAvailability resource for Product

Sample request:                    GET /products/{productID}/productAvailabilities

### Example


```python
import time
import partnercenter
from ..api import product_availability_client
from ..model.microsoft_ingestion_api_models_common_paged_collection_microsoft_ingestion_api_models_availabilities_product_availability import MicrosoftIngestionApiModelsCommonPagedCollectionMicrosoftIngestionApiModelsAvailabilitiesProductAvailability
from pprint import pprint
# Defining the host is optional and defaults to https://api.partner.microsoft.com/v1.0/ingestion
# See configuration.py for a list of all supported configuration parameters.
configuration = partnercenter.Configuration(
    host = "https://api.partner.microsoft.com/v1.0/ingestion"
)


# Enter a context with an instance of the API client
with partnercenter.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = product_availability_client.ProductAvailabilityClient(api_client)
    product_id = "productID_example" # str | ID of product
    authorization = "Authorization_example" # str | User authorization
    client_request_id = "Client-Request-ID_example" # str | ID of request provIDed by user (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a paged collection of ProductAvailability resource for Product
        api_response = api_instance.products_product_id_productavailabilities_get(product_id, authorization)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling ProductAvailabilityClient->products_product_id_productavailabilities_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a paged collection of ProductAvailability resource for Product
        api_response = api_instance.products_product_id_productavailabilities_get(product_id, authorization, client_request_id=client_request_id)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling ProductAvailabilityClient->products_product_id_productavailabilities_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| ID of product |
 **authorization** | **str**| User authorization |
 **client_request_id** | **str**| ID of request provIDed by user | [optional]

### Return type

[**MicrosoftIngestionApiModelsCommonPagedCollectionMicrosoftIngestionApiModelsAvailabilitiesProductAvailability**](MicrosoftIngestionApiModelsCommonPagedCollectionMicrosoftIngestionApiModelsAvailabilitiesProductAvailability.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a paged collection of ProductAvailability resource |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Resource not available |  -  |
**405** | Method not allowed |  -  |
**409** | Conflict |  -  |
**429** | Request rate exceeds limit |  -  |
**0** | Unknown error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_product_id_productavailabilities_post**
> MicrosoftIngestionApiModelsAvailabilitiesProductAvailability products_product_id_productavailabilities_post(product_id, authorization)

Create ProductAvailability resource for Product

Sample request:                    POST /products/{productID}/productAvailabilities

### Example


```python
import time
import partnercenter
from ..api import product_availability_client
from ..model.microsoft_ingestion_api_models_availabilities_product_availability import MicrosoftIngestionApiModelsAvailabilitiesProductAvailability
from pprint import pprint
# Defining the host is optional and defaults to https://api.partner.microsoft.com/v1.0/ingestion
# See configuration.py for a list of all supported configuration parameters.
configuration = partnercenter.Configuration(
    host = "https://api.partner.microsoft.com/v1.0/ingestion"
)


# Enter a context with an instance of the API client
with partnercenter.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = product_availability_client.ProductAvailabilityClient(api_client)
    product_id = "productID_example" # str | ID of product
    authorization = "Authorization_example" # str | User authorization
    client_request_id = "Client-Request-ID_example" # str | ID of request provIDed by user (optional)
    microsoft_ingestion_api_models_availabilities_product_availability = MicrosoftIngestionApiModelsAvailabilitiesProductAvailability(None) # MicrosoftIngestionApiModelsAvailabilitiesProductAvailability | Request body of a Microsoft.Ingestion.Api.Models.Availabilities.ProductAvailability (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create ProductAvailability resource for Product
        api_response = api_instance.products_product_id_productavailabilities_post(product_id, authorization)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling ProductAvailabilityClient->products_product_id_productavailabilities_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create ProductAvailability resource for Product
        api_response = api_instance.products_product_id_productavailabilities_post(product_id, authorization, client_request_id=client_request_id, microsoft_ingestion_api_models_availabilities_product_availability=microsoft_ingestion_api_models_availabilities_product_availability)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling ProductAvailabilityClient->products_product_id_productavailabilities_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| ID of product |
 **authorization** | **str**| User authorization |
 **client_request_id** | **str**| ID of request provIDed by user | [optional]
 **microsoft_ingestion_api_models_availabilities_product_availability** | [**MicrosoftIngestionApiModelsAvailabilitiesProductAvailability**](MicrosoftIngestionApiModelsAvailabilitiesProductAvailability.md)| Request body of a Microsoft.Ingestion.Api.Models.Availabilities.ProductAvailability | [optional]

### Return type

[**MicrosoftIngestionApiModelsAvailabilitiesProductAvailability**](MicrosoftIngestionApiModelsAvailabilitiesProductAvailability.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Returns ProductAvailability resource |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Resource not available |  -  |
**405** | Method not allowed |  -  |
**409** | Conflict |  -  |
**429** | Request rate exceeds limit |  -  |
**0** | Unknown error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_product_id_productavailabilities_product_availability_id_get**
> MicrosoftIngestionApiModelsAvailabilitiesProductAvailability products_product_id_productavailabilities_product_availability_id_get(product_id, product_availability_id, authorization)

Returns ProductAvailability resource for Product

Sample request:                    GET /products/{productID}/productAvailabilities/{productAvailabilityID}

### Example


```python
import time
import partnercenter
from ..api import product_availability_client
from ..model.microsoft_ingestion_api_models_availabilities_product_availability import MicrosoftIngestionApiModelsAvailabilitiesProductAvailability
from pprint import pprint
# Defining the host is optional and defaults to https://api.partner.microsoft.com/v1.0/ingestion
# See configuration.py for a list of all supported configuration parameters.
configuration = partnercenter.Configuration(
    host = "https://api.partner.microsoft.com/v1.0/ingestion"
)


# Enter a context with an instance of the API client
with partnercenter.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = product_availability_client.ProductAvailabilityClient(api_client)
    product_id = "productID_example" # str | ID of product
    product_availability_id = "productAvailabilityID_example" # str | ID of ProductAvailability
    authorization = "Authorization_example" # str | User authorization
    client_request_id = "Client-Request-ID_example" # str | ID of request provIDed by user (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns ProductAvailability resource for Product
        api_response = api_instance.products_product_id_productavailabilities_product_availability_id_get(product_id, product_availability_id, authorization)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling ProductAvailabilityClient->products_product_id_productavailabilities_product_availability_id_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns ProductAvailability resource for Product
        api_response = api_instance.products_product_id_productavailabilities_product_availability_id_get(product_id, product_availability_id, authorization, client_request_id=client_request_id)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling ProductAvailabilityClient->products_product_id_productavailabilities_product_availability_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| ID of product |
 **product_availability_id** | **str**| ID of ProductAvailability |
 **authorization** | **str**| User authorization |
 **client_request_id** | **str**| ID of request provIDed by user | [optional]

### Return type

[**MicrosoftIngestionApiModelsAvailabilitiesProductAvailability**](MicrosoftIngestionApiModelsAvailabilitiesProductAvailability.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns ProductAvailability resource |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Resource not available |  -  |
**405** | Method not allowed |  -  |
**409** | Conflict |  -  |
**429** | Request rate exceeds limit |  -  |
**0** | Unknown error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_product_id_productavailabilities_product_availability_id_put**
> MicrosoftIngestionApiModelsAvailabilitiesProductAvailability products_product_id_productavailabilities_product_availability_id_put(product_id, product_availability_id, authorization)

Update ProductAvailability resource for Product

Sample request:                    PUT /products/{productID}/productAvailabilities/{productAvailabilityID}

### Example


```python
import time
import partnercenter
from ..api import product_availability_client
from ..model.microsoft_ingestion_api_models_availabilities_product_availability import MicrosoftIngestionApiModelsAvailabilitiesProductAvailability
from pprint import pprint
# Defining the host is optional and defaults to https://api.partner.microsoft.com/v1.0/ingestion
# See configuration.py for a list of all supported configuration parameters.
configuration = partnercenter.Configuration(
    host = "https://api.partner.microsoft.com/v1.0/ingestion"
)


# Enter a context with an instance of the API client
with partnercenter.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = product_availability_client.ProductAvailabilityClient(api_client)
    product_id = "productID_example" # str | ID of product
    product_availability_id = "productAvailabilityID_example" # str | ID of ProductAvailability
    authorization = "Authorization_example" # str | User authorization
    client_request_id = "Client-Request-ID_example" # str | ID of request provIDed by user (optional)
    microsoft_ingestion_api_models_availabilities_product_availability = MicrosoftIngestionApiModelsAvailabilitiesProductAvailability(None) # MicrosoftIngestionApiModelsAvailabilitiesProductAvailability | Request body of a Microsoft.Ingestion.Api.Models.Availabilities.ProductAvailability (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update ProductAvailability resource for Product
        api_response = api_instance.products_product_id_productavailabilities_product_availability_id_put(product_id, product_availability_id, authorization)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling ProductAvailabilityClient->products_product_id_productavailabilities_product_availability_id_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update ProductAvailability resource for Product
        api_response = api_instance.products_product_id_productavailabilities_product_availability_id_put(product_id, product_availability_id, authorization, client_request_id=client_request_id, microsoft_ingestion_api_models_availabilities_product_availability=microsoft_ingestion_api_models_availabilities_product_availability)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling ProductAvailabilityClient->products_product_id_productavailabilities_product_availability_id_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| ID of product |
 **product_availability_id** | **str**| ID of ProductAvailability |
 **authorization** | **str**| User authorization |
 **client_request_id** | **str**| ID of request provIDed by user | [optional]
 **microsoft_ingestion_api_models_availabilities_product_availability** | [**MicrosoftIngestionApiModelsAvailabilitiesProductAvailability**](MicrosoftIngestionApiModelsAvailabilitiesProductAvailability.md)| Request body of a Microsoft.Ingestion.Api.Models.Availabilities.ProductAvailability | [optional]

### Return type

[**MicrosoftIngestionApiModelsAvailabilitiesProductAvailability**](MicrosoftIngestionApiModelsAvailabilitiesProductAvailability.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns ProductAvailability resource |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Resource not available |  -  |
**405** | Method not allowed |  -  |
**409** | Conflict |  -  |
**429** | Request rate exceeds limit |  -  |
**0** | Unknown error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

