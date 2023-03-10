# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long

from azure.cli.core.commands.parameters import get_enum_type
from azext_partnercenter.models import TargetType


def load_arguments(commands_loader, _):
    with commands_loader.argument_context("partnercenter marketplace offer submission") as c:
        c.argument("offer_id", options_list=["--offer-id"], help="The offer ID.")
        c.argument("submission_id", options_list=["--submission-id"], help="The offer submission ID.")

    with commands_loader.argument_context("partnercenter marketplace offer submission publish") as c:
        c.argument(
            "target",
            options_list=["--target"],
            arg_type=get_enum_type(TargetType),
            help="The target environment type to publish changes for the submission to.",
        )
