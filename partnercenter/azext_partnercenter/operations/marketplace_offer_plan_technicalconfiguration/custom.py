# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core.util import sdk_no_wait
from knack.util import CLIError

# API Operations
# pylint: disable=too-many-locals

def get_technicalconfiguration(client, offer_id, plan_id):
   return client.get(offer_id, plan_id)


def attach_technical_configuration_bundle(client, offer_id, plan_id, cluster_extension_type, tenant_id=None,
           subscription_id=None, resource_group_name=None, registry_name=None, repository_name=None, tag=None, digest=None):

