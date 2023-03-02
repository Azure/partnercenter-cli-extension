# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


from partnercenter.azext_partnercenter.clients.plan_client import PlanClient


def list_plan(client: PlanClient, offer_id):
    return client.list(offer_id)


def create_plan(client: PlanClient, offer_id, plan_id, name, subtype=None):
    return client.create(offer_id, plan_id, name, subtype)


def delete_plan(client: PlanClient, offer_id, plan_id):
    return client.delete(offer_id, plan_id)


def get_plan(client: PlanClient, offer_id, plan_id):
    return client.get(offer_id, plan_id)
