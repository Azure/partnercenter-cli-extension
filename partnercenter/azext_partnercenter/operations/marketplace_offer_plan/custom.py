# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core.util import sdk_no_wait
from knack.util import CLIError

# API Operations
# pylint: disable=too-many-locals

def list_plan(cmd, client, offer_id, resource_id=None):
    if (resource_id is not None):
        return client.list(resource_id)
    
    from partnercenter.azext_partnercenter._client_factory import cf_offers
    offer = cf_offers(cmd.cli_ctx).get_by_offer_id(offer_id)

    if offer is not None:
        return client.list(offer.id)
    return


def create_plan(cmd, arg):
    raise CLIError('TODO: Implement `partnercenter marketplace offer create`')


def update_plan(cmd, instance, arg):
    # TODO: Implement partnercenter marketplace offer update
    return instance


def delete_plan(cmd):
    raise CLIError('TODO: Implement `partnercenter marketplace offer plan delete`')


def get_plan(cmd):
    raise CLIError('TODO: Implement `partnercenter marketplace offer plan show`')
