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
        pass

    def publish(self, offer_external_id, submission_id, target):
        pass
