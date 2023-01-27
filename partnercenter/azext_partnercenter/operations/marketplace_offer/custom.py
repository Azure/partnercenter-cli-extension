# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


def create_offer(client, offer_id, offer_alias, offer_type):
    result = client.create(offer_id, offer_alias, offer_type)
    return result


def update_offer(instance):
    # TODO: Implement partnercenter marketplace offer update
    return instance


def delete_offer(client, offer_id):
    return client.delete(offer_id)


def get_offer(client, offer_id):
    return client.get(offer_id)


def list_offer(client):
    return client.list()


def publish_offer(client, offer_id, target):
    return client.publish(offer_id, target)
