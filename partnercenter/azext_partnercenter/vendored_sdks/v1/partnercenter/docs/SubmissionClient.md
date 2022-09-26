# partnercenter.SubmissionClient

All URIs are relative to *https://api.partner.microsoft.com/v1.0/ingestion*

Method | HTTP request | Description
------------- | ------------- | -------------
[**products_product_id_submissions_get**](SubmissionClient.md#products_product_id_submissions_get) | **GET** /products/{productID}/submissions | Returns a paged collection of Submissions
[**products_product_id_submissions_post**](SubmissionClient.md#products_product_id_submissions_post) | **POST** /products/{productID}/submissions | Creates a new Submission
[**products_product_id_submissions_submission_id_delete**](SubmissionClient.md#products_product_id_submissions_submission_id_delete) | **DELETE** /products/{productID}/submissions/{submissionID} | Deletes a Submission
[**products_product_id_submissions_submission_id_get**](SubmissionClient.md#products_product_id_submissions_submission_id_get) | **GET** /products/{productID}/submissions/{submissionID} | Returns a Submission
[**products_product_id_submissions_submission_id_promote_post**](SubmissionClient.md#products_product_id_submissions_submission_id_promote_post) | **POST** /products/{productID}/submissions/{submissionID}/promote | Promote a Preview Submission to live
[**products_product_id_submissions_submission_id_reports_get**](SubmissionClient.md#products_product_id_submissions_submission_id_reports_get) | **GET** /products/{productID}/submissions/{submissionID}/reports | Returns a collection of CertificationReport for a Submission
[**products_product_id_submissions_submission_id_validations_get**](SubmissionClient.md#products_product_id_submissions_submission_id_validations_get) | **GET** /products/{productID}/submissions/{submissionID}/validations | Returns Validation for a Submission
[**products_product_id_submissions_submission_id_workflowdetails_get**](SubmissionClient.md#products_product_id_submissions_submission_id_workflowdetails_get) | **GET** /products/{productID}/submissions/{submissionID}/workflowdetails | Returns workflow details for a Submission


# **products_product_id_submissions_get**
> MicrosoftIngestionApiModelsCommonPagedCollectionMicrosoftIngestionApiModelsSubmissionsSubmission products_product_id_submissions_get(product_id, authorization)

Returns a paged collection of Submissions

Sample request:                    GET /products/{productID}/submissions                        =&gt; returns both Inprogress and Published Submissions for Retail                    GET /products/{productID}/submissions?state={state}                        =&gt; returns the Submission (either Inprogress or Published) of requested state for Retail                    GET /products/{productID}/submissions?sandboxID={sandboxID}                        =&gt; returns both Inprogress and Published Submissions for requested Sandbox                    GET /products/{productID}/submissions?sandboxID={sandboxID}&amp;state={state}                        =&gt; returns the Submission (either Inprogress or Published) of requested state for requested Sandbox                    GET /products/{productID}/submissions?flightID={flightID}                        =&gt; returns both Inprogress and Published Submissions for requested Flight                    GET /products/{productID}/submissions?flightID={flightID}&amp;state={state}                        =&gt; returns the Submission (either Inprogress or Published) of requested state for requested Flight

### Example


```python
import time
import partnercenter
from ..api import submission_client
from ..model.microsoft_ingestion_api_models_common_paged_collection_microsoft_ingestion_api_models_submissions_submission import MicrosoftIngestionApiModelsCommonPagedCollectionMicrosoftIngestionApiModelsSubmissionsSubmission
from pprint import pprint
# Defining the host is optional and defaults to https://api.partner.microsoft.com/v1.0/ingestion
# See configuration.py for a list of all supported configuration parameters.
configuration = partnercenter.Configuration(
    host = "https://api.partner.microsoft.com/v1.0/ingestion"
)


# Enter a context with an instance of the API client
with partnercenter.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = submission_client.SubmissionClient(api_client)
    product_id = "productID_example" # str | ID of product
    authorization = "Authorization_example" # str | User authorization
    filter = "$filter_example" # str | Filter of submissions. Filter by State and/or Targets with operation eq is allowed. (optional)
    expand = "$expand_example" # str | Use $expand=PublishOption to Include publish option in response (optional)
    client_request_id = "Client-Request-ID_example" # str | ID of request provIDed by user (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a paged collection of Submissions
        api_response = api_instance.products_product_id_submissions_get(product_id, authorization)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling SubmissionClient->products_product_id_submissions_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a paged collection of Submissions
        api_response = api_instance.products_product_id_submissions_get(product_id, authorization, filter=filter, expand=expand, client_request_id=client_request_id)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling SubmissionClient->products_product_id_submissions_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| ID of product |
 **authorization** | **str**| User authorization |
 **filter** | **str**| Filter of submissions. Filter by State and/or Targets with operation eq is allowed. | [optional]
 **expand** | **str**| Use $expand&#x3D;PublishOption to Include publish option in response | [optional]
 **client_request_id** | **str**| ID of request provIDed by user | [optional]

### Return type

[**MicrosoftIngestionApiModelsCommonPagedCollectionMicrosoftIngestionApiModelsSubmissionsSubmission**](MicrosoftIngestionApiModelsCommonPagedCollectionMicrosoftIngestionApiModelsSubmissionsSubmission.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a paged collection of Submissions |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Resource not available |  -  |
**405** | Method not allowed |  -  |
**409** | Conflict |  -  |
**429** | Request rate exceeds limit |  -  |
**0** | Unknown error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_product_id_submissions_post**
> MicrosoftIngestionApiModelsSubmissionsSubmission products_product_id_submissions_post(product_id, authorization)

Creates a new Submission

Sample request:                    POST /products/{productID}/submissions      {          // empty Json body      }          =&gt; create Inprogress Submission for Retail                    POST /products/{productID}/submissions      {          \"sandboxID\":\"{sandboxID}\"      }          =&gt; create Inprogress Submission for a Sandbox                    POST /products/{productID}/submissions      {          \"flightID\":\"{flightID}\"      }          =&gt; create Inprogress Submission for a Flight

### Example


```python
import time
import partnercenter
from ..api import submission_client
from ..model.microsoft_ingestion_api_models_submissions_submission import MicrosoftIngestionApiModelsSubmissionsSubmission
from ..model.microsoft_ingestion_api_models_submissions_submission_creation_request import MicrosoftIngestionApiModelsSubmissionsSubmissionCreationRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.partner.microsoft.com/v1.0/ingestion
# See configuration.py for a list of all supported configuration parameters.
configuration = partnercenter.Configuration(
    host = "https://api.partner.microsoft.com/v1.0/ingestion"
)


# Enter a context with an instance of the API client
with partnercenter.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = submission_client.SubmissionClient(api_client)
    product_id = "productID_example" # str | ID of product
    authorization = "Authorization_example" # str | User authorization
    client_request_id = "Client-Request-ID_example" # str | ID of request provIDed by user (optional)
    microsoft_ingestion_api_models_submissions_submission_creation_request = MicrosoftIngestionApiModelsSubmissionsSubmissionCreationRequest(
        resource_type="SubmissionCreationRequest",
        targets=[
            MicrosoftIngestionApiModelsCommonTypeValuePair(
                type="type_example",
                value="value_example",
            ),
        ],
        resources=[
            MicrosoftIngestionApiModelsCommonTypeValuePair(
                type="type_example",
                value="value_example",
            ),
        ],
        variant_resources=[
            MicrosoftIngestionApiModelsSubmissionsVariantResource(
                variant_id="variant_id_example",
                resources=[
                    MicrosoftIngestionApiModelsCommonTypeValuePair(
                        type="type_example",
                        value="value_example",
                    ),
                ],
            ),
        ],
        publish_option=MicrosoftIngestionApiModelsSubmissionsPublishOption(
            release_time_in_utc=dateutil_parser('1970-01-01T00:00:00.00Z'),
            is_manual_publish=True,
            is_auto_promote=True,
            certification_notes="certification_notes_example",
        ),
        extended_properties=[
            MicrosoftIngestionApiModelsCommonTypeValuePair(
                type="type_example",
                value="value_example",
            ),
        ],
    ) # MicrosoftIngestionApiModelsSubmissionsSubmissionCreationRequest | Request body of a Microsoft.Ingestion.Api.Models.Submissions.SubmissionCreationRequest (optional)

    # example passing only required values which don't have defaults set
    try:
        # Creates a new Submission
        api_response = api_instance.products_product_id_submissions_post(product_id, authorization)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling SubmissionClient->products_product_id_submissions_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Creates a new Submission
        api_response = api_instance.products_product_id_submissions_post(product_id, authorization, client_request_id=client_request_id, microsoft_ingestion_api_models_submissions_submission_creation_request=microsoft_ingestion_api_models_submissions_submission_creation_request)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling SubmissionClient->products_product_id_submissions_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| ID of product |
 **authorization** | **str**| User authorization |
 **client_request_id** | **str**| ID of request provIDed by user | [optional]
 **microsoft_ingestion_api_models_submissions_submission_creation_request** | [**MicrosoftIngestionApiModelsSubmissionsSubmissionCreationRequest**](MicrosoftIngestionApiModelsSubmissionsSubmissionCreationRequest.md)| Request body of a Microsoft.Ingestion.Api.Models.Submissions.SubmissionCreationRequest | [optional]

### Return type

[**MicrosoftIngestionApiModelsSubmissionsSubmission**](MicrosoftIngestionApiModelsSubmissionsSubmission.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Returns the newly created Submission |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Resource not available |  -  |
**405** | Method not allowed |  -  |
**409** | Conflict |  -  |
**429** | Request rate exceeds limit |  -  |
**0** | Unknown error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_product_id_submissions_submission_id_delete**
> products_product_id_submissions_submission_id_delete(product_id, submission_id, authorization)

Deletes a Submission

Sample request:                    DELETE /products/{productID}/submissions/{submissionID}

### Example


```python
import time
import partnercenter
from ..api import submission_client
from pprint import pprint
# Defining the host is optional and defaults to https://api.partner.microsoft.com/v1.0/ingestion
# See configuration.py for a list of all supported configuration parameters.
configuration = partnercenter.Configuration(
    host = "https://api.partner.microsoft.com/v1.0/ingestion"
)


# Enter a context with an instance of the API client
with partnercenter.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = submission_client.SubmissionClient(api_client)
    product_id = "productID_example" # str | ID of product
    submission_id = "submissionID_example" # str | ID of submission
    authorization = "Authorization_example" # str | User authorization
    client_request_id = "Client-Request-ID_example" # str | ID of request provIDed by user (optional)

    # example passing only required values which don't have defaults set
    try:
        # Deletes a Submission
        api_instance.products_product_id_submissions_submission_id_delete(product_id, submission_id, authorization)
    except partnercenter.ApiException as e:
        print("Exception when calling SubmissionClient->products_product_id_submissions_submission_id_delete: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Deletes a Submission
        api_instance.products_product_id_submissions_submission_id_delete(product_id, submission_id, authorization, client_request_id=client_request_id)
    except partnercenter.ApiException as e:
        print("Exception when calling SubmissionClient->products_product_id_submissions_submission_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| ID of product |
 **submission_id** | **str**| ID of submission |
 **authorization** | **str**| User authorization |
 **client_request_id** | **str**| ID of request provIDed by user | [optional]

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
**204** | Deletes a Submission (only inprogress Submission can be deleted) |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Resource not available |  -  |
**405** | Method not allowed |  -  |
**409** | Conflict |  -  |
**429** | Request rate exceeds limit |  -  |
**0** | Unknown error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_product_id_submissions_submission_id_get**
> MicrosoftIngestionApiModelsSubmissionsSubmission products_product_id_submissions_submission_id_get(product_id, submission_id, authorization)

Returns a Submission

Sample request:                    GET /products/{productID}/submissions/{submissionID}

### Example


```python
import time
import partnercenter
from ..api import submission_client
from ..model.microsoft_ingestion_api_models_submissions_submission import MicrosoftIngestionApiModelsSubmissionsSubmission
from pprint import pprint
# Defining the host is optional and defaults to https://api.partner.microsoft.com/v1.0/ingestion
# See configuration.py for a list of all supported configuration parameters.
configuration = partnercenter.Configuration(
    host = "https://api.partner.microsoft.com/v1.0/ingestion"
)


# Enter a context with an instance of the API client
with partnercenter.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = submission_client.SubmissionClient(api_client)
    product_id = "productID_example" # str | ID of product
    submission_id = "submissionID_example" # str | ID of submission
    authorization = "Authorization_example" # str | User authorization
    expand = "$expand_example" # str | Use $expand=PublishOption to Include publish option in response (optional)
    client_request_id = "Client-Request-ID_example" # str | ID of request provIDed by user (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a Submission
        api_response = api_instance.products_product_id_submissions_submission_id_get(product_id, submission_id, authorization)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling SubmissionClient->products_product_id_submissions_submission_id_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a Submission
        api_response = api_instance.products_product_id_submissions_submission_id_get(product_id, submission_id, authorization, expand=expand, client_request_id=client_request_id)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling SubmissionClient->products_product_id_submissions_submission_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| ID of product |
 **submission_id** | **str**| ID of submission |
 **authorization** | **str**| User authorization |
 **expand** | **str**| Use $expand&#x3D;PublishOption to Include publish option in response | [optional]
 **client_request_id** | **str**| ID of request provIDed by user | [optional]

### Return type

[**MicrosoftIngestionApiModelsSubmissionsSubmission**](MicrosoftIngestionApiModelsSubmissionsSubmission.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a Submission |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Resource not available |  -  |
**405** | Method not allowed |  -  |
**409** | Conflict |  -  |
**429** | Request rate exceeds limit |  -  |
**0** | Unknown error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_product_id_submissions_submission_id_promote_post**
> MicrosoftIngestionApiModelsSubmissionsWorkflowDetail products_product_id_submissions_submission_id_promote_post(product_id, submission_id, authorization)

Promote a Preview Submission to live

Sample request:                    POST /products/{productID}/submissions/{submissionID}/promote      [empty body]

### Example


```python
import time
import partnercenter
from ..api import submission_client
from ..model.microsoft_ingestion_api_models_submissions_workflow_detail import MicrosoftIngestionApiModelsSubmissionsWorkflowDetail
from pprint import pprint
# Defining the host is optional and defaults to https://api.partner.microsoft.com/v1.0/ingestion
# See configuration.py for a list of all supported configuration parameters.
configuration = partnercenter.Configuration(
    host = "https://api.partner.microsoft.com/v1.0/ingestion"
)


# Enter a context with an instance of the API client
with partnercenter.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = submission_client.SubmissionClient(api_client)
    product_id = "productID_example" # str | ID of product
    submission_id = "submissionID_example" # str | ID of submission
    authorization = "Authorization_example" # str | User authorization
    client_request_id = "Client-Request-ID_example" # str | ID of request provIDed by user (optional)

    # example passing only required values which don't have defaults set
    try:
        # Promote a Preview Submission to live
        api_response = api_instance.products_product_id_submissions_submission_id_promote_post(product_id, submission_id, authorization)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling SubmissionClient->products_product_id_submissions_submission_id_promote_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Promote a Preview Submission to live
        api_response = api_instance.products_product_id_submissions_submission_id_promote_post(product_id, submission_id, authorization, client_request_id=client_request_id)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling SubmissionClient->products_product_id_submissions_submission_id_promote_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| ID of product |
 **submission_id** | **str**| ID of submission |
 **authorization** | **str**| User authorization |
 **client_request_id** | **str**| ID of request provIDed by user | [optional]

### Return type

[**MicrosoftIngestionApiModelsSubmissionsWorkflowDetail**](MicrosoftIngestionApiModelsSubmissionsWorkflowDetail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns Submission workflow details of the submission that has been promoted to live. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Resource not available |  -  |
**405** | Method not allowed |  -  |
**409** | Conflict |  -  |
**429** | Request rate exceeds limit |  -  |
**0** | Unknown error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_product_id_submissions_submission_id_reports_get**
> MicrosoftIngestionApiModelsCommonPagedCollectionMicrosoftIngestionApiModelsSubmissionsCertificationReport products_product_id_submissions_submission_id_reports_get(product_id, submission_id, authorization)

Returns a collection of CertificationReport for a Submission

Sample request:                    GET /products/{productID}/submissions/{submissionID}/reports

### Example


```python
import time
import partnercenter
from ..api import submission_client
from ..model.microsoft_ingestion_api_models_common_paged_collection_microsoft_ingestion_api_models_submissions_certification_report import MicrosoftIngestionApiModelsCommonPagedCollectionMicrosoftIngestionApiModelsSubmissionsCertificationReport
from pprint import pprint
# Defining the host is optional and defaults to https://api.partner.microsoft.com/v1.0/ingestion
# See configuration.py for a list of all supported configuration parameters.
configuration = partnercenter.Configuration(
    host = "https://api.partner.microsoft.com/v1.0/ingestion"
)


# Enter a context with an instance of the API client
with partnercenter.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = submission_client.SubmissionClient(api_client)
    product_id = "productID_example" # str | ID of product
    submission_id = "submissionID_example" # str | ID of submission
    authorization = "Authorization_example" # str | User authorization
    client_request_id = "Client-Request-ID_example" # str | ID of request provIDed by user (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a collection of CertificationReport for a Submission
        api_response = api_instance.products_product_id_submissions_submission_id_reports_get(product_id, submission_id, authorization)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling SubmissionClient->products_product_id_submissions_submission_id_reports_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a collection of CertificationReport for a Submission
        api_response = api_instance.products_product_id_submissions_submission_id_reports_get(product_id, submission_id, authorization, client_request_id=client_request_id)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling SubmissionClient->products_product_id_submissions_submission_id_reports_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| ID of product |
 **submission_id** | **str**| ID of submission |
 **authorization** | **str**| User authorization |
 **client_request_id** | **str**| ID of request provIDed by user | [optional]

### Return type

[**MicrosoftIngestionApiModelsCommonPagedCollectionMicrosoftIngestionApiModelsSubmissionsCertificationReport**](MicrosoftIngestionApiModelsCommonPagedCollectionMicrosoftIngestionApiModelsSubmissionsCertificationReport.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns collection of Certification-Report |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Resource not available |  -  |
**405** | Method not allowed |  -  |
**409** | Conflict |  -  |
**429** | Request rate exceeds limit |  -  |
**0** | Unknown error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_product_id_submissions_submission_id_validations_get**
> MicrosoftIngestionApiModelsCommonPagedCollectionMicrosoftIngestionApiModelsSubmissionsValidationItem products_product_id_submissions_submission_id_validations_get(product_id, submission_id, authorization)

Returns Validation for a Submission

Sample request:                   GET /products/{productID}/submissions/{submissionID}/validations

### Example


```python
import time
import partnercenter
from ..api import submission_client
from ..model.microsoft_ingestion_api_models_common_paged_collection_microsoft_ingestion_api_models_submissions_validation_item import MicrosoftIngestionApiModelsCommonPagedCollectionMicrosoftIngestionApiModelsSubmissionsValidationItem
from pprint import pprint
# Defining the host is optional and defaults to https://api.partner.microsoft.com/v1.0/ingestion
# See configuration.py for a list of all supported configuration parameters.
configuration = partnercenter.Configuration(
    host = "https://api.partner.microsoft.com/v1.0/ingestion"
)


# Enter a context with an instance of the API client
with partnercenter.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = submission_client.SubmissionClient(api_client)
    product_id = "productID_example" # str | ID of product
    submission_id = "submissionID_example" # str | ID of submission
    authorization = "Authorization_example" # str | User authorization
    client_request_id = "Client-Request-ID_example" # str | ID of request provIDed by user (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns Validation for a Submission
        api_response = api_instance.products_product_id_submissions_submission_id_validations_get(product_id, submission_id, authorization)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling SubmissionClient->products_product_id_submissions_submission_id_validations_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns Validation for a Submission
        api_response = api_instance.products_product_id_submissions_submission_id_validations_get(product_id, submission_id, authorization, client_request_id=client_request_id)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling SubmissionClient->products_product_id_submissions_submission_id_validations_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| ID of product |
 **submission_id** | **str**| ID of submission |
 **authorization** | **str**| User authorization |
 **client_request_id** | **str**| ID of request provIDed by user | [optional]

### Return type

[**MicrosoftIngestionApiModelsCommonPagedCollectionMicrosoftIngestionApiModelsSubmissionsValidationItem**](MicrosoftIngestionApiModelsCommonPagedCollectionMicrosoftIngestionApiModelsSubmissionsValidationItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A PagedCollection of ValidationItems |  * Request-ID - ID of request generated by service <br>  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Resource not available |  -  |
**405** | Method not allowed |  -  |
**409** | Conflict |  -  |
**429** | Request rate exceeds limit |  -  |
**0** | Unknown error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_product_id_submissions_submission_id_workflowdetails_get**
> MicrosoftIngestionApiModelsCommonPagedCollectionMicrosoftIngestionApiModelsSubmissionsWorkflowDetail products_product_id_submissions_submission_id_workflowdetails_get(product_id, submission_id, authorization)

Returns workflow details for a Submission

Sample request:                   GET /products/{productID}/submissions/{submissionID}/workflowdetails

### Example


```python
import time
import partnercenter
from ..api import submission_client
from ..model.microsoft_ingestion_api_models_common_paged_collection_microsoft_ingestion_api_models_submissions_workflow_detail import MicrosoftIngestionApiModelsCommonPagedCollectionMicrosoftIngestionApiModelsSubmissionsWorkflowDetail
from pprint import pprint
# Defining the host is optional and defaults to https://api.partner.microsoft.com/v1.0/ingestion
# See configuration.py for a list of all supported configuration parameters.
configuration = partnercenter.Configuration(
    host = "https://api.partner.microsoft.com/v1.0/ingestion"
)


# Enter a context with an instance of the API client
with partnercenter.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = submission_client.SubmissionClient(api_client)
    product_id = "productID_example" # str | ID of product
    submission_id = "submissionID_example" # str | ID of submission
    authorization = "Authorization_example" # str | User authorization
    client_request_id = "Client-Request-ID_example" # str | ID of request provIDed by user (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns workflow details for a Submission
        api_response = api_instance.products_product_id_submissions_submission_id_workflowdetails_get(product_id, submission_id, authorization)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling SubmissionClient->products_product_id_submissions_submission_id_workflowdetails_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns workflow details for a Submission
        api_response = api_instance.products_product_id_submissions_submission_id_workflowdetails_get(product_id, submission_id, authorization, client_request_id=client_request_id)
        pprint(api_response)
    except partnercenter.ApiException as e:
        print("Exception when calling SubmissionClient->products_product_id_submissions_submission_id_workflowdetails_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| ID of product |
 **submission_id** | **str**| ID of submission |
 **authorization** | **str**| User authorization |
 **client_request_id** | **str**| ID of request provIDed by user | [optional]

### Return type

[**MicrosoftIngestionApiModelsCommonPagedCollectionMicrosoftIngestionApiModelsSubmissionsWorkflowDetail**](MicrosoftIngestionApiModelsCommonPagedCollectionMicrosoftIngestionApiModelsSubmissionsWorkflowDetail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The submission workflow details resource |  * Request-ID - ID of request generated by service <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Resource not available |  -  |
**429** | Request rate exceeds limit |  -  |
**0** | Unknown error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

