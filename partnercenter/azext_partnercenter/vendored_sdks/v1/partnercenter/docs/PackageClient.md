# partnercenter.PackageClient

All URIs are relative to *https://api.partner.microsoft.com/v1.0/ingestion*

Method | HTTP request | Description
------------- | ------------- | -------------
[**products_product_id_packages_get**](PackageClient.md#products_product_id_packages_get) | **GET** /products/{productID}/packages | Returns a set of package instances for the product.
[**products_product_id_packages_package_id_delete**](PackageClient.md#products_product_id_packages_package_id_delete) | **DELETE** /products/{productID}/packages/{packageID} | Delete the package.
[**products_product_id_packages_package_id_get**](PackageClient.md#products_product_id_packages_package_id_get) | **GET** /products/{productID}/packages/{packageID} | Returns a package instance for the product.
[**products_product_id_packages_package_id_put**](PackageClient.md#products_product_id_packages_package_id_put) | **PUT** /products/{productID}/packages/{packageID} | Update the package.
[**products_product_id_packages_post**](PackageClient.md#products_product_id_packages_post) | **POST** /products/{productID}/packages | Create a package resource.


# **products_product_id_packages_get**
> MicrosoftIngestionApiModelsCommonPagedCollectionMicrosoftIngestionApiModelsPackagesBasePackage products_product_id_packages_get(product_id, authorization)

Returns a set of package instances for the product.

Returns a set of package instances for the product.

### Example


```python
import time
import partnercenter
from ..api import package_client
from ..model.microsoft_ingestion_api_models_common_paged_collection_microsoft_ingestion_api_models_packages_base_package import MicrosoftIngestionApiModelsCommonPagedCollectionMicrosoftIngestionApiModelsPackagesBasePackage
from pprint import pprint
# Defining the host is optional and defaults to https://api.partner.microsoft.com/v1.0/ingestion
# See configuration.py for a list of all supported configuration parameters.
configuration = partnercenter.Configuration(
    host = "https://api.partner.microsoft.com/v1.0/ingestion"
)


# Enter a context with an instance of the API client
with partnercenter.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = package_client.PackageClient(api_client)
    product_id = "productID_example" # str | ID of product
    authorization = "Authorization_example" # str | User authorization
    client_request_id = "Client-Request-ID_example" # str | ID of request provIDed by user (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a set of package instances for the product.
        api_response = api_instance.products_product_id_packages_get(product_id, authorization)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling PackageClient->products_product_id_packages_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a set of package instances for the product.
        api_response = api_instance.products_product_id_packages_get(product_id, authorization, client_request_id=client_request_id)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling PackageClient->products_product_id_packages_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| ID of product |
 **authorization** | **str**| User authorization |
 **client_request_id** | **str**| ID of request provIDed by user | [optional]

### Return type

[**MicrosoftIngestionApiModelsCommonPagedCollectionMicrosoftIngestionApiModelsPackagesBasePackage**](MicrosoftIngestionApiModelsCommonPagedCollectionMicrosoftIngestionApiModelsPackagesBasePackage.md)

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

# **products_product_id_packages_package_id_delete**
> str products_product_id_packages_package_id_delete(product_id, package_id, authorization)

Delete the package.

Delete the package.

### Example


```python
import time
import partnercenter
from ..api import package_client
from pprint import pprint
# Defining the host is optional and defaults to https://api.partner.microsoft.com/v1.0/ingestion
# See configuration.py for a list of all supported configuration parameters.
configuration = partnercenter.Configuration(
    host = "https://api.partner.microsoft.com/v1.0/ingestion"
)


# Enter a context with an instance of the API client
with partnercenter.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = package_client.PackageClient(api_client)
    product_id = "productID_example" # str | ID of product
    package_id = "packageID_example" # str | the ID of package
    authorization = "Authorization_example" # str | User authorization
    client_request_id = "Client-Request-ID_example" # str | ID of request provIDed by user (optional)

    # example passing only required values which don't have defaults set
    try:
        # Delete the package.
        api_response = api_instance.products_product_id_packages_package_id_delete(product_id, package_id, authorization)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling PackageClient->products_product_id_packages_package_id_delete: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete the package.
        api_response = api_instance.products_product_id_packages_package_id_delete(product_id, package_id, authorization, client_request_id=client_request_id)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling PackageClient->products_product_id_packages_package_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| ID of product |
 **package_id** | **str**| the ID of package |
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

# **products_product_id_packages_package_id_get**
> MicrosoftIngestionApiModelsPackagesAzurePackage products_product_id_packages_package_id_get(product_id, package_id, authorization)

Returns a package instance for the product.

Returns a package instance for the product.

### Example


```python
import time
import partnercenter
from ..api import package_client
from ..model.microsoft_ingestion_api_models_packages_azure_package import MicrosoftIngestionApiModelsPackagesAzurePackage
from pprint import pprint
# Defining the host is optional and defaults to https://api.partner.microsoft.com/v1.0/ingestion
# See configuration.py for a list of all supported configuration parameters.
configuration = partnercenter.Configuration(
    host = "https://api.partner.microsoft.com/v1.0/ingestion"
)


# Enter a context with an instance of the API client
with partnercenter.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = package_client.PackageClient(api_client)
    product_id = "productID_example" # str | ID of product
    package_id = "packageID_example" # str | 
    authorization = "Authorization_example" # str | User authorization
    client_request_id = "Client-Request-ID_example" # str | ID of request provIDed by user (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a package instance for the product.
        api_response = api_instance.products_product_id_packages_package_id_get(product_id, package_id, authorization)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling PackageClient->products_product_id_packages_package_id_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a package instance for the product.
        api_response = api_instance.products_product_id_packages_package_id_get(product_id, package_id, authorization, client_request_id=client_request_id)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling PackageClient->products_product_id_packages_package_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| ID of product |
 **package_id** | **str**|  |
 **authorization** | **str**| User authorization |
 **client_request_id** | **str**| ID of request provIDed by user | [optional]

### Return type

[**MicrosoftIngestionApiModelsPackagesAzurePackage**](MicrosoftIngestionApiModelsPackagesAzurePackage.md)

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

# **products_product_id_packages_package_id_put**
> MicrosoftIngestionApiModelsPackagesAzurePackage products_product_id_packages_package_id_put(product_id, package_id, authorization)

Update the package.

Update the package.

### Example


```python
import time
import partnercenter
from ..api import package_client
from ..model.microsoft_ingestion_api_models_packages_azure_package import MicrosoftIngestionApiModelsPackagesAzurePackage
from pprint import pprint
# Defining the host is optional and defaults to https://api.partner.microsoft.com/v1.0/ingestion
# See configuration.py for a list of all supported configuration parameters.
configuration = partnercenter.Configuration(
    host = "https://api.partner.microsoft.com/v1.0/ingestion"
)


# Enter a context with an instance of the API client
with partnercenter.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = package_client.PackageClient(api_client)
    product_id = "productID_example" # str | ID of product
    package_id = "packageID_example" # str | The ID of package
    authorization = "Authorization_example" # str | User authorization
    client_request_id = "Client-Request-ID_example" # str | ID of request provIDed by user (optional)
    microsoft_ingestion_api_models_packages_azure_package = MicrosoftIngestionApiModelsPackagesAzurePackage(None) # MicrosoftIngestionApiModelsPackagesAzurePackage | Request body of a Microsoft.Ingestion.Api.Models.Packages.BasePackage (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update the package.
        api_response = api_instance.products_product_id_packages_package_id_put(product_id, package_id, authorization)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling PackageClient->products_product_id_packages_package_id_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update the package.
        api_response = api_instance.products_product_id_packages_package_id_put(product_id, package_id, authorization, client_request_id=client_request_id, microsoft_ingestion_api_models_packages_azure_package=microsoft_ingestion_api_models_packages_azure_package)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling PackageClient->products_product_id_packages_package_id_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| ID of product |
 **package_id** | **str**| The ID of package |
 **authorization** | **str**| User authorization |
 **client_request_id** | **str**| ID of request provIDed by user | [optional]
 **microsoft_ingestion_api_models_packages_azure_package** | [**MicrosoftIngestionApiModelsPackagesAzurePackage**](MicrosoftIngestionApiModelsPackagesAzurePackage.md)| Request body of a Microsoft.Ingestion.Api.Models.Packages.BasePackage | [optional]

### Return type

[**MicrosoftIngestionApiModelsPackagesAzurePackage**](MicrosoftIngestionApiModelsPackagesAzurePackage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
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

# **products_product_id_packages_post**
> MicrosoftIngestionApiModelsPackagesAzurePackage products_product_id_packages_post(product_id, authorization)

Create a package resource.

Sample request:                    POST products/{productID}/packages      {          \"resourceType\": \"package\",          \"fileName\": \"sample.appx\"      }

### Example


```python
import time
import partnercenter
from ..api import package_client
from ..model.microsoft_ingestion_api_models_packages_azure_package import MicrosoftIngestionApiModelsPackagesAzurePackage
from pprint import pprint
# Defining the host is optional and defaults to https://api.partner.microsoft.com/v1.0/ingestion
# See configuration.py for a list of all supported configuration parameters.
configuration = partnercenter.Configuration(
    host = "https://api.partner.microsoft.com/v1.0/ingestion"
)


# Enter a context with an instance of the API client
with partnercenter.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = package_client.PackageClient(api_client)
    product_id = "productID_example" # str | ID of product
    authorization = "Authorization_example" # str | User authorization
    client_request_id = "Client-Request-ID_example" # str | ID of request provIDed by user (optional)
    microsoft_ingestion_api_models_packages_azure_package = MicrosoftIngestionApiModelsPackagesAzurePackage(None) # MicrosoftIngestionApiModelsPackagesAzurePackage | Request body of a Microsoft.Ingestion.Api.Models.Packages.BasePackage (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a package resource.
        api_response = api_instance.products_product_id_packages_post(product_id, authorization)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling PackageClient->products_product_id_packages_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a package resource.
        api_response = api_instance.products_product_id_packages_post(product_id, authorization, client_request_id=client_request_id, microsoft_ingestion_api_models_packages_azure_package=microsoft_ingestion_api_models_packages_azure_package)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling PackageClient->products_product_id_packages_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| ID of product |
 **authorization** | **str**| User authorization |
 **client_request_id** | **str**| ID of request provIDed by user | [optional]
 **microsoft_ingestion_api_models_packages_azure_package** | [**MicrosoftIngestionApiModelsPackagesAzurePackage**](MicrosoftIngestionApiModelsPackagesAzurePackage.md)| Request body of a Microsoft.Ingestion.Api.Models.Packages.BasePackage | [optional]

### Return type

[**MicrosoftIngestionApiModelsPackagesAzurePackage**](MicrosoftIngestionApiModelsPackagesAzurePackage.md)

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

