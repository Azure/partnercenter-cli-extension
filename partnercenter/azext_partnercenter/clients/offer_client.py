# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from ._util import get_api_client
from partnercenter.azext_partnercenter.vendored_sdks.v1.partnercenter.apis import (
    ListingClient, ProductClient)
from partnercenter.azext_partnercenter._util import _get_skip_token


class OfferClient():
    def __init__(self, cli_ctx, *_):
        self._api_client = get_api_client(cli_ctx, *_)
        self._product_client = ProductClient(self._api_client)


    def get_by_offer_id(self, offer_id):
        filter_expr = self._get_filter_by_offer_id_expression(offer_id)
        response = self._product_client.products_get(self._get_access_token(), filter=filter_expr)

        if (len(response.value) == 0):
            return None

        return response.value[0]

    def get(self, resource_id):
        return self._product_client.products_product_id_get(resource_id,  self._api_client.configuration.access_token)
    
    def list(self):
        results = self._product_client.products_get(self._api_client.configuration.access_token)
        return list(map(self._to_dict, results.value))

    def delete(self, product_id):
        results = self._product_client.products_product_id_delete(product_id, self._api_client.configuration.access_token)
        return results
    
    def _get_access_token(self):
        return self._api_client.configuration.access_token
    

    def _get_filter_by_offer_id_expression(self, offer_id):
        """Gets the odata filter expression for filtering by Offer ID"""
        return "externalIDs/Any(i:i/type eq 'AzureOfferId' and i/value eq '{offer_id}')".format(offer_id=offer_id)

    def _to_dict(self, item):
        return item.to_dict()