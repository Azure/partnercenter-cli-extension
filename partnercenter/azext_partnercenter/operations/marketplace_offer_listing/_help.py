# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.help_files import helps


def load_help():
    helps['partnercenter marketplace offer listing'] = """
        type: group
        short-summary: Manage a Marketplace Offer's listing.
    """

    helps['partnercenter marketplace offer listing show'] = """
        type: command
        short-summary: Get the listing of a marketplace offer
        examples:
        - name: Get an offer's listing
          text: |-
                az partnercenter marketplace offer listing show --offer-id MyOfferId
    """

    helps['partnercenter marketplace offer listing update'] = """
        type: command
        short-summary: Update the listing of a marketplace offer
        examples:
        - name: Update an offer listing
          text: |-
                az partnercenter marketplace offer listing update --offer-id MyOfferId --summary "My offer summary"
    """
