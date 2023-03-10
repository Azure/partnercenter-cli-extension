# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.testsdk import ScenarioTest


class PartnerCenterMarketplaceOfferScenarioTest(ScenarioTest):
    def setUp(self):
        self._initialize_variables()
        super().setUp()

    def test_marketplace_offer(self):
        self._create_offer()
        self._show_offer()
        self._list_offers_with_created_offer_in_result()
        self._delete_offer()

    def _create_offer(self):
        self.cmd('partnercenter marketplace offer create --id {offer_id} -a {offer_alias} --type AzureContainer', checks=[
            self.check('id', '{offer_id}'),
            self.check('alias', '{offer_alias}')
        ])

    def _show_offer(self):
        self.cmd('partnercenter marketplace offer show --id {offer_id}', checks=[
            self.check('id', '{offer_id}'),
            self.check('alias', '{offer_alias}'),
            self.check('type', 'AzureContainer')
        ])

    def _list_offers_with_created_offer_in_result(self):
        self.cmd('partnercenter marketplace offer list', checks=[self.check("[?id=='{offer_id}'].id | [0]", '{offer_id}')])

    def _delete_offer(self):
        self.cmd('partnercenter marketplace offer delete --id {offer_id} --yes')
        list = self.cmd('partnercenter marketplace offer list --query \'[?id==`{offer_id}`]\'').get_output_in_json()
        assert len(list) == 0

    def _initialize_variables(self):
        self.offer_id = self.create_random_name('offertest-', 15)

        # api variables
        self.kwargs.update({
            'offer_id': self.offer_id,
            'offer_alias': f'{self.offer_id}-alias',
        })
