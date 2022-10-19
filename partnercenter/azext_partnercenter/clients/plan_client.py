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


class PlanClient:
    def __init__(self, cli_ctx, *_):
        self._api_client = get_api_client(cli_ctx, *_)
        self._product_client = ProductClient(self._api_client)
        self._variant_client = VariantClient(self._api_client)

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


    def get(self, offer_resource_id, plan_resource_id):
        product = self._product_client.products_product_id_get(offer_resource_id, self._api_client.configuration.access_token)
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
