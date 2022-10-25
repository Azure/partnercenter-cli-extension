# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core.util import sdk_no_wait
from knack.util import CLIError
from azure.cli.core.azclierror import (RequiredArgumentMissingError, ResourceNotFoundError)
from partnercenter.azext_partnercenter.models.plan_listing import PlanListing

# API Operations
# pylint: disable=too-many-locals

def list_listing(cmd, client, offer_id=None, offer_resource_id=None):
   pass

def update_listing(cmd, client, product_external_id, description, short_description):
    plan_listing = PlanListing()
    plan_listing.offer_id = 'bobjacexternalid9'
    plan_listing.description = description
    plan_listing.short_description = short_description
    plan_listing.external_id = 'bobjacexternalid9'
    result = client.create_or_update(product_external_id, plan_listing)
    return result

def marketplace_offer_plan_listing_update_get(cmd, client, external_id, product_external_id, description, short_description):
    print('inside marketplace_offer_plan_listing_update_get')
    plan_listing = client.get_plan_listing(product_external_id, external_id)
    print(plan_listing)
    return plan_listing
    
def marketplace_offer_plan_listing_update_set(cmd, client, external_id, product_external_id, description, short_description, parameters=None):
    print('inside marketplace_offer_plan_listing_update_set')
    print(f'parameters - {parameters}')
    plan_listing = PlanListing()
    plan_listing.id = parameters.id
    plan_listing.external_id = external_id
    plan_listing.description = parameters.description
    plan_listing.short_description = parameters.short_description
    plan_listing.language_code = parameters.language_code
    plan_listing.odata_etag = parameters.odata_etag
    result = client.create_or_update(product_external_id, plan_listing)
    return result

def marketplace_offer_plan_listing_update_custom(instance, external_id, product_external_id, description, short_description):
    print('inside marketplace_offer_plan_listing_update_custom')
    print(f'instance - {instance}')
    instance.short_description = short_description
    instance.description = description
    return instance

def get_listing(cmd, client, offer_id=None, offer_resource_id=None, plan_id=None, plan_resource_id=None):
    pass

def create_listing(cmd, arg):
    raise CLIError('TODO: Implement `partnercenter marketplace offer plan listing create`')
