# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class ListingUri(Model):
    _attribute_map = {
        'type': {'key': 'title', 'type': 'str'},
        'uri': {'key': 'uri', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ListingUri, self).__init__(**kwargs)
        self.type = kwargs.get('type', None)
        self.uri = kwargs.get('uri', None)