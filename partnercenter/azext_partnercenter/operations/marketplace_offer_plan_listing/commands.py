# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long

from azure.cli.core.commands import CliCommandType

from partnercenter.azext_partnercenter._client_factory import cf_listing


def load_command_table(commands_loader, _):
    custom_command_type = CliCommandType(operations_tmpl='azext_partnercenter.operations.marketplace_offer_plan_listing.custom#{}', client_factory=cf_listing)

    with commands_loader.command_group('partnercenter marketplace offer plan listing', custom_command_type, is_preview=True) as g:
        g.custom_command('add', 'add_listing', supports_no_wait=True, table_transformer=None)
        g.generic_update_command('update',
                                    getter_name='_listing_update_get',
                                    setter_name='_listing_update_set',
                                    custom_func_name='listing_update',
                                    custom_func_type=custom_command_type,
                                    client_factory=cf_listing)
