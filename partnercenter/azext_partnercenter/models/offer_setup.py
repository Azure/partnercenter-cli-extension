# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model

class OfferSetup(Model):
    _attribute_map = {
        'sellingOption': {'key': 'selling_option', 'type': 'str'},
        'trialUri': {'key': 'trial_uri', 'type': 'str'},
        'enableTestDrive': {'key': 'enable_test_drive', 'type': 'bool'},
        'channelStates': {'key': 'channel_states', 'type': '[dict]'}
    }

    def __init__(self, **kwargs):
        super(OfferSetup, self).__init__(**kwargs)
        self.selling_option = kwargs.get('selling_option', None)
        self.trial_uri = kwargs.get('trial_uri', None)
        self.channel_states = kwargs.get('channel_states', None)
        self._resource = kwargs.get('resource', None)

    
    
