# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.help_files import helps


def load_help():
    helps['partnercenter marketplace offer plan listing'] = """
        type: group
        short-summary: Manage a Marketplace offer plan's listing.
    """

    helps['partnercenter marketplace offer plan listing show'] = """
        type: command
        short-summary: Get the plan listing of a marketplace offer
        examples:
        - name: Get an offer's plan listing
          text: |-
                az partnercenter marketplace offer plan listing show --offer-id MyOfferId --plan-id MyPlanId
    """


    helps['partnercenter marketplace offer plan listing update'] = """
        type: command
        short-summary: Update the plan listing of a marketplace offer
        examples:
        - name: Get an offer's plan listing
          text: |-
                az partnercenter marketplace offer plan listing update --offer-id MyOfferId --plan-id MyPlanId \
                    --description "Plan listing description"
    """
