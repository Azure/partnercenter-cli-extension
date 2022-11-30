# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long


def load_arguments(commands_loader, _):
    with commands_loader.argument_context('partnercenter marketplace offer listing contact') as c:
        c.argument('offer_id', options_list=['--offer-id'], help='The offerid.')
        c.argument('type', options_list=['--type'], help='The contact type.')
        c.argument('email', options_list=['--email'], help='The email address of the contact.')
        c.argument('name', options_list=['--name'], help='The name of the contact.')
        c.argument('phone', options_list=['--phone'], help='The phone number of the contact.')
        c.argument('uri', options_list=['--uri'], help='The uri associated with the contact.')
