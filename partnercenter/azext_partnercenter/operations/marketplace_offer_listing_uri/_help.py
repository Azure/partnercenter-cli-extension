# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.help_files import helps


def load_help():
    helps['partnercenter marketplace offer listing uri'] = """
        type: group
        short-summary: Manage a Marketplace Offer listing's URIs.
    """

    helps['partnercenter marketplace offer listing uri add'] = """
        type: command
        short-summary: Add a URI for a marketplace offer listing
        examples:
        - name: Add URI to an offer's listing
          text: |-
                az partnercenter marketplace offer listing uri add --offer-id MyOfferId --uri https://myuri --type PrivacyUri
    """

    helps['partnercenter marketplace offer listing uri delete'] = """
        type: command
        short-summary: Delete uri for a marketplace offer listing
        examples:
        - name: Delete a URI for an offer's listing
          text: |-
                az partnercenter marketplace offer listing uri delete --offer-id MyOfferId --uri https://myuri --type PrivacyUri
    """

    helps['partnercenter marketplace offer listing uri list'] = """
        type: command
        short-summary: List the uri for a marketplace offer listing
        examples:
        - name: List the URIs for an offer's listing
          text: |-
                az partnercenter marketplace offer listing uri list --offer-id MyOfferId
    """
