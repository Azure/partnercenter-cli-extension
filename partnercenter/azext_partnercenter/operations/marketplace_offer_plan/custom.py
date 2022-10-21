# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core.util import sdk_no_wait
from knack.util import CLIError
from azure.cli.core.azclierror import (RequiredArgumentMissingError, ResourceNotFoundError)

# API Operations
# pylint: disable=too-many-locals

def list_plan(cmd, client, offer_id=None, offer_resource_id=None):
    _validate_offer_ids(offer_id, offer_resource_id)

    if (offer_resource_id is not None):
        return client.list(offer_resource_id)

    from partnercenter.azext_partnercenter._client_factory import cf_offers
    offer = cf_offers(cmd.cli_ctx).get_by_offer_id(offer_id)

    if offer is not None:
        return client.list(offer.id)
    return


def create_plan(cmd, client, product_external_id, external_id, friendly_name):
    result = client.create(product_external_id, external_id, friendly_name)
    return result


def update_plan(cmd, instance, arg):
    # TODO: Implement partnercenter marketplace offer update
    return instance


def delete_plan(cmd):
    raise CLIError('TODO: Implement `partnercenter marketplace offer plan delete`')


def get_plan(cmd, client, offer_id=None, offer_resource_id=None, plan_id=None, plan_resource_id=None):
    _validate_offer_ids(offer_id, offer_resource_id)
    offer_resource_id = _get_offer_resource_id(cmd, offer_id, offer_resource_id)

    if (offer_resource_id is None):
        raise ResourceNotFoundError('Offer not found.')

    if (plan_id is None and plan_resource_id is None):
        raise RequiredArgumentMissingError("Either --plan-id or --plan-resource-id is required")

    if plan_resource_id is not None:
        return client.get(offer_resource_id, plan_resource_id)

    # since there is no odata filter underlying plan, we have to get them all and filter in memory
    plans = client.list(offer_resource_id)
    return next((p for p in plans if p.id == plan_id), None)

def _validate_offer_ids(offer_id, offer_resource_id):
    if (offer_id is None and offer_resource_id is None):
        raise RequiredArgumentMissingError("Either --offer-id or --offer-resource-id is required")

    
def _get_offer_resource_id(cmd, offer_id, offer_resource_id):
    if offer_resource_id is not None:
        return offer_resource_id

    from partnercenter.azext_partnercenter._client_factory import cf_offers
    offer = cf_offers(cmd.cli_ctx).get_by_offer_id(offer_id)
    return offer.id if offer is not None else None