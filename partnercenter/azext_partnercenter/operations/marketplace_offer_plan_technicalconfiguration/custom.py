# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=too-many-locals

from azext_partnercenter.vendored_sdks.production_ingestion.models import (ContainerCnabPlanTechnicalConfigurationProperties, CnabReference)


def get_technicalconfiguration(client, offer_id, plan_id):
    return client.get(offer_id, plan_id)


def add_technical_configuration_bundle(client, offer_id, plan_id, cluster_extension_type, tenant_id=None,
        subscription_id=None, resource_group_name=None, registry_name=None, repository_name=None, tag=None, digest=None):
    properties = ContainerCnabPlanTechnicalConfigurationProperties(
        payloadType='cnab',
        clusterExtensionType=cluster_extension_type,
        cnabReferences=[CnabReference(
            tenantId=tenant_id,
            subscriptionId=subscription_id,
            resourceGroupName=resource_group_name,
            registryName=registry_name,
            repositoryName=repository_name,
            tag=tag,
            digest=digest
        )]
    )
    result = client.add_bundle(offer_id, plan_id, properties)
    return result
