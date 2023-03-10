# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class ListingImage(Model):
    _attribute_map = {
        'file_name': {'key': 'fileName', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'display_text': {'key': 'displayText', 'type': 'str'},
        'file_sas_uri': {'key': 'fileSasUri', 'type': 'str'},
        'state': {'key': 'state', 'type': 'str'},
        'order': {'key': 'order', 'type': 'str'},
        'odata_etag': {'key': 'odata_etag', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.file_name = kwargs.get('fileName', None)
        self.type = kwargs.get('type', None)
        self.file_sas_uri = kwargs.get('fileSasUri', None)
        self.state = kwargs.get('state', None)
        self.order = kwargs.get('order', None)
        self.odata_etag = kwargs.get('odata_etag', None)
        self.id = kwargs.get('id', None)
