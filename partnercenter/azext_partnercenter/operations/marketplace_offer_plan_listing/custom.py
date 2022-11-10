# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core.util import sdk_no_wait
from knack.util import CLIError
from azure.cli.core.azclierror import (RequiredArgumentMissingError, ResourceNotFoundError)
from partnercenter.azext_partnercenter.models.listing import Listing

# API Operations
# pylint: disable=too-many-locals

def list_listing(cmd, client, offer_id=None, offer_resource_id=None):
   pass


def marketplace_offer_plan_listing_update_get(client, offer_id, plan_id, description=None, short_description=None, language_code=None):
    plan_listing = client.get_plan_listing(offer_id, plan_id)
    return plan_listing
    
def marketplace_offer_plan_listing_update_set(client, offer_id, plan_id, description=None, short_description=None, language_code=None, parameters=None):
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
    result = client.create_or_update(offer_id, listing, plan_id)
    return result

def marketplace_offer_plan_listing_update_custom(instance, description=None, short_description=None, language_code=None):
    instance.short_description = short_description
    instance.description = description
    instance.laguage_code = language_code
    return instance

def get_listing(cmd, client, offer_id=None, plan_id=None):
    pass

def add_listing(cmd, arg):
    raise CLIError('TODO: Implement `partnercenter marketplace offer plan listing create`')
