# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long

from azure.cli.core.azclierror import (ResourceNotFoundError, InvalidArgumentValueError)
from knack.cli import CLIError
from azext_partnercenter.models import OfferType
from ._cnab_util import (bundle, verify)


ISSUES_URL = "https://github.com/Azure/partnercenter-cli-extension/issues"


def build_package(client, offer_id, manifest_file=None):
    _execute_action_by_offer_type(client, offer_id, lambda: _build_cnab_bundle(manifest_file))


def verify_package(client, offer_id, manifest_file=None):
    _execute_action_by_offer_type(client, offer_id, lambda: _verify_cnab_bundle(manifest_file))


def _execute_action_by_offer_type(client, offer_id, action):
    offer = client.get(offer_id)
    if offer is None:
        raise ResourceNotFoundError('An Offer was not found with that ID.', 'Please check the value set for parameter --offer-id.')

    offer_type = offer.type

    if offer_type == OfferType.AZUREAPPLICATION:
        offer_setup = client.get_setup(offer_id)
        # if the offer type is "AzureApplication" AND the offer is setup to sell through Microsoft, we can build a CNAB bundle for it
        if offer_setup.sell_through_microsoft:
            action()
        else:
            raise InvalidArgumentValueError(f'{offer_id} offer is not setup to support a CNAB bundle. The offer type must be {OfferType.AZUREAPPLICATION} and setup to sell through Microsoft',
                                            f'Update the offer\'s setup to sell through Microsoft.\n\n   az partercenter marketplace offer setup --offer-id {offer_id} --sell-through-microsoft')

    # if we got to this point, the offer type isn't supported
    raise CLIError(f'{offer_id} offer is a {offer_type} type which is currently not supported by the CLI. Please submit an issue to get support at {ISSUES_URL}.')


def _verify_cnab_bundle(manifest_file):
    result = verify(manifest_file)
    return result


def _build_cnab_bundle(manifest_file):
    result = bundle(manifest_file)
    return result.output
