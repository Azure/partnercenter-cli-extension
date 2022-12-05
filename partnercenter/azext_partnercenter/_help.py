# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=unused-import

from knack.help_files import helps
from .operations.marketplace_bundle._help import helps
from .operations.marketplace_offer._help import helps
from .operations.marketplace_offer_listing._help import helps
from .operations.marketplace_offer_listing_contact._help import helps
from .operations.marketplace_offer_listing_media._help import helps
from .operations.marketplace_offer_listing_uri._help import helps
from .operations.marketplace_offer_plan._help import helps
from .operations.marketplace_offer_plan_listing._help import helps
from .operations.marketplace_offer_plan_technicalconfiguration._help import helps
from .operations.marketplace_offer_setup._help import helps


helps['partnercenter marketplace'] = """
    type: group
    short-summary: Commands to manage the Partner Center Marketplace.
"""
