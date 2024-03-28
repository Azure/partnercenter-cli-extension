# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class PackageAuthorization(Model):
    _attribute_map = {
        'principal_id': {'key': 'principalID', 'type': 'str'},
        'role_definition_id': {'key': 'roleDefinitionID', 'type': 'str'}
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.principal_id = kwargs.get('principal_id', None)
        self.role_definition_id = kwargs.get('role_definition_id', None)
