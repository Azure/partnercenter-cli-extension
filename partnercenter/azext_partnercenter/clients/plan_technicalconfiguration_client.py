# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azext_partnercenter.clients import OfferClient, PlanClient
from azext_partnercenter.clients._base_client import BaseClient

from partnercenter.azext_partnercenter.vendored_sdks.v1.partnercenter.exceptions import \
    NotFoundException

from ._util import (get_combined_paged_results, object_to_dict)
from knack.util import CLIError

class PlanTechnicalConfigurationClient(BaseClient):
    PACKAGE_MODULE = "Package"

    def __init__(self, cli_ctx, *_):
        super(PlanTechnicalConfigurationClient, self).__init__(cli_ctx, *_)

        self._offer_client = OfferClient(cli_ctx, *_)
        self._plan_client = PlanClient(cli_ctx, *_)

    def get(self, offer_external_id, plan_external_id):
        product = self._offer_client._get_sdk_product_by_external_offer_id(offer_external_id)

        if product is None:
            # TODO: determine if throwing CLIError is better here
            return None
        
        variants = get_combined_paged_results(lambda : self._sdk.variant_client.products_product_id_variants_get(product.id, self._get_access_token()))
        variant = next((v for v in variants if v['externalID'] == plan_external_id), None)

        if variant is None:
            raise CLIError(f'Plan not found for "{plan_external_id}"')
 
        branches = self._sdk.branches_client.products_product_id_branches_get_by_module_modulemodule_get(
                                             product.id, self.PACKAGE_MODULE, self._get_access_token())
        if len(branches.value) == 0:
            return None
        
        variant_package_branch = next((b for b in branches.value if hasattr(b, 'variant_id') and b.variant_id == variant['id']), None)

        if variant_package_branch is None:
            raise CLIError(f'Technical Configuration not found for Plan ID "{plan_external_id}"')
        
        try:
            self._sdk.package_client.products_product_id_packages_get_endpoint.settings['endpoint_path'] += f"/getByInstanceID(instanceID={plan_external_id})"
            # print(object_to_dict(self._sdk.package_client.products_product_id_packages_get_endpoint.settings))

            package = self._sdk.package_client.products_product_id_packages_get(product.id, self._get_access_token())
            return package
        except NotFoundException:
            pass

        return None