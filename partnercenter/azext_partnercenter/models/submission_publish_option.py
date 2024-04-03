# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class SubmissionPublishOption(Model):
    _attribute_map = {
        'release_time_in_utc': {'key': 'release_time_in_utc', 'type': 'str'},
        'is_manual_publish': {'key': 'is_manual_publish', 'type': 'bool'},
        'is_auto_promote': {'key': 'is_auto_promote', 'type': 'bool'},
        'certification_notes': {'key': 'certification_notes', 'type': 'str'}
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.release_time_in_utc = kwargs.get('release_time_in_utc', None)
        self.is_manual_publish = kwargs.get('is_manual_publish', False)
        self.is_auto_promote = kwargs.get('is_auto_promote', False)
        self.certification_notes = kwargs.get('certification_notes', None)