# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core.util import sdk_no_wait
from knack.util import CLIError
from azure.cli.core.azclierror import (RequiredArgumentMissingError, ResourceNotFoundError)
from partnercenter.azext_partnercenter.models.plan_listing import PlanListing
from partnercenter.azext_partnercenter.models.listing_contact import ListingContact

# API Operations
# pylint: disable=too-many-locals

def marketplace_offer_plan_listing_contact_update_get(cmd, client, plan_external_id, product_external_id, type=None, email=None, name=None, phone=None, uri=None):
    plan_listing = client.get_plan_listing(product_external_id, plan_external_id)
    print(f'plan_listing - {plan_listing}')
    #plan_listing = PlanListing()
    #plan_listing.external_id = plan_external_id

    # plan_listing.id = result.id
   # plan_listing.language_code = result.language_code
    
    #plan_listing.uris = []
    #plan_listing.odata_etag = result.odata_etag
    #plan_listing.description = result.description
    #plan_listing.short_description = result.short_description

    #contacts = []
    #for c in result.listing_contacts:
    #    listing_contact = ListingContact()
    #    listing_contact.email = c.email
    #    listing_contact.phone = c.phone
    #    listing_contact.name = c.name
    #    listing_contact.uri = c.uri
    #    listing_contact.type = c.type
    #    contacts.append(listing_contact)

    #plan_listing.contacts = contacts

    #plan_listing.contacts = list(map())
    
    return plan_listing

def marketplace_offer_plan_listing_contact_update_set(cmd, client, plan_external_id, product_external_id, type=None, email=None, name=None, phone=None, uri=None, parameters=None):
    print(f'inside marketplace_offer_plan_listing_contact_update_set with parameters of - {parameters}')

    plan_listing = PlanListing()
    plan_listing.id = parameters.id
    plan_listing.external_id = plan_external_id
    plan_listing.description = parameters.description
    plan_listing.short_description = parameters.short_description
    plan_listing.language_code = parameters.language_code
    plan_listing.odata_etag = parameters.odata_etag
    plan_listing.contacts = parameters.contacts
    plan_listing.uris = parameters.uris

    result = client.create_or_update(product_external_id, plan_listing)
    return result

def marketplace_offer_plan_listing_contact_update_custom(instance, plan_external_id, product_external_id, type=None, email=None, name=None, phone=None, uri=None):
    print(f'instance - {instance}')
    
    listing_contact = ListingContact()
    listing_contact.type = type
    listing_contact.email = email
    listing_contact.name = name
    listing_contact.phone = phone
    listing_contact.uri = uri

    instance.contacts.append(listing_contact)

    return instance

def list_contacts(cmd, client, plan_external_id, product_external_id, type=None, email=None, name=None, phone=None, uri=None):
   plan_listing = client.get_plan_listing(product_external_id, plan_external_id)
   if not plan_listing:
    raise CLIError(f'There was no plan with a product id of {product_external_id} anf a plan id of {plan_external_id}')

   return plan_listing.listing_contacts



