# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.util import CLIError
from azext_partnercenter.models import OfferType
from azext_partnercenter.tests.preparers import MarketplaceOfferPreparer
from ..base import PartnerCenterScenarioTest


class PartnerCenterMarketplaceOfferSetupScenarioTest(PartnerCenterScenarioTest):
    def setUp(self):
        self.cmd_delay = 5  # delay each cmd by 5 sec, default
        super().setUp()

    @MarketplaceOfferPreparer(offer_type=OfferType.AZURETHIRDPARTYVIRTUALMACHINE)
    def test_marketplace_offer_setup_test_drive_on_vm_type(self):
        self.cmd('partnercenter marketplace offer setup update --offer-id {offer_id} --test-drive {updated_test_drive}',
                 checks=[self.check('testDrive', True)])

    @MarketplaceOfferPreparer()
    def test_marketplace_offer_setup(self):
        self._offer_setup_show_returns_initial_default_values()

        self.cmd('partnercenter marketplace offer setup update --offer-id {offer_id} --sell-through-microsoft {updated_sell_through_microsoft} --trial-uri {updated_trial_uri}',
                 checks=[self.check('sellThroughMicrosoft', True),
                         self.check('trialUri', '{updated_trial_uri}')])

        self.cmd('partnercenter marketplace offer setup show --id {offer_id}',
                 checks=[self.check('sellThroughMicrosoft', True),
                         self.check('testDrive', False),
                         self.check('trialUri', '{updated_trial_uri}')])

        # should not allow Container offer type to test drive
        with self.assertRaises(CLIError):
            self.cmd('partnercenter marketplace offer setup update --id {offer_id} --test-drive true')

    def _offer_setup_show_returns_initial_default_values(self):
        result = self.cmd('partnercenter marketplace offer setup show --id {offer_id}').get_output_in_json()

        self.assertTrue(result['reseller']);
        self.assertFalse(result['sellThroughMicrosoft'])
        self.assertFalse(result['testDrive'])
        self.assertEqual('', result['trialUri'])

    def init_args(self):
        self.kwargs.update({
            'updated_sell_through_microsoft': 'true',
            'updated_test_drive': 'true',
            'updated_trial_uri': 'https://updated.tria.uri/'
        })
