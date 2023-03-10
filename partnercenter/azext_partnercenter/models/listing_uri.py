# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class ListingUri(Model):
    _attribute_map = {
        "type": {"key": "type", "type": "str"},
        "subtype": {"key": "subtype", "type": "str"},
        "display_text": {"key": "displayText", "type": "str"},
        "uri": {"key": "uri", "type": "str"},
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.type = kwargs.get("type")
        self.subtype = kwargs.get("subtype")
        self.display_text = kwargs.get("display_text")
        self.uri = kwargs.get("uri")
