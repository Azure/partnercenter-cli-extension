# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long

from azure.cli.core.commands.parameters import get_enum_type
from azext_partnercenter.models import OfferType, TargetType


def load_arguments(commands_loader, _):
    with commands_loader.argument_context("partnercenter marketplace offer") as c:
        c.argument("offer_id", options_list=["--offer-id", "--id"], help="The offer ID")

    with commands_loader.argument_context("partnercenter marketplace offer create") as c:
        c.argument(
            "offer_id",
            options_list=["--offer-id", "--id"],
            help="Use only lowercase, alphanumeric characters, dashes or underscores. ID cannot be modified.",
        )
        c.argument(
            "offer_alias",
            options_list=["--alias", "-a"],
            help="This name won't be used in the marketplace listing and is solely for reference within Partner Center.",
        )
        c.argument(
            "offer_type",
            options_list=["--type", "-t"],
            arg_type=get_enum_type(OfferType),
            help="The type of offer to create.",
        )

    with commands_loader.argument_context("partnercenter marketplace offer publish") as c:
        c.argument(
            "target",
            options_list=["--target"],
            arg_type=get_enum_type(TargetType),
            help="The target environment type to publish all draft resources",
        )
