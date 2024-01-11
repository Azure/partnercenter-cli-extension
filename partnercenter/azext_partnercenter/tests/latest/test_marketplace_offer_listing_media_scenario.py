# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azext_partnercenter.tests.preparers import MarketplaceOfferPreparer
from ..base import PartnerCenterScenarioTest


class PartnerCenterMarketplaceOfferListingMediaScenarioTest(PartnerCenterScenarioTest):
    def setUp(self):
        self.cmd_delay = 5  # delay each cmd by 5 sec, default
        super().setUp()

    @MarketplaceOfferPreparer()
    def test_marketplace_offer_listing_media(self):
        pass
        # self._test_add_large_logo()
        # self._test_video_thumbnail()

    def _test_video_thumbnail(self):
        self.cmd('partnercenter marketplace offer listing media add --offer-id {offer_id} --type {video_media_type} --file {video_thumbnail} --streaming-uri {streaming_uri}',
                 checks=[self.check('thumbnailState', '{thumbnail_state}'), self.check('type', '{video_output_type}')])

        result = self.cmd('partnercenter marketplace offer listing media list --offer-id {offer_id} --type {video_media_type}').get_output_in_json()
        self.assertEqual(len(result), 1)

    def _test_add_large_logo(self):
        self.cmd('partnercenter marketplace offer listing media add --offer-id {offer_id} --type {large_logo_media_type} --file {large_logo_file}',
                 checks=[self.check('state', '{add_cmd_state}'), self.check('type', '{large_logo_media_type}')])

        self.cmd('partnercenter marketplace offer listing media delete --offer-id {offer_id} --type {large_logo_media_type} --yes')

        result = self.cmd('partnercenter marketplace offer listing media list --offer-id {offer_id} --type {large_logo_media_type}').get_output_in_json()
        self.assertEqual(len(result), 0)

    def init_args(self):
        large_logo_abs_path = self.test_data.add("marketplace_offer_listing_media/largelogo.png")
        print(f'largo logo abs path: {large_logo_abs_path}')
        video_thumbnail_abs_path = self.test_data.add("marketplace_offer_listing_media/video.png")

        self.kwargs.update({
            'add_cmd_state': 'Uploaded',
            'large_logo_media_type': 'AzureLogoLarge',
            'large_logo_file': large_logo_abs_path,
            'video_media_type': 'Video',
            'image_media_type': 'Image',
            'video_output_type': 'ListingVideo',
            'video_thumbnail': video_thumbnail_abs_path,
            'thumbnail_state': 'Processed',
            'streaming_uri': '"https://www.youtube.com/watch?v=-Yz78dFgjKQ'
        })
