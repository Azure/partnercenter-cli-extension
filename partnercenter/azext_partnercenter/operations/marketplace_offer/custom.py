# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core.util import sdk_no_wait
from knack.util import CLIError

# API Operations
# pylint: disable=too-many-locals
def create_offer(client, arg):
    raise CLIError('TODO: Implement `partnercenter marketplace offer create`')


def update_api(instance, arg):
    # TODO: Implement partnercenter marketplace offer update
    return instance


def delete_offer(client):
    raise CLIError('TODO: Implement `partnercenter marketplace offer delete`')

def get_offer(client):
    raise CLIError('TODO: Implement `partnercenter marketplace offer show`')


def list_offer(client):
    raise CLIError('TODO: Implement `partnercenter marketplace offer show`')
