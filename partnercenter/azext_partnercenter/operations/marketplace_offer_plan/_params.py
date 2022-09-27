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