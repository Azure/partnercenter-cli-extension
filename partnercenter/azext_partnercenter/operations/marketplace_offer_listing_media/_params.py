# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long

from azure.cli.core.commands.parameters import (get_enum_type,
                                                get_three_state_flag)


def load_arguments(commands_loader, _):
    with commands_loader.argument_context('partnercenter marketplace offer listing media') as c:
        #c.argument('plan_external_id', options_list=['--offer-id'], help='The offer id.')
        c.argument('product_external_id', options_list=['--offer-id'], help='The product external id.')
        c.argument('type', options_list=['--type'], help='The type of the uri.')
        c.argument('file', options_list=['--file'], help='The type of the uri.')

