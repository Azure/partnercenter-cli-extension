# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class SubmissionVariantResource(Model):
    _attribute_map = {
        'variant_id': {'key': 'variant_id', 'type': 'str'},
        'resources': {'key': 'resources', 'type': '[TypeValue]'}
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.id = kwargs.get('variant_id', None)
        self.name = kwargs.get('resources', [])
