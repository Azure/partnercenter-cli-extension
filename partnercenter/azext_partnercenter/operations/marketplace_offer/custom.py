# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os
import os.path
import re
import subprocess
import time
from azext_partnercenter.models import offer
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

def delete_offer(cmd, client, offer_id):
    results = client.delete(offer_id)
    if not results:
        return "Deleted offer: " + offer_id
    else:
        raise CLIError("Failed to deleted offer: " + offer_id)

def get_offer(client, offer_id):
    return client.get(offer_id)


def list_offer(client):
    return client.list()

