# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from partnercenter.azext_partnercenter._util import (
    get_combined_paged_results, object_to_dict)
from partnercenter.azext_partnercenter.models import PlanListing, ListingContact
from partnercenter.azext_partnercenter.models.listing_uri import ListingUri
from partnercenter.azext_partnercenter.models.resource import Resource
from partnercenter.azext_partnercenter.vendored_sdks.v1.partnercenter.model.microsoft_ingestion_api_models_listings_azure_listing import MicrosoftIngestionApiModelsListingsAzureListing
from partnercenter.azext_partnercenter.vendored_sdks.v1.partnercenter.model.microsoft_ingestion_api_models_listings_listing_contact import MicrosoftIngestionApiModelsListingsListingContact
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
            # todo: throw exception
            return None

        plan_id = plan.resource.id
       
        module = 'Listing'
        authorization = self._api_client.configuration.access_token

        branches = self._branches_client.products_product_id_branches_get_by_module_modulemodule_get(product_id, module, authorization)
        if not branches:
            # todo: throw exception
            return None
        
        variant_branches = list(filter(lambda b: hasattr(b, 'variant_id'), branches.value))
        if not variant_branches:
            # todo: throw exception
            return None

        branch = next(filter(lambda b: b.variant_id == plan_id, variant_branches), None)
        if branch is None:
            # todo: raise exception
            return None
        
        instance_id = branch.current_draft_instance_id
        result = self._listing_client.products_product_id_listings_get_by_instance_id_instance_i_dinstance_id_get(product_id, instance_id, authorization)
        listing = result.value[0]
        listing_contcats = self._get_api_listing_contacts(plan_listing)
        updated_listing = MicrosoftIngestionApiModelsListingsAzureListing(
                        resource_type='AzureListing', 
                        description=plan_listing.description, 
                        short_description=plan_listing.short_description, 
                        odata_etag=listing.odata_etag, 
                        listing_contacts=listing_contcats)
                    
        update_result = self._listing_client.products_product_id_listings_listing_id_put(
                        product_id, 
                        listing.id, 
                        authorization,  
                        microsoft_ingestion_api_models_listings_azure_listing=updated_listing)

        return PlanListing(
                        description=update_result.description,
                        language_code=update_result.language_code,
                        short_description=update_result.short_description,
                        contacts=list(map(lambda c : ListingContact(**c.to_dict()), update_result.listing_contacts)),
                        uris=list(map(lambda c : ListingUri(**c.to_dict()), update_result.listing_uris)),
                        resource=Resource(id=update_result.id, type=update_result.resource_type)        
        )

    def _get_api_listing_contacts(self, plan_listing: PlanListing):
        return list(map(lambda c: MicrosoftIngestionApiModelsListingsListingContact(
            type=c.type, 
            email=c.email, 
            name=c.name, 
            phone=c.phone, 
            uri=c.uri), 
            plan_listing.contacts))
        
        
    def delete_plan_listing_contact(self, product_external_id, plan_external_id, contact: ListingContact):
        plan_listing = self.get_plan_listing(product_external_id, plan_external_id)
        
        try:
            plan_listing.contacts.remove(contact)
        except ValueError:
            return None

        plan_listing.external_id = plan_external_id
        return self.create_or_update(product_external_id, plan_listing)


    def get_plan_listing(self, product_external_id, plan_external_id):
        product_listing_branches = self._get_product_listing_branches(product_external_id)
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

        branch = next(filter(lambda b: b.variant_id == plan_id, product_listing_branches), None)
        if branch is None:
            return None
        
        instance_id = branch.current_draft_instance_id

        result = self._listing_client.products_product_id_listings_get_by_instance_id_instance_i_dinstance_id_get(
            product_id, 
            instance_id,
             self._get_authorication_token())

        listing = result.value[0]

        return PlanListing(
          #  title=listing.title,
          #  summary=listing.summary,
            description=listing.description,
            language_code=listing.language_code,
            short_description=listing.short_description,
            #getting_started_instructions=listing.getting_started_instructions,
            #keywords=listing.keywords,
            contacts=list(map(lambda c : ListingContact(**c.to_dict()), listing.listing_contacts)),
            uris=list(map(lambda c : ListingUri(**c.to_dict()), listing.listing_uris)),
            resource=Resource(id=listing.id, type=listing.resource_type)
        )


    def _get_authorication_token(self):
        return self._api_client.configuration.access_token

    def _get_product_listing_branches(self, product_external_id):
        offer = self._offer_client.get(product_external_id)
        product_id = offer._resource.id
        
        module = 'Listing'
        authorization = self._api_client.configuration.access_token
        branches = self._branches_client.products_product_id_branches_get_by_module_modulemodule_get(product_id, module, authorization)

        return list(filter(lambda x: hasattr(x, 'variant_id'), branches.value))



