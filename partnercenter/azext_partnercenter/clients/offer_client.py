# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from ._util import get_api_client
from partnercenter.azext_partnercenter._util import get_combined_paged_results
from partnercenter.azext_partnercenter.vendored_sdks.v1.partnercenter.apis import (
    ListingClient, ProductClient, BranchesClient)
from partnercenter.azext_partnercenter.vendored_sdks.v1.partnercenter.models import MicrosoftIngestionApiModelsBranchesBranch

class OfferClient():

    def __init__(self, cli_ctx, *_):
        self._api_client = get_api_client(cli_ctx, *_)
        self._product_client = ProductClient(self._api_client)
        self._branches_client = BranchesClient(self._api_client)
        self._listing_client = ListingClient(self._api_client)

    def get_by_offer_id(self, offer_id):
        filter_expr = self._get_filter_by_offer_id_expression(offer_id)
        response = self._product_client.products_get(self._get_access_token(), filter=filter_expr)

        if (len(response.value) == 0):
            return None

        return response.value[0]

    def get(self, resource_id):
        return self._product_client.products_product_id_get(resource_id,  self._api_client.configuration.access_token)
    

    def get_listing(self, resource_id):
        module = MicrosoftIngestionApiModelsBranchesBranch.allowed_values.get("module").get("LISTING")
        branch_listings = get_combined_paged_results(lambda : self._branches_client.products_product_id_branches_get_by_module_modulemodule_get(
                resource_id, module, self._api_client.configuration.access_token))

        current_draft_module = next((b for b in branch_listings if b.variant_id is not None), None)

        if current_draft_module is None:
            return None
        
        instance_id = current_draft_module.current_draft_instance_id

        listing = self._listing_client.products_product_id_listings_get_by_instance_id_instance_i_dinstance_id_get(
            resource_id, instance_id, self._get_access_token()
        )

        return
    
    def _get_access_token(self):
        return self._api_client.configuration.access_token
    

    def _get_filter_by_offer_id_expression(self, offer_id):
        """Gets the odata filter expression for filtering by Offer ID"""
        return "externalIDs/Any(i:i/type eq 'AzureOfferId' and i/value eq '{offer_id}')".format(offer_id=offer_id)

