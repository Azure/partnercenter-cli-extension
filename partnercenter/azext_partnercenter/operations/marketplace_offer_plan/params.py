# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long


def load_arguments(commands_loader, _):
    with commands_loader.argument_context('partnercenter marketplace offer plan') as c:
        c.argument('offer_id', options_list=['--offer-id'], help='The Offer ID.')
        c.argument('plan_id', options_list=['--plan-id', '--id'], help='The Plan ID')

    with commands_loader.argument_context('partnercenter marketplace offer plan create') as c:
        c.argument('name', options_list=['--name', '-n'], help='The friendly name of the Plan.')
