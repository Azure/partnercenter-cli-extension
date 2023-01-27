# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class OfferSubmission(Model):
    _attribute_map = {
        'offer_id': {'key': 'offerId', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
        'state': {'key': 'state', 'type': 'str'}
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.id = kwargs.get('id', None)
        self.offer_id = kwargs.get('offer_id', None)
        self.target = kwargs.get('target', None)
        self.state = kwargs.get('state', None)
