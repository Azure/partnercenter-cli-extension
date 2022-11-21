# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azext_partnercenter.vendored_sdks.production_ingestion.models import (ContainerPlanTechnicalConfiguration, ContainerCnabPlanTechnicalConfigurationProperties,
ConfigureResources, ConfigureResourcesStatus, JobStatus, ResourceReference, DurableId)
import requests
from time import time

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
            'get-container-plan-technical-configuration': '2022-03-01-preview3',
            'post-configure': '2022-03-01-preview2',
            'get-configure-status': '2022-03-01-preview2'
        }


    def get_version(self, operation_id):
        return self.endpoint_versions.get(operation_id)


class ProductIngestionApiClient:
    """The Product Ingestion API client"""
    def __init__(self, access_token=None):
        self.configuration = ProductIngestionApiClientConfiguration(access_token=access_token)
        self._default_headers = { 'Accept': 'application/json' }
    

    def configure_resources(self, *resources):
        """Configures one or more resources
        
        :return: response object with success / error messages
        """

        operation_id = 'post-configure'
        configure_resources = ConfigureResources()
        configure_resources.resources.append(resources)

        response = self.__call_api(operation_id, 'configure', data=configure_resources.dict())
        status = ConfigureResourcesStatus().parse_obj(response.json())

        if status.job_status != JobStatus.completed:
            # get the status until completed or timeout of 30 seconds
            timeout = time() + 30 
            while (status.job_status != JobStatus.completed):
                status = self._get_configure_resources_status(status.job_id)
                if time() > timeout:
                    break

        # otherwise the status of the job is completed, so return it
        return status.dict(exclude_unset=True, exclude={'$schema'})

    
    def update_container_plan_technical_configuration_for_bundle(self, offer_durable_id, plan_durable_id,
                         properties = ContainerCnabPlanTechnicalConfigurationProperties | None):
        """Updates the technical configuration for a 'list and sell' offer, which uses a CNAB bundle"""
        configuration = ContainerPlanTechnicalConfiguration(
            product=DurableId("product/" + offer_durable_id),
            plan=DurableId("plan/" + plan_durable_id)
        )

        # TODO: need to merge ContainerPlanTechnicalConfiguration + ContainerCnabPlanTechnicalConfigurationProperties
        # while keeping ContainerPlanTechnicalConfiguration's $schema in place

        return self.configure_resources(configuration)

    
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

    
    def _get_configure_resources_status(self, job_id):
        path = f'configure/{job_id}/status'
        return self.__call_api('get-configure-status', path)
        
    def set_default_header(self, key, value):
        self._default_headers[key] = value

    
    def __call_api(self, operation_id, path, params=None, data=None):
        url = f'{self.configuration._base_path}/{path}'
        params = self.__merge_params(params, { '$version': self.configuration.get_version(operation_id) })
        
        response = None

        if 'get' in operation_id:
            response = requests.get(url, params, headers=self.__get_request_headers())
        if 'post' in operation_id:
            response = requests.post(url, data=data, params=params, headers=self.__get_request_headers())

        return response


    def __get_request_headers(self):
        return self._default_headers

    
    def __merge_params(self, a, b):
        params = a.copy() if a is not None else {} 
        params.update(b if b is not None else {})
        return params

    