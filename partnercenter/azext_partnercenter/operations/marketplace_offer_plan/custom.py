# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core.azclierror import RequiredArgumentMissingError
from knack.util import CLIError


def list_plan(client, offer_id):
    from azext_partnercenter._client_factory import cf_offers
    if offer_id is None:
        raise RequiredArgumentMissingError("--offer-id is required")

    return client.list(offer_id)


def create_plan(client, offer_id, plan_id, friendly_name):
    result = client.create(offer_id, plan_id, friendly_name)
    return result


def update_plan(instance, arg):
    # TODO: Implement partnercenter marketplace offer update
    return instance


def delete_plan(cmd, client, offer_id, plan_id):
    if offer_id is None or plan_id is None:
        raise RequiredArgumentMissingError("Both --offer-id and --plan-id are required")

    results = client.delete(offer_id, plan_id)
    if results:
        return "Deleted plan: " + plan_id
    else:
        raise CLIError("Failed to delete plan: " + plan_id + ". Error: " + results)


def get_plan(client, offer_id, plan_id):
    return client.get(offer_id, plan_id)
