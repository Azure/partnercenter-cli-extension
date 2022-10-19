# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class ListingContact(Model):
    _attribute_map = {
        'type': {'key': 'title', 'type': 'str'},
        'email': {'key': 'summary', 'type': 'str'},
        'name': {'key': 'description', 'type': 'str'},
        'phone': {'key': 'languageCode', 'type': 'str'},
        'uri': {'key': 'shortDescription', 'type': 'str'}
    }

    def __init__(self, **kwargs):
        super(ListingContact, self).__init__(**kwargs)
        self.type = kwargs.get('type', None)
        self.name = kwargs.get('name', None)
        self.email = kwargs.get('email', None)
        self.phone = kwargs.get('phone', None)
        self.uri = kwargs.get('uri', None)
