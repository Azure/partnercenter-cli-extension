# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=too-many-locals
# pylint: disable=line-too-long

from azure.cli.core.azclierror import ResourceNotFoundError


def get_listing(client, offer_id, plan_id):
    listing = client.get(offer_id, plan_id)

    if listing is None:
        raise ResourceNotFoundError(
            "Plan not found.",
            f"Please create a plan on offer [{offer_id}] with ID [{plan_id}] using the create command.",
        )
    return listing


def update_listing(instance, name=None, summary=None, description=None):
    if name is not None:
        instance.name = name

    if summary is not None:
        instance.summary = summary

    if description is not None:
        instance.description = description
    return instance
