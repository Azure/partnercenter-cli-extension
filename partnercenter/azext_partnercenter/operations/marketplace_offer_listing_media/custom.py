# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core.util import sdk_no_wait
from knack.util import CLIError
from azure.cli.core.azclierror import (RequiredArgumentMissingError, ResourceNotFoundError)


# API Operations
# pylint: disable=too-many-locals

def list_media(cmd, client, offer_id, type="", file=""):
   # check different types.  for now, return images 
   images = client.get_listing_images(offer_id)
   return images

def add_media(cmd, client, offer_id, file, type=""):
    return client.add_listing_image(offer_id, type, file)

def delete_media(cmd, client, offer_id, type):
    result = client.delete_listing_image(offer_id, type)
    return result






