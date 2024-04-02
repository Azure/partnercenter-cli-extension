# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long

import datetime
import requests
from azext_partnercenter.vendored_sdks.v1.partnercenter.model.microsoft_ingestion_api_models_submissions_submission import (
    MicrosoftIngestionApiModelsSubmissionsSubmission
)
from azext_partnercenter.models import OfferSubmission
from azext_partnercenter.clients import OfferClient
from azext_partnercenter.vendored_sdks.v1.partnercenter.model.microsoft_ingestion_api_models_submissions_submission_creation_request import (
    MicrosoftIngestionApiModelsSubmissionsSubmissionCreationRequest)
from ._base_client import BaseClient

class OfferSubmissionClient(BaseClient):
    def __init__(self, cli_ctx, *_):
        print(f"Inside OfferSubmissionClient with a value of {cli_ctx}")
        super().__init__(cli_ctx, *_)
        self._offer_client = OfferClient(cli_ctx, *_)

    def get(self, offer_external_id, submission_id):
        offer = self._offer_client.get(offer_external_id)
        result = self._submission_client.products_product_id_submissions_submission_id_get(offer.resource.durable_id, submission_id, self._get_access_token())
        return result

    def list(self, offer_external_id):
        offer = self._offer_client.get(offer_external_id)
        result = self._submission_client.products_product_id_submissions_get(offer.resource.durable_id, self._get_access_token())
        return list(map(self._map_submission, result))

    def _get_offer_draft_instance(self, offer_external_id, module):
        print(f"Getting offer draft instance for {offer_external_id} and module {module}")
        product = self._offer_client.get(offer_external_id)
        print(f"Product is {product}")
        branches = self._sdk.branches_client.products_product_id_branches_get_by_module_modulemodule_get(
            product.resource.durable_id, module, self._get_access_token()
        )
        print(f"Branches are {branches}")
        if len(branches.value) == 0:
            return None
        variant_package_branch = next((b for b in branches.value if not hasattr(b, 'variant_id')), None)
        print(f"Variant package branch is {variant_package_branch}")
        return variant_package_branch

    def _get_reseller_configuration(self, offer_external_id):
        url = f"https://api.partner.microsoft.com/v1.0/ingestion/products/{offer_external_id}/branches/getByModule(module=ResellerConfiguration)"
        header = {
                "Content-Type": "application/json",
                "Authorization": self._get_access_token()
            },
        response = requests.get(url, headers=header)
        if response.status_code != 200:
            raise Exception("Failed to get offer branches")
        branches = response.json()["value"]
        for branch in branches:
            if branch.get("variantID") is None:
                offer_draft_instance_id = branch["currentDraftInstanceID"]
                break
        if not offer_draft_instance_id:
            raise Exception("Offer draft instance id has not been found")
        return offer_draft_instance_id


    def publish(self, offer_external_id, submission_id, target):
        offer = self._offer_client.get(offer_external_id)
        resource = offer.resource
        print(f"Resource is {resource}")
        print(f"Offer is {offer}")
        if offer.type == "AzureContainer":
            result = self._graph_api_client.publish_submission(target, offer.resource.durable_id, submission_id)
        if offer.type == "AzureApplication":
            modules = ["Availability", "Listing", "Package", "Property", "ResellerConfiguration"]
            resources = []
            variant_resources = [] # need to add the variant resources
            for m in modules:
                current_draft_instance = self._get_offer_draft_instance(offer_external_id, m)
                print(f"Current draft instance is {current_draft_instance}")
                if current_draft_instance is not None:
                    resources.append({"type": m, "value": current_draft_instance.current_draft_instance_id})
            resources.append({"type": "ResellerConfiguration", "value": self._get_reseller_configuration(offer_external_id)})
            print(f"Resources are {resources}")
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
                    "releaseTimeInUtc": datetime.datetime.utcnow().isoformat(),
                    "isManualPublish": True,
                    "isAutoPromote": False,
                    "certificationNotes": "Submission automatically generated"
                },
                "extendedProperties": []
            }
            offer_creation_request = MicrosoftIngestionApiModelsSubmissionsSubmissionCreationRequest(**offer_submission_dict)
            print(f"offer_creation_request is {offer_creation_request}")
            result = self._sdk.submission_client.products_product_id_submissions_post(offer.resource.durable_id,
                self._get_access_token(),
                microsoft_ingestion_api_models_submissions_submission_creation_request=offer_creation_request
            )
            print(f"Result is {result}")
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
        print(f"Mapping submission {s}")
        return OfferSubmission(
            id=s.id.root.split('/')[-1],
            # lifecycle_state=s.substate,
            # target=s.target.target_type,
            # status=s.state,
            # result=s.result,
            created=s.published_time_in_utc
        )
