# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long

from azure.cli.core.commands.parameters import (get_enum_type,
                                                get_three_state_flag)


def load_arguments(commands_loader, _):
    with commands_loader.argument_context('partnercenter marketplace offer plan') as c:
        c.argument('offer_id', options_list=['--offer-id'], help='The Offer ID.')
    
    with commands_loader.argument_context('partnercenter marketplace offer plan update') as c:
        c.argument('plan_id', options_list=['--plan-id', '--id'], help='The Plan ID')

    with commands_loader.argument_context('partnercenter marketplace offer plan delete') as c:
        c.argument('plan_id', options_list=['--plan-id', '--id'], help='The Plan ID')

    with commands_loader.argument_context('partnercenter marketplace offer plan create') as c:
        c.argument('plan_id', options_list=['--plan-id', '--id'], help='The Plan ID')
        c.argument('friendly_name', options_list=['--friendly-name'], help='The friendly name')
