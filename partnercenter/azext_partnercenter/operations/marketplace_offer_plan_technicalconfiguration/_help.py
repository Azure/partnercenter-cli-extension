# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.help_files import helps


def load_help():
    helps['partnercenter marketplace offer plan technical-configuration'] = """
        type: group
        short-summary: Manage a Marketplace offer plan's technical configuration.
    """

    helps['partnercenter marketplace offer plan technical-configuration package'] = """
        type: group
        short-summary: Manage packages for a plan's technical configuration.
    """

    helps['partnercenter marketplace offer plan technical-configuration show'] = """
        type: command
        short-summary: Show a plan's technical configuration
    """

    helps['partnercenter marketplace offer plan technical-configuration package add'] = """
        type: command
        short-summary: Adds a package to the technical configuration of a plan
    """

    helps['partnercenter marketplace offer plan technical-configuration package delete'] = """
        type: command
        short-summary: Deletes a package to the technical configuration of a plan
    """
