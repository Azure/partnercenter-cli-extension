# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core.util import sdk_no_wait
from knack.util import CLIError
from azure.cli.core.azclierror import (RequiredArgumentMissingError, ResourceNotFoundError)


# API Operations
# pylint: disable=too-many-locals

def list_media(cmd, client, plan_external_id, product_external_id, type="", file=""):
   # check different types.  for now, return images 
   print('list_media called')
   images = client.get_plan_listing_images(product_external_id, plan_external_id)
   return images

def add_media(cmd, client, plan_external_id, product_external_id, file, type=""):
    print(f'add_media: plan_external_id - {plan_external_id}, product_external_id - {product_external_id}, file - {file}, type - {type}')
    return client.add_plan_listing_image(product_external_id, plan_external_id, type, file)







