from azure.cli.testsdk import ScenarioTest

class PartnerCenterMarketplaceApplicationScenarioTest(ScenarioTest):
    def test_solution_template_create(self):
        self._create_offer()

        self._show_offer_listing()
        # self._update_offer_listing()

        self._create_st_plan()
        # self._update_plan_listing()

        self._delete_offer()

    def test_managed_app_create(self):
        self._create_offer()
        self._show_offer_listing()
        # self._update_offer_listing()

        self._create_ma_plan()
        # self._show_plan_tech_config()
        # self._update_plan_listing()

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
                "description": "<p>Unreal Cloud DDC is a centralized cloud-based cache designed to be used in conjunction with Epic Game's Unreal Cloud DDC to reduce build times and improve overall build performance. Unreal Cloud DDC enables you and your entire development team to connect and use Epic Game's Unreal Cloud DDC service.</p><p>This technology implements horizontally scalable, cloud-ready services to provide distributed compute and storage functionality for medium size and larger teams (>10 devs). The compute service manages agents and schedules work to execute on them. The storage service provides content-addressable storage backed by cloud object stores. Integrating storage and compute services allows caching, de-duplication, and locating data close to agents.</p> <p>In Unreal Engine 5 (UE5), ‘Unreal Cloud DDC’ is an optional service which users can enable and connect to cloud storage. Simplify provide the Unreal Cloud DDC URL and complete the authentication prompts to connect to your Unreal Cloud DDC deployment. By leveraging the ability to store smaller pre-computed elements, Unreal Cloud DDC makes it more efficient for sharing assets between developers.</p>",
                "plan_id": self.plan_id,
                "plan_name": self.plan_id + "name",
                "plan_summary": "Unreal Cloud DDC for Unreal Engine game development.",
                "plan_description":  "Unreal Cloud DDC for Unreal Engine game development." # "<p>Unreal Cloud DDC is a centralized cloud-based cache designed to be used in conjunction with Epic Game's Unreal Cloud DDC to reduce build times and improve overall build performance. Unreal Cloud DDC enables you and your entire development team to connect and use Epic Game's Unreal Cloud DDC service.</p><p>This technology implements horizontally scalable, cloud-ready services to provide distributed compute and storage functionality for medium size and larger teams (>10 devs). The compute service manages agents and schedules work to execute on them. The storage service provides content-addressable storage backed by cloud object stores. Integrating storage and compute services allows caching, de-duplication, and locating data close to agents.</p> <p>In Unreal Engine 5 (UE5), ‘Unreal Cloud DDC’ is an optional service which users can enable and connect to cloud storage. Simplify provide the Unreal Cloud DDC URL and complete the authentication prompts to connect to your Unreal Cloud DDC deployment. By leveraging the ability to store smaller pre-computed elements, Unreal Cloud DDC makes it more efficient for sharing assets between developers.</p>",
            },            
        )

    def _create_offer(self):
        self.cmd(
            "partnercenter marketplace offer create --id {offer_id} -a {offer_alias} --type AzureApplication",
            checks=[self.check("id", "{offer_id}"), self.check("alias", "{offer_alias}")],
        )

    def _show_offer_listing(self):
        self.cmd('partnercenter marketplace offer listing show --offer-id {offer_id}')

    def _update_offer_listing(self):
        self.cmd("partnercenter marketplace offer listing update --offer-id {offer_id} --summary '{summary}'' --short-description '{short_description}' --description '{description}'",
            checks=[self.check('description', '{description}'),
                    self.check('shortDescription', '{short_description}'),
                    self.check('summary', '{summary}')])

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

    def _update_plan_listing(self):
        self.cmd(
            "partnercenter marketplace offer plan listing update --offer-id {offer_id} --plan-id {plan_id} -n '{plan_name}' -d '{plan_description}' -s '{plan_summary}'",
            checks=[self.check("id", "{plan_id}"), self.check("name", "{plan_name}")],
        )

    def _show_plan_tech_config(self):
        self.cmd(
            "partnercenter marketplace offer plan technical-configuration show --offer-id {offer_id} --plan-id {plan_id}",
            checks=[self.check("id", "{plan_id}"), self.check("name", "{plan_name}")],
        )
