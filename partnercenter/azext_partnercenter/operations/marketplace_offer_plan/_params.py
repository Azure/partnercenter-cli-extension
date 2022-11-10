# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long

from azure.cli.core.commands.parameters import (get_enum_type,
                                                get_three_state_flag)


def load_arguments(commands_loader, _):
    with commands_loader.argument_context('partnercenter marketplace offer plan list') as c:
        c.argument('offer_id', options_list=['--offer-id'], help='The offer id in the partner center.')

    with commands_loader.argument_context('partnercenter marketplace offer plan create') as c:
        c.argument('product_external_id', options_list=['--product-external-id'], help='The system ID of the offer in the partner center.')
        c.argument('external_id', options_list=['--external-id'], help='The external ID')
        c.argument('friendly_name', options_list=['--friendly-name'], help='The friendly name')

    with commands_loader.argument_context('partnercenter marketplace offer plan delete') as c:
        c.argument('offer_id', options_list=['--offer-id'], help='The Offer ID')
        c.argument('plan_id', options_list=['--plan-id'], help='The Plan ID')

    with commands_loader.argument_context('partnercenter marketplace offer plan show') as c:
        c.argument('plan_resource_id', options_list=['--plan-resource-id'], help='The Offer Resource ID of the Offer for the Plan in the partner center.')
        c.argument('plan_id', options_list=['--plan-id', '--id'], help='The Plan ID.')
