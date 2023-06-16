# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
from azext_partnercenter.models import MediaType


def list_media(client, offer_id, media_type=None):
    if media_type is None:
        media_type = MediaType.Image
    elif isinstance(media_type, str):
        media_type = next((m for m in MediaType if m.value.lower() == media_type.lower()), None)

    if media_type is MediaType.Image:
        print('getting listing images')
        return client.get_listing_images(offer_id)

    if media_type is MediaType.Video:
        print('getting listing videos')
        return client.get_listing_videos(offer_id)

    return []


def add_media(client, offer_id, file, media_type=MediaType.Image, streaming_uri=None):
    if media_type == MediaType.Image:
        return client.add_listing_image(offer_id, media_type, file)

    if media_type == MediaType.Video:
        return client.add_listing_video(offer_id, file, streaming_uri)

    return None


def delete_media(client, offer_id, media_type):
    result = client.delete_listing_image(offer_id, media_type)
    return result
