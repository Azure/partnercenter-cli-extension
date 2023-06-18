# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long

from azure.cli.core.commands import CliCommandType
from azext_partnercenter._client_factory import cf_offer_listing


def load_command_table(commands_loader, _):
    command_type = CliCommandType(operations_tmpl='azext_partnercenter.clients#OfferListingClient.{}', client_factory=cf_offer_listing)
    custom_command_type = CliCommandType(operations_tmpl='azext_partnercenter.operations.marketplace_offer_listing.custom#{}', client_factory=cf_offer_listing)

    with commands_loader.command_group('partnercenter marketplace offer listing', command_type=command_type, custom_command_type=custom_command_type, is_preview=True) as g:
        g.custom_show_command('show', 'get_listing', table_transformer=None)
        g.generic_update_command('update', custom_func_name='update_listing', getter_name='get', setter_name='update')
