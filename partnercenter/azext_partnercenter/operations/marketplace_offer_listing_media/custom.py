# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


def list_media(client, offer_id):
    # TODO: implement beyond images
    images = client.get_listing_images(offer_id)
    return images


def add_media(client, offer_id, file, type=None):
    return client.add_listing_image(offer_id, type, file)


def delete_media(client, offer_id, type):
    result = client.delete_listing_image(offer_id, type)
    return result
