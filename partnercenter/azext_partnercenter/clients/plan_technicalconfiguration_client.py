# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long
# pylint: disable=protected-access
# pylint: disable=no-else-return

import os
from xml.dom.expatbuilder import FILTER_ACCEPT
from knack.util import CLIError
from azext_partnercenter.clients import OfferClient, PlanClient
from azext_partnercenter.clients._base_client import BaseClient
from azext_partnercenter.vendored_sdks.v1.partnercenter.model.microsoft_ingestion_api_models_packages_azure_package import (
    MicrosoftIngestionApiModelsPackagesAzurePackage)
from azext_partnercenter.vendored_sdks.production_ingestion.models import (ContainerCnabPlanTechnicalConfigurationProperties)
from ._util import get_combined_paged_results, upload_media


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
        elif variant_package_branch.product.resource_type == 'AzureApplication':
            print('you are a failure')
            technical_configuration= self._get_azure_application_plan_technical_configuration(offer_durable_id, plan_durable_id)
            print('technical_configuration: ')
            print(technical_configuration)
        else:
            technical_configuration = self._get_plan_technical_configuration(variant_package_branch.product.id, variant_package_branch.variant_id)
            technical_configuration['planId'] = plan_external_id

        print("about to return technical_configuration")
        return technical_configuration

    def delete_cnab_reference(self, offer_external_id, plan_external_id, repository_name, tag):
        technical_configuration = self.get(offer_external_id, plan_external_id)
        cnab_reference_index = -1

        for index, ref in enumerate(technical_configuration.cnab_references):
            # match repo and tab name for now. if more is required, we can add them here
            if ref['repositoryName'] == repository_name and ref['tag'] == tag:
                cnab_reference_index = index
                break

        if cnab_reference_index != -1:
            del technical_configuration.cnab_references[cnab_reference_index]

        result = self._update_technical_configuration_properties(offer_external_id, plan_external_id, technical_configuration)
        return result

    def add_bundle(self, offer_external_id, plan_external_id, properties=ContainerCnabPlanTechnicalConfigurationProperties | None):
        result = self._update_technical_configuration_properties(offer_external_id, plan_external_id, properties)
        return result

    def add_managed_app_bundle(self, offer_external_id, plan_external_id, package_path):
        variant_package_branch = self._get_variant_package_branch(offer_external_id, plan_external_id)
        offer_durable_id = variant_package_branch.product.id
        plan_durable_id = variant_package_branch.variant_id
        file_name = os.path.basename(package_path)
        print(f"file_name is {file_name}")

        input_package = MicrosoftIngestionApiModelsPackagesAzurePackage(
            resource_type='AzureApplicationPackage',
            file_name=file_name
        )

        output_package = self._sdk.package_client.products_product_id_packages_post(
            offer_durable_id,
            self._get_access_token(),
            microsoft_ingestion_api_models_packages_azure_package=input_package)
        print(f"package post result is {output_package}")

        upload_result = upload_media(package_path, output_package.file_sas_uri)
        print(f"The upload_result is {upload_result}")

        output_package.state = "Uploaded"

        updated_package = self._sdk.package_client.products_product_id_packages_package_id_put(
            offer_durable_id,
            output_package.id,
            self._get_access_token(),
            microsoft_ingestion_api_models_packages_azure_package=output_package
        )
        print(f"The modified package is {updated_package}")
        return updated_package

    def _update_technical_configuration_properties(self, offer_external_id, plan_external_id, properties=ContainerCnabPlanTechnicalConfigurationProperties | None):
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

    def _get_azure_application_plan_technical_configuration(self, offer_durable_id, plan_durable_id):
        technical_configuration = {}
        print(f"inside _get_azure_application_plan_technical_configuration with a {offer_durable_id} and {plan_durable_id}")
        product_id = '246aed98-915f-4706-b0e8-6d8f2a9a8fdc'
        package_configuration_id = 'dffef988-51de-43fd-af92-a2388252eb4d'
        package_configuration = self._sdk.package_configuration_client.products_product_id_packageconfigurations_package_configuration_id_get(product_id, package_configuration_id, self._get_access_token())
        print('package_configuration : ')
        print(package_configuration)
        return package_configuration


    def _get_plan_technical_configuration(self, offer_durable_id, plan_durable_id):
        """Since we don't know what type of technical plan this will be for now unless we map the types to the schema, this gets any technical configuration type"""

        print('offer_durable_id:' + offer_durable_id)
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
        import json
        response = self._graph_api_client.get_resource_tree(offer_durable_id)

        # show the json
        formatted_json = json.dumps(response, indent=4)
        print(formatted_json)

        return response['resources']
