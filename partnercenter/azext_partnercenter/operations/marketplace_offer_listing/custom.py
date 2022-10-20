# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core.util import sdk_no_wait
from knack.util import CLIError
from azure.cli.core.azclierror import (RequiredArgumentMissingError, ResourceNotFoundError)


def list_listing(client, offer_id=None, offer_resource_id=None):
    _validate_offer_ids(offer_id, offer_resource_id)

    if (offer_resource_id is not None):
        return client.get_listings(offer_resource_id)

    offer = client.get_by_offer_id(offer_id)
    if offer is not None:
        return client.get_listings(offer.id)
    
    return []


def get_listing(cmd, arg):
    raise CLIError('TODO: Implement `partnercenter marketplace offer create`')


def update_listing(cmd, instance, arg):
    # TODO: Implement partnercenter marketplace offer update
    return instance

def _validate_offer_ids(offer_id, offer_resource_id):
    if (offer_id is None and offer_resource_id is None):
        raise RequiredArgumentMissingError("Either --offer-id or --offer-resource-id is required")
