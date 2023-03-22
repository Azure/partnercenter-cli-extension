from azure.cli.testsdk import ScenarioTest


class PartnerCenterMarketplaceApplicationScenarioTest(ScenarioTest):
    def test_solution_template_creation(self):
        self._offer_create()

        self._offer_listing_show()
        self._offer_listing_update()

        self._offer_setup_show()
        self._offer_setup_update()

        self._plan_create_st()
        self._plan_listing_update()

        self._offer_delete()

    def test_managed_app_creation(self):
        self._offer_create()

        self._offer_listing_show()
        self._offer_listing_update()

        self._offer_setup_show()
        self._offer_setup_update()

        self._plan_create_ma()
        self._plan_listing_update()

        self._offer_delete()

    def setUp(self):
        super().setUp()
        self._initialize_variables()

    def _initialize_variables(self):
        self.offer_id = self.create_random_name("offertest-", 15)
        self.plan_id = self.create_random_name("plantest-", 15)
        self.kwargs.update(
            {
                "offer_id": self.offer_id,
                "offer_alias": f"{self.offer_id}-alias",
                "summary": "A storage offer for Unreal Engine Game Developers",
                "short_description": "Unreal Cloud DDC for Unreal Engine game development.",
                "description": "Unreal Cloud DDC for Unreal Engine game development.",
                "plan_id": self.plan_id,
                "plan_name": self.plan_id + "name",
                "plan_summary": "Unreal Cloud DDC for Unreal Engine game development.",
                "plan_description": "Unreal Cloud DDC for Unreal Engine game development.",
            },
        )

    def _offer_create(self):
        self.cmd(
            "partnercenter marketplace offer create --id {offer_id} -a {offer_alias} --type AzureApplication",
            checks=[self.check("id", "{offer_id}"), self.check("alias", "{offer_alias}")],
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

    def _offer_delete(self):
        self.cmd("partnercenter marketplace offer delete --id {offer_id} --yes")
        list = self.cmd("partnercenter marketplace offer list --query '[?id==`{offer_id}`]'").get_output_in_json()
        assert len(list) == 0

    def _plan_create_st(self):
        self.cmd(
            "partnercenter marketplace offer plan create --offer-id {offer_id} --plan-id {plan_id} --name '{plan_name}'",
            checks=[self.check("id", "{plan_id}"), self.check("name", "{plan_name}")],
        )

    def _plan_create_ma(self):
        self.cmd(
            "partnercenter marketplace offer plan create --offer-id {offer_id} --plan-id {plan_id} --name '{plan_name}' --subtype managed-application",
            checks=[self.check("id", "{plan_id}"), self.check("name", "{plan_name}")],
        )

    def _plan_listing_update(self):
        self.cmd(
            "partnercenter marketplace offer plan listing update --offer-id {offer_id} --plan-id {plan_id} --description '{plan_description}' --summary '{plan_summary}'",
            checks=[self.check("id", "{plan_id}"), self.check("name", "{plan_name}")],
        )
