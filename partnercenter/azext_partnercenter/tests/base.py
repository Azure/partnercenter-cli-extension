# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import time
from azure.cli.testsdk import ScenarioTest


class PartnerCenterScenarioTest(ScenarioTest):
    def cmd(self, command, checks=None, expect_failure=False, delay=0):
        """cmd that supports adding a delay into the execution of a command."""
        if delay > 0:
            time.sleep(delay)
        return super().cmd(command, checks=checks, expect_failure=expect_failure)
    