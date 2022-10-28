# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core.util import sdk_no_wait
from knack.util import CLIError
from azure.cli.core.azclierror import (RequiredArgumentMissingError, ResourceNotFoundError)
from partnercenter.azext_partnercenter.models.listing_uri import ListingUri
from partnercenter.azext_partnercenter.models.plan_listing import PlanListing
from partnercenter.azext_partnercenter.models.listing_contact import ListingContact

# API Operations
# pylint: disable=too-many-locals

def marketplace_offer_plan_listing_uri_update_get(cmd, client, plan_external_id, product_external_id, type="", subtype="", display_text="", uri=""):
    plan_listing = client.get_plan_listing(product_external_id, plan_external_id)    
    return plan_listing

def marketplace_offer_plan_listing_uri_update_set(cmd, client, plan_external_id, product_external_id, type="", subtype="", display_text="", uri="", parameters=None):
    print(f'parameters.uris - {parameters.uris}')
    for u in parameters.uris:
        print(f'u - {u}')
    plan_listing = PlanListing()
    plan_listing.id = parameters.id
    plan_listing.external_id = plan_external_id
    plan_listing.description = parameters.description
    plan_listing.short_description = parameters.short_description
    plan_listing.language_code = parameters.language_code
    plan_listing.odata_etag = parameters.odata_etag
    plan_listing.contacts = parameters.contacts
    plan_listing.uris = parameters.uris

    print(f'updated plan listing uris in custom.py')
    for uri in plan_listing.uris:
        print(f'uri - {uri}')

    result = client.create_or_update(product_external_id, plan_listing)
    return result

def marketplace_offer_plan_listing_uri_update_custom(instance, plan_external_id, product_external_id, type="", subtype="", display_text="", uri=""):
    print(f'inside marketplace_offer_plan_listing_uri_update_custom')
    print(f'type - {type}')
    print(f'display_text - {display_text}')
    listing_uri = ListingUri()
    listing_uri.type = type
    listing_uri.subtype = subtype
    listing_uri.display_text = display_text
    listing_uri.uri = uri
    print(f'listing_uri - {listing_uri.as_dict()}')
    instance.uris.append(listing_uri)

    print(f'created instance - {instance.uris}')

    return instance

def list_uris(cmd, client, plan_external_id, product_external_id, type="", subtype="", display_text="", uri=""):
   plan_listing = client.get_plan_listing(product_external_id, plan_external_id)
   if not plan_listing:
    raise CLIError(f'There was no plan with a product id of {product_external_id} anf a plan id of {plan_external_id}')

   return plan_listing.uris

def marketplace_offer_plan_listing_uri_delete(cmd, client, plan_external_id, product_external_id, type="", subtype="", display_text="", uri=""):
    listing_uri = ListingUri()
    listing_uri.type = type
    listing_uri.subtype = subtype
    listing_uri.display_text = display_text
    listing_uri.uri = uri
    return client.delete_plan_listing_uri(product_external_id, plan_external_id, listing_uri) 




