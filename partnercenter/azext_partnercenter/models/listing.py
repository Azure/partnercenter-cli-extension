# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=too-many-instance-attributes

from msrest.serialization import Model


class Listing(Model):
    _attribute_map = {
        "title": {"key": "title", "type": "str"},
        "summary": {"key": "summary", "type": "str"},
        "keywords": {"key": "keywords", "type": "[str]"},
        "contacts": {"key": "contacts", "type": "[ListingContact]"},
        "uris": {"key": "uris", "type": "[ListingUri]"},
        "getting_started_instructions": {"key": "gettingStartedInstructions", "type": "str"},
        "external_id": {"key": "external_id", "type": "str"},
        "name": {"key": "name", "type": "str"},
        "offer_id": {"key": "offerId", "type": "str"},
        "description": {"key": "description", "type": "str"},
        "short_description": {"key": "short_description", "type": "str"},
        "language_code": {"key": "language_code", "type": "str"},
        "odata_etag": {"key": "odata_etag", "type": "str"},
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = kwargs.get("title")
        self.summary = kwargs.get("summary")
        self.description = kwargs.get("description")
        self.language_code = kwargs.get("language_code")
        self.short_description = kwargs.get("short_description")
        self.keywords = kwargs.get("keywords", [])
        self.contacts = kwargs.get("contacts", [])
        self.uris = kwargs.get("uris", [])
        self.getting_started_instructions = kwargs.get("getting_started_instructions")
        self.name = kwargs.get("name")
        self.offer_id = kwargs.get("offer_id")
        self.odata_etag = kwargs.get("odata_etag")
        self._resource = kwargs.get("resource")
