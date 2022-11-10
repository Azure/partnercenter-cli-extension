# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core.util import sdk_no_wait
from knack.util import CLIError
from azure.cli.core.azclierror import (RequiredArgumentMissingError, ResourceNotFoundError)
from partnercenter.azext_partnercenter.models.listing import Listing
from partnercenter.azext_partnercenter.models.listing_contact import ListingContact

# API Operations
# pylint: disable=too-many-locals

def marketplace_offer_listing_contact_update_get(cmd, client,  product_external_id, type=None, email=None, name=None, phone=None, uri=None):
    listing = client.get_listing(product_external_id)    
    return listing

def marketplace_offer_listing_contact_update_set(cmd, client, product_external_id, type=None, email=None, name=None, phone=None, uri=None, parameters=None):
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
    result = client.create_or_update(product_external_id, listing)
    return result

def marketplace_offer_listing_contact_update_custom(instance, product_external_id, type=None, email=None, name=None, phone=None, uri=None):
    listing_contact = ListingContact()
    listing_contact.type = type
    listing_contact.email = email
    listing_contact.name = name
    listing_contact.phone = phone
    listing_contact.uri = uri
    instance.contacts.append(listing_contact)
    return instance

def list_contacts(cmd, client, product_external_id, type=None, email=None, name=None, phone=None, uri=None):
   listing = client.get_listing(product_external_id)
   if not listing:
    raise CLIError(f'There was no plan with a product id of {product_external_id}')

   return listing.listing_contacts

def marketplace_offer_listing_contact_delete(cmd, client, product_external_id, type=None, email=None, name=None, phone=None, uri=None):
    listing_contact = ListingContact()
    listing_contact.type = type
    listing_contact.email = email
    listing_contact.name = name
    listing_contact.phone = phone
    listing_contact.uri = uri
    return client.delete_listing_contact(product_external_id, listing_contact) 




