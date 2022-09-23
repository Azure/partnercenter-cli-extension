# partnercenter.PropertyClient

All URIs are relative to *https://api.partner.microsoft.com/v1.0/ingestion*

Method | HTTP request | Description
------------- | ------------- | -------------
[**products_product_id_properties_get**](PropertyClient.md#products_product_id_properties_get) | **GET** /products/{productID}/properties | Returns a paged collection of Property resources for a Product
[**products_product_id_properties_get_by_instance_id_instance_i_dinstance_id_get**](PropertyClient.md#products_product_id_properties_get_by_instance_id_instance_i_dinstance_id_get) | **GET** /products/{productID}/properties/getByInstanceID(instanceID&#x3D;{instanceID}) | Returns a paged collection of Property resources for a Product
[**products_product_id_properties_post**](PropertyClient.md#products_product_id_properties_post) | **POST** /products/{productID}/properties | Create a Property resource for a Product
[**products_product_id_properties_property_id_get**](PropertyClient.md#products_product_id_properties_property_id_get) | **GET** /products/{productID}/properties/{propertyID} | Returns a Property resource for a Product
[**products_product_id_properties_property_id_put**](PropertyClient.md#products_product_id_properties_property_id_put) | **PUT** /products/{productID}/properties/{propertyID} | Update the Property resource for a Product


# **products_product_id_properties_get**
> MicrosoftIngestionApiModelsCommonPagedCollectionMicrosoftIngestionApiModelsPropertiesBaseProperty products_product_id_properties_get(product_id, authorization)

Returns a paged collection of Property resources for a Product

Sample request:                    GET /products/{productID}/properties

### Example


```python
import time
import partnercenter
from ..api import property_client
from ..model.microsoft_ingestion_api_models_common_paged_collection_microsoft_ingestion_api_models_properties_base_property import MicrosoftIngestionApiModelsCommonPagedCollectionMicrosoftIngestionApiModelsPropertiesBaseProperty
from pprint import pprint
# Defining the host is optional and defaults to https://api.partner.microsoft.com/v1.0/ingestion
# See configuration.py for a list of all supported configuration parameters.
configuration = partnercenter.Configuration(
    host = "https://api.partner.microsoft.com/v1.0/ingestion"
)


# Enter a context with an instance of the API client
with partnercenter.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = property_client.PropertyClient(api_client)
    product_id = "productID_example" # str | ID of product
    authorization = "Authorization_example" # str | User authorization
    client_request_id = "Client-Request-ID_example" # str | ID of request provIDed by user (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a paged collection of Property resources for a Product
        api_response = api_instance.products_product_id_properties_get(product_id, authorization)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling PropertyClient->products_product_id_properties_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a paged collection of Property resources for a Product
        api_response = api_instance.products_product_id_properties_get(product_id, authorization, client_request_id=client_request_id)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling PropertyClient->products_product_id_properties_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| ID of product |
 **authorization** | **str**| User authorization |
 **client_request_id** | **str**| ID of request provIDed by user | [optional]

### Return type

[**MicrosoftIngestionApiModelsCommonPagedCollectionMicrosoftIngestionApiModelsPropertiesBaseProperty**](MicrosoftIngestionApiModelsCommonPagedCollectionMicrosoftIngestionApiModelsPropertiesBaseProperty.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a paged collection of Property resources |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Resource not available |  -  |
**405** | Method not allowed |  -  |
**409** | Conflict |  -  |
**429** | Request rate exceeds limit |  -  |
**0** | Unknown error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_product_id_properties_get_by_instance_id_instance_i_dinstance_id_get**
> MicrosoftIngestionApiModelsCommonPagedCollectionMicrosoftIngestionApiModelsPropertiesBaseProperty products_product_id_properties_get_by_instance_id_instance_i_dinstance_id_get(product_id, instance_id, authorization)

Returns a paged collection of Property resources for a Product

Sample request:                   GET /products/{productID}/properties/getByInstanceID(instanceID={instanceID})

### Example


```python
import time
import partnercenter
from ..api import property_client
from ..model.microsoft_ingestion_api_models_common_paged_collection_microsoft_ingestion_api_models_properties_base_property import MicrosoftIngestionApiModelsCommonPagedCollectionMicrosoftIngestionApiModelsPropertiesBaseProperty
from pprint import pprint
# Defining the host is optional and defaults to https://api.partner.microsoft.com/v1.0/ingestion
# See configuration.py for a list of all supported configuration parameters.
configuration = partnercenter.Configuration(
    host = "https://api.partner.microsoft.com/v1.0/ingestion"
)


# Enter a context with an instance of the API client
with partnercenter.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = property_client.PropertyClient(api_client)
    product_id = "productID_example" # str | ID of product
    instance_id = "instanceID_example" # str | Resource instance ID
    authorization = "Authorization_example" # str | User authorization
    client_request_id = "Client-Request-ID_example" # str | ID of request provIDed by user (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a paged collection of Property resources for a Product
        api_response = api_instance.products_product_id_properties_get_by_instance_id_instance_i_dinstance_id_get(product_id, instance_id, authorization)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling PropertyClient->products_product_id_properties_get_by_instance_id_instance_i_dinstance_id_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a paged collection of Property resources for a Product
        api_response = api_instance.products_product_id_properties_get_by_instance_id_instance_i_dinstance_id_get(product_id, instance_id, authorization, client_request_id=client_request_id)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling PropertyClient->products_product_id_properties_get_by_instance_id_instance_i_dinstance_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| ID of product |
 **instance_id** | **str**| Resource instance ID |
 **authorization** | **str**| User authorization |
 **client_request_id** | **str**| ID of request provIDed by user | [optional]

### Return type

[**MicrosoftIngestionApiModelsCommonPagedCollectionMicrosoftIngestionApiModelsPropertiesBaseProperty**](MicrosoftIngestionApiModelsCommonPagedCollectionMicrosoftIngestionApiModelsPropertiesBaseProperty.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A PagedCollection of a certain type of BaseProperty |  * Request-ID - ID of request generated by service <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Resource not available |  -  |
**429** | Request rate exceeds limit |  -  |
**0** | Unknown error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_product_id_properties_post**
> MicrosoftIngestionApiModelsPropertiesAzureProperty products_product_id_properties_post(product_id, authorization)

Create a Property resource for a Product

Sample request:                    POST /products/{productID}/properties [Body Property]

### Example


```python
import time
import partnercenter
from ..api import property_client
from ..model.microsoft_ingestion_api_models_properties_azure_property import MicrosoftIngestionApiModelsPropertiesAzureProperty
from pprint import pprint
# Defining the host is optional and defaults to https://api.partner.microsoft.com/v1.0/ingestion
# See configuration.py for a list of all supported configuration parameters.
configuration = partnercenter.Configuration(
    host = "https://api.partner.microsoft.com/v1.0/ingestion"
)


# Enter a context with an instance of the API client
with partnercenter.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = property_client.PropertyClient(api_client)
    product_id = "productID_example" # str | ID of product
    authorization = "Authorization_example" # str | User authorization
    client_request_id = "Client-Request-ID_example" # str | ID of request provIDed by user (optional)
    microsoft_ingestion_api_models_properties_azure_property = MicrosoftIngestionApiModelsPropertiesAzureProperty(None) # MicrosoftIngestionApiModelsPropertiesAzureProperty | Request body of a Microsoft.Ingestion.Api.Models.Properties.BaseProperty (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a Property resource for a Product
        api_response = api_instance.products_product_id_properties_post(product_id, authorization)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling PropertyClient->products_product_id_properties_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a Property resource for a Product
        api_response = api_instance.products_product_id_properties_post(product_id, authorization, client_request_id=client_request_id, microsoft_ingestion_api_models_properties_azure_property=microsoft_ingestion_api_models_properties_azure_property)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling PropertyClient->products_product_id_properties_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| ID of product |
 **authorization** | **str**| User authorization |
 **client_request_id** | **str**| ID of request provIDed by user | [optional]
 **microsoft_ingestion_api_models_properties_azure_property** | [**MicrosoftIngestionApiModelsPropertiesAzureProperty**](MicrosoftIngestionApiModelsPropertiesAzureProperty.md)| Request body of a Microsoft.Ingestion.Api.Models.Properties.BaseProperty | [optional]

### Return type

[**MicrosoftIngestionApiModelsPropertiesAzureProperty**](MicrosoftIngestionApiModelsPropertiesAzureProperty.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns Property resource |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Resource not available |  -  |
**405** | Method not allowed |  -  |
**409** | Conflict |  -  |
**429** | Request rate exceeds limit |  -  |
**0** | Unknown error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_product_id_properties_property_id_get**
> MicrosoftIngestionApiModelsPropertiesAzureProperty products_product_id_properties_property_id_get(product_id, property_id, authorization)

Returns a Property resource for a Product

Sample request:                    GET /products/{productID}/properties/{propertyID}

### Example


```python
import time
import partnercenter
from ..api import property_client
from ..model.microsoft_ingestion_api_models_properties_azure_property import MicrosoftIngestionApiModelsPropertiesAzureProperty
from pprint import pprint
# Defining the host is optional and defaults to https://api.partner.microsoft.com/v1.0/ingestion
# See configuration.py for a list of all supported configuration parameters.
configuration = partnercenter.Configuration(
    host = "https://api.partner.microsoft.com/v1.0/ingestion"
)


# Enter a context with an instance of the API client
with partnercenter.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = property_client.PropertyClient(api_client)
    product_id = "productID_example" # str | ID of product
    property_id = "propertyID_example" # str | ID of Property
    authorization = "Authorization_example" # str | User authorization
    client_request_id = "Client-Request-ID_example" # str | ID of request provIDed by user (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a Property resource for a Product
        api_response = api_instance.products_product_id_properties_property_id_get(product_id, property_id, authorization)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling PropertyClient->products_product_id_properties_property_id_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a Property resource for a Product
        api_response = api_instance.products_product_id_properties_property_id_get(product_id, property_id, authorization, client_request_id=client_request_id)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling PropertyClient->products_product_id_properties_property_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| ID of product |
 **property_id** | **str**| ID of Property |
 **authorization** | **str**| User authorization |
 **client_request_id** | **str**| ID of request provIDed by user | [optional]

### Return type

[**MicrosoftIngestionApiModelsPropertiesAzureProperty**](MicrosoftIngestionApiModelsPropertiesAzureProperty.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns Property resource |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Resource not available |  -  |
**405** | Method not allowed |  -  |
**409** | Conflict |  -  |
**429** | Request rate exceeds limit |  -  |
**0** | Unknown error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_product_id_properties_property_id_put**
> MicrosoftIngestionApiModelsPropertiesAzureProperty products_product_id_properties_property_id_put(product_id, property_id, authorization)

Update the Property resource for a Product

Sample request:                    PUT /products/{productID}/properties/{propertyID} [Body Property]

### Example


```python
import time
import partnercenter
from ..api import property_client
from ..model.microsoft_ingestion_api_models_properties_azure_property import MicrosoftIngestionApiModelsPropertiesAzureProperty
from pprint import pprint
# Defining the host is optional and defaults to https://api.partner.microsoft.com/v1.0/ingestion
# See configuration.py for a list of all supported configuration parameters.
configuration = partnercenter.Configuration(
    host = "https://api.partner.microsoft.com/v1.0/ingestion"
)


# Enter a context with an instance of the API client
with partnercenter.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = property_client.PropertyClient(api_client)
    product_id = "productID_example" # str | ID of product
    property_id = "propertyID_example" # str | ID of Property
    authorization = "Authorization_example" # str | User authorization
    client_request_id = "Client-Request-ID_example" # str | ID of request provIDed by user (optional)
    microsoft_ingestion_api_models_properties_azure_property = MicrosoftIngestionApiModelsPropertiesAzureProperty(None) # MicrosoftIngestionApiModelsPropertiesAzureProperty | Request body of a Microsoft.Ingestion.Api.Models.Properties.BaseProperty (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update the Property resource for a Product
        api_response = api_instance.products_product_id_properties_property_id_put(product_id, property_id, authorization)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling PropertyClient->products_product_id_properties_property_id_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update the Property resource for a Product
        api_response = api_instance.products_product_id_properties_property_id_put(product_id, property_id, authorization, client_request_id=client_request_id, microsoft_ingestion_api_models_properties_azure_property=microsoft_ingestion_api_models_properties_azure_property)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling PropertyClient->products_product_id_properties_property_id_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| ID of product |
 **property_id** | **str**| ID of Property |
 **authorization** | **str**| User authorization |
 **client_request_id** | **str**| ID of request provIDed by user | [optional]
 **microsoft_ingestion_api_models_properties_azure_property** | [**MicrosoftIngestionApiModelsPropertiesAzureProperty**](MicrosoftIngestionApiModelsPropertiesAzureProperty.md)| Request body of a Microsoft.Ingestion.Api.Models.Properties.BaseProperty | [optional]

### Return type

[**MicrosoftIngestionApiModelsPropertiesAzureProperty**](MicrosoftIngestionApiModelsPropertiesAzureProperty.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns Property resource |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Resource not available |  -  |
**405** | Method not allowed |  -  |
**409** | Conflict |  -  |
**429** | Request rate exceeds limit |  -  |
**0** | Unknown error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

