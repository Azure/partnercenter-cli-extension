# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azext_partnercenter.tests.preparers import MarketplaceOfferPreparer
from azure.cli.testsdk import ScenarioTest


class PartnerCenterMarketplaceOfferListingScenarioTest(ScenarioTest):
    def setUp(self):
        self._initialize_variables()
        super().setUp()

    @MarketplaceOfferPreparer(offer_type='AzureThirdPartyVirtualMachine')
    def test_offer_listing(self, offer_id):
        assert len(offer_id) > 0
 

    def _initialize_variables(self):
        self.offer_id = self.create_random_name('offertest-', 15)

        # api variables
        self.kwargs.update({
            'offer_id': self.offer_id,
            'offer_alias': f'{self.offer_id}-alias',
        })
