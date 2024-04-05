# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


def get_submission(client, offer_id, submission_id):
    return client.get(offer_id, submission_id)


def list_submission(client, offer_id):
    return client.list(offer_id)


def publish_submission(client, offer_id, submission_id, target):
    result = client.publish(offer_id, submission_id, target)
    return result
