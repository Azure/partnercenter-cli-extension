# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core.util import sdk_no_wait
from knack.util import CLIError
from azure.cli.core.azclierror import (RequiredArgumentMissingError, ResourceNotFoundError)

def list_submission(client, offer_id):
    return client.list(offer_id)


def get_submission(client, offer_id):
    return client.get(offer_id)


def update_submission(cmd, instance, arg):
    # TODO: Implement partnercenter marketplace offer update
    return instance

def delete_submission(client, offer_id):
    pass

