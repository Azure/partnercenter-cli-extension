# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import time
from azext_partnercenter.tests.preparers import MarketplaceOfferPreparer
from ..base import PartnerCenterScenarioTest


class PartnerCenterMarketplaceOfferListingScenarioTest(PartnerCenterScenarioTest):
    def setUp(self):
        self._initialize_variables()
        super().setUp()

    @MarketplaceOfferPreparer()
    def test_marketplace_offer_listing(self):
        self.cmd('partnercenter marketplace offer listing show --offer-id {offer_id}',
                 checks=[self.check('description', ''),
                         self.check('shortDescription', ''),
                         self.check('summary', '')])

        self.cmd('partnercenter marketplace offer listing update --offer-id {offer_id} --summary {summary} --short-description {short_description} --description {description}',
                 checks=[self.check('description', '{description}'),
                         self.check('shortDescription', '{short_description}'),
                         self.check('summary', '{summary}')])

        self.cmd('partnercenter marketplace offer listing show --offer-id {offer_id}',
                 checks=[self.check('description', '{description}'),
                         self.check('shortDescription', '{short_description}'),
                         self.check('summary', '{summary}'),
                         self.check('contacts', []),
                         self.check('uris', [])], delay=5)

    def _initialize_variables(self):
        self.kwargs.update({
            'summary': self.create_random_name('summary-', 20),
            'short_description': self.create_random_name('short-desc-', 20),
            'description': self.create_random_name('desc-', 20),
        })
