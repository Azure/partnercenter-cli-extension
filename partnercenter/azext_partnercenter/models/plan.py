# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class Plan(Model):
    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'offer_id': {'key': 'offerId', 'type': 'str'},
        'state': {'key': 'state', 'type': 'str'},
        'cloud_availabilities': {'key': 'cloudAvailabilities', 'type': '[str]'}
    }

    def __init__(self, **kwargs):
        super(Plan, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)
        self.name = kwargs.get('name', None)
        self.offer_id = kwargs.get('offer_id', None)
        self.state = kwargs.get('state', None)
        self.cloud_availabilities = kwargs.get('cloud_availabilities', [])
        self.resource = kwargs.get('resource', None)