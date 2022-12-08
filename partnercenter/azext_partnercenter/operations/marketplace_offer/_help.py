# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.help_files import helps


def load_help():
    helps['partnercenter marketplace offer'] = """
        type: group
        short-summary: Manage Marketplace offers.
    """

    helps['partnercenter marketplace offer create'] = """
        type: command
        short-summary: Create a marketplace offer
        examples:
        - name: Create an offer
            text: |-
                az partnercenter marketplace offer create --id MyOfferId
    """

    helps['partnercenter marketplace offer create delete'] = """
        type: command
        short-summary: Delete a marketplace offer
        examples:
        - name: Delete an offer
            text: |-
                az partnercenter marketplace offer delete --id MyOfferId
    """

    helps['partnercenter marketplace offer create list'] = """
        type: command
        short-summary: List marketplace offers
        examples:
        - name: List offers
            text: |-
                az partnercenter marketplace offer list
    """
