# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long

from azure.cli.core.commands import CliCommandType

from azext_partnercenter._client_factory import cf_plan_technicalconfiguration


def load_command_table(commands_loader, _):
    custom_command_type = CliCommandType(operations_tmpl='azext_partnercenter.operations.marketplace_offer_plan_technicalconfiguration.custom#{}', client_factory=cf_plan_technicalconfiguration)

    with commands_loader.command_group('partnercenter marketplace offer plan technical-configuration', custom_command_type=custom_command_type, is_preview=True) as g:
        g.custom_show_command('show', 'get_technicalconfiguration')

    with commands_loader.command_group('partnercenter marketplace offer plan technical-configuration package', custom_command_type=custom_command_type, is_preview=True) as g:
        g.custom_command('add', 'add_technical_configuration_bundle', supports_no_wait=True, table_transformer=None)
        g.custom_command('delete', 'delete_technicalconfiguration_package', supports_no_wait=True)
