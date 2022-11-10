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
    if (offer_resource_id is not None):
        return client.list(offer_resource_id)

    from partnercenter.azext_partnercenter._client_factory import cf_offers
    offer = cf_offers(cmd.cli_ctx).get_by_offer_id(offer_id)

    if offer is not None:
        return client.list(offer.id)

    return []


def create_plan(cmd, client, product_external_id, external_id, friendly_name):
    result = client.create(product_external_id, external_id, friendly_name)
    return result


def update_plan(cmd, instance, arg):
    # TODO: Implement partnercenter marketplace offer update
    return instance


def delete_plan(cmd, client, offer_id, plan_id):
    if (offer_id is None or plan_id is None):
        raise RequiredArgumentMissingError("Both --offer-id and --plan-id are required")
    
    results = client.delete(offer_id, plan_id)
    if results:
        return "Deleted plan: " + plan_id
    else:
        raise CLIError("Failed to delete plan: " + plan_id + ". Error: " + results)

def get_plan(cmd, client, offer_id, plan_id):
    if (offer_id is None):
        raise RequiredArgumentMissingError("--offer-id is required")
    
    offer_resource_id = _get_offer_resource_id(cmd, offer_id)
    if (offer_resource_id is None):
        raise ResourceNotFoundError('Offer not found.')

    if (plan_id is None):
        raise RequiredArgumentMissingError("--plan-id is required")

    # since there is no odata filter underlying plan, we have to get them all and filter in memory
    plans = client.list(offer_resource_id)
    return next((p for p in plans if p.id == plan_id), None)

def _get_offer_resource_id(cmd, offer_id):
    from partnercenter.azext_partnercenter._client_factory import cf_offers
    offer = cf_offers(cmd.cli_ctx).get(offer_id)
    print(f'offer - {offer}')
    print(f'offer._resource - {offer._resource}')
    return offer._resource.id if offer is not None else None

def _get_plan_resource_id(cmd, plan_id, offer_resource_id):
    from partnercenter.azext_partnercenter._client_factory import cf_plans
    plans = cf_plans(cmd.cli_ctx).list(offer_resource_id)
    for p in plans:
        print(f'plan - {p}')
        if p.id == plan_id:
            return p.resource.id