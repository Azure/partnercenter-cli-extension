# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


from ._util import get_api_client
from partnercenter.azext_partnercenter._util import (
    get_combined_paged_results, object_to_dict)
from partnercenter.azext_partnercenter.models import (Plan, Resource)
from partnercenter.azext_partnercenter.vendored_sdks.v1.partnercenter.apis import (
    ProductClient, VariantClient)
from partnercenter.azext_partnercenter.clients.offer_client import OfferClient
from partnercenter.azext_partnercenter.vendored_sdks.v1.partnercenter.models import ProductsProductIDVariantsGetRequest

class PlanClient:
    def __init__(self, cli_ctx, *_):
        self._api_client = get_api_client(cli_ctx, *_)
        self._product_client = ProductClient(self._api_client)
        self._variant_client = VariantClient(self._api_client)
        self._offer_client = OfferClient(cli_ctx, *_)

    def create(self, product_external_id, external_id, friendly_name):
        resource_type = "AzureSkuVariant"
        offer = self._offer_client.get_by_offer_id(product_external_id)
        product_id = offer.id

        prod_var_req = ProductsProductIDVariantsGetRequest(resource_type=resource_type, friendly_name=friendly_name, external_id=external_id)
        result = self._variant_client.products_product_id_variants_post(product_id=product_id, authorization=self._api_client.configuration.access_token, products_product_id_variants_get_request=prod_var_req)
        return result.to_dict()

    def list(self, offer_resource_id):
        product = self._product_client.products_product_id_get(offer_resource_id, self._api_client.configuration.access_token)
        variants = get_combined_paged_results(lambda : self._variant_client.products_product_id_variants_get(offer_resource_id, self._api_client.configuration.access_token))

        items = []

        for variant in variants:
            item = Plan(
                id=variant['externalID'],
                name=variant['friendlyName'],
                offer_id=product['externalIDs'][0]['value'],
                state=variant['state'],
                cloud_availabilities=variant['cloudAvailabilities'],
                resource=Resource(id=variant['id'], type=variant['resourceType'])
            )
            items.append(item)

        return items

    def find_by_external_id(self, offer_resource_id, plan_external_id):
        items = self.list(offer_resource_id)
        
        item: Plan
        for item in items:
            if item.id == plan_external_id:
                return item
        
        return None

    def get(self, offer_resource_id, plan_resource_id):
        product = self._product_client.products_product_id_get(offer_resource_id, self._api_client.configuration.access_token)
        #self._variant_client.products_product_id_variants_get()
        variant = self._variant_client.products_product_id_variants_variant_id_get(
                offer_resource_id,
                plan_resource_id,
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

    