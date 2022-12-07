# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os
import time
from azure.cli.testsdk import ScenarioTest


TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))


class PartnercenterScenarioTest(ScenarioTest):
    def test_partnercenter_offer_container_submission(self):
        offer_id = self.create_random_name('o', 10)
        offer_alias = self.create_random_name('oa', 10)
        offer_type = 'AzureContainer'
        summary = self.create_random_name('os', 15)
        short_description = self.create_random_name('sd', 10)
        description = self.create_random_name('d', 20)
        uri = 'http://www.contoso.com'
        uri_display_text = self.create_random_name('d', 20)
        uri_type = 'PrivacyUri'
        uri_sub_type = 'subtype'
        contact_type = 'Engineering'
        contact_email = 'testuser@contoso.com'
        contact_name = 'Jane Doe'
        contact_phone = '4259999999'
        contact_uri = uri
        media_type = 'AzureLogoLarge'
        media_file = self._get_test_media_file()

        self.kwargs.update({
            'offer_id': offer_id,
            'offer_alias': offer_alias,
            'offer_type': offer_type,
            'summary': summary,
            'short_description': short_description,
            'description': description,
            'uri': uri,
            'uri_display_text': uri_display_text,
            'uri_type': uri_type,
            'uri_sub_type': uri_sub_type,
            'contact_type': contact_type,
            'contact_email': contact_email,
            'contact_name': contact_name,
            'contact_phone': contact_phone,
            'contact_uri': contact_uri,
            'media_type': media_type,
            'media_file': media_file
        })

        self.cmd('partnercenter marketplace offer create --offer-id {offer_id} --offer-alias {offer_alias} --offer-type {offer_type}',
                 checks=[self.check('id', '{offer_id}'),
                         self.check('name', '{offer_alias}')])

        time.sleep(5)

        result = self.cmd('az partnercenter marketplace offer listing show --offer-id {offer_id}',
                          checks=[self.check('description', '{description}'),
                                  self.check('shortDescription', '{short_description}'),
                                  self.check('summary', '{summary}'),
                                  self.check('contacts', []),
                                  self.check('uris', [])])

        time.sleep(5)

        result = self.cmd('partnercenter marketplace offer listing contact list --offer-id {offer_id} ').get_output_in_json()
        self.assertEqual(len(result), 0)

        time.sleep(5)

        self.cmd('partnercenter marketplace offer listing contact add --offer-id {offer_id} --type {contact_type} --email {contact_email} --name "{contact_name}" --phone {contact_phone} --uri {contact_uri}',
                 checks=[self.check('contacts[0].type', '{contact_type}'),
                         self.check('contacts[0].email', '{contact_email}'),
                         self.check('contacts[0].name', '{contact_name}'),
                         self.check('contacts[0].phone', '{contact_phone}'),
                         self.check('contacts[0].uri', '{contact_uri}')])

        time.sleep(5)

        self.cmd('partnercenter marketplace offer listing contact delete --offer-id {offer_id} --type {contact_type} --email {contact_email} --name "{contact_name}" --phone {contact_phone} --uri {contact_uri} --yes')
        result = self.cmd('partnercenter marketplace offer listing contact list --offer-id {offer_id} ').get_output_in_json()
        self.assertEqual(len(result), 0)

        time.sleep(5)
        self.cmd('partnercenter marketplace offer delete --offer-id {offer_id} --yes')

    def _get_test_media_file(self):
        import inspect
        currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
        parentdir = os.path.dirname(currentdir)
        test_data_dir = os.path.join(parentdir, "testdata")
        media_file = os.path.join(test_data_dir, "largelogo.png")

        return media_file
