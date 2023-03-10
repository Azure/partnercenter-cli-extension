# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core.azclierror import ResourceNotFoundError
from azext_partnercenter.tests.preparers import MarketplaceOfferPreparer
from ..base import PartnerCenterScenarioTest


class PartnerCenterMarketplaceOfferPlanListingScenarioTest(PartnerCenterScenarioTest):
    def setUp(self):
        self.cmd_delay = 5  # delay each cmd by 5 sec, default
        super().setUp()

    @MarketplaceOfferPreparer()
    def test_marketplace_offer_plan_listing(self):
        with self.assertRaises(ResourceNotFoundError):
            self.cmd("partnercenter marketplace offer plan listing show --offer-id {offer_id} --id {plan_id}")

        self.cmd(
            "partnercenter marketplace offer plan create --offer-id {offer_id} --id {plan_id} -n '{plan_name}'",
            checks=[self.check("id", "{plan_id}"), self.check("name", "{plan_name}")],
        )

        self.cmd(
            "partnercenter marketplace offer plan listing update --offer-id {offer_id} --id {plan_id} -n '{updated_name}' -s '{updated_summary}' -d '{updated_description}'",
            checks=[
                self.check("name", "{updated_name}"),
                self.check("summary", "{updated_summary}"),
                self.check("description", "{updated_description}"),
            ],
        )

    def init_args(self):
        self.plan_id = self.create_random_name("plantest-", 15)
        self.kwargs.update(
            {
                "updated_name": "updated name",
                "updated_summary": "updated summary",
                "updated_description": "updated description",
                "plan_id": self.plan_id,
                "plan_name": f"{self.plan_id} name",
            }
        )
