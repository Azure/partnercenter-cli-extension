# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


from azext_partnercenter.models.target_type import TargetType


def get_submission(client, offer_id, submission_id):
    return client.get(offer_id, submission_id)


def list_submission(client, offer_id):
    return client.list(offer_id)


def delete_submission(client, offer_id, submission_id):
    return client.delete(offer_id, submission_id)


def publish_submission(client, offer_id, submission_id=None, target=TargetType.Draft.value):
    result = client.publish(offer_id, submission_id, target)
    return result
