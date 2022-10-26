# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long

from azure.cli.core.commands.parameters import (get_enum_type,
                                                get_three_state_flag)


def load_arguments(commands_loader, _):
    with commands_loader.argument_context('partnercenter marketplace offer plan listing contact list') as c:
        c.argument('plan_external_id', options_list=['--plan-external-id'], help='The plan external id.')
        c.argument('product_external_id', options_list=['--product-external-id'], help='The product external id.')
        c.argument('type', options_list=['--type'], help='The contact type.')
        c.argument('email', options_list=['--email'], help='The email address of the contact.')
        c.argument('name', options_list=['--name'], help='The name of the contact.')
        c.argument('phone', options_list=['--phone'], help='The phone number of the contact.')
        c.argument('uri', options_list=['--uri'], help='The uri associated with the contact.')


