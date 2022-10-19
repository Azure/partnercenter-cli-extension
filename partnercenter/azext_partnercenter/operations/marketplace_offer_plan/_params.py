# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long

from azure.cli.core.commands.parameters import (get_enum_type,
                                                get_three_state_flag)


def load_arguments(commands_loader, _):
    with commands_loader.argument_context('partnercenter marketplace offer plan') as c:
        c.argument('offer_resource_id', options_list=['--offer-resource-id'], help='The Offer Resource ID of the Offer for the Plan in the partner center.')
        c.argument('offer_id', options_list=['--azure-offer-id', '--offer-id'], help='The offer ID of the Offer for the Plan.')