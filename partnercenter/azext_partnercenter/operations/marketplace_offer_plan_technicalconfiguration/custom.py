# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long
from knack.cli import CLIError
from azext_partnercenter.vendored_sdks.production_ingestion.models import (ContainerCnabPlanTechnicalConfigurationProperties, CnabReference)
from azext_partnercenter import ISSUES_URL
from azext_partnercenter.models import PlanTechnicalConfigurationType


def get_technicalconfiguration(client, offer_id, plan_id):
    return client.get(offer_id, plan_id)


def delete_technicalconfiguration_package(client, offer_id, plan_id, repository_name=None, tag=None):
    technical_configuration_type = _get_technical_configuration_type(
        repository_name=repository_name,
        tag=tag
    )

    if technical_configuration_type is None:
        raise CLIError(f'This technical configuration type is currently not supported by the CLI. Please submit an issue to get support at {ISSUES_URL}.')

    if technical_configuration_type == PlanTechnicalConfigurationType.ContainerCnab:
        return client.delete_cnab_reference(offer_id, plan_id, repository_name, tag)

    return None


def add_technical_configuration_bundle(client, offer_id, plan_id, cluster_extension_type=None, tenant_id=None,
                                       subscription_id=None, resource_group_name=None, registry_name=None,
                                       repository_name=None, tag=None, digest=None, package_path=None, public_azure_tenant_id=None, public_azure_authorization_principal=None, public_azure_authorization_role=None):

    technical_configuration_bundle = client.get(offer_id, plan_id)
    if hasattr(technical_configuration_bundle, 'cluster_extension_type'):
        if technical_configuration_bundle.cluster_extension_type != cluster_extension_type:
            raise CLIError("The cluster extension type of the technical configuration bundle does not match the one provided.")
        cnab_references = []
        for cnab_json in technical_configuration_bundle.cnab_references:
            cnab_reference = CnabReference.parse_obj(cnab_json)
            cnab_references.append(cnab_reference)
        cnab_references.append(CnabReference(
            tenantId=tenant_id,
            subscriptionId=subscription_id,
            resourceGroupName=resource_group_name,
            registryName=registry_name,
            repositoryName=repository_name,
            tag=tag,
            digest=digest
        ))
        properties = ContainerCnabPlanTechnicalConfigurationProperties(
            payloadType='cnab',
            clusterExtensionType=cluster_extension_type,
            cnabReferences=cnab_references
        )
        result = client.add_bundle(offer_id, plan_id, properties)
        return result

    if _has_existing_package(technical_configuration_bundle):
        return {
            'Message': "package_references exists and has a length greater than zero"
        }

    result = client.add_managed_app_bundle(offer_id, plan_id, package_path, public_azure_tenant_id, public_azure_authorization_principal, public_azure_authorization_role)
    return result


def _has_existing_package(technical_configuration):
    return technical_configuration.get('package_references') and len(technical_configuration['package_references']) > 0


def _get_technical_configuration_type(repository_name=None, tag=None):
    if repository_name is not None and tag is not None:
        return PlanTechnicalConfigurationType.ContainerCnab

    # return none for not supported
    return None
