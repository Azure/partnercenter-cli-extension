# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class PlanListing(Model):
    _attribute_map = {
        'title': {'key': 'title', 'type': 'str'},
        'summary': {'key': 'summary', 'type': 'str'},
        # 'description': {'key': 'description', 'type': 'str'},
        # 'language_code': {'key': 'languageCode', 'type': 'str'},
        # 'short_description': {'key': 'shortDescription', 'type': 'str'},
        'keywords': {'key': 'keywords', 'type': '[str]'},
        'contacts': {'key': 'contacts', 'type': '[ListingContact]'},
        'uris': {'key': 'uris', 'type': '[ListingUri]'},
        'getting_started_instructions': {'key': 'gettingStartedInstructions', 'type': 'str'},
        # 'etag': {'key': '@odata.etag', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'external_id': {'key': 'external_id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'offer_id': {'key': 'offerId', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'short_description': {'key': 'short_description', 'type': 'str'},
        'language_code': {'key': 'language_code', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'Resource'},
        'odata_etag': {'key': 'odata_etag', 'type': 'str'}
    }

    def __init__(self, **kwargs):
        super(PlanListing, self).__init__(**kwargs)
        self.title = kwargs.get('title', None)
        self.summary = kwargs.get('summary', None)
        self.description = kwargs.get('description', None)
        self.language_code = kwargs.get('language_code', None)
        self.short_description = kwargs.get('short_description', None)
        self.keywords = kwargs.get('keywords', [])
        self.contacts = kwargs.get('contacts', [])
        self.uris = kwargs.get('uris', [])
        self.getting_started_instructions = kwargs.get('getting_started_instructions', None)
        self.id = kwargs.get('id', None)
        self.external_id = kwargs.get('external_id', None)
        self.name = kwargs.get('name', None)
        self.offer_id = kwargs.get('offer_id', None)
        self.odata_etag = kwargs.get('odata_etag', None)
