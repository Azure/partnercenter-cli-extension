# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import time
from azure.cli.testsdk import ScenarioTest


class PartnerCenterScenarioTest(ScenarioTest):
    def __init__(self, method_name, config_file=None, recording_name=None, recording_processors=None, replay_processors=None, recording_patches=None, replay_patches=None):
        super().__init__(method_name, config_file, recording_name, recording_processors, replay_processors, recording_patches, replay_patches)
        self.cmd_delay = 0

    def cmd(self, command, checks=None, expect_failure=False, delay=0):
        """cmd that supports adding a delay into the execution of a command."""
        if delay > 0 or self.cmd_delay > 0:
            if delay > 0:
                time.sleep(delay)
            else:
                time.sleep(self.cmd_delay)
        return super().cmd(command, checks=checks, expect_failure=expect_failure)
    