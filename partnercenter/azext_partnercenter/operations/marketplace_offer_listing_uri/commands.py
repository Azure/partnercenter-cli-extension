# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long

from azure.cli.core.commands import CliCommandType

from azext_partnercenter._client_factory import cf_listing


def load_command_table(commands_loader, _):
    custom_command_type = CliCommandType(operations_tmpl='azext_partnercenter.operations.marketplace_offer_listing_uri.custom#{}', client_factory=cf_listing)

    with commands_loader.command_group('partnercenter marketplace offer listing uri', custom_command_type, is_preview=True) as g:
        g.custom_command('list', 'list_uris', table_transformer=None, custom_command_type=custom_command_type)
        g.custom_command('delete', 'marketplace_offer_listing_uri_delete', confirmation=True, custom_command_type=custom_command_type)
        g.generic_update_command('add',
                                    getter_name='marketplace_offer_listing_uri_update_get',
                                    setter_name='marketplace_offer_listing_uri_update_set',
                                    custom_func_name='marketplace_offer_listing_uri_update_custom',
                                    custom_func_type=custom_command_type,
                                    client_factory=cf_listing)

