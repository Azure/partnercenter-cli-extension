# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=too-many-locals
# pylint: disable=line-too-long

from knack.util import CLIError
from azext_partnercenter.models.listing_uri import ListingUri
from azext_partnercenter.models.listing import Listing


def marketplace_offer_listing_uri_update_custom(instance, uri_type=None, subtype=None, display_text=None, uri=None):
    listing_uri = ListingUri()
    listing_uri.type = uri_type
    listing_uri.subtype = subtype
    listing_uri.display_text = display_text
    listing_uri.uri = uri
    instance.uris.append(listing_uri)
    return instance


def list_uri(client, offer_id):
    plan_listing = client.get_listing(offer_id)
    if not plan_listing:
        raise CLIError(f'Offer \'{offer_id}\' not found.')

    return plan_listing.uris


def marketplace_offer_listing_uri_delete(client, offer_id, type=None, subtype=None, display_text=None, uri=None):
    listing_uri = ListingUri()
    listing_uri.type = type
    listing_uri.subtype = subtype
    listing_uri.display_text = display_text
    listing_uri.uri = uri

    return client.delete_listing_uri(offer_id, listing_uri)


def _add_set(client, offer_id, parameters=None):
    listing = Listing()
    listing.id = parameters.id
    listing.summary = parameters.summary
    listing.title = parameters.title
    listing.description = parameters.description
    listing.short_description = parameters.short_description
    listing.language_code = parameters.language_code
    listing.odata_etag = parameters.odata_etag
    listing.contacts = parameters.contacts
    listing.uris = parameters.uris
    result = client.create_or_update(offer_id, listing)
    return result


def _add_get(client, product_external_id):
    listing = client.get_listing(product_external_id)
    return listing
