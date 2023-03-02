from azure.cli.testsdk import ScenarioTest

class PartnerCenterMarketplaceOfferPlanListingScenarioTest(ScenarioTest):
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
                "plan_id": self.plan_id,
                "plan_name": self.plan_id + "name",
            },            
        )

    def _create_offer(self):
        self.cmd(
            "partnercenter marketplace offer create --id {offer_id} -a {offer_alias} --type AzureApplication",
            checks=[self.check("id", "{offer_id}"), self.check("alias", "{offer_alias}")],
        )

    def _delete_offer(self):
        self.cmd("partnercenter marketplace offer delete --id {offer_id} --yes")
        list = self.cmd("partnercenter marketplace offer list --query '[?id==`{offer_id}`]'").get_output_in_json()
        assert len(list) == 0

    def _create_st_plan(self):
        self.cmd(
            "partnercenter marketplace offer plan create --offer-id {offer_id} --id {plan_id} -n '{plan_name}'",
            checks=[self.check("id", "{plan_id}"), self.check("name", "{plan_name}")],
        )

    def _create_ma_plan(self):
        self.cmd(
            "partnercenter marketplace offer plan create --offer-id {offer_id} --id {plan_id} -n '{plan_name}' --subtype managed-application",
            checks=[self.check("id", "{plan_id}"), self.check("name", "{plan_name}")],
        )

    def _create_ma_plan_listing(self):
        self.cmd(
            "partnercenter marketplace offer plan listing create --offer-id {offer_id} --id {plan_id} -n '{plan_name}'",
            checks=[self.check("id", "{plan_id}"), self.check("name", "{plan_name}")],
        )

    def test_solution_template_create(self):
        self._create_offer()
        self._create_st_plan()
        self._delete_offer()

    def test_managed_app_create(self):
        self._create_offer()
        self._create_ma_plan()
        self._delete_offer()
