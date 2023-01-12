# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class OfferSetup(Model):
    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'sell_through_microsoft': {'key': 'sellThroughMicrosoft', 'type': 'bool'},
        'trial_uri': {'key': 'trialUri', 'type': 'str'},
        'reseller': {'key': 'reseller', 'type': 'bool'},
        'test_drive': {'key': 'testDrive', 'type': 'bool'}
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.id = kwargs.get('id', None)
        self.reseller = kwargs.get('reseller', None)
        self.test_drive = kwargs.get('test_drive', None)
        self.sell_through_microsoft = kwargs.get('sell_through_microsoft', None)
        self.trial_uri = kwargs.get('trial_uri', None)
        self._resource = kwargs.get('resource', None)
