# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from partnercenter.azext_partnercenter._util import get_combined_paged_results
from partnercenter.azext_partnercenter.models import (ListingContact,
                                                      ListingUri, Offer,
                                                      PlanListing, Resource)
from partnercenter.azext_partnercenter.vendored_sdks.v1.partnercenter.apis import (
    BranchesClient, ListingClient, ProductClient)

from ._util import get_api_client


class OfferClient():

    def __init__(self, cli_ctx, *_):
        self._api_client = get_api_client(cli_ctx, *_)
        self._product_client = ProductClient(self._api_client)
        self._branches_client = BranchesClient(self._api_client)
        self._listing_client = ListingClient(self._api_client)

    
    def list(self):
        results = get_combined_paged_results(lambda skip_token: self._product_client.products_get(self._get_access_token(), skip_token=skip_token))
        return list(map(lambda product : Offer(
                id=(next((x for x in product.externalIDs if x['type'] == "AzureOfferId"), None))['value'],
                name=product.name,
                resource=Resource(id=product.id, type=product.resource_type)
            ), results))

    def get(self, offer_external_id):
        filter_expr = self._get_filter_by_offer_id_expression(offer_external_id)
        products = self._product_client.products_get(self._get_access_token(), filter=filter_expr)

        if (len(products.value) == 0):
            return None

        product = products.value[0]

        return Offer(
            id=(next((x for x in product.externalIDs if x['type'] == "AzureOfferId"), None))['value'],
            name=product.name,
            resource=Resource(id=product.id, type=product.resource_type)
        )

    def get_listing(self, offer_external_id):
        offer = self.get(offer_external_id)

        if offer is None:
            return None
        
        branch_listings = get_combined_paged_results(lambda : self._branches_client.products_product_id_branches_get_by_module_modulemodule_get(
                offer._resource.id, "Listing", self._api_client.configuration.access_token))

        # TODO: circle back on this as not sure what to do when multiple offer listings exist
        current_draft_module = next((b for b in branch_listings if not hasattr(b, 'variant_id')), None)

        if current_draft_module is None:
            return None
        
        instance_id = current_draft_module.current_draft_instance_id

        listings = get_combined_paged_results(lambda : 
            self._listing_client.products_product_id_listings_get_by_instance_id_instance_i_dinstance_id_get(
            offer._resource.id, instance_id, self._get_access_token()))
        
        # TODO: there should only be 1 active listing (that we can confirm as of now)
        if len(listings) == 0:
            return None

        listing = listings[0]
        
        return PlanListing(
            title=listing.title,
            summary=listing.summary,
            description=listing.description,
            language_code=listing.language_code,
            short_description=listing.short_description,
            getting_started_instructions=listing.getting_started_instructions,
            keywords=listing.keywords,
            contacts=list(map(lambda c : ListingContact(**c.to_dict()), listing.listing_contacts)),
            uris=list(map(lambda c : ListingUri(**c.to_dict()), listing.listing_uris)),
            resource=Resource(id=listing.id, type=listing.resource_type)
        )
    
    def _get_access_token(self):
        return self._api_client.configuration.access_token
    

    def _get_filter_by_offer_id_expression(self, offer_id):
        """Gets the odata filter expression for filtering by Offer ID"""
        return "externalIDs/Any(i:i/type eq 'AzureOfferId' and i/value eq '{offer_id}')".format(offer_id=offer_id)
