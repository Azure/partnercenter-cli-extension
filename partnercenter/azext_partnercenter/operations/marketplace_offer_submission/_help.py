# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.help_files import helps


def load_help():
    helps['partnercenter marketplace offer submission'] = """
        type: group
        short-summary: Manage a Marketplace Offer's submissions.
    """

    helps['partnercenter marketplace offer submission show'] = """
        type: command
        short-summary: Get the submission of a marketplace offer
        examples:
        - name: Get an offer's submission
          text: |-
                az partnercenter marketplace offer submission show --offer-id MyOfferId --submission-id 11521167929065
    """

    helps['partnercenter marketplace offer submission list'] = """
        type: command
        short-summary: List the submissions of a marketplace offer
        examples:
        - name: List an offer's submissions
          text: |-
                az partnercenter marketplace offer submission list --offer-id MyOfferId
    """

    helps['partnercenter marketplace offer submission publish'] = """
        type: command
        short-summary: Publish the submissions of a marketplace offer
        examples:
        - name: Publish an offer's submissions
          text: |-
                az partnercenter marketplace offer submission publish --offer-id MyOfferId  --submission-id 11521167929065
    """
