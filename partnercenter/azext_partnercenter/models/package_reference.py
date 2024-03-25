# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class PackageReference(Model):
    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'}
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.type = kwargs.get('type', None)
        self.value = kwargs.get('value', None)