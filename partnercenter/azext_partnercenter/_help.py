# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import importlib
from knack.help_files import helps


def _get_help_module(module_name):
    return importlib.import_module(f'.{module_name}._help', 'azext_partnercenter.operations')


def _load_operations_help():
    operations_modules = [
        'marketplace_offer',
        'marketplace_offer_listing',
        'marketplace_offer_listing_contact',
        'marketplace_offer_listing_media',
        'marketplace_offer_listing_uri',
        'marketplace_offer_package',
        'marketplace_offer_plan',
        'marketplace_offer_plan_listing',
        'marketplace_offer_plan_technicalconfiguration',
        'marketplace_offer_submission'
    ]
    for module_name in operations_modules:
        _get_help_module(f'{module_name}').load_help()


helps['partnercenter'] = """
    type: group
    short-summary: Partner Center management
"""

helps['partnercenter marketplace'] = """
    type: group
    short-summary: Commands to manage the Partner Center Marketplace.
"""

_load_operations_help()
