# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long

from azure.cli.core.commands.parameters import (get_enum_type,
                                                get_three_state_flag)


def load_arguments(commands_loader, _):
    with commands_loader.argument_context('partnercenter marketplace offer plan listing') as c:
        c.argument('external_id', options_list=['--external-id'], help='The plan listing external id.')
        c.argument('product_external_id', options_list=['--product-external-id'], help='The product external id.')
        c.argument('description', options_list=['--description'], help='The description of the plan listing.')
        c.argument('short_description', options_list=['--short-description'], help='The description of the plan listing.')
        c.argument('language_code', options_list=['--language-code'], help='The language code of the plan listing.')

        # c.argument('offer_resource_id', options_list=['--offer-resource-id'], help='The Offer Resource ID of the Offer for the Plan in the partner center.')
        # c.argument('offer_id', options_list=['--offer-id'], help='The offer ID of the Offer for the Plan.')

    with commands_loader.argument_context('partnercenter marketplace offer plan listing update') as c:
        c.argument('product_external_id', options_list=['--product-external-id'], help='The product external id.')
        c.argument('description', options_list=['--description'], help='The description of the plan listing.')
        c.argument('short_description', options_list=['--short-description'], help='The description of the plan listing.')
