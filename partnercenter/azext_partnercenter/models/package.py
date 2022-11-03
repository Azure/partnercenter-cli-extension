# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class Package(Model):
    _attribute_map = {
        'industries': {'key': 'industries', 'type': '[dict]'},
        'categories': {'key': 'categories', 'type': '[dict]'},
        'additionalCategories': {'key': 'additional_categories', 'type': '[dict]'},
        'submissionVersion': {'key': 'submission_version', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '[str]'},
        'appVersion': {'key': 'app_version', 'type': 'str'},
        'useEnterpriseContract': {'key': 'use_enterprise_contract', 'type': 'bool'},
        'termsOfUse': {'key': 'terms_of_use', 'type': 'str'},
        'extendedProperties': {'key': 'extended_properties', 'type': '[dict]'},
        'applicableProducts': {'key': 'applicable_products', 'type': '[dict]'},
        'marketingOnlyChange': {'key': 'marketing_only_change', 'type': 'bool'},
        'globalAmendmentTerms': {'key': 'global_amendment_terms', 'type': 'str'},
        'customAmendments': {'key': 'custom_amendments', 'type': 'str'},
        'leveledIndustries': {'key': 'leveled_industries', 'type': 'dict'},
        'leveledCategories': {'key': 'leveled_categories', 'type': 'dict'},
    }

    def __init__(self, **kwargs):
        super(Package, self).__init__(**kwargs)
        self.industries = kwargs.get('industries', None)
        self.categories = kwargs.get('categories', None)
        self.additional_categories = kwargs.get('additional_categories', None)
        self.submission_version = kwargs.get('submission_version', None)
        self.tags = kwargs.get('tags', None)
        self.app_version = kwargs.get('app_version', None)
        self.use_enterprise_contract = kwargs.get('use_enterprise_contract', None)
        self.terms_of_use = kwargs.get('terms_of_use', None)
        self.extended_properties = kwargs.get('extended_properties', None)
        self.applicable_products = kwargs.get('applicable_products', None)
        self.marketing_only_change = kwargs.get('marketing_only_change', None)
        self.global_amendment_terms = kwargs.get('global_amendment_terms', None)
        self.custom_amendments = kwargs.get('custom_amendments', None)
        self.leveled_industries = kwargs.get('leveled_industries', None)
        self.leveled_categories = kwargs.get('leveled_categories', None)

        self._resource = kwargs.get('resource', None)
