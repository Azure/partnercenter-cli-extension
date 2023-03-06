from azure.cli.testsdk import ScenarioTest


class PartnerCenterMarketplaceApplicationScenarioTest(ScenarioTest):
    def test_solution_template_creation(self):
        """
        OFFER_ID=offertest1
        PLAN_ID=stPlanTest1

        az partnercenter marketplace
        ... offer                           create --offer-id $OFFER_ID --alias $OFFER_ID --type AzureApplication
        ... ... listing                     show   --offer-id $OFFER_ID
        ... ... listing                     update --offer-id $OFFER_ID --summary "a storage offer" --short-description "a short description" --description @description.html
        ... ... setup                       show   --offer-id $OFFER_ID
        ... ... setup                       update --offer-id $OFFER_ID --reseller false --sell-through-microsoft false --test-drive false
        ... ... plan                        create --offer-id $OFFER_ID --plan-id $PLAN_ID --name $PLAN_ID
        ... ... ... listing                 show   --offer-id $OFFER_ID --plan-id $PLAN_ID
        ... ... ... listing                 update --offer-id $OFFER_ID --plan-id $PLAN_ID --summary "a storage offer" --description @description.html
        ... ... ... technical-configuration show   --offer-id $OFFER_ID --plan-id $PLAN_ID
        """
        self._create_offer()

        self._show_offer_listing()
        self._update_offer_listing()
        self._show_offer_setup()
        self._update_offer_setup()

        self._create_st_plan()
        self._update_plan_listing()
        # self._show_plan_tech_config()

        self._delete_offer()

    def test_managed_app_creation(self):
        """
        OFFER_ID=offertest1
        PLAN_ID=maPlanTest1

        az partnercenter marketplace
        ... offer                           create --offer-id $OFFER_ID --alias $OFFER_ID --type AzureApplication
        ... ... listing                     show   --offer-id $OFFER_ID
        ... ... listing                     update --offer-id $OFFER_ID --summary "a storage offer" --short-description "a short description" --description @description.html
        ... ... setup                       show   --offer-id $OFFER_ID
        ... ... setup                       update --offer-id $OFFER_ID --reseller false --sell-through-microsoft false --test-drive false
        ... ... plan                        create --offer-id $OFFER_ID --plan-id $PLAN_ID --name $PLAN_ID --subtype managed-application
        ... ... ... listing                 show   --offer-id $OFFER_ID --plan-id $PLAN_ID
        ... ... ... listing                 update --offer-id $OFFER_ID --plan-id $PLAN_ID --summary "a storage offer" --description @description.html
        ... ... ... technical-configuration show   --offer-id $OFFER_ID --plan-id $PLAN_ID
        """
        self._create_offer()
        self._show_offer_listing()
        self._update_offer_listing()
        self._show_offer_setup()
        self._update_offer_setup()

        self._create_ma_plan()
        self._update_plan_listing()
        # self._show_plan_tech_config()

        self._delete_offer()

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
                "description": "Unreal Cloud DDC for Unreal Engine game development.",  # "@description.html",
                "plan_id": self.plan_id,
                "plan_name": self.plan_id + "name",
                "plan_summary": "Unreal Cloud DDC for Unreal Engine game development.",
                "plan_description": "Unreal Cloud DDC for Unreal Engine game development.",  # "@description.html",
            },
        )

    def _create_offer(self):
        self.cmd(
            "partnercenter marketplace offer create --id {offer_id} -a {offer_alias} --type AzureApplication",
            checks=[self.check("id", "{offer_id}"), self.check("alias", "{offer_alias}")],
        )

    def _show_offer_listing(self):
        self.cmd("partnercenter marketplace offer listing show --offer-id {offer_id}")

    def _update_offer_listing(self):
        self.cmd(
            "partnercenter marketplace offer listing update --offer-id {offer_id} --summary '{summary}' --short-description '{short_description}' --description '{description}'",
            checks=[
                self.check("description", "{description}"),
                self.check("shortDescription", "{short_description}"),
                self.check("summary", "{summary}"),
            ],
        )

    def _show_offer_setup(self):
        self.cmd("partnercenter marketplace offer setup show --offer-id {offer_id}")

    def _update_offer_setup(self):
        self.cmd(
            "partnercenter marketplace offer setup update --offer-id {offer_id}"
        )

    def _delete_offer(self):
        self.cmd("partnercenter marketplace offer delete --id {offer_id} --yes")
        list = self.cmd("partnercenter marketplace offer list --query '[?id==`{offer_id}`]'").get_output_in_json()
        assert len(list) == 0

    def _create_st_plan(self):
        self.cmd(
            "partnercenter marketplace offer plan create --offer-id {offer_id} --plan-id {plan_id} --name '{plan_name}'",
            checks=[self.check("id", "{plan_id}"), self.check("name", "{plan_name}")],
        )

    def _create_ma_plan(self):
        self.cmd(
            "partnercenter marketplace offer plan create --offer-id {offer_id} --plan-id {plan_id} --name '{plan_name}' --subtype managed-application",
            checks=[self.check("id", "{plan_id}"), self.check("name", "{plan_name}")],
        )

    def _update_plan_listing(self):
        self.cmd(
            "partnercenter marketplace offer plan listing update --offer-id {offer_id} --plan-id {plan_id} --description '{plan_description}' --summary '{plan_summary}'",
            checks=[self.check("id", "{plan_id}"), self.check("name", "{plan_name}")],
        )

    def _show_plan_tech_config(self):
        self.cmd(
            "partnercenter marketplace offer plan technical-configuration show --offer-id {offer_id} --plan-id {plan_id}",
            checks=[self.check("id", "{plan_id}"), self.check("name", "{plan_name}")],
        )
