# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=too-many-locals

from azure.cli.core.util import sdk_no_wait
from knack.util import CLIError
from azext_partnercenter.models.listing_uri import ListingUri
from azext_partnercenter.models.listing import Listing


def marketplace_offer_listing_uri_update_get(cmd, client, product_external_id, type=None, subtype=None, display_text=None, uri=None):
    listing = client.get_listing(product_external_id)
    return listing


def marketplace_offer_listing_uri_update_set(cmd, client, product_external_id, type=None, subtype=None, display_text=None, uri=None, parameters=None):
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
    result = client.create_or_update(product_external_id, listing)
    return result


def marketplace_offer_listing_uri_update_custom(instance, product_external_id, type=None, subtype=None, display_text=None, uri=None):
    listing_uri = ListingUri()
    listing_uri.type = type
    listing_uri.subtype = subtype
    listing_uri.display_text = display_text
    listing_uri.uri = uri
    instance.uris.append(listing_uri)
    return instance


def list_uris(client, product_external_id, type=None, subtype=None, display_text=None, uri=None):
    plan_listing = client.get_listing(product_external_id)
    if not plan_listing:
        raise CLIError(f'There was no plan with a product id of {product_external_id}')

    return plan_listing.uris


def marketplace_offer_listing_uri_delete(cmd, client, product_external_id, type=None, subtype=None, display_text=None, uri=None):
    listing_uri = ListingUri()
    listing_uri.type = type
    listing_uri.subtype = subtype
    listing_uri.display_text = display_text
    listing_uri.uri = uri

    return client.delete_listing_uri(product_external_id, listing_uri)
