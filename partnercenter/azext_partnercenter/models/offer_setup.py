# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class OfferSetup(Model):
    _attribute_map = {
        'sell_through_microsoft': {'key': 'sellThroughMicrosoft', 'type': 'bool'},
        'trial_uri': {'key': 'trialUri', 'type': 'str'},
        'enable_test_drive': {'key': 'enableTestDrive', 'type': 'bool'},
        'channel_states': {'key': 'channelStates', 'type': '[dict]'}
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.sell_through_microsoft = kwargs.get('sell_through_microsoft', None)
        self.trial_uri = kwargs.get('trial_uri', None)
        self.channel_states = kwargs.get('channel_states', None)
        self._resource = kwargs.get('resource', None)
