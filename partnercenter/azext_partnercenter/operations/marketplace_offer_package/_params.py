# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


argument_help = {
    'manifest_file': """The path to the package manifest YAML file that describes the package, the CNAB bundle, and dependent artifacts."""
}


def load_arguments(commands_loader, _):
    with commands_loader.argument_context('partnercenter marketplace offer package') as c:
        c.argument('offer_id', options_list=['--offer-id'], help='The Offer ID.')
        c.argument('manifest_file', options_list=['--manifest-file'], arg_group='AKS Offer',  help=argument_help['manifest_file'])
