# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long

from azure.cli.core.commands import CliCommandType
from azext_partnercenter._client_factory import cf_offer_listing


def load_command_table(commands_loader, _):
    command_type = CliCommandType(
        operations_tmpl="azext_partnercenter.clients#OfferListingClient.{}", client_factory=cf_offer_listing
    )
    custom_command_type = CliCommandType(
        operations_tmpl="azext_partnercenter.operations.marketplace_offer_listing_contact.custom#{}",
        client_factory=cf_offer_listing,
    )

    with commands_loader.command_group(
        "partnercenter marketplace offer listing contact",
        command_type=command_type,
        custom_command_type=custom_command_type,
        is_preview=True,
    ) as g:
        g.custom_command("list", "list_contact", table_transformer=None)
        g.custom_command("delete", "delete_contact", confirmation=True)
        g.generic_update_command(
            "add", custom_func_name="add_contact", getter_name="get_contacts", setter_name="update_contacts"
        )
