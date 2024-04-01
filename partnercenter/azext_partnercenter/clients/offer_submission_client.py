# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long

import datetime
from azext_partnercenter.vendored_sdks.v1.partnercenter.model.microsoft_ingestion_api_models_submissions_submission import (
    MicrosoftIngestionApiModelsSubmissionsSubmission
)
from azext_partnercenter.models import OfferSubmission
from azext_partnercenter.clients import OfferClient
from azext_partnercenter.vendored_sdks.v1.partnercenter.model.microsoft_ingestion_api_models_submissions_submission_creation_request import (
    MicrosoftIngestionApiModelsSubmissionsSubmissionCreationRequest)
from ._base_client import BaseClient
from ._sdk_client_provider import SubmissionClient
from ._sdk_client_provider import BranchesClient


class OfferSubmissionClient(BaseClient):
    def __init__(self, cli_ctx, *_):
        super().__init__(cli_ctx, *_)
        self._offer_client = OfferClient(cli_ctx, *_)
        self._submission_client = SubmissionClient(cli_ctx, *_)
        self._branch_client = BranchesClient(cli_ctx, *_)

    def get(self, offer_external_id, submission_id):
        offer = self._offer_client.get(offer_external_id)
        result = self._submission_client.products_product_id_submissions_submission_id_get(offer.resource.durable_id, submission_id, self._get_access_token())
        return result

    def list(self, offer_external_id):
        offer = self._offer_client.get(offer_external_id)
        result = self._submission_client.products_product_id_submissions_get(offer.resource.durable_id, self._get_access_token())
        return list(map(self._map_submission, result))

    def _get_offer_draft_instance(self, offer_external_id, module):
        product = self._offer_client._get_sdk_product_by_external_offer_id(offer_external_id)
        branches = self._branch_client.products_product_id_branches_get_by_module_modulemodule_get(
            product.id, module, self._get_access_token()
        )
        if len(branches.value) == 0:
            return None
        variant_package_branch = next((b for b in branches.value if not hasattr(b, 'variant_id')), None)
        return variant_package_branch


    def publish(self, offer_external_id, submission_id, target):
        offer = self._offer_client.get(offer_external_id)
        if offer.resourceType == "AzureContainer":
            result = self._graph_api_client.publish_submission(target, offer.resource.durable_id, submission_id)
        if offer.resourceType == "AzureApplication":
            modules = ["Availability", "Listing", "Package", "Property"]
            resources = []
            for m in modules:
                current_draft_instance = self._get_offer_draft_instance(offer.resource.durable_id, m)
                if current_draft_instance is not None:
                    resources.append({"type": m, "values": current_draft_instance.currentDraftInstanceId})
            offer_submission_dict = {
                "resourceType": "SubmissionCreationRequest",
                "targets": [
                    {
                        "type": "Scope",
                        "value": "preview"
                    }
                ],
                "resources": resources
                ,
                "publishOption": {
                    "releaseTimeInUtc": datetime.utcnow().isoformat(),
                    "isManualPublish": True,
                    "isAutoPromote": False,
                    "certificationNotes": "Submission automatically generated"
                },
                "extendedProperties": []
            }
            offer_creation_request = MicrosoftIngestionApiModelsSubmissionsSubmissionCreationRequest(**offer_submission_dict)
            print(offer_creation_request)
            result = self._submission_client.products_product_id_submissions_post(offer.resource.durable_id,
            self._get_access_token(),
            offer_creation_request
            )
        return result


#TODO: understand attribute mapping
#v1 has
    # 'resource_type': (str,),  # noqa: E501
    # 'state': (str,),  # noqa: E501
    # 'substate': (str,),  # noqa: E501
    # 'targets': ([MicrosoftIngestionApiModelsCommonTypeValuePair],),  # noqa: E501
    # 'resources': ([MicrosoftIngestionApiModelsCommonTypeValuePair],),  # noqa: E501
    # 'variant_resources': ([MicrosoftIngestionApiModelsSubmissionsVariantResource],),  # noqa: E501
    # 'publish_option': (MicrosoftIngestionApiModelsSubmissionsPublishOption,),  # noqa: E501
    # 'published_time_in_utc': (datetime,),  # noqa: E501
    # 'pending_update_info': (MicrosoftIngestionApiModelsSubmissionsPendingUpdateInfo,),  # noqa: E501
    # 'extended_properties': ([MicrosoftIngestionApiModelsCommonTypeValuePair],),  # noqa: E501
    # 'release_number': (int,),  # noqa: E501
    # 'friendly_name': (str,),  # noqa: E501
    # 'are_resources_ready': (bool,),  # noqa: E501
    # 'id': (str,),  # noqa: E501



    @staticmethod
    def _map_submission(s: MicrosoftIngestionApiModelsSubmissionsSubmission) -> OfferSubmission:
        return OfferSubmission(
            id=s.id.root.split('/')[-1],
            # lifecycle_state=s.substate,
            # target=s.target.target_type,
            # status=s.state,
            # result=s.result,
            created=s.published_time_in_utc
        )
