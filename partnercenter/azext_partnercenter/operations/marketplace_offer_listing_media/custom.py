# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


def list_media(client, offer_id, media_type="image"):
    # TODO: implement beyond images
    if media_type == "image":
        return client.get_listing_images(offer_id)

    if media_type == "video":
        return client.get_listing_videos(offer_id)

    return None

def add_media(client, offer_id, file, media_type=None):
    return client.add_listing_image(offer_id, media_type, file)


def delete_media(client, offer_id, media_type):
    result = client.delete_listing_image(offer_id, media_type)
    return result
