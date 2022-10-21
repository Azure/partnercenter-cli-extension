# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os
import os.path
import re
import subprocess
import time
#import docker
from azure.cli.core.util import sdk_no_wait
from knack.util import CLIError


# API Operations
# pylint: disable=too-many-locals
def create_offer(cmd, client, offer_id, offer_alias, resource_type):
    result = client.create(offer_id, offer_alias, resource_type)
    return result

def update_offer(cmd, instance, arg):
    # TODO: Implement partnercenter marketplace offer update
    return instance

def delete_offer(cmd, client, product_id):
    results = client.delete(product_id)
    if not results:
        return "Deleted offer: " + product_id
    else:
        raise CLIError("Failed to deleted offer: " + product_id)

def get_offer(cmd):
    raise CLIError('TODO: Implement `partnercenter marketplace offer show`')

def list_offers(cmd, client):
    results = client.list()
    return results

