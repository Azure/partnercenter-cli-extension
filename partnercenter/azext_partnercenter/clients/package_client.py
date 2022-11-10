# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


from ._base_client import BaseClient
from . import OfferClient
from ._util import object_to_dict
from partnercenter.azext_partnercenter.vendored_sdks.v1.partnercenter.apis import (
    PackageClient as SdkPackageClient, ProductClient as SdkProductClient)

class PackageClient(BaseClient):
    def __init__(self, cli_ctx, *_):
        BaseClient.__init__(self, cli_ctx, *_)
        self._sdk_product_client = SdkProductClient(self._api_client)
        self._sdk_package_client = SdkPackageClient(self._api_client)
        self._offer_client = OfferClient(cli_ctx, *_)
    def create(self):
        pass


    def list(self, offer_id):
        offer = self._offer_client.get(offer_id)
        packages = self._sdk_package_client.products_product_id_packages_get(offer._resource.id, self._get_access_token())

        # TODO: the packages get isn't returning anything for certain products and need to find out why
        return packages


    def delete(self, offer_external_id):
       pass