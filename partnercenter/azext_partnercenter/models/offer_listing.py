# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class OfferListing(Model):
    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'Resource'},
    }

    def __init__(self, **kwargs):
        super(OfferListing, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)
        self.resource = kwargs.get('resource', None)