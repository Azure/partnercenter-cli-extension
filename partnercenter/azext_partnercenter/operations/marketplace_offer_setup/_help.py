# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.help_files import helps


def load_help():
    helps[
        "partnercenter marketplace offer setup"
    ] = """
        type: group
        short-summary: Manage a Marketplace Offer's setup.
    """

    helps[
        "partnercenter marketplace offer setup update"
    ] = """
        type: command
        short-summary: Update a marketplace offer
        examples:
        - name: Update an offer setup
          text: |-
                az partnercenter marketplace offer setup update --offer-id MyOfferId --sell-through-microsoft true
    """

    helps[
        "partnercenter marketplace offer setup show"
    ] = """
        type: command
        short-summary: Show the offer setup
        examples:
        - name: Show an offer's setup
          text: |-
                az partnercenter marketplace offer setup show --offer-id MyOfferId
    """
