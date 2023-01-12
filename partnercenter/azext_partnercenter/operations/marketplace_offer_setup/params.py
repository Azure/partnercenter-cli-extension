# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long

from enum import Enum
from azure.cli.core.commands.parameters import get_three_state_flag
from .validators import validate_test_drive


class Arg(str, Enum):
    """Setup command Arguments"""
    reseller = 'reseller',
    test_drive = 'test_drive',
    sell_through_microsoft = 'sell_through_microsoft'

arg_help = {
    Arg.reseller: 'Indicates to enable the reseller channel for the offer.',
    Arg.test_drive: """Whether test drive is enabled for the offer. The test drive option in the Microsoft commercial marketplace lets you configure a hands-on, self-guided tour of your product's key features""",
    Arg.sell_through_microsoft: """Whether to sell through microsoft or list the offer through the marketplace and process transactions independently."""
}

def load_arguments(commands_loader, _):
    with commands_loader.argument_context('partnercenter marketplace offer setup') as c:
        c.argument('offer_id', options_list=['--offer-id', '--id'], help='The Offer ID.')

    with commands_loader.argument_context('partnercenter marketplace offer setup update') as c:
        c.argument('offer_external_id', options_list=['--offer-id', '--id'], help='The Offer ID.')
        c.argument(Arg.reseller, arg_type=get_three_state_flag(), options_list=['--reseller'], help=arg_help[Arg.reseller])
        c.argument(Arg.test_drive, arg_type=get_three_state_flag(), options_list=['--test-drive'], help=arg_help[Arg.test_drive], validator=validate_test_drive)
        c.argument(Arg.sell_through_microsoft, arg_type=get_three_state_flag(), options_list=['--sell-through-microsoft'], help=arg_help[Arg.sell_through_microsoft])
        c.argument('trial_uri', options_list=['--trial-uri'], help='The trial uri.')
