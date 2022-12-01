# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long
# pylint: disable=protected-access
# pylint: disable=no-self-use
from azext_partnercenter.models.listing_image import ListingImage
from azext_partnercenter.clients.offer_listing_client import OfferListingClient
from azext_partnercenter.clients.offer_client import OfferClient
from azext_partnercenter.vendored_sdks.v1.partnercenter.apis import (
    ProductClient, VariantClient, ListingImageClient)
from azext_partnercenter.vendored_sdks.v1.partnercenter.model.microsoft_ingestion_api_models_listings_listing_image import (
    MicrosoftIngestionApiModelsListingsListingImage)

from ._client_factory import get_api_client


class ListingMediaClient:
    def __init__(self, cli_ctx, *_):
        self._api_client = get_api_client(cli_ctx, *_)
        self._plan_listing_client = OfferListingClient(cli_ctx, *_)
        self._offer_client = OfferClient(cli_ctx, *_)
        self._product_client = ProductClient(self._api_client)
        self._variant_client = VariantClient(self._api_client)
        self._listing_image_client = ListingImageClient(self._api_client)

    def get_listing_images(self, offer_external_id):
        offer = self._offer_client.get(offer_external_id)
        if offer is None:
            return None
        offer_resource_id = offer._resource.durable_id

        listing = self._offer_client.get_listing(offer_external_id)

        if listing is None:
            return None
        listing_resource_id = listing._resource.durable_id

        images = self._listing_image_client.products_product_id_listings_listing_id_images_get(
            offer_resource_id, listing_resource_id,
            self._get_authorication_token(),
            expand="$expand=FileSasUri")

        return self._map_images(images)

    def delete_listing_image(self, offer_external_id, image_type):
        offer = self._offer_client.get(offer_external_id)
        if offer is None:
            return None
        offer_resource_id = offer._resource.durable_id

        listing = self._offer_client.get_listing(offer_external_id)
        if listing is None:
            return None
        listing_resource_id = listing._resource.durable_id

        images = self._listing_image_client.products_product_id_listings_listing_id_images_get(
            offer_resource_id,
            listing_resource_id,
            self._get_authorication_token(),
            expand="$expand=FileSasUri")

        deleted_ids = []
        for _, x in enumerate(images.value):
            cur_listing_image = self._map_image(x)
            if cur_listing_image.type == image_type:
                image_id = cur_listing_image.id
                self._listing_image_client.products_product_id_listings_listing_id_images_image_id_delete(
                    offer_resource_id,
                    listing_resource_id,
                    image_id,
                    self._get_authorication_token())
                deleted_ids.append(image_id)

        return deleted_ids

    def add_listing_image(self, offer_external_id, image_type, file_path):
        import ntpath
        file = ntpath.basename(file_path)

        offer = self._offer_client.get(offer_external_id)
        if offer is None:
            return None
        offer_resource_id = offer._resource.durable_id

        listing = self._offer_client.get_listing(offer_external_id)
        if listing is None:
            return None
        listing_resource_id = listing._resource.durable_id

        file_name = self._get_file_name(file)

        listing_image = self._post_image(offer_resource_id, listing_resource_id, image_type, file_name)
        self._upload_media(file_path, listing_image)

        return self._put_image(offer_resource_id, listing_resource_id, listing_image)

    def _put_image(self, offer_resource_id, listing_resource_id, image: ListingImage):
        state = "Uploaded"
        resource_type = "ListingImage"
        order = 0

        listing_image = MicrosoftIngestionApiModelsListingsListingImage(
            resource_type=resource_type,
            file_name=image.file_name,
            type=image.type,
            state=state,
            order=order,
            file_sas_uri=image.file_sas_uri,
            id=image.id,
            odata_etag=image.odata_etag)

        result = self._listing_image_client.products_product_id_listings_listing_id_images_image_id_put(
            offer_resource_id,
            listing_resource_id,
            image.id,
            self._get_authorication_token(),
            microsoft_ingestion_api_models_listings_listing_image=listing_image)

        return self._map_image(result)

    def _post_image(self, offer_resource_id, listing_resource_id, image_type, file_name):
        state = "PendingUpload"
        resource_type = "ListingImage"
        order = 0

        listing_image = MicrosoftIngestionApiModelsListingsListingImage(resource_type=resource_type, file_name=file_name, type=image_type, state=state, order=order)

        result = self._listing_image_client.products_product_id_listings_listing_id_images_post(offer_resource_id,
                                                                                                listing_resource_id,
                                                                                                self._get_authorication_token(),
                                                                                                microsoft_ingestion_api_models_listings_listing_image=listing_image)

        return self._map_image(result)

    def _upload_media(self, upload_file_path, listing_image: ListingImage):
        from azure.storage.blob import BlobClient
        blob_client = BlobClient.from_blob_url(listing_image.file_sas_uri)
        with open(upload_file_path, 'rb') as data:
            result = blob_client.upload_blob(data)
            return result

    def _get_file_name(self, file):
        return file

    def _map_images(self, images):
        return list(map(lambda x: self._map_image(x), images.value))

    def _map_image(self, image):
        listing_image = ListingImage(fileName=image.file_name, type=image.type, fileSasUri=image.file_sas_uri, state=image.state,
                                     order=image.order, odata_etag=image.odata_etag, id=image.id)

        return listing_image

    def _get_authorication_token(self):
        return self._api_client.configuration.access_token
