# partnercenter.LeadConfigurationClient

All URIs are relative to *https://api.partner.microsoft.com/v1.0/ingestion*

Method | HTTP request | Description
------------- | ------------- | -------------
[**products_product_id_leadconfiguration_get**](LeadConfigurationClient.md#products_product_id_leadconfiguration_get) | **GET** /products/{productID}/leadconfiguration | Returns the LeadConfiguration associated with the product
[**products_product_id_leadconfiguration_post**](LeadConfigurationClient.md#products_product_id_leadconfiguration_post) | **POST** /products/{productID}/leadconfiguration | Creates a new LeadConfiguration associated with the product


# **products_product_id_leadconfiguration_get**
> ProductsProductIDLeadconfigurationGet200Response products_product_id_leadconfiguration_get(product_id, authorization)

Returns the LeadConfiguration associated with the product

Sample request:                    GET /products/{productID}/leadconfiguration  

### Example


```python
import time
import partnercenter
from ..api import lead_configuration_client
from ..model.products_product_id_leadconfiguration_get200_response import ProductsProductIDLeadconfigurationGet200Response
from pprint import pprint
# Defining the host is optional and defaults to https://api.partner.microsoft.com/v1.0/ingestion
# See configuration.py for a list of all supported configuration parameters.
configuration = partnercenter.Configuration(
    host = "https://api.partner.microsoft.com/v1.0/ingestion"
)


# Enter a context with an instance of the API client
with partnercenter.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = lead_configuration_client.LeadConfigurationClient(api_client)
    product_id = "productID_example" # str | ID of product
    authorization = "Authorization_example" # str | User authorization
    client_request_id = "Client-Request-ID_example" # str | ID of request provIDed by user (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns the LeadConfiguration associated with the product
        api_response = api_instance.products_product_id_leadconfiguration_get(product_id, authorization)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling LeadConfigurationClient->products_product_id_leadconfiguration_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns the LeadConfiguration associated with the product
        api_response = api_instance.products_product_id_leadconfiguration_get(product_id, authorization, client_request_id=client_request_id)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling LeadConfigurationClient->products_product_id_leadconfiguration_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| ID of product |
 **authorization** | **str**| User authorization |
 **client_request_id** | **str**| ID of request provIDed by user | [optional]

### Return type

[**ProductsProductIDLeadconfigurationGet200Response**](ProductsProductIDLeadconfigurationGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the LeadConfiguration resource associated with the product |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Resource not available |  -  |
**405** | Method not allowed |  -  |
**409** | Conflict |  -  |
**429** | Request rate exceeds limit |  -  |
**0** | Unknown error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_product_id_leadconfiguration_post**
> ProductsProductIDLeadconfigurationGet200Response products_product_id_leadconfiguration_post(product_id, authorization)

Creates a new LeadConfiguration associated with the product

Sample request:                    POST /products/{productID}/leadconfiguration  

### Example


```python
import time
import partnercenter
from ..api import lead_configuration_client
from ..model.products_product_id_leadconfiguration_get200_response import ProductsProductIDLeadconfigurationGet200Response
from pprint import pprint
# Defining the host is optional and defaults to https://api.partner.microsoft.com/v1.0/ingestion
# See configuration.py for a list of all supported configuration parameters.
configuration = partnercenter.Configuration(
    host = "https://api.partner.microsoft.com/v1.0/ingestion"
)


# Enter a context with an instance of the API client
with partnercenter.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = lead_configuration_client.LeadConfigurationClient(api_client)
    product_id = "productID_example" # str | ID of product
    authorization = "Authorization_example" # str | User authorization
    client_request_id = "Client-Request-ID_example" # str | ID of request provIDed by user (optional)
    products_product_id_leadconfiguration_get200_response = ProductsProductIDLeadconfigurationGet200Response(None) # ProductsProductIDLeadconfigurationGet200Response | Request body of a Microsoft.Ingestion.Api.Models.LeadManagement.BaseLeadConfiguration (optional)

    # example passing only required values which don't have defaults set
    try:
        # Creates a new LeadConfiguration associated with the product
        api_response = api_instance.products_product_id_leadconfiguration_post(product_id, authorization)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling LeadConfigurationClient->products_product_id_leadconfiguration_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Creates a new LeadConfiguration associated with the product
        api_response = api_instance.products_product_id_leadconfiguration_post(product_id, authorization, client_request_id=client_request_id, products_product_id_leadconfiguration_get200_response=products_product_id_leadconfiguration_get200_response)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling LeadConfigurationClient->products_product_id_leadconfiguration_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| ID of product |
 **authorization** | **str**| User authorization |
 **client_request_id** | **str**| ID of request provIDed by user | [optional]
 **products_product_id_leadconfiguration_get200_response** | [**ProductsProductIDLeadconfigurationGet200Response**](ProductsProductIDLeadconfigurationGet200Response.md)| Request body of a Microsoft.Ingestion.Api.Models.LeadManagement.BaseLeadConfiguration | [optional]

### Return type

[**ProductsProductIDLeadconfigurationGet200Response**](ProductsProductIDLeadconfigurationGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the newly created LeadConfiguration resource associated with the product |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

