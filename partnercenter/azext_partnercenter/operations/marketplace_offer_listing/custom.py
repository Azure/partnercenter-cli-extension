# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long

from azext_partnercenter.models.listing import Listing


def get(client, offer_id):
    return client.get_listing(offer_id)


def marketplace_offer_listing_update_get(client, offer_id):
    listing = client.get_listing(offer_id)
    return listing


def marketplace_offer_listing_update_set(client, offer_id, parameters=None):
    listing = Listing()
    listing.id = parameters.id
    listing.title = parameters.title
    listing.summary = parameters.summary
    listing.description = parameters.description
    listing.short_description = parameters.short_description
    listing.language_code = parameters.language_code
    listing.odata_etag = parameters.odata_etag
    listing.contacts = parameters.contacts
    listing.uris = parameters.uris
    result = client.create_or_update(offer_id, listing)
    return result


def marketplace_offer_listing_update_custom(instance, summary=None, short_description=None, description=None):
    instance.summary = summary
    instance.short_description = short_description
    instance.description = description
    return instance


def marketplace_offer_listing_delete(client, offer_id):
    return client.delete_offer_listing(offer_id)
