# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long

from knack.util import CLIError
from azext_partnercenter._client_factory import cf_offers
from azext_partnercenter.models import OfferType


offer_types_supporting_test_drive = [OfferType.AZURETHIRDPARTYVIRTUALMACHINE, OfferType.AZUREAPPLICATION]


def validate_test_drive(cmd, namespace):
    """Validates that if test drive option is attempted to be enabled, that the offer type is supported."""
    client = cf_offers(cmd.cli_ctx)
    offer = client.get(namespace.offer_external_id)

    if namespace.test_drive and (offer.type not in offer_types_supporting_test_drive):
        raise CLIError(
            f"Test Drive can only be enabled for the following offer types: {OfferType.AZURETHIRDPARTYVIRTUALMACHINE}, {OfferType.AZUREAPPLICATION}"
        )
