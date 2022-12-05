# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import time
from azext_partnercenter.tests.preparers import MarketplaceOfferPreparer
from azure.cli.testsdk import ScenarioTest


class PartnerCenterMarketplaceOfferListingScenarioTest(ScenarioTest):
    def setUp(self):
        self._initialize_variables()
        super().setUp()

    @MarketplaceOfferPreparer(offer_type='AzureThirdPartyVirtualMachine')
    def test_offer_listing(self):
        self.cmd('partnercenter marketplace offer listing show --offer-id {offer_id}',
            checks=[self.check('offerId', '{offer_id}')])

        self.cmd('partnercenter marketplace offer listing update --offer-id {offer_id} --summary {summary} --short-description {short_description} --description {description}',
                 checks=[self.check('description', '{description}'),
                         self.check('shortDescription', '{short_description}'),
                         self.check('summary', '{summary}')])
        time.sleep(5)
        self.cmd('partnercenter marketplace offer listing show --offer-id {offer_id}',
                 checks=[self.check('description', '{description}'),
                         self.check('shortDescription', '{short_description}'),
                         self.check('summary', '{summary}'),
                         self.check('contacts', []),
                         self.check('uris', [])])

        time.sleep(5)
 

    def _initialize_variables(self):
        self.kwargs.update({
            'summary': self.create_random_name('summary-', 20),
            'short_description': self.create_random_name('short-desc-', 20),
            'description': self.create_random_name('desc-', 20),
        })
