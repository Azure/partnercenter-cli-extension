# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long

from azure.cli.core.commands import CliCommandType
from azext_partnercenter._client_factory import cf_partnercenter


def load_command_table(commands_loader, _):
    sdk = CliCommandType(operations_tmpl='azext_partnercenter.vendored_sdks.azure_mgmt_preview_aks.'
                        'operations._offer_operations#OfferOperations.{}', client_factory=cf_partnercenter)

    with commands_loader.command_group('partnercenter marketplace offer', sdk, is_preview=True) as g:
        g.custom_command('create', 'create_offer', supports_no_wait=True, table_transformer=None)
        g.custom_command('delete', 'delete_offer', confirmation=True, supports_no_wait=True)
        g.custom_show_command('show', 'get_offer', table_transformer=None)
        g.custom_command('list', 'list_offer', table_transformer=None)
        g.generic_update_command('update', setter_name='begin_create_or_update', custom_func_name='update_offer', supports_no_wait=True)
