# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from partnercenter.azext_partnercenter._util import (
    get_combined_paged_results, object_to_dict)
from partnercenter.azext_partnercenter.models import PlanListing
from partnercenter.azext_partnercenter.vendored_sdks.v1.partnercenter.model.microsoft_ingestion_api_models_listings_azure_listing import MicrosoftIngestionApiModelsListingsAzureListing
from partnercenter.azext_partnercenter.clients.offer_client import OfferClient
from partnercenter.azext_partnercenter.clients.plan_client import PlanClient
from partnercenter.azext_partnercenter.vendored_sdks.v1.partnercenter.apis import (
    ProductClient, VariantClient, BranchesClient, ListingClient)

from ._util import get_api_client


class PlanListingClient:
    def __init__(self, cli_ctx, *_):
        self._api_client = get_api_client(cli_ctx, *_)
        self._product_client = ProductClient(self._api_client)
        self._variant_client = VariantClient(self._api_client)
        self._branches_client = BranchesClient(self._api_client)
        self._listing_client = ListingClient(self._api_client)
        self._offer_client = OfferClient(cli_ctx, *_)
        self._plan_client = PlanClient(cli_ctx, *_)

    def get(self, product_external_id, plan_listing_external_id):
        return True

        
    def create_or_update(self, product_external_id, plan_listing: PlanListing):
        offer = self._offer_client.get(product_external_id)
        product_id = offer._resource.id
        plan = self._plan_client.find_by_external_id(product_id, plan_listing.external_id)
        
        if plan is None:
            # todo: throw exception and remove print
            print('plan is none')

        plan_id = plan.resource.id
       
        module = 'Listing'
        authorization = self._api_client.configuration.access_token
        branches = self._branches_client.products_product_id_branches_get_by_module_modulemodule_get(product_id, module, authorization)

        # todo: refactor to new method or use caching if we decide that
        for branch in branches.value:
            if hasattr(branch, 'variant_id'):
                if branch.variant_id == plan_id:
                    instance_id = branch.current_draft_instance_id
                    result = self._listing_client.products_product_id_listings_get_by_instance_id_instance_i_dinstance_id_get(product_id, instance_id, authorization)
                    listing = result.value[0]
                    
                    updated_listing = MicrosoftIngestionApiModelsListingsAzureListing(resource_type='AzureListing', description=plan_listing.description, short_description=plan_listing.short_description, odata_etag=listing.odata_etag)
                    update_result = self._listing_client.products_product_id_listings_listing_id_put(product_id, listing.id, authorization,  microsoft_ingestion_api_models_listings_azure_listing=updated_listing)
                    # print(f'update_result - {update_result}')
                    return update_result.to_dict()

    def get_plan_listing(self, product_external_id, plan_external_id):
        product_listing_branches = self.get_product_listing_branches(product_external_id)
        if not product_listing_branches:
            return None

        product = self._offer_client.get(product_external_id)
        if product is None:
            return None

        product_id = product._resource.id

        plan = self._plan_client.find_by_external_id(product_id, plan_external_id)
        if plan is None:
            return None

        plan_id = plan.resource.id

        for branch in product_listing_branches:
            if branch.variant_id == plan_id:
                instance_id = branch.current_draft_instance_id
                authorization = self._api_client.configuration.access_token
                result = self._listing_client.products_product_id_listings_get_by_instance_id_instance_i_dinstance_id_get(product_id, instance_id, authorization)
                listing = result.value[0]
                return listing

        return None

    def get_product_listing_branches(self, product_external_id):
        offer = self._offer_client.get(product_external_id)
        product_id = offer._resource.id
        
        module = 'Listing'
        authorization = self._api_client.configuration.access_token
        branches = self._branches_client.products_product_id_branches_get_by_module_modulemodule_get(product_id, module, authorization)

        return list(filter(lambda x: hasattr(x, 'variant_id'), branches.value))



