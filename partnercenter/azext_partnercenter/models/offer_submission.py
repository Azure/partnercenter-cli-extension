# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class OfferSubmission(Model):
    _attribute_map = {
        "offer_id": {"key": "offerId", "type": "str"},
        "id": {"key": "id", "type": "str"},
        "lifecycle_state": {"key": "lifecycleState", "type": "str"},
        "target": {"key": "target", "type": "str"},
        "status": {"key": "status", "type": "str"},
        "result": {"key": "result", "type": "str"},
        "created": {"key": "created", "type": "str"},
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.id = kwargs.get("id")
        self.offer_id = kwargs.get("offer_id")
        self.lifecycle_state = kwargs.get("lifecycle_state")
        self.target = kwargs.get("target")
        self.status = kwargs.get("status")
        self.result = kwargs.get("result")
        self.created = kwargs.get("created")
