# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core.util import sdk_no_wait
from knack.util import CLIError
from azure.cli.core.azclierror import (RequiredArgumentMissingError, ResourceNotFoundError)


def get_listing(cmd, arg):
    raise CLIError('TODO: Implement `partnercenter marketplace offer create`')


def update_listing(cmd, instance, arg):
    # TODO: Implement partnercenter marketplace offer update
    return instance
