# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long

from azure.cli.core.azclierror import (ResourceNotFoundError, InvalidArgumentValueError)
from knack.cli import CLIError
from azext_partnercenter.models import OfferType
from azext_partnercenter import ISSUES_URL
from ._cnab_util import (bundle, verify)


def build_package(client, offer_id, manifest_file=None):
   return _execute_action_by_offer_type(client, offer_id, manifest_file, _build_cnab_bundle)


def verify_package(client, offer_id, manifest_file=None):
    return _execute_action_by_offer_type(client, offer_id, manifest_file, _verify_cnab_bundle)


def _execute_action_by_offer_type(client, offer_id, manifest_file, action):
    offer = client.get(offer_id)
    if offer is None:
        raise ResourceNotFoundError('An Offer was not found with that ID.', 'Please check the value set for parameter --offer-id.')

    offer_type = offer.type

    if offer_type == OfferType.AZURECONTAINER:
        offer_setup = client.get_setup(offer_id)
        # if the offer type is "AzureApplication" AND the offer is setup to sell through Microsoft, we can build a CNAB bundle for it
        if offer_setup.sell_through_microsoft:
            return action(manifest_file)
        else:
            raise InvalidArgumentValueError(f'{offer_id} offer is not setup to support a CNAB bundle. The offer type must be {OfferType.AZUREAPPLICATION} and setup to sell through Microsoft',
                                            f'Update the offer\'s setup to sell through Microsoft.\n\n   az partercenter marketplace offer setup --offer-id {offer_id} --sell-through-microsoft')

    # if we got to this point, the offer type isn't supported
    raise CLIError(f'{offer_id} offer is a {offer_type} type which is currently not supported by the CLI. Please submit an issue to get support at {ISSUES_URL}.')


def _verify_cnab_bundle(manifest_file):
    result = verify(manifest_file)
    print(result.output.decode("utf-8"))
    return result


def _build_cnab_bundle(manifest_file):
    result = bundle(manifest_file)
    print(result.output.decode("utf-8"))
    return result
