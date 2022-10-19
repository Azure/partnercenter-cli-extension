# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class PlanListing(Model):
    _attribute_map = {
        'title': {'key': 'title', 'type': 'str'},
        'summary': {'key': 'summary', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'language_code': {'key': 'languageCode', 'type': 'str'},
        'short_description': {'key': 'shortDescription', 'type': 'str'},
        'keywords': {'key': 'keywords', 'type': '[str]'},
        'contacts': {'key': 'contacts', 'type': '[ListingContact]'},
        'uris': {'key': 'uris', 'type': '[ListingUri]'},
        'getting_started_instructions': {'key': 'gettingStartedInstructions', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'Resource'},
    }

    def __init__(self, **kwargs):
        super(PlanListing, self).__init__(**kwargs)
        self.title = kwargs.get('title', None)
        self.summary = kwargs.get('summary', None)
        self.description = kwargs.get('description', None)
        self.language_code = kwargs.get('language_code', None)
        self.short_description = kwargs.get('short_description', None)
        self.getting_started_instructions = kwargs.get('getting_started_instructions', None)
        self.keywords = kwargs.get('keywords', [])
        self.contacts = kwargs.get('offer_id', [])
        self.uris = kwargs.get('uris', [])
