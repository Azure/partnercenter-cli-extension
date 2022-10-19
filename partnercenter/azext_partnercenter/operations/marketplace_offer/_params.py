# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long

from azure.cli.core.commands.parameters import (get_enum_type, get_three_state_flag)


def load_arguments(commands_loader, _):
    # pass

    with commands_loader.argument_context('partnercenter marketplace offer list') as c:
        c.argument('product_id', options_list=['--product_id', '-p'], help='The ID of product')
        c.argument('instance_id', options_list=['--instance_id', '-i'], help='The Resource instance ID')

    with commands_loader.argument_context('partnercenter marketplace offer create') as d:
        d.argument('offer_id', options_list=['--offer-id', '-id'], help='Use only lowercase, alphanumeric characters, dashes or underscores. ID cannot be modified after selecting Create.')
        d.argument('offer_alias', options_list=['--offer-alias', '-a'], help='This name won\'t be used in the marketplace listing and is solely for reference within Partner Center.')
        d.argument('resource_type', options_list=['--resource-type', '-t'], help='The type of offer to create.')