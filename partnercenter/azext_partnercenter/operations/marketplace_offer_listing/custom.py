# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long

from azext_partnercenter.models.listing import Listing


def get(client, offer_id):
    return client.get_listing(offer_id)


def update_listing(instance, summary=None, short_description=None, description=None):
    if summary is not None:
        instance.summary = summary

    if short_description is not None:
        instance.short_description = short_description

    if description is not None:
        instance.description = description
    return instance


def marketplace_offer_listing_delete(client, offer_id):
    return client.delete_offer_listing(offer_id)


def _update_get(client, offer_id):
    return client.get_listing(offer_id)


def _update_set(client, offer_id, parameters):
    listing = Listing(
        offer_id=offer_id,
        title=parameters.title,
        summary=parameters.summary,
        description=parameters.description,
        short_description=parameters.short_description,
        language_code=parameters.language_code,
        odata_etag=parameters.odata_etag,
        contacts=parameters.contacts,
        uris=parameters.uris
    )

    result = client.create_or_update(offer_id, listing)
    return result
