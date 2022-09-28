# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long

from azure.cli.core.commands.parameters import (get_enum_type, get_three_state_flag)


def load_arguments(commands_loader, _):
    pass
    # with commands_loader.argument_context('partnercenter marketplace offer') as c:
    #     c.argument('arg', options_list=['--arg', '-a'], help='The argument help')
    with commands_loader.argument_context('partnercenter marketplace offer list') as c:
        c.argument('product_id', options_list=['--product_id', '-p'], help='The ID of product')
        c.argument('instance_id', options_list=['--instance_id', '-i'], help='The Resource instance ID')