# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import importlib


class SubGroupOperations:
    """Base for sub group operations loader"""

    def __init__(self, parent):
        self.parent = parent
        self._load_arguments = self._get_module("params").load_arguments
        self._load_command_table = self._get_module("commands").load_command_table

        self.load_help()

    def load_arguments(self, _):
        self._load_arguments(self.parent.commands_loader, _)

    def load_command_table(self, _):
        self._load_command_table(self.parent.commands_loader, _)

    def load_help(self):
        load_help = self._get_module("_help").load_help
        load_help()

    def _get_module(self, module_name):
        return importlib.import_module(f".{module_name}", self.__module__)
