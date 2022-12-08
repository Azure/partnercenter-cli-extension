# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.help_files import helps


def load_help():
    helps['partnercenter marketplace offer plan'] = """
        type: group
        short-summary: Manage a Marketplace offer plans.
    """

    helps['partnercenter marketplace offer plan show'] = """
        type: command
        short-summary: Get the plan of a marketplace offer
        examples:
        - name: Get an offer's plan
          text: |-
                az partnercenter marketplace offer plan show --offer-id MyOfferId --plan-id MyPlanId
    """

    helps['partnercenter marketplace offer plan update'] = """
        type: command
        short-summary: Update the plan of a marketplace offer
        examples:
        - name: Update an offer plan
          text: |-
                az partnercenter marketplace offer plan update --offer-id MyOfferId --plan-id MyPlanId
    """

    helps['partnercenter marketplace offer plan list'] = """
        type: command
        short-summary: List the plans of a marketplace offer
        examples:
        - name: List an offer's plans
          text: |-
                az partnercenter marketplace offer plan list --offer-id MyOfferId
    """
