# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long
# pylint: disable=protected-access
# pylint: disable=no-else-return

from knack.util import CLIError
from azext_partnercenter.clients import OfferClient, PlanClient
from azext_partnercenter.clients._base_client import BaseClient
from azext_partnercenter.vendored_sdks.production_ingestion.models import ContainerCnabPlanTechnicalConfigurationProperties
from ._util import get_combined_paged_results


class PlanTechnicalConfigurationClient(BaseClient):
    PACKAGE_MODULE = "Package"

    def __init__(self, cli_ctx, *_):
        super().__init__(cli_ctx, *_)

        self._offer_client = OfferClient(cli_ctx, *_)
        self._plan_client = PlanClient(cli_ctx, *_)

    def get(self, offer_external_id, plan_external_id):
        variant_package_branch = self._get_variant_package_branch(offer_external_id, plan_external_id)
        if variant_package_branch is None:
            raise CLIError(f'Technical Configuration not found for Plan ID "{plan_external_id}"')

        # if the resource type is AzureContainer, use alternative API
        offer_durable_id = variant_package_branch.product.id
        plan_durable_id = variant_package_branch.variant_id
        sell_through_microsoft = self._get_sell_through_microsoft(offer_durable_id)

        technical_configuration = None

        if variant_package_branch.product.resource_type == 'AzureContainer':
            technical_configuration = self._graph_api_client.get_container_plan_technical_configuration(offer_durable_id, plan_durable_id, sell_through_microsoft)
        else:
            technical_configuration = self._get_plan_technical_configuration(variant_package_branch.product.id, variant_package_branch.variant_id)
            technical_configuration['planId'] = plan_external_id

        return technical_configuration

    def add_bundle(self, offer_external_id, plan_external_id, properties=ContainerCnabPlanTechnicalConfigurationProperties | None):
        variant_package_branch = self._get_variant_package_branch(offer_external_id, plan_external_id)
        offer_durable_id = variant_package_branch.product.id
        plan_durable_id = variant_package_branch.variant_id

        # here is where we receive the fragmented properties arg, update
        status = self._graph_api_client.update_container_plan_technical_configuration_for_bundle(
            offer_durable_id, plan_durable_id, properties)

        if len(status.errors) > 0:
            return {
                'errors': status.errors,
                'result': status.job_result
            }
        else:
            return {
                'message': status.job_status.value,
                'result': status.job_result
            }

    def _get_sell_through_microsoft(self, offer_durable_id):
        sell_through_microsoft_enum_value = 'ListAndSell'
        setup = self._sdk.product_client.products_product_id_setup_get(offer_durable_id, self._get_access_token())
        return setup.selling_option == sell_through_microsoft_enum_value

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
        variants = get_combined_paged_results(lambda: self._sdk.variant_client.products_product_id_variants_get(offer_durable_id, self._get_access_token()))
        for v in variants:
            if v['resourceType'] == resource_type and v['state'] == 'Active':
                if v['externalID'] == plan_external_id:
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

    def _get_resource_tree(self, offer_durable_id):
        response = self._graph_api_client.get_resource_tree(offer_durable_id)
        return response['resources']
