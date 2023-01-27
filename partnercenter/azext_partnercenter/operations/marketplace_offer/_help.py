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

    helps['partnercenter marketplace offer show'] = """
        type: command
        short-summary: Get a marketplace offer
        examples:
        - name: Get an offer
          text: |-
                az partnercenter marketplace offer show --id MyOfferId
    """

    helps['partnercenter marketplace offer create'] = """
        type: command
        short-summary: Create a marketplace offer
        examples:
        - name: Create an Azure Container offer
          text: |-
                az partnercenter marketplace offer create --id MyOfferId --alias "My Offer Alias" --type AzureContainer
    """

    helps['partnercenter marketplace offer delete'] = """
        type: command
        short-summary: Delete a marketplace offer
        examples:
        - name: Delete an offer
          text: |-
                az partnercenter marketplace offer delete --id MyOfferId
    """

    helps['partnercenter marketplace offer list'] = """
        type: command
        short-summary: List marketplace offers
        examples:
        - name: List all offer
          text: |-
                az partnercenter marketplace offer list
    """

    helps['partnercenter marketplace offer publish'] = """
        type: command
        short-summary: Publishes all draft changes made to a marketplace offer.
        long-summary:  This command publishes every change that's in draft. If you want to target a specific submission, use offer submission commands
        examples:
        - name: Publish all draft changes for an offer
          text: |-
                az partnercenter marketplace offer publish --id myOfferId --target preview
    """