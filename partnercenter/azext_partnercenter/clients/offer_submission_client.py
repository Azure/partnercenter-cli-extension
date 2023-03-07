# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long

from azext_partnercenter.vendored_sdks.production_ingestion.models import Submission
from azext_partnercenter.models import OfferSubmission
from azext_partnercenter.clients import OfferClient
from ._base_client import BaseClient


class OfferSubmissionClient(BaseClient):
    def __init__(self, cli_ctx, *_):
        super().__init__(cli_ctx, *_)
        self._offer_client = OfferClient(cli_ctx, *_)

    def get(self, offer_external_id, submission_id) -> OfferSubmission:
        offer = self._offer_client.get(offer_external_id)
        result = self._graph_api_client.get_submission(offer._resource.durable_id, submission_id)
        return self._map_submission(result)

    def list(self, offer_external_id):
        offer = self._offer_client.get(offer_external_id)
        result = self._graph_api_client.get_submissions(offer._resource.durable_id)
        return list(map(self._map_submission, result))

    def publish(self, offer_external_id, submission_id, target):
        offer = self._offer_client.get(offer_external_id)
        result = self._graph_api_client.publish_submission(target, offer._resource.durable_id, submission_id)
        return result

    @staticmethod
    def _map_submission(s: Submission) -> OfferSubmission:
        return OfferSubmission(
            id=s.id.__root__.split('/')[-1],
            lifecycle_state=s.lifecycle_state,
            target=s.target.target_type,
            status=s.status,
            result=s.result,
            created=s.created
        )
