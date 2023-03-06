# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long
# pylint: disable=protected-access

from azext_partnercenter.models import (Plan, Resource)
from azext_partnercenter.clients import OfferClient
from azext_partnercenter.vendored_sdks.v1.partnercenter.models import ProductsProductIDVariantsGetRequest
from ._util import get_combined_paged_results
from ._base_client import BaseClient


class PlanClient(BaseClient):
    def __init__(self, cli_ctx, *_):
        super().__init__(cli_ctx, *_)
        self._offer_client = OfferClient(cli_ctx, *_)

    def create(self, offer_external_id, plan_external_id, name, subtype=None):
        resource_type = "AzureSkuVariant"
        offer = self._offer_client.get(offer_external_id)
        product_id = offer._resource.durable_id

        prod_var_req = ProductsProductIDVariantsGetRequest(resource_type=resource_type, friendly_name=name, external_id=plan_external_id)
        if subtype:
            prod_var_req['SubType'] = subtype
        result = self._sdk.variant_client.products_product_id_variants_post(product_id=product_id,
                                                                            authorization=self._api_client.configuration.access_token,
                                                                            products_product_id_variants_get_request=prod_var_req)
        return Plan(
            id=result.external_id,
            name=result.friendly_name,
            offer_id=offer_external_id,
            state=result.state,
            cloud_availabilities=result.cloud_availabilities,
            resource=Resource(durable_id=result.id, type=result.resource_type),
            subtype=subtype
        )

    def get(self, offer_external_id, plan_external_id):
        return self.find_by_external_id(offer_external_id, plan_external_id)

    def list(self, offer_external_id):
        offer = self._offer_client.get(offer_external_id)
        if offer is None:
            return []

        offer_durable_id = offer._resource.durable_id
        variants = get_combined_paged_results(lambda: self._sdk.variant_client.products_product_id_variants_get(
            offer_durable_id,
            self._api_client.configuration.access_token))

        items = []

        for variant in variants:
            if "externalID" in variant:
                item = Plan(
                    id=variant['externalID'],
                    name=variant['friendlyName'],
                    offer_id=offer_external_id,
                    state=variant['state'],
                    cloud_availabilities=variant['cloudAvailabilities'],
                    resource=Resource(durable_id=variant['id'], type=variant['resourceType'])
                )
                items.append(item)

        return items

    def find_by_external_id(self, offer_external_id, plan_external_id):
        plans = self.list(offer_external_id)
        return next((plan for plan in plans if plan.id == plan_external_id), None)

    # TODO: remove get_listing
    def get_listing(self, offer_external_id, plan_external_id):
        offer = self._offer_client.get(offer_external_id)
        offer_durable_id = offer._resource.durable_id
        branches = self._sdk.branches_client.products_product_id_branches_get_by_module_modulemodule_get(offer_durable_id, 'Listing',
                                                                                                         self._get_access_token())

        plan = self.find_by_external_id(offer_external_id, plan_external_id)
        branch_listing = next((b for b in branches if b['variantID'] == plan._resource.durable_id), None)
        instance_id = branch_listing['currentDraftInstanceID']

        listing = self._sdk.listing_client.products_product_id_listings_get_by_instance_id_instance_i_dinstance_id_get(
            offer_durable_id, instance_id, self._get_access_token()
        )
        return {
            'name': listing['title'],
            'shortDescription': listing['shortDescription'],
            'description': listing['description']
        }

    # TODO: remove if automated tests show this is unneeded
    def _get(self, offer_durable_id, plan_durable_id):
        """Internal get of the plan"""
        product = self._sdk.product_client.products_product_id_get(offer_durable_id, self._api_client.configuration.access_token)
        variant = self._sdk.variant_client.products_product_id_variants_variant_id_get(
            offer_durable_id,
            plan_durable_id,
            self._api_client.configuration.access_token)

        item = Plan(
            id=variant['externalID'],
            name=variant['friendlyName'],
            offer_id=product['externalIDs'][0]['value'],
            state=variant['state'],
            cloud_availabilities=variant['cloudAvailabilities'],
            resource=Resource(id=variant['id'], type=variant['resourceType'])
        )
        return item

    def delete(self, offer_external_id, plan_external_id):
        offer = self._offer_client.get(offer_external_id)

        if offer is None:
            return

        plan = self.find_by_external_id(offer_external_id, plan_external_id)

        if plan is None:
            return

        offer_durable_id = offer._resource.durable_id
        plan_resource_id = plan._resource.durable_id
        self._sdk.variant_client.products_product_id_variants_variant_id_delete(offer_durable_id, plan_resource_id, self._api_client.configuration.access_token, async_req=True)
