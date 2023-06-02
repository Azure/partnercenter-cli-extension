# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long
# pylint: disable=protected-access
# pylint: disable=no-self-use
import resource
from azext_partnercenter.models.listing_image import ListingImage
from azext_partnercenter.models.listing_video import ListingVideo
from azext_partnercenter.clients.offer_listing_client import OfferListingClient
from azext_partnercenter.clients.offer_client import OfferClient
from azext_partnercenter.vendored_sdks.v1.partnercenter.apis import (
    ProductClient, VariantClient, ListingImageClient, ListingVideoClient)
from azext_partnercenter.vendored_sdks.v1.partnercenter.model.microsoft_ingestion_api_models_listings_listing_image import (
    MicrosoftIngestionApiModelsListingsListingImage)
from azext_partnercenter.vendored_sdks.v1.partnercenter.model.microsoft_ingestion_api_models_listings_listing_video import (
    MicrosoftIngestionApiModelsListingsListingVideo)
from azext_partnercenter.vendored_sdks.v1.partnercenter.model.microsoft_ingestion_api_models_listings_listing_video_thumbnail import (
    MicrosoftIngestionApiModelsListingsListingVideoThumbnail)
from partnercenter.azext_partnercenter.models import listing_video

from ._client_factory import get_api_client


class ListingMediaClient:
    def __init__(self, cli_ctx, *_):
        self._api_client = get_api_client(cli_ctx, *_)
        self._plan_listing_client = OfferListingClient(cli_ctx, *_)
        self._offer_client = OfferClient(cli_ctx, *_)
        self._product_client = ProductClient(self._api_client)
        self._variant_client = VariantClient(self._api_client)
        self._listing_image_client = ListingImageClient(self._api_client)
        self._listing_video_client = ListingVideoClient(self._api_client)

    def get_listing_videos(self, offer_external_id):
        offer = self._offer_client.get(offer_external_id)
        if offer is None:
            return None
        offer_resource_id = offer.resource.durable_id

        listing = self._offer_client.get_listing(offer_external_id)

        if listing is None:
            return None
        listing_resource_id = listing._resource.durable_id

        videos = self._listing_video_client.products_product_id_listings_listing_id_videos_get(
            offer_resource_id, listing_resource_id,
            self._get_authorication_token(),
            expand="$expand=FileSasUri")

        return self._map_videos(videos)

    def get_listing_images(self, offer_external_id):
        offer = self._offer_client.get(offer_external_id)
        if offer is None:
            return None
        offer_resource_id = offer.resource.durable_id

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
        offer_resource_id = offer.resource.durable_id

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

    def add_listing_video(self, offer_external_id, file_path, streaming_uri):
        import ntpath
        file = ntpath.basename(file_path)

        offer = self._offer_client.get(offer_external_id)
        if offer is None:
            return None
        offer_resource_id = offer.resource.durable_id

        listing = self._offer_client.get_listing(offer_external_id)
        if listing is None:
            return None
        listing_resource_id = listing._resource.durable_id

        file_name = self._get_file_name(file)

        # offer_resource_id, listing_resource_id, streaming_uri, video_type, file_name, title
        title = file_name
        listing_video = self._post_video(offer_resource_id, listing_resource_id, streaming_uri, file_name, title)
        file_sas_uri = listing_video.thumbnail_file_sas_uri
        self._upload_media(file_path, file_sas_uri)
        return self._put_video(offer_resource_id, listing_resource_id, listing_video)

    def add_listing_image(self, offer_external_id, image_type, file_path):
        import ntpath
        file = ntpath.basename(file_path)

        offer = self._offer_client.get(offer_external_id)
        if offer is None:
            return None
        offer_resource_id = offer.resource.durable_id

        listing = self._offer_client.get_listing(offer_external_id)
        if listing is None:
            return None
        listing_resource_id = listing._resource.durable_id

        file_name = self._get_file_name(file)

        listing_image = self._post_image(offer_resource_id, listing_resource_id, image_type, file_name)
        file_sas_uri = listing_image.file_sas_uri
        self._upload_media(file_path, file_sas_uri)

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

    def _put_video(self, offer_resource_id, listing_resource_id, video: ListingVideo):
        state = "Uploaded"
        resource_type = "ListingVideo"
        order = 0

        listing_video_thumbnail = MicrosoftIngestionApiModelsListingsListingVideoThumbnail(
            file_name=video.thumbnail_file_name,
            title=video.thumbnail_title,
            state=state,
            file_sas_uri=video.thumbnail_file_sas_uri,
            odata_etag=video.odata_etag)

        listing_video = MicrosoftIngestionApiModelsListingsListingVideo(
            id=video.id,
            resource_type=resource_type,
            streaming_uri=video.streaming_uri,
            state=state,
            thumbnail=listing_video_thumbnail)

        result = self._listing_video_client.products_product_id_listings_listing_id_videos_video_id_put(
            offer_resource_id,
            listing_resource_id,
            video.id,
            self._get_authorication_token(),
            microsoft_ingestion_api_models_listings_listing_video=listing_video)

        return self._map_video(result)

    def _post_video(self, offer_resource_id, listing_resource_id, streaming_uri, file_name, title):
        state = "PendingUpload"
        resource_type = "ListingVideo"
        #publisher_defined_sas_uri = "https://gamesingestion12.blob.core.windows.net/948cedf1-1b0b-4f5c-b217-c77d0a699f85/video.png?sv=2016-05-31&sr=c&si=948cedf1-1b0b-4f5c-b217-c77d0a699f852023-5-11-18-05-09&sig=5rKWaKkXmMZ4n%2F719JEnDp%2FeV7WYl0R6rr%2BXlscwQ1o%3D&se=2023-06-07T17%3A23%3A06Z&t=DCE"

        listing_video_thumbnail = MicrosoftIngestionApiModelsListingsListingVideoThumbnail(file_name=file_name, title=title, state=state)
        listing_video = MicrosoftIngestionApiModelsListingsListingVideo(resource_type=resource_type, streaming_uri=streaming_uri, state=state, thumbnail=listing_video_thumbnail)
        result = self._listing_video_client.products_product_id_listings_listing_id_videos_post(offer_resource_id,
                                                                                                listing_resource_id,
                                                                                                self._get_authorication_token(),
                                                                                                microsoft_ingestion_api_models_listings_listing_video=listing_video)

        return self._map_video(result)


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

    def _upload_media(self, upload_file_path, file_sas_uri):
        from azure.storage.blob import BlobClient
        blob_client = BlobClient.from_blob_url(file_sas_uri)
        with open(upload_file_path, 'rb') as data:
            result = blob_client.upload_blob(data)
            return result

    def _get_file_name(self, file):
        return file

    def _map_images(self, images):
        return list(map(self._map_image, images.value))

    def _map_image(self, image):
        listing_image = ListingImage(fileName=image.file_name, type=image.type, fileSasUri=image.file_sas_uri if hasattr(image, 'file_sas_uri') else '', state=image.state,
                                     order=image.order, odata_etag=image.odata_etag, id=image.id)

        return listing_image

    def _map_videos(self, videos):
        return list(map(self._map_video, videos.value))

    def _map_video(self, video):
        listing_video = ListingVideo(type=video.resource_type, thumbnailFileName=video.thumbnail.file_name, thumbnailFileSasUri=video.thumbnail.file_sas_uri,
                                     thumbnailState=video.thumbnail.state, thumbnailTitle=video.thumbnail.title, streamingUri=video.streaming_uri, odata_etag=video.odata_etag, id=video.id)

        return listing_video

    def _get_authorication_token(self):
        return self._api_client.configuration.access_token
