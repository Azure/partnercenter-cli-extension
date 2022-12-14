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
from ..model.microsoft_ingestion_api_models_common_paged_collection_microsoft_ingestion_api_models_cosell_cosell_asset import MicrosoftIngestionApiModelsCommonPagedCollectionMicrosoftIngestionApiModelsCosellCosellAsset
from ..model.microsoft_ingestion_api_models_cosell_cosell_asset import MicrosoftIngestionApiModelsCosellCosellAsset


class CosellAssetClient(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.products_product_id_cosell_assets_cosell_asset_id_delete_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [],
                'endpoint_path': '/products/{productID}/cosellAssets/{cosellAssetID}',
                'operation_id': 'products_product_id_cosell_assets_cosell_asset_id_delete',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'product_id',
                    'cosell_asset_id',
                ],
                'required': [
                    'product_id',
                    'cosell_asset_id',
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
                    'cosell_asset_id':
                        (str,),
                },
                'attribute_map': {
                    'product_id': 'productID',
                    'cosell_asset_id': 'cosellAssetID',
                },
                'location_map': {
                    'product_id': 'path',
                    'cosell_asset_id': 'path',
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
        self.products_product_id_cosell_assets_cosell_asset_id_get_endpoint = _Endpoint(
            settings={
                'response_type': (MicrosoftIngestionApiModelsCosellCosellAsset,),
                'auth': [],
                'endpoint_path': '/products/{productID}/cosellAssets/{cosellAssetID}',
                'operation_id': 'products_product_id_cosell_assets_cosell_asset_id_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'product_id',
                    'cosell_asset_id',
                ],
                'required': [
                    'product_id',
                    'cosell_asset_id',
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
                    'cosell_asset_id':
                        (str,),
                },
                'attribute_map': {
                    'product_id': 'productID',
                    'cosell_asset_id': 'cosellAssetID',
                },
                'location_map': {
                    'product_id': 'path',
                    'cosell_asset_id': 'path',
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
        self.products_product_id_cosell_assets_cosell_asset_id_put_endpoint = _Endpoint(
            settings={
                'response_type': (MicrosoftIngestionApiModelsCosellCosellAsset,),
                'auth': [],
                'endpoint_path': '/products/{productID}/cosellAssets/{cosellAssetID}',
                'operation_id': 'products_product_id_cosell_assets_cosell_asset_id_put',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'product_id',
                    'cosell_asset_id',
                    'microsoft_ingestion_api_models_cosell_cosell_asset',
                ],
                'required': [
                    'product_id',
                    'cosell_asset_id',
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
                    'cosell_asset_id':
                        (str,),
                    'microsoft_ingestion_api_models_cosell_cosell_asset':
                        (MicrosoftIngestionApiModelsCosellCosellAsset,),
                },
                'attribute_map': {
                    'product_id': 'productID',
                    'cosell_asset_id': 'cosellAssetID',
                },
                'location_map': {
                    'product_id': 'path',
                    'cosell_asset_id': 'path',
                    'microsoft_ingestion_api_models_cosell_cosell_asset': 'body',
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
        self.products_product_id_cosell_assets_get_endpoint = _Endpoint(
            settings={
                'response_type': (MicrosoftIngestionApiModelsCommonPagedCollectionMicrosoftIngestionApiModelsCosellCosellAsset,),
                'auth': [],
                'endpoint_path': '/products/{productID}/cosellAssets',
                'operation_id': 'products_product_id_cosell_assets_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'product_id',
                ],
                'required': [
                    'product_id',
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
                },
                'attribute_map': {
                    'product_id': 'productID',
                },
                'location_map': {
                    'product_id': 'path',
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
        self.products_product_id_cosell_assets_get_by_instance_id_instance_i_dinstance_id_get_endpoint = _Endpoint(
            settings={
                'response_type': (MicrosoftIngestionApiModelsCommonPagedCollectionMicrosoftIngestionApiModelsCosellCosellAsset,),
                'auth': [],
                'endpoint_path': '/products/{productID}/cosellAssets/getByInstanceID(instanceID={instanceID})',
                'operation_id': 'products_product_id_cosell_assets_get_by_instance_id_instance_i_dinstance_id_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'product_id',
                    'instance_id',
                ],
                'required': [
                    'product_id',
                    'instance_id',
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
                },
                'attribute_map': {
                    'product_id': 'productID',
                    'instance_id': 'instanceID',
                },
                'location_map': {
                    'product_id': 'path',
                    'instance_id': 'path',
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
        self.products_product_id_cosell_assets_post_endpoint = _Endpoint(
            settings={
                'response_type': (MicrosoftIngestionApiModelsCosellCosellAsset,),
                'auth': [],
                'endpoint_path': '/products/{productID}/cosellAssets',
                'operation_id': 'products_product_id_cosell_assets_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'product_id',
                    'microsoft_ingestion_api_models_cosell_cosell_asset',
                ],
                'required': [
                    'product_id',
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
                    'microsoft_ingestion_api_models_cosell_cosell_asset':
                        (MicrosoftIngestionApiModelsCosellCosellAsset,),
                },
                'attribute_map': {
                    'product_id': 'productID',
                },
                'location_map': {
                    'product_id': 'path',
                    'microsoft_ingestion_api_models_cosell_cosell_asset': 'body',
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

    def products_product_id_cosell_assets_cosell_asset_id_delete(
        self,
        product_id,
        cosell_asset_id,
        **kwargs
    ):
        """Deletes a CosellAsset  # noqa: E501

        Deletes a CosellAsset  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.products_product_id_cosell_assets_cosell_asset_id_delete(product_id, cosell_asset_id, async_req=True)
        >>> result = thread.get()

        Args:
            product_id (str): ID of product
            cosell_asset_id (str): ID of Cosellasset

        Keyword Args:
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
            None
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
        kwargs['cosell_asset_id'] = \
            cosell_asset_id
        return self.products_product_id_cosell_assets_cosell_asset_id_delete_endpoint.call_with_http_info(**kwargs)

    def products_product_id_cosell_assets_cosell_asset_id_get(
        self,
        product_id,
        cosell_asset_id,
        **kwargs
    ):
        """Returns a CosellAsset  # noqa: E501

        Returns a CosellAsset  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.products_product_id_cosell_assets_cosell_asset_id_get(product_id, cosell_asset_id, async_req=True)
        >>> result = thread.get()

        Args:
            product_id (str): ID of product
            cosell_asset_id (str): ID of Cosellasset

        Keyword Args:
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
            MicrosoftIngestionApiModelsCosellCosellAsset
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
        kwargs['cosell_asset_id'] = \
            cosell_asset_id
        return self.products_product_id_cosell_assets_cosell_asset_id_get_endpoint.call_with_http_info(**kwargs)

    def products_product_id_cosell_assets_cosell_asset_id_put(
        self,
        product_id,
        cosell_asset_id,
        **kwargs
    ):
        """Updates a CosellAsset  # noqa: E501

        Updates a CosellAsset  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.products_product_id_cosell_assets_cosell_asset_id_put(product_id, cosell_asset_id, async_req=True)
        >>> result = thread.get()

        Args:
            product_id (str): ID of product
            cosell_asset_id (str): ID of Cosellasset

        Keyword Args:
            microsoft_ingestion_api_models_cosell_cosell_asset (MicrosoftIngestionApiModelsCosellCosellAsset): Request body of a CosellAsset. [optional]
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
            MicrosoftIngestionApiModelsCosellCosellAsset
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
        kwargs['cosell_asset_id'] = \
            cosell_asset_id
        return self.products_product_id_cosell_assets_cosell_asset_id_put_endpoint.call_with_http_info(**kwargs)

    def products_product_id_cosell_assets_get(
        self,
        product_id,
        **kwargs
    ):
        """Returns a paged collection of CosellAsset resources for product  # noqa: E501

        Returns a paged collection of CosellAsset resources for product  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.products_product_id_cosell_assets_get(product_id, async_req=True)
        >>> result = thread.get()

        Args:
            product_id (str): ID of product

        Keyword Args:
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
            MicrosoftIngestionApiModelsCommonPagedCollectionMicrosoftIngestionApiModelsCosellCosellAsset
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
        return self.products_product_id_cosell_assets_get_endpoint.call_with_http_info(**kwargs)

    def products_product_id_cosell_assets_get_by_instance_id_instance_i_dinstance_id_get(
        self,
        product_id,
        instance_id,
        **kwargs
    ):
        """Returns a paged collection of CosellAsset resources for given CosellListing instanceID  # noqa: E501

        Returns a paged collection of CosellAsset resources for given CosellListing instanceID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.products_product_id_cosell_assets_get_by_instance_id_instance_i_dinstance_id_get(product_id, instance_id, async_req=True)
        >>> result = thread.get()

        Args:
            product_id (str): ID of product
            instance_id (str): Instance ID

        Keyword Args:
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
            MicrosoftIngestionApiModelsCommonPagedCollectionMicrosoftIngestionApiModelsCosellCosellAsset
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
        return self.products_product_id_cosell_assets_get_by_instance_id_instance_i_dinstance_id_get_endpoint.call_with_http_info(**kwargs)

    def products_product_id_cosell_assets_post(
        self,
        product_id,
        **kwargs
    ):
        """Create a CosellAsset  # noqa: E501

        Create a CosellAsset  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.products_product_id_cosell_assets_post(product_id, async_req=True)
        >>> result = thread.get()

        Args:
            product_id (str): ID of product

        Keyword Args:
            microsoft_ingestion_api_models_cosell_cosell_asset (MicrosoftIngestionApiModelsCosellCosellAsset): Request body of a CosellAsset. [optional]
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
            MicrosoftIngestionApiModelsCosellCosellAsset
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
        return self.products_product_id_cosell_assets_post_endpoint.call_with_http_info(**kwargs)

