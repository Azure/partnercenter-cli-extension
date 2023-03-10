# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core import AzCommandsLoader
from azure.cli.core.commands import CliCommandType
from azext_partnercenter._help import helps  # pylint: disable=unused-import
from azext_partnercenter.operations import PartnerCenterSubGroupCommandsLoader


class PartnerCenterCommandsLoader(AzCommandsLoader):
    def __init__(self, cli_ctx=None):
        super().__init__(cli_ctx=cli_ctx, custom_command_type=CliCommandType(operations_tmpl="azext_partnercenter#{}"))

        self.subgroups_loader = PartnerCenterSubGroupCommandsLoader(self)

    def load_command_table(self, args):
        self.subgroups_loader.load_command_table(args)
        return self.command_table

    def load_arguments(self, command):
        self.subgroups_loader.load_arguments(command)


COMMAND_LOADER_CLS = PartnerCenterCommandsLoader
