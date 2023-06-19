from azext_partnercenter.tests.preparers import MarketplaceOfferPreparer
from ..base import PartnerCenterScenarioTest


class PartnerCenterMarketplaceApplicationScenarioTest(PartnerCenterScenarioTest):
    @MarketplaceOfferPreparer(offer_type="AzureApplication")
    def test_solution_template_creation(self):
        self._offer_listing_show()
        self._offer_listing_update()

        self._offer_setup_show()
        self._offer_setup_update()

        self._plan_create_solution_template()
        self._plan_listing_update()

    @MarketplaceOfferPreparer(offer_type="AzureApplication")
    def test_managed_app_creation(self):
        self.init_args()

        self._offer_listing_show()
        self._offer_listing_update()

        self._offer_setup_show()
        self._offer_setup_update()

        self._plan_create_managed_application()
        self._plan_listing_update()

    def init_args(self):
        self.plan_id = self.create_random_name("plantest-", 15)
        self.kwargs.update(
            {
                "summary": "A storage offer for Unreal Engine Game Developers",
                "short_description": "Unreal Cloud DDC for Unreal Engine game development.",
                "description": "Unreal Cloud DDC for Unreal Engine game development.",
                "plan_id": self.plan_id,
                "plan_name": self.plan_id + "name",
                "plan_summary": "Unreal Cloud DDC for Unreal Engine game development.",
                "plan_description": "Unreal Cloud DDC for Unreal Engine game development.",
            },
        )

    def _offer_listing_show(self):
        self.cmd("partnercenter marketplace offer listing show --offer-id {offer_id}")

    def _offer_listing_update(self):
        self.cmd(
            "partnercenter marketplace offer listing update --offer-id {offer_id} --summary '{summary}' --short-description '{short_description}' --description '{description}'",
            checks=[
                self.check("description", "{description}"),
                self.check("shortDescription", "{short_description}"),
                self.check("summary", "{summary}"),
            ],
        )

    def _offer_setup_show(self):
        self.cmd("partnercenter marketplace offer setup show --offer-id {offer_id}")

    def _offer_setup_update(self):
        self.cmd(
            "partnercenter marketplace offer setup update --offer-id {offer_id}"
        )

    def _plan_create_solution_template(self):
        self.cmd(
            "partnercenter marketplace offer plan create --offer-id {offer_id} --plan-id {plan_id} --name '{plan_name}'",
            checks=[self.check("id", "{plan_id}"), self.check("name", "{plan_name}")],
        )

    def _plan_create_managed_application(self):
        self.cmd(
            "partnercenter marketplace offer plan create --offer-id {offer_id} --plan-id {plan_id} --name '{plan_name}' --subtype managed-application",
            checks=[self.check("id", "{plan_id}"), self.check("name", "{plan_name}")],
        )

    def _plan_listing_update(self):
        self.cmd(
            "partnercenter marketplace offer plan listing update --offer-id {offer_id} --plan-id {plan_id} --description \'{plan_description}\' --summary \'{plan_summary}\'",
            checks=[self.check("id", "{plan_id}"), self.check("name", "{plan_name}")], delay=10
        )
