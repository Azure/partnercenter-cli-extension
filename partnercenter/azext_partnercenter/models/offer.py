# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class Offer(Model):
    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, **kwargs):
        super(Offer, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)
        self.name = kwargs.get('name', None)
        self._resource = kwargs.get('resource', None)