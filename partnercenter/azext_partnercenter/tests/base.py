# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from abc import ABC, abstractmethod
import os
import time
from azure.cli.testsdk import ScenarioTest


class PartnerCenterScenarioTest(ScenarioTest, ABC):
    def __init__(self, method_name, config_file=None, recording_name=None, recording_processors=None, replay_processors=None, recording_patches=None, replay_patches=None):
        super().__init__(method_name, config_file, recording_name, recording_processors, replay_processors, recording_patches, replay_patches)
        self.cmd_delay = 0
        self.test_data = TestData()

    def setUp(self):
        self.init_args()
        super().setUp()

    def cmd(self, command, checks=None, expect_failure=False, delay=0):
        """cmd that supports adding a delay into the execution of a command."""
        if delay > 0 or self.cmd_delay > 0:
            if delay > 0:
                time.sleep(delay)
            else:
                time.sleep(self.cmd_delay)
        return super().cmd(command, checks=checks, expect_failure=expect_failure)

    @abstractmethod
    def init_args(self):
        """initialize all the args needed for the test. Called on setUp by the test scaffolding."""
        pass


class TestData:
    """Test Data from the file system"""

    TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))
    """The root test directory path"""

    def __init__(self, test_data_dir='latest/data'):
        self.test_data_dir = os.path.join(self.TEST_DIR, test_data_dir).replace('\\', '\\\\')
        self._ensure_dir(self.test_data_dir)

        self.data = {}

    def list(self):
        """Returns the list of data files that have been added"""
        return self.data.items()

    def clear(self):
        """Clears all test data"""
        self.data.clear()

    def add(self, file_path):
        """Adds the test data file to the set of test data and returns the absolute path for the test data file"""
        abs_file_path = os.path.join(self.test_data_dir, file_path).replace('\\', '\\\\')
        self.data[file_path] = abs_file_path

        return abs_file_path

    def _ensure_dir(self, dirpath):
        if not os.path.exists(dirpath):
            os.makedirs(dirpath)
