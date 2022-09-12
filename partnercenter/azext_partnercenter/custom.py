# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.util import CLIError


def create_partnercenter(cmd, resource_group_name, partnercenter_name, location=None, tags=None):
    raise CLIError('TODO: Implement `partnercenter create`')


def list_partnercenter(cmd, resource_group_name=None):
    raise CLIError('TODO: Implement `partnercenter list`')


def update_partnercenter(cmd, instance, tags=None):
    with cmd.update_context(instance) as c:
        c.set_param('tags', tags)
    return instance