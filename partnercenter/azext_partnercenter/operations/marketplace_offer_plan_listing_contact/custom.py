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

def list_contacts(cmd, client, plan_external_id, product_external_id, type=None, email=None, name=None, phone=None, uri=None):
   plan_listing = client.get_plan_listing(product_external_id, plan_external_id)
   if not plan_listing:
    raise CLIError(f'There was no plan with a product id of {product_external_id} anf a plan id of {plan_external_id}')

   return plan_listing.listing_contacts

