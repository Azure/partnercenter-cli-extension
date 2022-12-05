# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long

from knack.util import CLIError
from azext_partnercenter.models.listing import Listing
from azext_partnercenter.models.listing_contact import ListingContact


def marketplace_offer_listing_contact_update_get(client, offer_id):
    listing = client.get_listing(offer_id)
    return listing


def marketplace_offer_listing_contact_update_set(client, offer_id, parameters=None):
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


def marketplace_offer_listing_contact_update_custom(instance, type=None, email=None, name=None, phone=None, uri=None):
    listing_contact = ListingContact()
    listing_contact.type = type
    listing_contact.email = email
    listing_contact.name = name
    listing_contact.phone = phone
    listing_contact.uri = uri
    instance.contacts.append(listing_contact)
    return instance


def list_contacts(client, offer_id):
    listing = client.get_listing(offer_id)
    if not listing:
        raise CLIError(f'Listing contacts not found for Offer "{offer_id}"')

    return listing.contacts


def marketplace_offer_listing_contact_delete(client, offer_id, type=None, email=None, name=None, phone=None, uri=None):
    listing_contact = ListingContact()
    listing_contact.type = type
    listing_contact.email = email
    listing_contact.name = name
    listing_contact.phone = phone
    listing_contact.uri = uri
    return client.delete_listing_contact(offer_id, listing_contact)
