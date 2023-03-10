# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class PlanListing(Model):
    _attribute_map = {
        "offer_id": {"key": "offerId", "type": "str"},
        "id": {"key": "id", "type": "str"},
        "name": {"key": "name", "type": "str"},
        "summary": {"key": "summary", "type": "str"},
        "description": {"key": "description", "type": "str"},
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.id = kwargs.get("id")
        self.offer_id = kwargs.get("offer_id")
        self.name = kwargs.get("name")
        self.summary = kwargs.get("summary")
        self.description = kwargs.get("description")
        self._resource = kwargs.get("resource")
