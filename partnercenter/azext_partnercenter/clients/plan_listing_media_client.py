# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from partnercenter.azext_partnercenter._util import (
    get_combined_paged_results, object_to_dict)
from partnercenter.azext_partnercenter.models import PlanSetup
from partnercenter.azext_partnercenter.models.listing_image import ListingImage
from partnercenter.azext_partnercenter.clients.plan_listing_client import PlanListingClient
from partnercenter.azext_partnercenter.clients.offer_client import OfferClient
from partnercenter.azext_partnercenter.vendored_sdks.v1.partnercenter.apis import (
    ProductClient, VariantClient, ListingImageClient)
from partnercenter.azext_partnercenter.vendored_sdks.v1.partnercenter.model.microsoft_ingestion_api_models_listings_listing_image import MicrosoftIngestionApiModelsListingsListingImage

from ._util import get_api_client


class PlanListingMediaClient:
    def __init__(self, cli_ctx, *_):
        self._api_client = get_api_client(cli_ctx, *_)
        self._plan_listing_client = PlanListingClient(cli_ctx, *_)
        self._offer_client = OfferClient(cli_ctx, *_)
        self._product_client = ProductClient(self._api_client)
        self._variant_client = VariantClient(self._api_client)
        self._listing_image_client = ListingImageClient(self._api_client)

    def get_plan_listing_images(self, product_external_id, plan_external_id):
        product = self._offer_client.get(product_external_id)
        if product is None:
            return None
        product_id = product._resource.id

        plan_listing = self._plan_listing_client.get_plan_listing(product_external_id, plan_external_id)
        if plan_listing is None:
            return None
        listing_id = plan_listing.resource.id

        images = self._listing_image_client.products_product_id_listings_listing_id_images_get(product_id, listing_id, self._get_authorication_token(), expand="$expand=FileSasUri")
        return self._map_images(images)

    def add_plan_listing_image(self, product_external_id, plan_external_id, type, file):
        print(f'inside add_plan_listing_image: product_external_id - {product_external_id}')

        product = self._offer_client.get(product_external_id)
        if product is None:
            return None
        product_id = product._resource.id
        print(f'product_id - {product_id}')

        plan_listing = self._plan_listing_client.get_plan_listing(product_external_id, plan_external_id)
        if plan_listing is None:
            return None
        listing_id = plan_listing.resource.id
        print(f'listing_id - {listing_id}')

        file_name = self._get_file_name(file)
        state = "PendingUpload"
        resource_type = "ListingImage"
        order = 0
        listing_image = MicrosoftIngestionApiModelsListingsListingImage(resource_type=resource_type, file_name=file_name, type="AzureLogoSmall", state=state, order=order)

        result = self._listing_image_client.products_product_id_listings_listing_id_images_post(product_id, listing_id, self._get_authorication_token(), microsoft_ingestion_api_models_listings_listing_image=listing_image)
        print(f'result - {result}')
        return self._map_image(result)

    def _get_file_name(self, file):
        return file

    def _map_images(self, images):
        return images

    def _map_image(self, image):
        listing_image = ListingImage(fileName=image.file_name, type=image.type, fileSasUri=image.file_sas_uri, state=image.state, order=image.order, odata_etag=image.odata_etag, id=image.id)
        return  listing_image


    def _get_authorication_token(self):
        return self._api_client.configuration.access_token

