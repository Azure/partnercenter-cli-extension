# partnercenter.FeatureAvailabilityClient

All URIs are relative to *https://api.partner.microsoft.com/v1.0/ingestion*

Method | HTTP request | Description
------------- | ------------- | -------------
[**products_product_id_feature_availabilities_get_by_instance_id_instance_i_dinstance_id_get**](FeatureAvailabilityClient.md#products_product_id_feature_availabilities_get_by_instance_id_instance_i_dinstance_id_get) | **GET** /products/{productID}/featureAvailabilities/getByInstanceID(instanceID&#x3D;{instanceID}) | Returns a paged collection of feature availability resource
[**products_product_id_featureavailabilities_feature_availability_id_get**](FeatureAvailabilityClient.md#products_product_id_featureavailabilities_feature_availability_id_get) | **GET** /products/{productID}/featureavailabilities/{featureAvailabilityID} | Returns a feature availability.
[**products_product_id_featureavailabilities_feature_availability_id_put**](FeatureAvailabilityClient.md#products_product_id_featureavailabilities_feature_availability_id_put) | **PUT** /products/{productID}/featureavailabilities/{featureAvailabilityID} | Update a feature availability resouce


# **products_product_id_feature_availabilities_get_by_instance_id_instance_i_dinstance_id_get**
> MicrosoftIngestionApiModelsCommonPagedCollectionMicrosoftIngestionApiModelsAvailabilitiesFeatureAvailability products_product_id_feature_availabilities_get_by_instance_id_instance_i_dinstance_id_get(product_id, instance_id, authorization)

Returns a paged collection of feature availability resource

Sample request:                   GET /products/{productID}/featureAvailabilities/getByInstanceID(instanceID={instanceID})                   GET /products/{productID}/featureAvailabilities/getByInstanceID(instanceID={instanceID})&amp;$expand=MarketStates,PriceSchedule,Trial

### Example


```python
import time
import partnercenter
from ..api import feature_availability_client
from ..model.microsoft_ingestion_api_models_common_paged_collection_microsoft_ingestion_api_models_availabilities_feature_availability import MicrosoftIngestionApiModelsCommonPagedCollectionMicrosoftIngestionApiModelsAvailabilitiesFeatureAvailability
from pprint import pprint
# Defining the host is optional and defaults to https://api.partner.microsoft.com/v1.0/ingestion
# See configuration.py for a list of all supported configuration parameters.
configuration = partnercenter.Configuration(
    host = "https://api.partner.microsoft.com/v1.0/ingestion"
)


# Enter a context with an instance of the API client
with partnercenter.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = feature_availability_client.FeatureAvailabilityClient(api_client)
    product_id = "productID_example" # str | ID of product
    instance_id = "instanceID_example" # str | Resource instance ID
    authorization = "Authorization_example" # str | User authorization
    expand = "$expand_example" # str | Use $expand to include MarketStates, PriceSchedules, and Trial in request/response (optional)
    client_request_id = "Client-Request-ID_example" # str | ID of request provIDed by user (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a paged collection of feature availability resource
        api_response = api_instance.products_product_id_feature_availabilities_get_by_instance_id_instance_i_dinstance_id_get(product_id, instance_id, authorization)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling FeatureAvailabilityClient->products_product_id_feature_availabilities_get_by_instance_id_instance_i_dinstance_id_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a paged collection of feature availability resource
        api_response = api_instance.products_product_id_feature_availabilities_get_by_instance_id_instance_i_dinstance_id_get(product_id, instance_id, authorization, expand=expand, client_request_id=client_request_id)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling FeatureAvailabilityClient->products_product_id_feature_availabilities_get_by_instance_id_instance_i_dinstance_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| ID of product |
 **instance_id** | **str**| Resource instance ID |
 **authorization** | **str**| User authorization |
 **expand** | **str**| Use $expand to include MarketStates, PriceSchedules, and Trial in request/response | [optional]
 **client_request_id** | **str**| ID of request provIDed by user | [optional]

### Return type

[**MicrosoftIngestionApiModelsCommonPagedCollectionMicrosoftIngestionApiModelsAvailabilitiesFeatureAvailability**](MicrosoftIngestionApiModelsCommonPagedCollectionMicrosoftIngestionApiModelsAvailabilitiesFeatureAvailability.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a paged collection of feature availability resources |  * Request-ID - ID of request generated by service <br>  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Resource not available |  -  |
**405** | Method not allowed |  -  |
**409** | Conflict |  -  |
**429** | Request rate exceeds limit |  -  |
**0** | Unknown error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_product_id_featureavailabilities_feature_availability_id_get**
> MicrosoftIngestionApiModelsAvailabilitiesFeatureAvailability products_product_id_featureavailabilities_feature_availability_id_get(product_id, feature_availability_id, authorization)

Returns a feature availability.

Sample request:                   GET products/{productID}/featureavailabilities/{featureAvailabilityID}

### Example


```python
import time
import partnercenter
from ..api import feature_availability_client
from ..model.microsoft_ingestion_api_models_availabilities_feature_availability import MicrosoftIngestionApiModelsAvailabilitiesFeatureAvailability
from pprint import pprint
# Defining the host is optional and defaults to https://api.partner.microsoft.com/v1.0/ingestion
# See configuration.py for a list of all supported configuration parameters.
configuration = partnercenter.Configuration(
    host = "https://api.partner.microsoft.com/v1.0/ingestion"
)


# Enter a context with an instance of the API client
with partnercenter.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = feature_availability_client.FeatureAvailabilityClient(api_client)
    product_id = "productID_example" # str | ID of product
    feature_availability_id = "featureAvailabilityID_example" # str | Feature availability ID
    authorization = "Authorization_example" # str | User authorization
    expand = "$expand_example" # str | Use $expand to include MarketStates, PriceSchedules, and Trial in request/response (optional)
    client_request_id = "Client-Request-ID_example" # str | ID of request provIDed by user (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a feature availability.
        api_response = api_instance.products_product_id_featureavailabilities_feature_availability_id_get(product_id, feature_availability_id, authorization)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling FeatureAvailabilityClient->products_product_id_featureavailabilities_feature_availability_id_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a feature availability.
        api_response = api_instance.products_product_id_featureavailabilities_feature_availability_id_get(product_id, feature_availability_id, authorization, expand=expand, client_request_id=client_request_id)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling FeatureAvailabilityClient->products_product_id_featureavailabilities_feature_availability_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| ID of product |
 **feature_availability_id** | **str**| Feature availability ID |
 **authorization** | **str**| User authorization |
 **expand** | **str**| Use $expand to include MarketStates, PriceSchedules, and Trial in request/response | [optional]
 **client_request_id** | **str**| ID of request provIDed by user | [optional]

### Return type

[**MicrosoftIngestionApiModelsAvailabilitiesFeatureAvailability**](MicrosoftIngestionApiModelsAvailabilitiesFeatureAvailability.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns FeatureAvailability resource |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Resource not available |  -  |
**409** | Conflict |  -  |
**429** | Request rate exceeds limit |  -  |
**0** | Unknown error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_product_id_featureavailabilities_feature_availability_id_put**
> MicrosoftIngestionApiModelsAvailabilitiesFeatureAvailability products_product_id_featureavailabilities_feature_availability_id_put(product_id, feature_availability_id, authorization)

Update a feature availability resouce

Sample request:                   PUT products/{productID}/featureavailabilities/{featureavailabilityID}                   {                       ...                   }

### Example


```python
import time
import partnercenter
from ..api import feature_availability_client
from ..model.microsoft_ingestion_api_models_availabilities_feature_availability import MicrosoftIngestionApiModelsAvailabilitiesFeatureAvailability
from pprint import pprint
# Defining the host is optional and defaults to https://api.partner.microsoft.com/v1.0/ingestion
# See configuration.py for a list of all supported configuration parameters.
configuration = partnercenter.Configuration(
    host = "https://api.partner.microsoft.com/v1.0/ingestion"
)


# Enter a context with an instance of the API client
with partnercenter.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = feature_availability_client.FeatureAvailabilityClient(api_client)
    product_id = "productID_example" # str | ID of product
    feature_availability_id = "featureAvailabilityID_example" # str | Feature availability ID
    authorization = "Authorization_example" # str | User authorization
    expand = "$expand_example" # str | Use $expand to include MarketStates, PriceSchedules, and Trial in request/response (optional)
    client_request_id = "Client-Request-ID_example" # str | ID of request provIDed by user (optional)
    microsoft_ingestion_api_models_availabilities_feature_availability = MicrosoftIngestionApiModelsAvailabilitiesFeatureAvailability(None) # MicrosoftIngestionApiModelsAvailabilitiesFeatureAvailability | Request body of a Microsoft.Ingestion.Api.Models.Availabilities.FeatureAvailability (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a feature availability resouce
        api_response = api_instance.products_product_id_featureavailabilities_feature_availability_id_put(product_id, feature_availability_id, authorization)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling FeatureAvailabilityClient->products_product_id_featureavailabilities_feature_availability_id_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a feature availability resouce
        api_response = api_instance.products_product_id_featureavailabilities_feature_availability_id_put(product_id, feature_availability_id, authorization, expand=expand, client_request_id=client_request_id, microsoft_ingestion_api_models_availabilities_feature_availability=microsoft_ingestion_api_models_availabilities_feature_availability)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling FeatureAvailabilityClient->products_product_id_featureavailabilities_feature_availability_id_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| ID of product |
 **feature_availability_id** | **str**| Feature availability ID |
 **authorization** | **str**| User authorization |
 **expand** | **str**| Use $expand to include MarketStates, PriceSchedules, and Trial in request/response | [optional]
 **client_request_id** | **str**| ID of request provIDed by user | [optional]
 **microsoft_ingestion_api_models_availabilities_feature_availability** | [**MicrosoftIngestionApiModelsAvailabilitiesFeatureAvailability**](MicrosoftIngestionApiModelsAvailabilitiesFeatureAvailability.md)| Request body of a Microsoft.Ingestion.Api.Models.Availabilities.FeatureAvailability | [optional]

### Return type

[**MicrosoftIngestionApiModelsAvailabilitiesFeatureAvailability**](MicrosoftIngestionApiModelsAvailabilitiesFeatureAvailability.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns FeatureAvailability resource |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Resource not available |  -  |
**405** | Method not allowed |  -  |
**409** | Conflict |  -  |
**429** | Request rate exceeds limit |  -  |
**0** | Unknown error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

