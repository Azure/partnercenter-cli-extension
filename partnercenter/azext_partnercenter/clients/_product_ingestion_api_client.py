# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long
# pylint: disable=protected-access
# pylint: disable=too-few-public-methods

from time import time
import requests
from pydantic import Extra
from azext_partnercenter.vendored_sdks.production_ingestion.models import (
    Submission,
    ContainerPlanTechnicalConfiguration,
    ContainerCnabPlanTechnicalConfigurationProperties,
    ConfigureResources,
    ConfigureResourcesStatus,
    JobStatus,
    DurableId)


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
            'get-configure-status': '2022-03-01-preview2',
            'get-submission': '2022-03-01-preview2'
        }

    def get_version(self, operation_id):
        return self.endpoint_versions.get(operation_id)


class ProductIngestionApiClient:
    """The Product Ingestion API client"""
    def __init__(self, access_token=None):
        self.configuration = ProductIngestionApiClientConfiguration(access_token=access_token)
        self._default_headers = {'Accept': 'application/json'}

    def configure_resources(self, *resources):
        """Configures one or more resources

        :return: response object with success / error messages
        """

        operation_id = 'post-configure'
        configure_resources = ConfigureResources(resources=resources)
        data = configure_resources.dict(by_alias=True, exclude_unset=True)
        data['$schema'] = 'https://product-ingestion.azureedge.net/schema/configure/2022-03-01-preview2'

        for resource in data['resources']:
            if 'resourceName' in resource.keys():
                del resource['resourceName']
            if 'validations' in resource.keys():
                del resource['validations']

        response = self.__call_api(operation_id, 'configure', data=data)
        response.raise_for_status()

        ConfigureResourcesStatus.Config.extra = Extra.allow
        status = ConfigureResourcesStatus.parse_obj(response.json())

        if status.job_status != JobStatus.completed:
            # get the status until completed or timeout of 30 seconds
            timeout = time() + 30
            while status.job_status != JobStatus.completed:
                status = self._get_configure_resources_status(status.job_id)
                if time() > timeout:
                    break

        # otherwise the status of the job is completed, so return it
        return status

    def update_container_plan_technical_configuration_for_bundle(self, offer_durable_id, plan_durable_id,
                                                                 properties=ContainerCnabPlanTechnicalConfigurationProperties | None):
        """Updates the technical configuration for a 'list and sell' offer, which uses a CNAB bundle"""

        durable_id = DurableId(root=f'container-plan-technical-configuration/{offer_durable_id}/{plan_durable_id}')
        product_id = DurableId(root="product/" + offer_durable_id)
        plan_id = DurableId(root=f"plan/{offer_durable_id}/{plan_durable_id}")

        configuration = ContainerPlanTechnicalConfiguration(
            id=durable_id.root,
            product=product_id.root,
            plan=plan_id.root
        )
        setattr(configuration, 'payloadType', 'cnab')
        setattr(configuration, 'clusterExtensionType', properties.cluster_extension_type)
        setattr(configuration, 'cnabReferences', properties.cnab_references)

        resource = configuration.dict(by_alias=True)
        resource['$schema'] = 'https://product-ingestion.azureedge.net/schema/container-plan-technical-configuration/2022-03-01-preview3'

        del resource['resourceName']
        del resource['validations']

        return self.configure_resources(resource)

    def get_submissions(self, offer_durable_id):
        """Gets the response from the Graph endpoint of submissions

        :return: list of Submission [azext_partnercenter.vendored_sdks.product_ingestion.models]
        """
        response = self.__call_api('get-submission', f'submission/{offer_durable_id}')
        json = response.json() | {}

        submissions = list(map(Submission.parse_obj, json['value']))
        return submissions

    def get_submission(self, offer_durable_id, submission_id):
        """Gets the response from the Graph endpoint of submissions

        :return: instance of Submission [azext_partnercenter.vendored_sdks.product_ingestion.models]
        """
        response = self.__call_api('get-submission', f'submission/{offer_durable_id}/{submission_id}')
        json = response.json() | {}

        return Submission.parse_obj(json)

    def publish_submission(self, target, offer_durable_id, submission_id=None):
        """Publishes a product, either all its draft changes or a specific submission using the submission_id"""
        product_id = DurableId(root="product/" + offer_durable_id)
        durable_id = DurableId(root=f"submission/{offer_durable_id}/{submission_id}") if submission_id is not None else None

        resource = {
            '$schema': 'https://product-ingestion.azureedge.net/schema/submission/2022-03-01-preview2',
            'id': (None if durable_id is None else durable_id.root),
            'product': product_id.root,
            'target': {'targetType': target}
        }

        # if there isn't a submission id provided, this will cause all draft changes to be submitted
        # the id property must be expicitly removed so the API processes it correctly
        # see: https://learn.microsoft.com/en-us/azure/marketplace/product-ingestion-api#method-1-publish-all-draft-resources

        if durable_id is None:
            del resource['id']

        result = self.configure_resources(resource)
        return result.dict(exclude={'$schema'}, exclude_unset=True)

    def get_container_plan_technical_configuration(self, offer_durable_id, plan_durable_id, sell_through_microsoft):
        """Gets the response from the Graph endpoint for the container plan technical configuration

        :return: instance of ContainerPlanTechnicalConfiguration [azext_partnercenter.vendored_sdks.production_ingestion.models.container_plan_technical_configuration]
        """

        operation_id = 'get-container-plan-technical-configuration'
        path = f'container-plan-technical-configuration/{offer_durable_id}/{plan_durable_id}'
        response = self.__call_api(operation_id, path)

        configuration = self._parse_technical_configuration_response(response, sell_through_microsoft)
        return configuration

    def get_resource_tree(self, offer_durable_id):
        """Returns the raw response as a dictionary"""
        operation_id = 'get-resource-tree'
        path = f'resource-tree/product/{offer_durable_id}'

        return self.__call_api(operation_id, path).json()

    def _parse_technical_configuration_response(self, response, sell_through_microsoft):
        r"""If the offer setup is configured to sell through microsoft, then CNAB, otherwise it's Image

        :param response: :class:`Response <Response>` object from the Response library
        :param sell_through_microsoft Boolean. whether this is a sell through microsoft Setup
        """
        json = response.json() | {}

        if sell_through_microsoft:
            # the API response is inconsistent in its object shape based on the sell through microsoft
            # this attr must be added for deserialization purposes
            if 'cnabReferences' not in json:
                json['cnabReferences'] = []

            data = {
                'cnabReferences': json['cnabReferences'] if 'cnabReferences' in json else [],
                'payloadType': 'cnab',
                'clusterExtensionType': json['clusterExtensionType'] if 'clusterExtensionType' in json else None
            }
            properties = ContainerCnabPlanTechnicalConfigurationProperties.construct(**data)
            return properties

        return ContainerPlanTechnicalConfiguration.parse_obj(response.json())

    def _get_configure_resources_status(self, job_id):
        path = f'configure/{job_id}/status'
        response = self.__call_api('get-configure-status', path)
        return ConfigureResourcesStatus.parse_obj(response.json())

    def set_default_header(self, key, value):
        self._default_headers[key] = value

    def __call_api(self, operation_id, path, params=None, data=None):
        url = f'{self.configuration._base_path}/{path}'
        params = self.__merge_params(params, {'$version': self.configuration.get_version(operation_id)})

        timeout = 10  # timeout in 10 seconds
        response = None

        if 'get' in operation_id:
            response = requests.get(url, params, headers=self.__get_request_headers(), timeout=timeout)
        if 'post' in operation_id:
            response = requests.post(url, json=data, params=params, headers=self.__get_request_headers(), timeout=timeout)

        return response

    def __get_request_headers(self):
        return self._default_headers

    def __merge_params(self, a, b):
        params = a.copy() if a is not None else {}
        params.update(b if b is not None else {})
        return params
