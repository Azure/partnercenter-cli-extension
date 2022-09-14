# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core import AzCommandsLoader

from azext_partnercenter._help import helps  # pylint: disable=unused-import


class PartnerCenterCommandsLoader(AzCommandsLoader):

    def __init__(self, cli_ctx=None):
        from azure.cli.core.commands import CliCommandType
        from azext_partnercenter._client_factory import cf_partnercenter
        from azext_partnercenter.operations import PartnerCenterSubGroupCommandsLoader

        self.subgroups_loader = PartnerCenterSubGroupCommandsLoader(self)
        partnercenter_custom = CliCommandType(
            operations_tmpl='azext_partnercenter.custom#{}',
            client_factory=cf_partnercenter)
        super(PartnerCenterCommandsLoader, self).__init__(cli_ctx=cli_ctx,
                                                  custom_command_type=partnercenter_custom)

    def load_command_table(self, args):
        from azext_partnercenter.commands import load_command_table
        load_command_table(self, args)
        self.subgroups_loader.load_command_table(args)

        return self.command_table

    def load_arguments(self, command):
        from azext_partnercenter._params import load_arguments
        load_arguments(self, command)
        self.subgroups_loader.load_arguments(command)


COMMAND_LOADER_CLS = PartnerCenterCommandsLoader
