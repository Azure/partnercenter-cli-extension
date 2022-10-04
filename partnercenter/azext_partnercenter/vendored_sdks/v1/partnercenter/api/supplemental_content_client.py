"""
    https://api.partner.microsoft.com/v1.0/ingestion

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from ..api_client import ApiClient, Endpoint as _Endpoint
from ..model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from ..model.microsoft_ingestion_api_data_model_certification_supplemental_content import MicrosoftIngestionApiDataModelCertificationSupplementalContent
from ..model.microsoft_ingestion_api_models_common_paged_collection_microsoft_ingestion_api_data_model_certification_supplemental_content import MicrosoftIngestionApiModelsCommonPagedCollectionMicrosoftIngestionApiDataModelCertificationSupplementalContent


class SupplementalContentClient(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.products_product_id_supplemental_contents_instance_id_commit_post_endpoint = _Endpoint(
            settings={
                'response_type': (MicrosoftIngestionApiDataModelCertificationSupplementalContent,),
                'auth': [],
                'endpoint_path': '/products/{productID}/supplementalContents/{instanceID}/commit',
                'operation_id': 'products_product_id_supplemental_contents_instance_id_commit_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'product_id',
                    'instance_id',
                    'authorization',
                    'client_request_id',
                ],
                'required': [
                    'product_id',
                    'instance_id',
                    'authorization',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'product_id':
                        (str,),
                    'instance_id':
                        (str,),
                    'authorization':
                        (str,),
                    'client_request_id':
                        (str,),
                },
                'attribute_map': {
                    'product_id': 'productID',
                    'instance_id': 'instanceID',
                    'authorization': 'Authorization',
                    'client_request_id': 'Client-Request-ID',
                },
                'location_map': {
                    'product_id': 'path',
                    'instance_id': 'path',
                    'authorization': 'header',
                    'client_request_id': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.products_product_id_supplemental_contents_instance_id_get_endpoint = _Endpoint(
            settings={
                'response_type': (MicrosoftIngestionApiDataModelCertificationSupplementalContent,),
                'auth': [],
                'endpoint_path': '/products/{productID}/supplementalContents/{instanceID}',
                'operation_id': 'products_product_id_supplemental_contents_instance_id_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'product_id',
                    'instance_id',
                    'authorization',
                    'client_request_id',
                ],
                'required': [
                    'product_id',
                    'instance_id',
                    'authorization',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'product_id':
                        (str,),
                    'instance_id':
                        (str,),
                    'authorization':
                        (str,),
                    'client_request_id':
                        (str,),
                },
                'attribute_map': {
                    'product_id': 'productID',
                    'instance_id': 'instanceID',
                    'authorization': 'Authorization',
                    'client_request_id': 'Client-Request-ID',
                },
                'location_map': {
                    'product_id': 'path',
                    'instance_id': 'path',
                    'authorization': 'header',
                    'client_request_id': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.products_product_id_supplemental_contents_instance_id_put_endpoint = _Endpoint(
            settings={
                'response_type': (MicrosoftIngestionApiDataModelCertificationSupplementalContent,),
                'auth': [],
                'endpoint_path': '/products/{productID}/supplementalContents/{instanceID}',
                'operation_id': 'products_product_id_supplemental_contents_instance_id_put',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'product_id',
                    'instance_id',
                    'authorization',
                    'if_match',
                    'client_request_id',
                    'microsoft_ingestion_api_data_model_certification_supplemental_content',
                ],
                'required': [
                    'product_id',
                    'instance_id',
                    'authorization',
                    'if_match',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'product_id':
                        (str,),
                    'instance_id':
                        (str,),
                    'authorization':
                        (str,),
                    'if_match':
                        (str,),
                    'client_request_id':
                        (str,),
                    'microsoft_ingestion_api_data_model_certification_supplemental_content':
                        (MicrosoftIngestionApiDataModelCertificationSupplementalContent,),
                },
                'attribute_map': {
                    'product_id': 'productID',
                    'instance_id': 'instanceID',
                    'authorization': 'Authorization',
                    'if_match': 'If-Match',
                    'client_request_id': 'Client-Request-ID',
                },
                'location_map': {
                    'product_id': 'path',
                    'instance_id': 'path',
                    'authorization': 'header',
                    'if_match': 'header',
                    'client_request_id': 'header',
                    'microsoft_ingestion_api_data_model_certification_supplemental_content': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.products_product_id_supplementalcontents_get_by_instance_id_instance_i_dinstance_id_get_endpoint = _Endpoint(
            settings={
                'response_type': (MicrosoftIngestionApiModelsCommonPagedCollectionMicrosoftIngestionApiDataModelCertificationSupplementalContent,),
                'auth': [],
                'endpoint_path': '/products/{productID}/supplementalcontents/getByInstanceID(instanceID={instanceID})',
                'operation_id': 'products_product_id_supplementalcontents_get_by_instance_id_instance_i_dinstance_id_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'product_id',
                    'instance_id',
                    'authorization',
                    'client_request_id',
                ],
                'required': [
                    'product_id',
                    'instance_id',
                    'authorization',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'product_id':
                        (str,),
                    'instance_id':
                        (str,),
                    'authorization':
                        (str,),
                    'client_request_id':
                        (str,),
                },
                'attribute_map': {
                    'product_id': 'productID',
                    'instance_id': 'instanceID',
                    'authorization': 'Authorization',
                    'client_request_id': 'Client-Request-ID',
                },
                'location_map': {
                    'product_id': 'path',
                    'instance_id': 'path',
                    'authorization': 'header',
                    'client_request_id': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )

    def products_product_id_supplemental_contents_instance_id_commit_post(
        self,
        product_id,
        instance_id,
        authorization,
        **kwargs
    ):
        """Commit a SupplementalContent.  # noqa: E501

        Commit a SupplementalContent.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.products_product_id_supplemental_contents_instance_id_commit_post(product_id, instance_id, authorization, async_req=True)
        >>> result = thread.get()

        Args:
            product_id (str): ID of product
            instance_id (str): ID of supplemental content instance
            authorization (str): User authorization

        Keyword Args:
            client_request_id (str): ID of request provIDed by user. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            MicrosoftIngestionApiDataModelCertificationSupplementalContent
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['product_id'] = \
            product_id
        kwargs['instance_id'] = \
            instance_id
        kwargs['authorization'] = \
            authorization
        return self.products_product_id_supplemental_contents_instance_id_commit_post_endpoint.call_with_http_info(**kwargs)

    def products_product_id_supplemental_contents_instance_id_get(
        self,
        product_id,
        instance_id,
        authorization,
        **kwargs
    ):
        """Returns a SupplementalContent.  # noqa: E501

        Returns a SupplementalContent.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.products_product_id_supplemental_contents_instance_id_get(product_id, instance_id, authorization, async_req=True)
        >>> result = thread.get()

        Args:
            product_id (str): ID of product
            instance_id (str): ID of supplemental content instance
            authorization (str): User authorization

        Keyword Args:
            client_request_id (str): ID of request provIDed by user. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            MicrosoftIngestionApiDataModelCertificationSupplementalContent
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['product_id'] = \
            product_id
        kwargs['instance_id'] = \
            instance_id
        kwargs['authorization'] = \
            authorization
        return self.products_product_id_supplemental_contents_instance_id_get_endpoint.call_with_http_info(**kwargs)

    def products_product_id_supplemental_contents_instance_id_put(
        self,
        product_id,
        instance_id,
        authorization,
        if_match,
        **kwargs
    ):
        """Update a SupplementalContent.  # noqa: E501

        Update a SupplementalContent.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.products_product_id_supplemental_contents_instance_id_put(product_id, instance_id, authorization, if_match, async_req=True)
        >>> result = thread.get()

        Args:
            product_id (str): ID of product
            instance_id (str): ID of supplemental content instance
            authorization (str): User authorization
            if_match (str): ETag of the resource to be matched

        Keyword Args:
            client_request_id (str): ID of request provIDed by user. [optional]
            microsoft_ingestion_api_data_model_certification_supplemental_content (MicrosoftIngestionApiDataModelCertificationSupplementalContent): Request body of a SupplementalContent. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            MicrosoftIngestionApiDataModelCertificationSupplementalContent
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['product_id'] = \
            product_id
        kwargs['instance_id'] = \
            instance_id
        kwargs['authorization'] = \
            authorization
        kwargs['if_match'] = \
            if_match
        return self.products_product_id_supplemental_contents_instance_id_put_endpoint.call_with_http_info(**kwargs)

    def products_product_id_supplementalcontents_get_by_instance_id_instance_i_dinstance_id_get(
        self,
        product_id,
        instance_id,
        authorization,
        **kwargs
    ):
        """Returns a set of SupplementalContents for the product.  # noqa: E501

        Returns a set of SupplementalContents for the product.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.products_product_id_supplementalcontents_get_by_instance_id_instance_i_dinstance_id_get(product_id, instance_id, authorization, async_req=True)
        >>> result = thread.get()

        Args:
            product_id (str): ID of product
            instance_id (str): Resource instance ID
            authorization (str): User authorization

        Keyword Args:
            client_request_id (str): ID of request provIDed by user. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            MicrosoftIngestionApiModelsCommonPagedCollectionMicrosoftIngestionApiDataModelCertificationSupplementalContent
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['product_id'] = \
            product_id
        kwargs['instance_id'] = \
            instance_id
        kwargs['authorization'] = \
            authorization
        return self.products_product_id_supplementalcontents_get_by_instance_id_instance_i_dinstance_id_get_endpoint.call_with_http_info(**kwargs)
