# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long

from azure.cli.core.commands.parameters import (get_enum_type,
                                                get_three_state_flag)


def load_arguments(commands_loader, _):
    with commands_loader.argument_context('partnercenter marketplace offer plan') as c:
        c.argument('productId', options_list=['--id'], help='The system ID of the offer in the partner center.')
        c.argument('offerId', options_list=['--azure-offer-id', '--offer-id'], help='The offer ID')

    with commands_loader.argument_context('partnercenter marketplace offer plan create') as d:
        d.argument('product_id', options_list=['--product-id'], help='The system ID of the offer in the partner center.')
        d.argument('external_id', options_list=['--external-id'], help='The external ID')
        d.argument('friendly_name', options_list=['--friendly-name'], help='The friendly name')