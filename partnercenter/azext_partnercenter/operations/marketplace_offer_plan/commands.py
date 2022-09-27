# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long

from azure.cli.core.commands import CliCommandType


def load_command_table(commands_loader, _):
    custom_command_type = CliCommandType(operations_tmpl='azext_partnercenter.operations.marketplace_offer_plan.custom#{}', client_factory=_get_client_factory)

    with commands_loader.command_group('partnercenter marketplace offer plan', custom_command_type=custom_command_type, is_preview=True) as g:
        # g.custom_command('create', 'create_offer', supports_no_wait=True, table_transformer=None)
        # g.custom_command('delete', 'delete_offer', confirmation=True, supports_no_wait=True)
        # g.custom_show_command('show', 'get_offer', table_transformer=None)
        g.custom_command('list', 'list_plan', table_transformer=None)
        #g.custom_command('bundle', 'bundle_offer', supports_no_wait=True, table_transformer=None)


def _get_client_factory(cli_ctx, *_):
    from ._client import PlanClient
    client = PlanClient(cli_ctx, *_)
    return client