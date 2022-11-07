# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


from azext_partnercenter.clients.base_client import BaseClient
from azext_partnercenter.clients import OfferClient, PlanClient
from ._util import object_to_dict
from partnercenter.azext_partnercenter.vendored_sdks.v1.partnercenter.apis import (
    PackageClient as SdkPackageClient, ProductClient as SdkProductClient)

class PlanTechnicalConfigurationClient(BaseClient):
    def __init__(self, cli_ctx, *_):
        BaseClient.__init__(self, cli_ctx, *_)
        self._offer_client = OfferClient(cli_ctx, *_)
        self._plan_client = PlanClient(cli_ctx, *_)

    def get(self, offer_external_id, plan_external_id):
        offer = self._offer_client.get(offer_external_id)
        return {}


    def delete(self, offer_external_id):
       pass