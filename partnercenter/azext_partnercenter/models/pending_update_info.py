# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class PendingUpdateInfo(Model):
    _attribute_map = {
        'update_type': {'key': 'update_type', 'type': 'str'},
        'status': {'key': 'status', 'type': 'str'},
        'href': {'key': 'href', 'type': 'str'},
        'failure_reason': {'key': 'failure_reason', 'type': 'str'}
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.update_type = kwargs.get('update_type', None)
        self.status = kwargs.get('status', None)
        self.href = kwargs.get('href', None)
        self.failure_reason = kwargs.get('failure_reason', None)
