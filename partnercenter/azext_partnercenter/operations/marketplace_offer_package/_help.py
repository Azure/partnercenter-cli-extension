# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.help_files import helps


def load_help():
    helps['partnercenter marketplace offer package'] = """
        type: group
        short-summary: Manage the creation of offer packages, including CNAB bundles for AKS (Azure Container offerings that you sell through Microsoft).
    """

    helps['partnercenter marketplace offer package verify'] = """
        type: command
        short-summary: Verifies the package contents for an offer prior to building it
        examples:
        - name: Verify a CNAB bundle for an AKS offering
          text: |-
                az partnercenter marketplace offer package verify --offer-id MyOfferId --manifest-file path/to/manifest.yaml
    """

    helps['partnercenter marketplace offer package build'] = """
        type: command
        short-summary: Builds the package for an offer, preparing it for upload or publishing to the offer's technical configuration
        examples:
        - name: Builds a CNAB bundle for an AKS offering
          text: |-
                az partnercenter marketplace offer package build --offer-id MyOfferId --manifest-file path/to/manifest.yaml
    """
