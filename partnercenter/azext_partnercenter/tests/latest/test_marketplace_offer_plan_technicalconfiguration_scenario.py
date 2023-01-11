# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azext_partnercenter.tests.preparers import MarketplaceOfferPreparer
from ..base import PartnerCenterScenarioTest


class PartnerCenterMarketplaceOfferPlanTechnicalConfigurationScenarioTest(PartnerCenterScenarioTest):

    @MarketplaceOfferPreparer()
    def test_aks_offer_technicalconfiguration(self):
        self._create_plan()

    def _create_plan(self):
        self.cmd('partnercenter marketplace offer plan create --offer-id {offer_id} --plan-id {plan_id} --friendly-name {plan_name}', checks=[
            self.check('', '{offer_id}'),
            self.check('alias', '{offer_alias}')
        ])

    def _init_args(self):
        self.plan_id = self._apply_kwargs('{offer_id}-plan1')

        self.kwargs.update({
            'plan_id': self.plan_id,
            'plan_name': f"{self.plan_id} Friendly Name"
        })
