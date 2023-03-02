# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long
# pylint: disable=protected-access

from azext_partnercenter.models import PlanListing
from azext_partnercenter.clients import (OfferClient, PlanClient)
from ._util import get_combined_paged_results
from ._base_client import BaseClient


class PlanListingClient(BaseClient):
    def __init__(self, cli_ctx, *_):
        super().__init__(cli_ctx, *_)
        self._offer_client = OfferClient(cli_ctx, *_)
        self._plan_client = PlanClient(cli_ctx, *_)

    def get(self, offer_external_id, plan_external_id) -> PlanListing:
        """Gets the listing using the external offer and plan ID."""

        offer = self._offer_client.get(offer_external_id)
        listing = self._get_listing_instance(offer, plan_external_id)

        if listing is None:
            return None

        return PlanListing(
            offer_id=offer_external_id,
            id=plan_external_id,
            name=listing.title,
            summary=(listing.short_description if hasattr(listing, 'short_description') else ''),
            description=(listing.description if hasattr(listing, 'description') else '')
        )

    def update(self, offer_external_id, plan_external_id, parameters: PlanListing):
        offer = self._offer_client.get(offer_external_id)
        updated_listing = self._get_listing_instance(offer, plan_external_id)

        updated_listing.title = parameters.name
        updated_listing.short_description = parameters.summary
        updated_listing.description = parameters.description

        self._sdk.listing_client.products_product_id_listings_listing_id_put(
            offer.resource.durable_id, updated_listing.id, self._get_access_token(),
            microsoft_ingestion_api_models_listings_azure_listing=updated_listing)

        return PlanListing(
            offer_id=offer_external_id,
            id=plan_external_id,
            name=updated_listing.title,
            summary=updated_listing.short_description,
            description=updated_listing.description
        )

    def _get_listing_instance(self, offer, plan_external_id):
        offer_durable_id = offer.resource.durable_id

        branches = get_combined_paged_results(lambda: self._sdk.branches_client.products_product_id_branches_get_by_module_modulemodule_get(
                                              offer_durable_id, "Listing", self._get_access_token()))

        plan = self._plan_client.get(offer.id, plan_external_id)
        branch_listing = next((b for b in branches if hasattr(b, 'variant_id') and b.variant_id == plan._resource.durable_id), None)

        if branch_listing is None:
            return None

        instance_id = branch_listing.current_draft_instance_id

        listing = self._sdk.listing_client.products_product_id_listings_get_by_instance_id_instance_i_dinstance_id_get(
            offer_durable_id, instance_id, self._get_access_token()
        )
        return listing.value[0]
