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
    result = client.update_plan_listing(product_external_id, plan_listing)
    return result
    

def get_listing(cmd, client, offer_id=None, offer_resource_id=None, plan_id=None, plan_resource_id=None):
    pass

def create_listing(cmd, arg):
    raise CLIError('TODO: Implement `partnercenter marketplace offer plan listing create`')
