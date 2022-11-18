# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import requests
from ._util import get_api_client, get_api_client_for_graph
from ._sdk_client_provider import SdkClientProvider


class ProductIngestionApiClientConfiguration:
    """Configuration for the Product Ingestion API Client
    
        Attributes:
            server_resource     The server resource path that will be used to get the correct access token
    """

    server_resource = "https://graph.microsoft.com"

    def __init__(self, access_token=None):
        self._base_path = "https://graph.microsoft.com/rp/product-ingestion"
        self.access_token = access_token
        self.endpoint_versions = {
            'resource-tree': '2022-03-01-preview3'
        }


    def get_version(self, endpoint_name):
        return self.endpoint_versions.get(endpoint_name)


class ProductIngestionApiClient:
    """The Product Ingestion API client"""
    def __init__(self, access_token=None):
        self.configuration = ProductIngestionApiClientConfiguration(access_token=access_token)
        self._default_headers = { 'Accept': 'application/json' }
    
    def get_resource_tree(self, offer_durable_id):
        path = f'resource-tree/product/{offer_durable_id}'
        response = self.__call_api('resource-tree', path)
        return response
        
    def set_default_header(self, key, value):
        self._default_headers[key] = value

    def __call_api(self, endpoint_name, path, params=None):
        url = f'{self.configuration._base_path}/{path}'
        params = self.__merge_params(params, { '$version': self.configuration.get_version(endpoint_name) })

        response = requests.get(url, params, headers=self._get_request_headers())
        return response.json()


    def __get_request_headers(self):
        return self._default_headers

    
    def __merge_params(self, a, b):
        params = a.copy() if a is not None else {} 
        params.update(b if b is not None else {})
        return params

    