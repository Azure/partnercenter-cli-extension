# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long

from azure.cli.core.commands.parameters import (get_enum_type,
                                                get_three_state_flag)


def load_arguments(commands_loader, _):
    with commands_loader.argument_context('partnercenter marketplace offer plan listing') as c:
        c.argument('offer_id', options_list=['--offer-id'], help='The Offer ID.')
        c.argument('plan_id', options_list=['--plan-id', '--id'], help='The Plan ID.')
        c.argument('description', options_list=['--description'], help='The description of the plan listing.')
        c.argument('short_description', options_list=['--short-description'], help='The description of the plan listing.')
        c.argument('language_code', options_list=['--language-code'], help='The language code of the plan listing.')

