# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os
import unittest

from azure.cli.testsdk import (ScenarioTest, ResourceGroupPreparer)


TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))


class PartnercenterScenarioTest(ScenarioTest):

    def test_partnercenter_offer_container_submission(self):
        offer_id = self.create_random_name('o', 10)
        offer_alias = self.create_random_name('oa', 10)
        offer_type = 'AzureContainer'
        summary = self.create_random_name('os', 15)
        short_description = self.create_random_name('sd', 10)
        description = self.create_random_name('d', 20)

        self.kwargs.update({
            'offer_id': offer_id,
            'offer_alias': offer_alias,
            'offer_type': offer_type,
            'summary': summary,
            'short_description': short_description,
            'description': description
        })

        self.cmd('partnercenter marketplace offer create --offer-id {offer_id} --offer-alias {offer_alias} --offer-type {offer_type}',
                checks=[self.check('id', '{offer_id}'),
                        self.check('name', '{offer_alias}')])
        
        self.cmd('partnercenter marketplace offer listing update --offer-id {offer_id} --summary {summary} --short-description {short_description} --description {description}',
                checks=[self.check('description', '{description}'),
                        self.check('shortDescription', '{short_description}'),
                        self.check('summary', '{summary}')])

        self.cmd('partnercenter marketplace offer delete --offer-id {offer_id} -y')