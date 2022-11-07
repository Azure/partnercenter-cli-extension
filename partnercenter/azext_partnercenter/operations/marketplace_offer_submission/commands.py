# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long

from azure.cli.core.commands import CliCommandType
from partnercenter.azext_partnercenter._client_factory import cf_submission


def load_command_table(commands_loader, _):
    custom_command_type = CliCommandType(operations_tmpl='azext_partnercenter.operations.marketplace_offer_submission.custom#{}', client_factory=cf_submission)

    with commands_loader.command_group('partnercenter marketplace offer submission', custom_command_type=custom_command_type, is_preview=True) as g:
        g.custom_command('list', 'list_submission')
        # g.custom_show_command('show', 'get_submission')
        # g.custom_command('update', 'update_submission', supports_no_wait=True, table_transformer=None)
        # g.custom_command('delete', 'delete_submission', confirmation=True, supports_no_wait=True)
