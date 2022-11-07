# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long

from azure.cli.core.commands import CliCommandType

from partnercenter.azext_partnercenter._client_factory import cf_listing_media


def load_command_table(commands_loader, _):
    custom_command_type = CliCommandType(operations_tmpl='azext_partnercenter.operations.marketplace_offer_listing_media.custom#{}', client_factory=cf_listing_media)

    with commands_loader.command_group('partnercenter marketplace offer listing media', custom_command_type, is_preview=True) as g:
        g.custom_command('list', 'list_media', table_transformer=None, custom_command_type=custom_command_type)
        g.custom_command('add', 'add_media', table_transformer=None, custom_command_type=custom_command_type)
        g.custom_command('delete', 'delete_media', table_transformer=None, custom_command_type=custom_command_type)
        

