# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long

import datetime
from azext_partnercenter.models.pending_update_info import PendingUpdateInfo
import requests
from azext_partnercenter.vendored_sdks.v1.partnercenter.model.microsoft_ingestion_api_models_submissions_submission import (
    MicrosoftIngestionApiModelsSubmissionsSubmission
)
from azext_partnercenter.models.offer_submission import OfferSubmission
from azext_partnercenter.models.application_submission import ApplicationSubmission
from azext_partnercenter.models.type_value import TypeValue
from azext_partnercenter.models.submission_variant_resource import SubmissionVariantResource
from azext_partnercenter.models.submission_publish_option import SubmissionPublishOption
from azext_partnercenter.clients import OfferClient
from azext_partnercenter.vendored_sdks.v1.partnercenter.model.microsoft_ingestion_api_models_submissions_submission_creation_request import (
    MicrosoftIngestionApiModelsSubmissionsSubmissionCreationRequest)
from azext_partnercenter.vendored_sdks.v1.partnercenter.model.microsoft_ingestion_api_models_submissions_variant_resource import (
    MicrosoftIngestionApiModelsSubmissionsVariantResource
)
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

    def _get_offer_draft_instance(self, offer_durable_id, module):
        #print(f"Getting offer draft instance for {offer_external_id} and module {module}")
       # product = self._offer_client.get(offer_external_id)
       # print(f"Product is {product}")
        branches = self._sdk.branches_client.products_product_id_branches_get_by_module_modulemodule_get(
            offer_durable_id, module, self._get_access_token()
        )
        print(f"Branches are {branches}")
        if len(branches.value) == 0:
            return None
        variant_package_branch = next((b for b in branches.value if not hasattr(b, 'variant_id')), None)
        print(f"Variant package branch is {variant_package_branch}")
        return variant_package_branch



    def _get_reseller_configuration(self, offer_external_id):
        print(f"Inside get reseller configuration for {offer_external_id}")
        url = f"https://api.partner.microsoft.com/v1.0/ingestion/products/{offer_external_id}/branches/getByModule(module=ResellerConfiguration)"
        bearer_token = f"Bearer {self._get_access_token()}"
        headers = {
            "Content-Type": "application/json",
            "Authorization": bearer_token
        }
        response = requests.get(url, headers=headers)
        print(f"Response is {response}")

        if response.status_code != 200:
            raise Exception(f"Failed to get offer branches for {offer_external_id}, status code: {response.status_code}")

        reseller_configuration = response.json().get("value")
        print(f"Reseller configuration resources are {reseller_configuration}")

        if not reseller_configuration:
            return None

        reseller_configuration_obj = reseller_configuration[0]
        print(f"Reseller configuration object is {reseller_configuration_obj}")

        current_draft_instance_id = reseller_configuration_obj.get("currentDraftInstanceID")
        print(f"Current draft instance id inside _get_reseller_configuration is {current_draft_instance_id}")
        return current_draft_instance_id


    def _get_variant_resources(self, offer_external_id):
        print(f"Getting variant resources for {offer_external_id}")
        variant_ids = []
        variant_resources = []
        variants = self._sdk._variant_client.products_product_id_variants_get(offer_external_id)
        print(f"Variants are {variants}")
        for v in variants.value:
            print(f"Variant is {v}")
            if (v.get("subType") == "managed-application"):
                variant_ids.append(v.get(id));
        for i in variant_ids:
            print(f"variant - {i}")
            current_resources = []
            for module in ["Availability", "Listing", "Package"]:
                current_draft_instance = self._get_offer_draft_instance(i, module)
                current_resources.append({"type": module, "value": current_draft_instance.current_draft_instance_id})
            variant_resources.append({"variantID": i, "resources": current_resources})
            print(f"Variant resources are {variant_resources}")
        return variant_resources


    def _map_application_submission(self, submission):
        print(f"Mapping application submission {submission}")
        return ApplicationSubmission(
            id=submission.id if hasattr(submission, 'id') else None,
            resource_type=submission.resource_type if hasattr(submission, 'resource_type') else None,
            state=submission.state if hasattr(submission, 'state') else None,
            substate=submission.substate if hasattr(submission, 'substate') else None,
            targets=submission.targets if hasattr(submission, 'targets') else [],
            resources=self._map_list_to_type_value(submission.resources) if hasattr(submission, 'resources') else [],
            variant_resources=self._map_list_to_variant_resources(submission.variant_resources) if hasattr(submission, 'variant_resources') else [],
            publish_option=self._map_submission_publish_option(submission.publish_option) if hasattr(submission, 'publish_option') else None,
            published_time_in_utc=submission.published_time_in_utc.isoformat() if hasattr(submission, 'published_time_in_utc') else None,
            pending_update_info=self._map_pending_update_info(submission.pending_update_info) if hasattr(submission, 'pending_update_info') else None,
            extended_properties=self._map_list_to_type_value(submission.extended_properties) if hasattr(submission, 'extended_properties') else [],
            release_number=submission.release_number if hasattr(submission, 'release_number') else 0,
            friendly_name=submission.friendly_name if hasattr(submission, 'friendly_name') else None,
            are_resources_ready=submission.are_resources_ready if hasattr(submission, 'are_resources_ready') else False
        )

    def _map_submission_publish_option(self, publish_option):
        print(f"Mapping submission publish option {publish_option}")
        return SubmissionPublishOption(
            release_time_in_utc=publish_option.release_time_in_utc if hasattr(publish_option, 'release_time_in_utc') else None,
            is_manual_publish=publish_option.is_manual_publish if hasattr(publish_option, 'is_manual_publish') else False,
            is_auto_promote=publish_option.is_auto_promote if hasattr(publish_option, 'is_auto_promote') else False,
            certification_notes=publish_option.certification_notes if hasattr(publish_option, 'certification_notes') else None
        )

    def _map_pending_update_info(self, pending_update_info):
        print(f"Mapping pending update info {pending_update_info}")
        return PendingUpdateInfo(
            update_type=pending_update_info.update_type if hasattr(pending_update_info, 'update_type') else None,
            status=pending_update_info.status if hasattr(pending_update_info, 'status') else None,
            href=pending_update_info.href if hasattr(pending_update_info, 'href') else None,
            failure_reason=pending_update_info.failure_reason if hasattr(pending_update_info, 'failure_reason') else None)

    def _map_list_to_type_value(self, list):
        print(f"Mapping list to type value {list}")
        return [TypeValue(type=type_value.type, value=type_value.value) for type_value in list]

    def _map_list_to_variant_resources(self, list):
        print(f"Mapping list to variant resources {list}")
        return [SubmissionVariantResource(variant_id=variant_resource.variant_id, resources=self._map_list_to_type_value(variant_resource.resources)) for variant_resource in list]

    def publish(self, offer_external_id, submission_id, target):
        offer = self._offer_client.get(offer_external_id)
        resource = offer.resource
        print(f"Resource is {resource}")
        print(f"Offer is {offer}")

        if offer.type == "AzureContainer":
            result = self._graph_api_client.publish_submission(target, offer.resource.durable_id, submission_id)
            return result

        if offer.type == "AzureApplication":
            resources = []
            variant_resources = []
            managed_application_variants = []

            variants = self._sdk.variant_client.products_product_id_variants_get(offer.resource.durable_id, self._get_access_token())
            print(f"Variants are {variants}")
            for v in variants.value:
                print(f"Variant v is {v}")
                if v["resourceType"] == "AzureSkuVariant":
                    print(f"resource type is AzureSkuVariant")
                    if 'subType' in v:
                        print(f"v has subType")
                        if v.get("subType") == "managed-application":
                            print(f"subType is managed-application")
                            managed_application_variants.append(v.get("id"))

            print(f"Managed application variants are {managed_application_variants}")

            variant_resources_dict = {}
            modules = ["Availability", "Listing", "Package", "Property"]
            for m in modules:
                branches = self._sdk.branches_client.products_product_id_branches_get_by_module_modulemodule_get(
                    offer.resource.durable_id, m, self._get_access_token()
                )

                for b in branches.value:
                    if not hasattr(b, 'variant_id'):
                        resources.append({"type": m, "value": b.current_draft_instance_id})
                    else:
                        variant_id = getattr(b, 'variant_id')
                        if variant_id in managed_application_variants:
                            if variant_id not in variant_resources_dict:
                                variant_resources_dict[variant_id] = []
                            variant_resources_dict[variant_id].append({"type": m, "value": b.current_draft_instance_id})

            variant_resources_list = [{"variantID": variant_id, "resources": resources} for variant_id, resources in variant_resources_dict.items()]

            reseller_instance_id = self._get_reseller_configuration(offer.resource.durable_id)
            resources.append({"type": "ResellerConfiguration", "value": reseller_instance_id})

            print(f"Resources are {resources}")
            offer_submission_dict = {
                "resourceType": "SubmissionCreationRequest",
                "targets": [
                    {
                        "type": "Scope",
                        "value": "preview"
                    }
                ],
                "resources": resources,
                "variantResources": variant_resources_list,
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
            return self._map_application_submission(result)

        print(f"returning empty result")
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
