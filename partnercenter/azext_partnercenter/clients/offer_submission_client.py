# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long
# pylint: disable=protected-access

from azext_partnercenter.models import OfferSubmission
from azext_partnercenter.clients import OfferClient
from ._base_client import BaseClient


class OfferSubmissionClient(BaseClient):
    def __init__(self, cli_ctx, *_):
        super().__init__(cli_ctx, *_)
        self._offer_client = OfferClient(cli_ctx, *_)

    def get(self, offer_external_id, submission_id) -> OfferSubmission:
        pass

    def list(self, offer_external_id):
        offer = self._offer_client.get(offer_external_id)
        result = self._graph_api_client.get_submissions(offer._resource.durable_id)
        return list(map(lambda x: OfferSubmission(
            id = x.id.__root__.split('/')[-1],
            offer_id = offer_external_id,
            lifecycle_state = x.lifecycle_state,
            target = x.target.target_type,
            status = x.status,
            result = x.result,
            created = x.created
        ), result))

    def publish(self, offer_external_id, submission_id, target):
        pass
