# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class ListingContact(Model):
    _attribute_map = {
        "type": {"key": "type", "type": "str"},
        "email": {"key": "email", "type": "str"},
        "name": {"key": "name", "type": "str"},
        "phone": {"key": "phone", "type": "str"},
        "uri": {"key": "uri", "type": "str"},
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.type = kwargs.get("type")
        self.name = kwargs.get("name")
        self.email = kwargs.get("email")
        self.phone = kwargs.get("phone")
        self.uri = kwargs.get("uri")

    def is_equal(self, other):
        return (
            self.__class__ == other.__class__
            and self.type == other.type
            and self.name == other.name
            and self.email == other.email
            and self.phone == other.phone
            and self.uri == other.uri
        )
