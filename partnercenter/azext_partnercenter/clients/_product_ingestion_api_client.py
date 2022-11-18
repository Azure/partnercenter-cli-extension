# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azext_partnercenter.vendored_sdks.production_ingestion.models.container_plan_technical_configuration import ContainerPlanTechnicalConfiguration
import requests


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
            'get-resource-tree': '2022-03-01-preview3',
            'get-container-plan-technical-configuration': '2022-03-01-preview3'
        }


    def get_version(self, operation_id):
        return self.endpoint_versions.get(operation_id)


class ProductIngestionApiClient:
    """The Product Ingestion API client"""
    def __init__(self, access_token=None):
        self.configuration = ProductIngestionApiClientConfiguration(access_token=access_token)
        self._default_headers = { 'Accept': 'application/json' }
    

    def get_container_plan_technical_configuration(self, offer_durable_id, plan_durable_id):
        """Gets the response from the Graph endpoint for the container plan technical configuration
        
        :return: instance of ContainerPlanTechnicalConfiguration [azext_partnercenter.vendored_sdks.production_ingestion.models.container_plan_technical_configuration]
        """

        operation_id = 'get-container-plan-technical-configuration'
        path = f'container-plan-technical-configuration/{offer_durable_id}/{plan_durable_id}'
        response = self.__call_api(operation_id, path)

        configuration = ContainerPlanTechnicalConfiguration.parse_obj(response.json())
        return configuration.dict(exclude_unset=True, exclude={'id', '$schema', 'plan', 'product'})

    
    def get_resource_tree(self, offer_durable_id):
        """Returns the raw response as a dictionary"""
        operation_id = 'get-resource-tree'
        path = f'resource-tree/product/{offer_durable_id}'

        return self.__call_api(operation_id, path).json()

        
    def set_default_header(self, key, value):
        self._default_headers[key] = value

    
    def __call_api(self, operation_id, path, params=None):
        url = f'{self.configuration._base_path}/{path}'
        params = self.__merge_params(params, { '$version': self.configuration.get_version(operation_id) })

        response = requests.get(url, params, headers=self.__get_request_headers())
        return response


    def __get_request_headers(self):
        return self._default_headers

    
    def __merge_params(self, a, b):
        params = a.copy() if a is not None else {} 
        params.update(b if b is not None else {})
        return params

    