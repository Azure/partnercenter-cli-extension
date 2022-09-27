# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core.util import sdk_no_wait
from knack.util import CLIError

# API Operations
# pylint: disable=too-many-locals

def list_plan(cmd, client):
    results = client.list()
    return results


def create_plan(cmd, arg):
    raise CLIError('TODO: Implement `partnercenter marketplace offer create`')


def update_plan(cmd, instance, arg):
    # TODO: Implement partnercenter marketplace offer update
    return instance


def delete_plan(cmd):
    raise CLIError('TODO: Implement `partnercenter marketplace offer plan delete`')


def get_plan(cmd):
    raise CLIError('TODO: Implement `partnercenter marketplace offer plan show`')
