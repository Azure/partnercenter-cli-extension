# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=too-many-locals
# pylint: disable=line-too-long

from knack.util import CLIError
from azext_partnercenter.models.listing_uri import ListingUri


def add_uri(instance, uri_type, subtype, display_text, uri):
    listing_uri = ListingUri(
        type=uri_type,
        subtype=subtype,
        display_text=display_text,
        uri=uri
    )
    instance.append(listing_uri)
    return instance


def list_uri(client, offer_id):
    listing = client.get(offer_id)
    if not listing:
        raise CLIError(f'Offer \'{offer_id}\' not found.')
    return listing.uris


def delete_uri(client, offer_id, uri_type=None, subtype=None, display_text=None, uri=None):
    listing_uri = ListingUri()
    listing_uri.type = uri_type
    listing_uri.subtype = subtype
    listing_uri.display_text = display_text
    listing_uri.uri = uri
    return client.delete_uri(offer_id, listing_uri)
