# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core.util import sdk_no_wait
from knack.util import CLIError
from azure.cli.core.azclierror import (RequiredArgumentMissingError, ResourceNotFoundError)
from partnercenter.azext_partnercenter.models.listing import Listing


def get_setup(client, offer_id):
    return client.get_setup(offer_id)

def create_setup(client, offer_id, reseller_enabled=False, test_drive_enabled=False, selling_option='ListingOnly', trial_uri=''):
    return client.create_setup(offer_id, test_drive_enabled, reseller_enabled, selling_option, trial_uri)

def marketplace_offer_setup_update_get(cmd, client, offer_id, summary=None, short_description=None, description=None):
    listing = client.get_listing(offer_id)    
    return listing

def marketplace_offer_setup_update_set(cmd, client, offer_id, summary=None, short_description=None, description=None, parameters=None):
    listing = Listing()
    listing.id = parameters.id
    listing.title = parameters.title
    listing.summary = parameters.summaryrm 
    listing.description = parameters.description
    listing.short_description = parameters.short_description
    listing.language_code = parameters.language_code
    listing.odata_etag = parameters.odata_etag
    listing.contacts = parameters.contacts
    listing.uris = parameters.uris
    result = client.create_or_update(offer_id, listing)
    return result

def marketplace_offer_setup_update_custom(instance, offer_id, summary=None, short_description=None, description=None):
    instance.summary = summary
    instance.short_description = short_description
    instance.description = description
    return instance




