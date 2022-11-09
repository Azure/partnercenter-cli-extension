# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long

from azure.cli.core.commands.parameters import (get_enum_type,
                                                get_three_state_flag)


def load_arguments(commands_loader, _):
    with commands_loader.argument_context('partnercenter marketplace offer listing update') as c:
        c.argument('offer_id', options_list=['--offer-id'], help='The offer ID of the Offer for the Plan.')
        c.argument('summary', options_list=['--summary'], help='The summary that appears in search results.')
        c.argument('short_description', options_list=['--short-description'], help='The short description of the listing.')
        c.argument('description', options_list=['--description'], help='The description of the listing.')