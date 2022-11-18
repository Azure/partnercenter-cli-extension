# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azext_partnercenter.clients import OfferClient, PlanClient
from azext_partnercenter.clients._base_client import BaseClient
from azext_partnercenter.vendored_sdks.v1.partnercenter.api_client import Endpoint

from partnercenter.azext_partnercenter.vendored_sdks.v1.partnercenter.exceptions import \
    NotFoundException

from ._util import (get_combined_paged_results, object_to_dict, GRAPH_API_BASE_URL)
from knack.util import CLIError
import requests
from ..models import ContainerPlanTechnicalConfiguration

class PlanTechnicalConfigurationClient(BaseClient):
    PACKAGE_MODULE = "Package"

    def __init__(self, cli_ctx, *_):
        super(PlanTechnicalConfigurationClient, self).__init__(cli_ctx, *_)
        
        self._offer_client = OfferClient(cli_ctx, *_)
        self._plan_client = PlanClient(cli_ctx, *_)

    def get(self, offer_external_id, plan_external_id):
        variant_package_branch = self._get_variant_package_branch(offer_external_id, plan_external_id)
        if variant_package_branch is None:
            raise CLIError(f'Technical Configuration not found for Plan ID "{plan_external_id}"')
        
        # if the resource type is AzureContainer, use alternative API
        technical_configuration = None

        if variant_package_branch.product.resource_type == 'AzureContainer':
            technical_configuration = self._get_container_plan_technical_configuration(variant_package_branch.product.id, variant_package_branch.variant_id)
            technical_configuration['planId'] = plan_external_id
        else:
            technical_configuration = self._get_plan_technical_configuration(variant_package_branch.product.id, variant_package_branch.variant_id)
            technical_configuration['planId'] = plan_external_id

        return technical_configuration

    def create_or_update(self, offer_external_id, plan_external_id, properties=None):
        pass

    def _get_variant_package_branch(self, offer_external_id, plan_external_id):
        product = self._offer_client._get_sdk_product_by_external_offer_id(offer_external_id)
        if product is None:
            # TODO: determine if throwing CLIError is better here
            return None
        
        variant = self._get_active_azure_sku_variant_by_external_id(product.id, plan_external_id)
        if variant is None:
            raise CLIError(f'Plan not found for "{plan_external_id}"')
 
        branches = self._sdk.branches_client.products_product_id_branches_get_by_module_modulemodule_get(
                                             product.id, self.PACKAGE_MODULE, self._get_access_token())
        if len(branches.value) == 0:
            return None
        
        variant_package_branch = next((b for b in branches.value if hasattr(b, 'variant_id') and b.variant_id == variant['id']), None)
        
        if variant_package_branch is not None:
            setattr(variant_package_branch, 'product', product)

        return variant_package_branch


    def _get_active_azure_sku_variant_by_external_id(self, offer_durable_id, plan_external_id):
        resource_type = 'AzureSkuVariant'
        variants = get_combined_paged_results(lambda : self._sdk.variant_client.products_product_id_variants_get(offer_durable_id, self._get_access_token()))
        for v in variants:
            if (v['resourceType'] == resource_type and v['state'] == 'Active'):
                if (v['externalID'] == plan_external_id):
                    return v
        return None


    def _get_plan_technical_configuration(self, offer_durable_id, plan_durable_id):
        """Since we don't know what type of technical plan this will be for now unless we map the types to the schema, this gets any technical configuration type"""

        resources = self._get_resource_tree(offer_durable_id)
        technical_configuration = None

        for r in resources:
            if 'plan-technical-configuration' in r['id'] and plan_durable_id in r['plan']:
                technical_configuration = r
                del technical_configuration['$schema']
                del technical_configuration['id']
                del technical_configuration['product']
                del technical_configuration['plan']

        return technical_configuration


    def _get_container_plan_technical_configuration(self, offer_durable_id, plan_durable_id):
        """Gets the response from the Graph endpoint for the container plan technical configuration which is different than the standard ingestion API client package"""

        url = f'{GRAPH_API_BASE_URL}/container-plan-technical-configuration/{offer_durable_id}/{plan_durable_id}'
        params = { '$version': '2022-03-01-preview3' }
        response = requests.get(url, params, headers=self._get_request_headers())

        configuration = ContainerPlanTechnicalConfiguration.parse_obj(response.json())
        return configuration.dict(
            exclude_unset=True, 
            exclude={'id', '$schema', 'plan', 'product'})


    def _get_resource_tree(self, offer_durable_id):
        url = f'{GRAPH_API_BASE_URL}/resource-tree/product/{offer_durable_id}'
        params = { '$version': '2022-03-01-preview3' }
        response = requests.get(url, params, headers=self._get_request_headers())

        resources = response.json()['resources']
        return resources

        return Endpoint(
            settings={
                'response_type': (dict,),
                'auth': [],
                'endpoint_path': '/resource-tree/product/{productId}',
                'operation_id': 'resource_tree_get_product_id',
                'http_method': 'GET',
                'servers': [{ 'url': GRAPH_API_BASE_URL }],
            },
            params_map={
                'all': [
                    'product_id',
                    'authorization',
                    'version',
                ],
                'required': [
                    'product_id',
                    'version'
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
                    'authorization':
                        (str,),
                    'version':
                        (str,),
                },
                'attribute_map': {
                    'product_id': 'productId',
                    'authorization': 'Authorization',
                    'version': '$version',
                },
                'location_map': {
                    'product_id': 'path',
                    'authorization': 'header',
                    'version': 'query',
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
            api_client=self._graph_api_client
        )