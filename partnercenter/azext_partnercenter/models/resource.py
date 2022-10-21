# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class Resource(Model):
    """This is to track the internal id and type of the objects. It shouldn't be returned by the CLI in production."""
    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(Resource, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)
        self.type = kwargs.get('type', None)