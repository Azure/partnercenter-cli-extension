# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from partnercenter.azext_partnercenter._util import (
    get_combined_paged_results, object_to_dict)
from partnercenter.azext_partnercenter.models import PlanListing
from partnercenter.azext_partnercenter.clients.offer_client import OfferClient
from partnercenter.azext_partnercenter.clients.plan_client import PlanClient
from partnercenter.azext_partnercenter.vendored_sdks.v1.partnercenter.apis import (
    ProductClient, VariantClient, BranchesClient)

from ._util import get_api_client


class PlanListingClient:
    def __init__(self, cli_ctx, *_):
        self._api_client = get_api_client(cli_ctx, *_)
        self._product_client = ProductClient(self._api_client)
        self._variant_client = VariantClient(self._api_client)
        self._branches_client = BranchesClient(self._api_client)
        self._offer_client = OfferClient(cli_ctx, *_)
        self._plan_client = PlanClient(cli_ctx, *_)

    def update_plan_listing(self, product_external_id, plan_listing: PlanListing):
        offer = self._offer_client.get_by_offer_id(product_external_id)
        product_id = offer.id
        plan = self._plan_client.find_by_external_id(product_id, plan_listing.external_id)
        print(f'plan - {plan}')
        
        if plan is None:
            # todo: throw exception and remove print
            print('plan is none')

        plan_id = plan.resource.id
        print(f'plan_id - {plan_id}')
       
        module = 'Listing'
        authorization = self._api_client.configuration.access_token
        listings = self._branches_client.products_product_id_branches_get_by_module_modulemodule_get(product_id, module, authorization)

        for listing in listings.value:
            print(f'listing - {listing}')
            if hasattr(listing, 'variant_id'):
                if listing.variant_id == plan_id:
                    print(f'found the plan - {listing}')
                    # get the listing by the branch instance




