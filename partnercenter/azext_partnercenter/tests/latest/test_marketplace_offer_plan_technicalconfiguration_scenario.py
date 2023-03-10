# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azext_partnercenter.tests.preparers import MarketplaceOfferPreparer
from ..base import PartnerCenterScenarioTest


class PartnerCenterMarketplaceOfferPlanTechnicalConfigurationScenarioTest(PartnerCenterScenarioTest):
    @MarketplaceOfferPreparer()
    def test_aks_offer_technicalconfiguration(self):
        pass

    def _create_plan(self):
        self.cmd(
            "partnercenter marketplace offer plan create --offer-id {offer_id} --plan-id {plan_id} --friendly-name {plan_name}",
            checks=[self.check("", "{offer_id}"), self.check("alias", "{offer_alias}")],
        )

    def init_args(self):
        self.plan_id = self.create_random_name("plan-", 15)

        self.kwargs.update({"plan_id": self.plan_id, "plan_name": f"{self.plan_id} Friendly Name"})
