# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
from azext_partnercenter.models import MediaType


def list_media(client, offer_id, media_type):
    if media_type == MediaType.Video:
        return client.get_listing_videos(offer_id)

    return client.get_listing_images(offer_id)


def add_media(client, offer_id, file, media_type, streaming_uri=None):
    if media_type == MediaType.Image:
        return client.add_listing_image(offer_id, media_type, file)

    if media_type == MediaType.Video:
        return client.add_listing_video(offer_id, file, streaming_uri)

    return None


def delete_media(client, offer_id, media_type):
    result = client.delete_listing_image(offer_id, media_type)
    return result
