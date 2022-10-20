# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core.util import sdk_no_wait
from knack.util import CLIError
from azure.cli.core.azclierror import (RequiredArgumentMissingError, ResourceNotFoundError)

# API Operations
# pylint: disable=too-many-locals

def list_setup(cmd, client, offer_id=None, offer_resource_id=None):
   pass

def get_setup(cmd, client, offer_id=None, offer_resource_id=None, plan_id=None, plan_resource_id=None):
    pass

def create_setup(cmd, arg):
    raise CLIError('TODO: Implement `partnercenter marketplace offer plan setup create`')
