# -----------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# -----------------------------------------------------------------------------

import os
from azure.cli.testsdk import LiveScenarioTest
from azure.cli.testsdk.reverse_dependency import get_dummy_cli
from azure.cli.testsdk.scenario_tests import SingleValueReplacer, AbstractPreparer

# This preparer's traffic is not recorded.
# As a result when tests are run in record mode, sdk calls cannot be made to return the prepared resource group.
# Rather the deterministic prepared resource's information should be returned.
class NoTrafficRecordingPreparer(AbstractPreparer):
    from azure.cli.testsdk.base import execute as _raw_execute

    def __init__(self, *args, **kwargs):
        super(NoTrafficRecordingPreparer, self).__init__(disable_recording=True, *args, **kwargs)

    def live_only_execute(self, cli_ctx, command, expect_failure=False):
        # call AbstractPreparer.moniker to make resource counts and self.resource_moniker consistent between live and
        # play-back. see SingleValueReplacer.process_request, AbstractPreparer.__call__._preparer_wrapper
        # and ScenarioTest.create_random_name. This is so that when self.create_random_name is called for the
        # first time during live or playback, it would have the same value.
        _ = self.moniker

        try:
            if self.test_class_instance.in_recording:
                return self._raw_execute(cli_ctx, command, expect_failure)
        except AttributeError:
            # A test might not have an in_recording attribute. Run live if this is an instance of LiveScenarioTest
            if isinstance(self.test_class_instance, LiveScenarioTest):
                return self._raw_execute(cli_ctx, command, expect_failure)

        return None


# Marketplace Offer Preparer and its shorthand decorator

# pylint: disable=line-too-long
# pylint: disable=too-many-instance-attributes
class MarketplaceOfferPreparer(NoTrafficRecordingPreparer, SingleValueReplacer):
    def __init__(self, name_prefix='clitest',
                 parameter_name='offer_id',
                 skip_delete=False,
                 dev_setting_name='AZURE_CLI_TEST_DEV_MARKETPLACE_OFFER_NAME',
                 key='offer_id',
                 offer_type='AzureContainer'):
        super().__init__(name_prefix, 24)
        self.cli_ctx = get_dummy_cli()
        self.offer_type = offer_type
        self.skip_delete = skip_delete
        self.parameter_name = parameter_name
        self.dev_setting_name = os.environ.get(dev_setting_name, None)
        self.key = key

    def create_resource(self, name, **kwargs):
        if not self.dev_setting_name:
            import time
            delay_return_for_partercenter_to_create_supporting_child_entities = 3

            template = 'az partnercenter marketplace offer create --id  {} -a \'{}\' -t {}'
            self.live_only_execute(self.cli_ctx, template.format(name, f'{name} Alias', self.offer_type))
            self.test_class_instance.kwargs[self.key] = name
            time.sleep(delay_return_for_partercenter_to_create_supporting_child_entities)

            return {self.parameter_name: name }

        return {self.parameter_name: self.dev_setting_name }

    def remove_resource(self, name, **kwargs):
        if not self.skip_delete and not self.dev_setting_name:
            self.live_only_execute(self.cli_ctx, 'az partnercenter marketplace offer delete --id {} --yes'.format(name))
