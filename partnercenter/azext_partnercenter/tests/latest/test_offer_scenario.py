# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.testsdk import ScenarioTest


class PartnerCenterMarketplaceOfferScenarioTest(ScenarioTest):
    def setUp(self):
        self._initialize_variables()
        super().setUp()
    
    def _initialize_variables(self):
        self.offer_id = self.create_random_name('offertest-', 15)

        # api variables
        self.kwargs.update({
            'offer_id': self.offer_id,
            'offer_alias': f'{self.offer_id}-alias',
        })