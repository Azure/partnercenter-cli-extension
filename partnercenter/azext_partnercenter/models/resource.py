# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class Resource(Model):
    """This is to track the resource durable and external id and type of the objects."""
    _attribute_map = {
        'durableId': {'key': 'durable_id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.durable_id = kwargs.get('durable_id', None)
        self.type = kwargs.get('type', None)
