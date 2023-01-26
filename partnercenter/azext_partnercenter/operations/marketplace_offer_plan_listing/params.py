# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long


def load_arguments(commands_loader, _):
    with commands_loader.argument_context('partnercenter marketplace offer plan listing') as c:
        c.argument('offer_id', options_list=['--offer-id'], help='The Offer ID.')
        c.argument('plan_id', options_list=['--plan-id', '--id'], help='The Plan ID.')

    with commands_loader.argument_context('partnercenter marketplace offer plan listing update') as c:
        c.argument('offer_external_id', options_list=['--offer-id'], help='The Offer ID.')
        c.argument('plan_external_id', options_list=['--plan-id', '--id'], help='The Plan ID.')
        c.argument('name', options_list=['--name', '-n'], help='The name of the plan listing.')
        c.argument('summary', options_list=['--summary', '-s'], help='The summary of the plan listing.')
        c.argument('description', options_list=['--description', '-d'], help='The description of the plan listing.')
