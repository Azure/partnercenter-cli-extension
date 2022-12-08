# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.help_files import helps


def load_help():
    helps['partnercenter marketplace offer listing media'] = """
        type: group
        short-summary: Manage a Marketplace Offer listing's media including images, videos, and thumbnails.
    """


    helps['partnercenter marketplace offer listing media add'] = """
        type: command
        short-summary: Add media for a marketplace offer listing
        examples:
        - name: Add media to an offer's listing
          text: |-
                az partnercenter marketplace offer listing media add --offer-id MyOfferId --type LargeLogo
    """

    helps['partnercenter marketplace offer listing media delete'] = """
        type: command
        short-summary: Delete media for a marketplace offer listing
        examples:
        - name: Delete a media to an offer's listing
          text: |-
                az partnercenter marketplace offer listing media delete --offer-id MyOfferId --type LargeLogo
    """

    helps['partnercenter marketplace offer listing media list'] = """
        type: command
        short-summary: List the media for a marketplace offer listing
        examples:
        - name: List the media for an offer's listing
          text: |-
                az partnercenter marketplace offer listing media list --offer-id MyOfferId
    """
    
