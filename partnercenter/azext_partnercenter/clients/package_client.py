# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


from ._util import get_api_client
from partnercenter.azext_partnercenter._util import (
    get_combined_paged_results, object_to_dict)
from partnercenter.azext_partnercenter.vendored_sdks.v1.partnercenter.apis import (
    ProductClient, VariantClient)
from partnercenter.azext_partnercenter.clients.offer_client import OfferClient

class PackageClient:
    def __init__(self, cli_ctx, *_):
        self._api_client = get_api_client(cli_ctx, *_)
        self._product_client = ProductClient(self._api_client)

    def create(self):
        pass

    def list(self, offer_external_id):
       pass