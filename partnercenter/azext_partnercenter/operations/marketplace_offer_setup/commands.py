# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long

from azure.cli.core.commands import CliCommandType
from azext_partnercenter._client_factory import cf_offers


def load_command_table(commands_loader, _):
    operations_tmpl='azext_partnercenter.operations.marketplace_offer_setup.custom#{}'
    custom_command_type = CliCommandType(operations_tmpl=operations_tmpl, client_factory=cf_offers)

    with commands_loader.command_group('partnercenter marketplace offer setup', custom_command_type=custom_command_type, is_preview=True) as g:
        g.custom_show_command('show', 'get_setup', table_transformer=None)
        g.custom_command('create', 'create_setup', supports_no_wait=True, table_transformer=None)        
