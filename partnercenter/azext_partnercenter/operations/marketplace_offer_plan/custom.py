# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core.util import sdk_no_wait
from knack.util import CLIError

# API Operations
# pylint: disable=too-many-locals

def list_plan(cmd, client, offer_id=None, offer_resource_id=None):
    if (offer_id is None and offer_resource_id is None):
        raise CLIError('offer-id or offer-resource-id is required')

    if (offer_resource_id is not None):
        return client.list(offer_resource_id)

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
