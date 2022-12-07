# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


def get_listing(client, offer_id):
    return client.get(offer_id)


def update_listing(instance, summary=None, short_description=None, description=None):
    if summary is not None:
        instance.summary = summary

    if short_description is not None:
        instance.short_description = short_description

    if description is not None:
        instance.description = description
    return instance


def delete_listing(client, offer_id):
    return client.delete_offer_listing(offer_id)

