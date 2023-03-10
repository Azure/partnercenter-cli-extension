# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.help_files import helps


def load_help():
    helps[
        "partnercenter marketplace offer listing contact"
    ] = """
        type: group
        short-summary: Manage a Marketplace Offer listing's contacts.
    """

    helps[
        "partnercenter marketplace offer listing contact add"
    ] = """
        type: command
        short-summary: Add a contact to a marketplace offer listing
        examples:
        - name: Add a contact to an offer's listing
          text: |-
                az partnercenter marketplace offer listing contact add --offer-id MyOfferId --type Engineering
    """

    helps[
        "partnercenter marketplace offer listing contact delete"
    ] = """
        type: command
        short-summary: Delete a contact to a marketplace offer listing
        examples:
        - name: Delete a contact to an offer's listing
          text: |-
                az partnercenter marketplace offer listing contact delete --offer-id MyOfferId --type Engineering
    """

    helps[
        "partnercenter marketplace offer listing contact list"
    ] = """
        type: command
        short-summary: List the contacts for a marketplace offer listing
        examples:
        - name: List the contacts for an offer's listing
          text: |-
                az partnercenter marketplace offer listing contact list --offer-id MyOfferId
    """
