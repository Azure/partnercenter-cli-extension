# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long

from azure.cli.core.commands import CliCommandType
from azext_partnercenter._client_factory import cf_offer_listing


def load_command_table(commands_loader, _):
    custom_command_type = CliCommandType(operations_tmpl='azext_partnercenter.operations.marketplace_offer_listing.custom#{}', client_factory=cf_offer_listing)

    with commands_loader.command_group('partnercenter marketplace offer listing', custom_command_type=custom_command_type, is_preview=True) as g:
        g.custom_show_command('show', table_transformer=None)
        g.custom_command('delete', 'offer_listing_delete', confirmation=True)
        g.generic_update_command('update',
                                 getter_name='_update_get',
                                 setter_name='_update_set',
                                 setter_type=custom_command_type,
                                 getter_type=custom_command_type,
                                 custom_func_name='update_listing',
                                 custom_func_type=custom_command_type,
                                 client_factory=cf_offer_listing)
