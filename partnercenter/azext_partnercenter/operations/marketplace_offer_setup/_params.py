# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long

from azure.cli.core.commands.parameters import (get_enum_type,
                                                get_three_state_flag)


def load_arguments(commands_loader, _):
    with commands_loader.argument_context('partnercenter marketplace offer setup') as c:
        c.argument('offer_id', options_list=['--offer-id'], help='The offer ID of the Offer.')
        c.argument('reseller_enabled', options_list=['--enable-resell'], help='Boolen value indicating if reseller is enabled.')
        c.argument('test_drive_enabled', options_list=['--enable-test-drive'], help='Boolen value indicating if test drive is enabled.')
        c.argument('selling_option', options_list=['--selling-option'], help='The selling option.')
        c.argument('trial_uri', options_list=['--trial-uri'], help='The trial uri.')
