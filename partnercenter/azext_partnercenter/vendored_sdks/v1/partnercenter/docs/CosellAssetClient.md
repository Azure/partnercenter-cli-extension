# partnercenter.CosellAssetClient

All URIs are relative to *https://api.partner.microsoft.com/v1.0/ingestion*

Method | HTTP request | Description
------------- | ------------- | -------------
[**products_product_id_cosell_assets_cosell_asset_id_delete**](CosellAssetClient.md#products_product_id_cosell_assets_cosell_asset_id_delete) | **DELETE** /products/{productID}/cosellAssets/{cosellAssetID} | Deletes a CosellAsset
[**products_product_id_cosell_assets_cosell_asset_id_get**](CosellAssetClient.md#products_product_id_cosell_assets_cosell_asset_id_get) | **GET** /products/{productID}/cosellAssets/{cosellAssetID} | Returns a CosellAsset
[**products_product_id_cosell_assets_cosell_asset_id_put**](CosellAssetClient.md#products_product_id_cosell_assets_cosell_asset_id_put) | **PUT** /products/{productID}/cosellAssets/{cosellAssetID} | Updates a CosellAsset
[**products_product_id_cosell_assets_get**](CosellAssetClient.md#products_product_id_cosell_assets_get) | **GET** /products/{productID}/cosellAssets | Returns a paged collection of CosellAsset resources for product
[**products_product_id_cosell_assets_get_by_instance_id_instance_i_dinstance_id_get**](CosellAssetClient.md#products_product_id_cosell_assets_get_by_instance_id_instance_i_dinstance_id_get) | **GET** /products/{productID}/cosellAssets/getByInstanceID(instanceID&#x3D;{instanceID}) | Returns a paged collection of CosellAsset resources for given CosellListing instanceID
[**products_product_id_cosell_assets_post**](CosellAssetClient.md#products_product_id_cosell_assets_post) | **POST** /products/{productID}/cosellAssets | Create a CosellAsset


# **products_product_id_cosell_assets_cosell_asset_id_delete**
> products_product_id_cosell_assets_cosell_asset_id_delete(product_id, cosell_asset_id)

Deletes a CosellAsset

Deletes a CosellAsset

### Example


```python
import time
import partnercenter
from ..api import cosell_asset_client
from pprint import pprint
# Defining the host is optional and defaults to https://api.partner.microsoft.com/v1.0/ingestion
# See configuration.py for a list of all supported configuration parameters.
configuration = partnercenter.Configuration(
    host = "https://api.partner.microsoft.com/v1.0/ingestion"
)


# Enter a context with an instance of the API client
with partnercenter.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = cosell_asset_client.CosellAssetClient(api_client)
    product_id = "productID_example" # str | ID of product
    cosell_asset_id = "cosellAssetID_example" # str | ID of Cosellasset

    # example passing only required values which don't have defaults set
    try:
        # Deletes a CosellAsset
        api_instance.products_product_id_cosell_assets_cosell_asset_id_delete(product_id, cosell_asset_id)
    except partnercenter.ApiException as e:
        print("Exception when calling CosellAssetClient->products_product_id_cosell_assets_cosell_asset_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| ID of product |
 **cosell_asset_id** | **str**| ID of Cosellasset |

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

# **products_product_id_cosell_assets_cosell_asset_id_get**
> MicrosoftIngestionApiModelsCosellCosellAsset products_product_id_cosell_assets_cosell_asset_id_get(product_id, cosell_asset_id)

Returns a CosellAsset

Returns a CosellAsset

### Example


```python
import time
import partnercenter
from ..api import cosell_asset_client
from ..model.microsoft_ingestion_api_models_cosell_cosell_asset import MicrosoftIngestionApiModelsCosellCosellAsset
from pprint import pprint
# Defining the host is optional and defaults to https://api.partner.microsoft.com/v1.0/ingestion
# See configuration.py for a list of all supported configuration parameters.
configuration = partnercenter.Configuration(
    host = "https://api.partner.microsoft.com/v1.0/ingestion"
)


# Enter a context with an instance of the API client
with partnercenter.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = cosell_asset_client.CosellAssetClient(api_client)
    product_id = "productID_example" # str | ID of product
    cosell_asset_id = "cosellAssetID_example" # str | ID of Cosellasset

    # example passing only required values which don't have defaults set
    try:
        # Returns a CosellAsset
        api_response = api_instance.products_product_id_cosell_assets_cosell_asset_id_get(product_id, cosell_asset_id)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling CosellAssetClient->products_product_id_cosell_assets_cosell_asset_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| ID of product |
 **cosell_asset_id** | **str**| ID of Cosellasset |

### Return type

[**MicrosoftIngestionApiModelsCosellCosellAsset**](MicrosoftIngestionApiModelsCosellCosellAsset.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a paged collection of CosellAsset resource |  * Request-ID - ID of request generated by service <br>  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Resource not available |  -  |
**405** | Method not allowed |  -  |
**409** | Conflict |  -  |
**429** | Request rate exceeds limit |  -  |
**0** | Unknown error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_product_id_cosell_assets_cosell_asset_id_put**
> MicrosoftIngestionApiModelsCosellCosellAsset products_product_id_cosell_assets_cosell_asset_id_put(product_id, cosell_asset_id)

Updates a CosellAsset

Updates a CosellAsset

### Example


```python
import time
import partnercenter
from ..api import cosell_asset_client
from ..model.microsoft_ingestion_api_models_cosell_cosell_asset import MicrosoftIngestionApiModelsCosellCosellAsset
from pprint import pprint
# Defining the host is optional and defaults to https://api.partner.microsoft.com/v1.0/ingestion
# See configuration.py for a list of all supported configuration parameters.
configuration = partnercenter.Configuration(
    host = "https://api.partner.microsoft.com/v1.0/ingestion"
)


# Enter a context with an instance of the API client
with partnercenter.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = cosell_asset_client.CosellAssetClient(api_client)
    product_id = "productID_example" # str | ID of product
    cosell_asset_id = "cosellAssetID_example" # str | ID of Cosellasset
    microsoft_ingestion_api_models_cosell_cosell_asset = MicrosoftIngestionApiModelsCosellCosellAsset(None) # MicrosoftIngestionApiModelsCosellCosellAsset | Request body of a CosellAsset (optional)

    # example passing only required values which don't have defaults set
    try:
        # Updates a CosellAsset
        api_response = api_instance.products_product_id_cosell_assets_cosell_asset_id_put(product_id, cosell_asset_id)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling CosellAssetClient->products_product_id_cosell_assets_cosell_asset_id_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Updates a CosellAsset
        api_response = api_instance.products_product_id_cosell_assets_cosell_asset_id_put(product_id, cosell_asset_id, microsoft_ingestion_api_models_cosell_cosell_asset=microsoft_ingestion_api_models_cosell_cosell_asset)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling CosellAssetClient->products_product_id_cosell_assets_cosell_asset_id_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| ID of product |
 **cosell_asset_id** | **str**| ID of Cosellasset |
 **microsoft_ingestion_api_models_cosell_cosell_asset** | [**MicrosoftIngestionApiModelsCosellCosellAsset**](MicrosoftIngestionApiModelsCosellCosellAsset.md)| Request body of a CosellAsset | [optional]

### Return type

[**MicrosoftIngestionApiModelsCosellCosellAsset**](MicrosoftIngestionApiModelsCosellCosellAsset.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns an updated CosellAsset resource |  * Request-ID - ID of request generated by service <br>  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Resource not available |  -  |
**405** | Method not allowed |  -  |
**409** | Conflict |  -  |
**429** | Request rate exceeds limit |  -  |
**0** | Unknown error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_product_id_cosell_assets_get**
> MicrosoftIngestionApiModelsCommonPagedCollectionMicrosoftIngestionApiModelsCosellCosellAsset products_product_id_cosell_assets_get(product_id)

Returns a paged collection of CosellAsset resources for product

Returns a paged collection of CosellAsset resources for product

### Example


```python
import time
import partnercenter
from ..api import cosell_asset_client
from ..model.microsoft_ingestion_api_models_common_paged_collection_microsoft_ingestion_api_models_cosell_cosell_asset import MicrosoftIngestionApiModelsCommonPagedCollectionMicrosoftIngestionApiModelsCosellCosellAsset
from pprint import pprint
# Defining the host is optional and defaults to https://api.partner.microsoft.com/v1.0/ingestion
# See configuration.py for a list of all supported configuration parameters.
configuration = partnercenter.Configuration(
    host = "https://api.partner.microsoft.com/v1.0/ingestion"
)


# Enter a context with an instance of the API client
with partnercenter.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = cosell_asset_client.CosellAssetClient(api_client)
    product_id = "productID_example" # str | ID of product

    # example passing only required values which don't have defaults set
    try:
        # Returns a paged collection of CosellAsset resources for product
        api_response = api_instance.products_product_id_cosell_assets_get(product_id)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling CosellAssetClient->products_product_id_cosell_assets_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| ID of product |

### Return type

[**MicrosoftIngestionApiModelsCommonPagedCollectionMicrosoftIngestionApiModelsCosellCosellAsset**](MicrosoftIngestionApiModelsCommonPagedCollectionMicrosoftIngestionApiModelsCosellCosellAsset.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a paged collection of CosellAsset resource |  * Request-ID - ID of request generated by service <br>  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Resource not available |  -  |
**405** | Method not allowed |  -  |
**409** | Conflict |  -  |
**429** | Request rate exceeds limit |  -  |
**0** | Unknown error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_product_id_cosell_assets_get_by_instance_id_instance_i_dinstance_id_get**
> MicrosoftIngestionApiModelsCommonPagedCollectionMicrosoftIngestionApiModelsCosellCosellAsset products_product_id_cosell_assets_get_by_instance_id_instance_i_dinstance_id_get(product_id, instance_id)

Returns a paged collection of CosellAsset resources for given CosellListing instanceID

Returns a paged collection of CosellAsset resources for given CosellListing instanceID

### Example


```python
import time
import partnercenter
from ..api import cosell_asset_client
from ..model.microsoft_ingestion_api_models_common_paged_collection_microsoft_ingestion_api_models_cosell_cosell_asset import MicrosoftIngestionApiModelsCommonPagedCollectionMicrosoftIngestionApiModelsCosellCosellAsset
from pprint import pprint
# Defining the host is optional and defaults to https://api.partner.microsoft.com/v1.0/ingestion
# See configuration.py for a list of all supported configuration parameters.
configuration = partnercenter.Configuration(
    host = "https://api.partner.microsoft.com/v1.0/ingestion"
)


# Enter a context with an instance of the API client
with partnercenter.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = cosell_asset_client.CosellAssetClient(api_client)
    product_id = "productID_example" # str | ID of product
    instance_id = "instanceID_example" # str | Instance ID

    # example passing only required values which don't have defaults set
    try:
        # Returns a paged collection of CosellAsset resources for given CosellListing instanceID
        api_response = api_instance.products_product_id_cosell_assets_get_by_instance_id_instance_i_dinstance_id_get(product_id, instance_id)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling CosellAssetClient->products_product_id_cosell_assets_get_by_instance_id_instance_i_dinstance_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| ID of product |
 **instance_id** | **str**| Instance ID |

### Return type

[**MicrosoftIngestionApiModelsCommonPagedCollectionMicrosoftIngestionApiModelsCosellCosellAsset**](MicrosoftIngestionApiModelsCommonPagedCollectionMicrosoftIngestionApiModelsCosellCosellAsset.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a paged collection of CosellAsset resource |  * Request-ID - ID of request generated by service <br>  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Resource not available |  -  |
**405** | Method not allowed |  -  |
**409** | Conflict |  -  |
**429** | Request rate exceeds limit |  -  |
**0** | Unknown error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_product_id_cosell_assets_post**
> MicrosoftIngestionApiModelsCosellCosellAsset products_product_id_cosell_assets_post(product_id)

Create a CosellAsset

Create a CosellAsset

### Example


```python
import time
import partnercenter
from ..api import cosell_asset_client
from ..model.microsoft_ingestion_api_models_cosell_cosell_asset import MicrosoftIngestionApiModelsCosellCosellAsset
from pprint import pprint
# Defining the host is optional and defaults to https://api.partner.microsoft.com/v1.0/ingestion
# See configuration.py for a list of all supported configuration parameters.
configuration = partnercenter.Configuration(
    host = "https://api.partner.microsoft.com/v1.0/ingestion"
)


# Enter a context with an instance of the API client
with partnercenter.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = cosell_asset_client.CosellAssetClient(api_client)
    product_id = "productID_example" # str | ID of product
    microsoft_ingestion_api_models_cosell_cosell_asset = MicrosoftIngestionApiModelsCosellCosellAsset(None) # MicrosoftIngestionApiModelsCosellCosellAsset | Request body of a CosellAsset (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a CosellAsset
        api_response = api_instance.products_product_id_cosell_assets_post(product_id)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling CosellAssetClient->products_product_id_cosell_assets_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a CosellAsset
        api_response = api_instance.products_product_id_cosell_assets_post(product_id, microsoft_ingestion_api_models_cosell_cosell_asset=microsoft_ingestion_api_models_cosell_cosell_asset)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling CosellAssetClient->products_product_id_cosell_assets_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| ID of product |
 **microsoft_ingestion_api_models_cosell_cosell_asset** | [**MicrosoftIngestionApiModelsCosellCosellAsset**](MicrosoftIngestionApiModelsCosellCosellAsset.md)| Request body of a CosellAsset | [optional]

### Return type

[**MicrosoftIngestionApiModelsCosellCosellAsset**](MicrosoftIngestionApiModelsCosellCosellAsset.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the created CosellAsset resource |  * Request-ID - ID of request generated by service <br>  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Resource not available |  -  |
**405** | Method not allowed |  -  |
**409** | Conflict |  -  |
**429** | Request rate exceeds limit |  -  |
**0** | Unknown error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

