# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long
# pylint: disable=protected-access
from ._util import object_to_dict
from ._base_client import BaseClient
from partnercenter.azext_partnercenter.clients.offer_client import OfferClient


class SubmissionClient(BaseClient):
    def __init__(self, cli_ctx, *_):
        super(SubmissionClient, self).__init__(cli_ctx, *_)
        self._offer_client = OfferClient(cli_ctx, *_)

    def create(self):
        pass

    def list(self, offer_external_id):
        offer = self._offer_client.get(offer_external_id)
        submissions = self._sdk.submission_client.products_product_id_submissions_get(
            offer._resource.durable_id,
            self._get_access_token())
        return object_to_dict(submissions)

    def get(self, offer_external_id):
        pass

    def delete(self, offer_external_id):
        pass
