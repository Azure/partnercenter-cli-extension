# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long

from azure.cli.core.commands import CliCommandType
from azext_partnercenter._client_factory import cf_offers


# TODO: use https://github.com/Azure/azure-cli/blob/75b08317b30620e9d11e688bcf9bce630a48804c/src/azure-cli/azure/cli/command_modules/appservice/commands.py#L126C33-L126C42
# as a reference for adding exception handling and validation

def load_command_table(commands_loader, _):
    custom_command_type = CliCommandType(operations_tmpl='azext_partnercenter.operations.marketplace_offer_package.custom#{}', client_factory=cf_offers)

    with commands_loader.command_group('partnercenter marketplace offer package', custom_command_type=custom_command_type, is_preview=True) as g:
        g.custom_command('verify', 'verify_package', supports_no_wait=True)
        g.custom_command('build', 'build_package', supports_no_wait=True)
