# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from ._util import object_to_dict
from .base_client import BaseClient
from partnercenter.azext_partnercenter.clients.offer_client import OfferClient


class SubmissionClient(BaseClient):
    def __init__(self, cli_ctx, *_):
        super(SubmissionClient, self).__init__(cli_ctx, *_)
        self._sdk_clients = SdkClients(self._api_client)
        self._offer_client = OfferClient(cli_ctx, *_)

    def create(self):
        pass


    def list(self, offer_external_id):
        offer = self._offer_client.get(offer_external_id)
        submissions = self._sdk_clients.submission_client.products_product_id_submissions_get(offer._resource.id, self._get_access_token())
        return object_to_dict(submissions)

    def get(self, offer_external_id):
       pass


    def delete(self, offer_external_id):
       pass

class SdkClients:
    def __init__(self, api_client):
        from partnercenter.azext_partnercenter.vendored_sdks.v1.partnercenter.apis import SubmissionClient
        self.submission_client = SubmissionClient(api_client)
