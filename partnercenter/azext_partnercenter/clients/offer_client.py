# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long
# pylint: disable=protected-access
# pylint: disable=no-self-use

from azext_partnercenter.models.offer_setup import OfferSetup
from azext_partnercenter.models import (ListingContact, ListingUri, Offer, Listing, Resource)
from azext_partnercenter.vendored_sdks.v1.partnercenter.models import (
    MicrosoftIngestionApiModelsProductsAzureProduct,
    MicrosoftIngestionApiModelsCommonTypeValuePair,
    MicrosoftIngestionApiModelsProductsAzureProductSetup)
from ._base_client import BaseClient
from ._util import get_combined_paged_results


class OfferClient(BaseClient):

    def delete(self, offer_external_id):
        filter_expr = self._get_sdk_odata_filter_expression_by_external_offer_id(offer_external_id)
        products = self._sdk.product_client.products_get(self._get_access_token(), filter=filter_expr)

        if len(products.value) == 0:
            return None

        product_id = products.value[0].id
        self._sdk.product_client.products_product_id_delete(product_id, self._get_access_token())
        return None

    def list(self):
        results = get_combined_paged_results(lambda skip_token: self._sdk.product_client.products_get(
            self._get_access_token(),
            skip_token=skip_token))
        return list(map(self._map_product_to_offer, results))

    def create(self, offer_external_id, offer_alias, resource_type):
        external_id = MicrosoftIngestionApiModelsCommonTypeValuePair(
            type='AzureOfferID',
            value=offer_external_id)

        external_ids = [external_id]
        authorization = self._get_access_token()

        product = MicrosoftIngestionApiModelsProductsAzureProduct(external_ids=external_ids, name=offer_alias, resource_type=resource_type,
                                                                  id=offer_external_id, is_modular_publishing=True)

        product = self._sdk.product_client.products_post(authorization=authorization, microsoft_ingestion_api_models_products_azure_product=product)
        return self._map_product_to_offer(product)

    def get(self, offer_external_id):
        filter_expr = self._get_sdk_odata_filter_expression_by_external_offer_id(offer_external_id)
        products = self._sdk.product_client.products_get(self._get_access_token(), filter=filter_expr)

        if len(products.value) == 0:
            return None

        product = products.value[0]
        return self._map_product_to_offer(product)

    def publish(self, offer_external_id, target):
        """Publishes all draft changes for the offer to the target environment"""
        offer = self.get(offer_external_id)
        result = self._graph_api_client.publish_submission(target, offer.resource.durable_id)
        return result

    def _map_product_to_offer(self, product):
        return Offer(
            id=(next((x for x in product['externalIDs'] if x['type'] == "AzureOfferId"), None))['value'],
            alias=product.name,
            type=product.resource_type,
            resource=Resource(durable_id=product.id, type=product.resource_type)
        )

    def get_setup(self, offer_external_id):
        offer = self.get(offer_external_id)
        result = self._sdk.product_client.products_product_id_setup_get(offer.resource.durable_id, self._get_access_token())
        return self._map_setup(offer_external_id, result)

    def update_setup(self, parameters: OfferSetup):
        offer = self.get(parameters.id)

        channel_state = MicrosoftIngestionApiModelsCommonTypeValuePair(type='Reseller', value='Enabled' if parameters.reseller else 'Disabled')
        channel_states = [channel_state]

        kwargs = {
            'resource_type': 'AzureProductSetup',
            'enable_test_drive': parameters.test_drive,
            'selling_option': 'ListAndSell' if parameters.sell_through_microsoft else 'ListingOnly',
            'trial_uri': parameters.trial_uri,
            'channel_states': channel_states
        }

        # test drive option is only valid for VM and Azure App offer types
        if parameters.test_drive:
            kwargs['test_drive_type'] = 'AzureResourceManager'

        api_product_setup = MicrosoftIngestionApiModelsProductsAzureProductSetup(**kwargs)

        # TODO: check for failure, esure update occurred before trying to fetch latest setup instance
        self._sdk.product_client.products_product_id_setup_post(
            offer.resource.durable_id,
            self._get_access_token(),
            microsoft_ingestion_api_models_products_azure_product_setup=api_product_setup)

        offer_setup = self.get_setup(parameters.id)
        return offer_setup

    def _map_setup(self, offer_external_id, api_setup: MicrosoftIngestionApiModelsProductsAzureProductSetup) -> OfferSetup:
        reseller = (next((x for x in api_setup.channel_states if x['type'] == "Reseller"), None))['value'] == 'Enabled'
        sell_through_microsoft = (api_setup.selling_option == 'ListAndSell')

        offer_setup = OfferSetup(
            id=offer_external_id,
            reseller=reseller,
            test_drive=api_setup.enable_test_drive,
            sell_through_microsoft=sell_through_microsoft,
            trial_uri=api_setup.trial_uri,
        )
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
            offer.resource.durable_id, "Listing", self._api_client.configuration.access_token))

        # TODO: circle back on this as not sure what to do when multiple offer listings exist
        current_draft_module = next((b for b in branch_listings if not hasattr(b, 'variant_id')), None)

        if current_draft_module is None:
            return None

        instance_id = current_draft_module.current_draft_instance_id

        listings = get_combined_paged_results(
            lambda: self._sdk.listing_client.products_product_id_listings_get_by_instance_id_instance_i_dinstance_id_get(
                offer.resource.durable_id, instance_id, self._get_access_token()))

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
            offer_id=offer_external_id,
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
        return f'externalIDs/Any(i:i/type eq \'AzureOfferId\' and i/value eq \'{offer_id}\')'
