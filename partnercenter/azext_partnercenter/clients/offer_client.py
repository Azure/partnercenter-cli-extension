# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long
# pylint: disable=protected-access
# pylint: disable=no-self-use

from azext_partnercenter.models.offer_setup import OfferSetup
from azext_partnercenter._util import get_combined_paged_results
from azext_partnercenter.models import (ListingContact, ListingUri, Offer, Listing, Resource)
from azext_partnercenter.vendored_sdks.v1.partnercenter.models import (
    MicrosoftIngestionApiModelsProductsAzureProduct,
    MicrosoftIngestionApiModelsCommonTypeValuePair,
    MicrosoftIngestionApiModelsProductsAzureProductSetup)
from ._base_client import BaseClient


class OfferClient(BaseClient):

    def __init__(self, cli_ctx, *_):
        super(OfferClient, self).__init__(cli_ctx, *_)

    def delete(self, offer_external_id):
        filter_expr = self._get_sdk_odata_filter_expression_by_external_offer_id(offer_external_id)
        products = self._sdk.product_client.products_get(self._get_access_token(), filter=filter_expr)

        if len(products.value) == 0:
            return

        product_id = products.value[0].id
        response = self._sdk.product_client.products_product_id_delete(product_id, self._get_access_token())

        return response

    def list(self):
        results = get_combined_paged_results(lambda skip_token: self._sdk.product_client.products_get(
            self._get_access_token(),
            skip_token=skip_token))

        return list(map(lambda product: Offer(
            id=(next((x for x in product.externalIDs if x['type'] == "AzureOfferId"), None))['value'],
            name=product.name,
            type=product.resource_type,
            resource=Resource(durable_id=product.id, type=product.resource_type)
        ), results))

    def create(self, offer_external_id, offer_alias, resource_type):
        external_id = MicrosoftIngestionApiModelsCommonTypeValuePair(
            type='AzureOfferID',
            value=offer_external_id)

        external_ids = [external_id]
        authorization = self._get_access_token()

        product = MicrosoftIngestionApiModelsProductsAzureProduct(external_ids=external_ids, name=offer_alias, resource_type=resource_type,
                                                                  id=offer_external_id, is_modular_publishing=True)

        product = self._sdk.product_client.products_post(authorization=authorization, microsoft_ingestion_api_models_products_azure_product=product)

        return Offer(
            id=(next((x for x in product.externalIDs if x['type'] == "AzureOfferId"), None))['value'],
            name=product.name,
            type=product.resource_type,
            resource=Resource(durable_id=product.id, type=product.resource_type)
        )

    def get(self, offer_external_id):
        filter_expr = self._get_sdk_odata_filter_expression_by_external_offer_id(offer_external_id)
        products = self._sdk.product_client.products_get(self._get_access_token(), filter=filter_expr)

        if len(products.value) == 0:
            return None

        product = products.value[0]

        return Offer(
            id=(next((x for x in product.externalIDs if x['type'] == "AzureOfferId"), None))['value'],
            name=product.name,
            type=product.resource_type,
            resource=Resource(durable_id=product.id, type=product.resource_type)
        )

    # def delete(self, offer_external_id):
    #    offer = self.get(offer_external_id)
    #    return self._sdk.product_client.products_product_id_delete(offer._resource.durable_id, self._get_access_token())

    def get_setup(self, offer_external_id):
        offer = self.get(offer_external_id)
        result = self._sdk.product_client.products_product_id_setup_get(offer._resource.durable_id, self._get_access_token())
        return self._map_setup(result)

    def create_setup(self, offer_external_id, test_drive_enabled: bool, reseller_enabled: bool, selling_option, trial_uri):
        offer = self.get(offer_external_id)

        enabled_value = 'Enabled'
        if not reseller_enabled:
            enabled_value = 'Disabled'

        resource_type = 'AzureProductSetup'

        channel_state = MicrosoftIngestionApiModelsCommonTypeValuePair(type='Reseller', value=enabled_value)
        channel_states = [channel_state]
        api_product_setup = MicrosoftIngestionApiModelsProductsAzureProductSetup(
            resource_type=resource_type,
            enable_test_drive=test_drive_enabled,
            selling_option=selling_option,
            trial_uri=trial_uri,
            channel_states=channel_states)

        result = self._sdk.product_client.products_product_id_setup_post(
            offer._resource.durable_id,
            self._get_access_token(),
            microsoft_ingestion_api_models_products_azure_product_setup=api_product_setup)

        return result

    def _map_setup(self, api_setup: MicrosoftIngestionApiModelsProductsAzureProductSetup) -> OfferSetup:
        channel_states = list(map(lambda x: self._map_channel_state(x), api_setup.channel_states))
        offer_setup = OfferSetup(
            sell_through_microsoft=(True if api_setup.selling_option == 'ListAndSell' else False),
            trial_uri=api_setup.get('trial_uri'),
            enable_test_drive=api_setup.enable_test_drive,
            channel_states=channel_states)
        return offer_setup

    def _map_channel_state(self, channel_state):
        return {
            'type': channel_state.type,
            'value': channel_state.value
        }

    def get_listing(self, offer_external_id):
        offer = self.get(offer_external_id)

        if offer is None:
            return None

        branch_listings = get_combined_paged_results(lambda: self._sdk.branches_client.products_product_id_branches_get_by_module_modulemodule_get(
            offer._resource.durable_id, "Listing", self._api_client.configuration.access_token))

        # TODO: circle back on this as not sure what to do when multiple offer listings exist
        current_draft_module = next((b for b in branch_listings if not hasattr(b, 'variant_id')), None)

        if current_draft_module is None:
            return None

        instance_id = current_draft_module.current_draft_instance_id

        listings = get_combined_paged_results(
            lambda: self._sdk.listing_client.products_product_id_listings_get_by_instance_id_instance_i_dinstance_id_get(
                offer._resource.durable_id, instance_id, self._get_access_token()))

        # TODO: there should only be 1 active listing (that we can confirm as of now)
        if len(listings) == 0:
            return None

        listing = listings[0]

        return Listing(
            title=listing.title if hasattr(listing, 'title') else '',
            summary=listing.summary if hasattr(listing, 'summary') else '',
            description=listing.description if hasattr(listing, 'description') else '',
            language_code=listing.language_code if hasattr(listing, 'language_code') else '',
            short_description=listing.short_description if hasattr(listing, 'short_description') else '',
            getting_started_instructions=listing.getting_started_instructions if hasattr(listing, 'getting_started_instructions') else '',
            # keywords=listing.keywords,
            odata_etag=listing.odata_etag,
            contacts=list(map(lambda c: ListingContact(**c.to_dict()), listing.listing_contacts)),
            uris=list(map(lambda c: ListingUri(**c.to_dict()), listing.listing_uris)),
            resource=Resource(durable_id=listing.id, type=listing.resource_type)
        )

    def _get_sdk_product_by_external_offer_id(self, offer_external_id):
        """Package Internal helper method to get the SDK product object by Offer ID"""
        filter_expr = self._get_sdk_odata_filter_expression_by_external_offer_id(offer_external_id)
        products = self._sdk.product_client.products_get(self._get_access_token(), filter=filter_expr)

        if products is None or len(products.value) == 0:
            return None

        return products.value[0]

    def _get_sdk_odata_filter_expression_by_external_offer_id(self, offer_id):
        """Gets the odata filter expression for filtering by Offer ID found in externalIDs collection"""
        return "externalIDs/Any(i:i/type eq 'AzureOfferId' and i/value eq '{offer_id}')".format(offer_id=offer_id)
