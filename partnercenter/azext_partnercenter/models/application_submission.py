# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class ApplicationSubmission(Model):
    _attribute_map = {
        'resource_type': {'key': 'resource_type', 'type': 'str'},
        'state': {'key': 'state', 'type': 'str'},
        'substate': {'key': 'substate', 'type': 'str'},
        'targets': {'key': 'targets', 'type': '[TypeValue]'},
        'resources': {'key': 'resources', 'type': '[TypeValue]'},
        'variant_resources': {'key': 'variant_resources', 'type': '[SubmissionVariantResource]'},
        'publish_option': {'key': 'publish_option', 'type': 'SubmissionPublishOption'},
        'published_time_in_utc': {'key': 'published_time_in_utc', 'type': 'str'},
        'pending_update_info': {'key': 'pending_update_info', 'type': 'PendingUpdateInfo'},
        'extended_properties': {'key': 'extended_properties', 'type': '[TypeValue]'},
        'release_number': {'key': 'release_number', 'type': 'int'},
        'friendly_name': {'key': 'friendly_name', 'type': 'str'},
        'are_resources_ready': {'key': 'are_resources_ready', 'type': 'bool'},
        'id': {'key': 'id', 'type': 'str'}
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.resource_type = kwargs.get('resource_type', None)
        self.state = kwargs.get('state', None)
        self.substate = kwargs.get('substate', None)
        self.targets = kwargs.get('targets', [])
        self.resources = kwargs.get('resources', [])
        self.variant_resources = kwargs.get('variant_resources', [])
        self.publish_option = kwargs.get('publish_option', None)
        self.published_time_in_utc = kwargs.get('published_time_in_utc', None)
        self.pending_update_info = kwargs.get('pending_update_info', None)
        self.extended_properties = kwargs.get('extended_properties', [])
        self.release_number = kwargs.get('release_number', 0)
        self.friendly_name = kwargs.get('friendly_name', None)
        self.are_resources_ready = kwargs.get('are_resources_ready', False)
        self.id = kwargs.get('id', None)
