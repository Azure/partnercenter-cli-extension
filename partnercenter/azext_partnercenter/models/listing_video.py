# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class ListingVideo(Model):
    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'file_sas_uri': {'key': 'fileSasUri', 'type': 'str'},
        'streaming_uri': {'key': 'streamingUri', 'type': 'str'},
        'thumbnail_state': {'key': 'thumbnailState', 'type': 'str'},
        'thumbnail_file_name': {'key': 'thumbnailFileName', 'type': 'str'},
        'thumbnail_file_sas_uri': {'key': 'thumbnailFileSasUri', 'type': 'str'},
        'thumbnail_title': {'key': 'thumbnailTitle', 'type': 'str'},
        'odata_etag': {'key': 'odata_etag', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.type = kwargs.get('type', None)
        self.file_sas_uri = kwargs.get('fileSasUri', None)
        self.streaming_uri = kwargs.get('streamingUri', None)
        self.thumbnail_state = kwargs.get('thumbnailState', None)
        self.thumbnail_file_name = kwargs.get('thumbnailFileName', None)
        self.thumbnail_file_sas_uri = kwargs.get('thumbnailFileSasUri', None)
        self.thumbnail_title = kwargs.get('thumbnailTitle', None)
        self.odata_etag = kwargs.get('odata_etag', None)
        self.id = kwargs.get('id', None)
