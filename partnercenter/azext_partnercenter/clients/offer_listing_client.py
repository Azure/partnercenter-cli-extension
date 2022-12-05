# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long
# pylint: disable=protected-access
# pylint: disable=no-self-use

from azext_partnercenter.models import ListingContact, Listing, ListingUri, Resource
from azext_partnercenter.vendored_sdks.v1.partnercenter.models import (
    MicrosoftIngestionApiModelsListingsAzureListing,
    MicrosoftIngestionApiModelsListingsListingContact,
    MicrosoftIngestionApiModelsListingsListingUri)
from azext_partnercenter.clients import OfferClient, PlanClient
from ._base_client import BaseClient


class OfferListingClient(BaseClient):
    def __init__(self, cli_ctx, *_):
        super().__init__(cli_ctx, *_)
        self._offer_client = OfferClient(cli_ctx, *_)
        self._plan_client = PlanClient(cli_ctx, *_)

    def get_plan_listing(self, product_external_id, plan_external_id):
        product_listing_branches = self._get_product_listing_branches(product_external_id)
        if not product_listing_branches:
            return None
        product = self._offer_client.get(product_external_id)
        if product is None:
            return None
        product_id = product._resource.durable_id
        plan = self._plan_client.find_by_external_id(product_external_id, plan_external_id)
        if plan is None:
            return None
        plan_durable_id = plan._resource.durable_id

        branch = next(filter(lambda b: b.variant_id == plan_durable_id, product_listing_branches), None)
        if branch is None:
            return None

        instance_id = branch.current_draft_instance_id
        result = self._sdk.listing_client.products_product_id_listings_get_by_instance_id_instance_i_dinstance_id_get(
            product_id,
            instance_id,
            self._get_access_token())
        listing = result.value[0]
        return Listing(
            description=listing.description,
            title=listing.title,
            summary=listing.summary if hasattr(listing, 'summary') else '',
            language_code=listing.language_code if hasattr('language_code', 'summary') else '',
            short_description=listing.short_description if hasattr('short_description', 'summary') else '',
            contacts=list(map(lambda c: ListingContact(**c.to_dict()), listing.listing_contacts)),
            uris=list(map(lambda c: ListingUri(**c.to_dict()), listing.listing_uris)),
            odata_etag=listing.odata_etag,
            resource=Resource(id=listing.id, type=listing.resource_type)
        )

    def create_or_update(self, offer_id, listing_model: Listing, plan_external_id=None):
        offer = self._offer_client.get(offer_id)
        if offer is None:
            return None
        product_id = offer._resource.durable_id

        listing = None
        if plan_external_id is None:
            listing = self._offer_client.get_listing(offer_id)
        else:
            listing = self.get_plan_listing(offer_id, plan_external_id)

        if listing is None:
            return None

        listing_id = listing._resource.durable_id

        listing_contacts = self._get_api_listing_contacts(listing_model)
        listing_uris = self._get_api_listing_uris(listing_model)

        updated_listing = MicrosoftIngestionApiModelsListingsAzureListing(
            resource_type='AzureListing',
            description=listing_model.description,
            title=listing_model.title,
            summary=listing_model.summary,
            short_description=listing_model.short_description,
            odata_etag=listing.odata_etag,
            listing_uris=listing_uris,
            listing_contacts=listing_contacts)
        update_result = self._sdk.listing_client.products_product_id_listings_listing_id_put(
            product_id,
            listing_id,
            self._get_access_token(),
            microsoft_ingestion_api_models_listings_azure_listing=updated_listing)
        return Listing(
            description=update_result.description,
            title=update_result.title,
            summary=update_result.summary,
            language_code=update_result.language_code,
            short_description=update_result.short_description,
            contacts=list(map(lambda c: ListingContact(**c.to_dict()), update_result.listing_contacts)),
            uris=list(map(
                lambda c: ListingUri(type=c.type, subtype=c.subtype, uri=c.uri, display_text=c.display_text), update_result.listing_uris)
            ),
            odata_etag=update_result.odata_etag,
            resource=Resource(id=update_result.id, type=update_result.resource_type)
        )

    def _get_api_listing_uris(self, listing_model: Listing):
        return list(map(lambda u: MicrosoftIngestionApiModelsListingsListingUri(
            type=u.type if u.type is not None else '',
            subtype=u.subtype if u.subtype is not None else '',
            display_text=u.display_text if u.display_text is not None else '',
            uri=u.uri if u.uri is not None else ''),
            listing_model.uris))

    def _get_api_listing_contacts(self, listing_model: Listing):
        return list(map(lambda c: MicrosoftIngestionApiModelsListingsListingContact(
            type=c.type,
            email=c.email,
            name=c.name,
            phone=c.phone,
            uri=c.uri),
            listing_model.contacts))

    def delete_offer_listing(self, product_external_id):
        product = self._offer_client.get(product_external_id)
        if product is None:
            return None
        product_id = product._resource.durable_id

        listing = self._offer_client.get_listing(product_external_id)
        if listing is None:
            return None
        listing_id = listing._resource.durable_id

        return self._sdk.listing_client.products_product_id_listings_listing_id_delete(product_id, listing_id, self._get_access_token())

    def delete_listing_contact(self, product_external_id, contact: ListingContact):
        listing = self._offer_client.get_listing(product_external_id)
        try:
            listing.contacts.remove(contact)
        except ValueError:
            return None

        return self.create_or_update(product_external_id, listing)

    def delete_listing_uri(self, product_external_id, uri: ListingUri):
        listing = self._offer_client.get_listing(product_external_id)
        try:
            listing.uris.remove(uri)
        except ValueError:
            return None

        return self.create_or_update(product_external_id, listing)

    def delete_latest_listing_uri(self, product_external_id):
        listing = self._offer_client.get_listing(product_external_id)
        if len(listing.uris) > 0:
            del listing.uris[0]
        return self.create_or_update(product_external_id, listing)

    def get_listing(self, product_external_id):
        return self._offer_client.get_listing(product_external_id)

    def _get_product_listing_branches(self, product_external_id):
        offer = self._offer_client.get(product_external_id)
        product_id = offer._resource.durable_id

        module = 'Listing'
        branches = self._sdk.branches_client.products_product_id_branches_get_by_module_modulemodule_get(
            product_id, module, self._get_access_token())

        return list(filter(lambda x: hasattr(x, 'variant_id'), branches.value))
