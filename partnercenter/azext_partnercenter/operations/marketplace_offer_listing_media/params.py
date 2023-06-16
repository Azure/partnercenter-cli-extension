# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core.commands.parameters import get_enum_type
from azext_partnercenter.models import (MediaType)


def load_arguments(commands_loader, _):
    with commands_loader.argument_context('partnercenter marketplace offer listing media') as c:
        c.argument('offer_id', options_list=['--offer-id', '--id'], help='The Offer ID.')
        c.argument('media_type', options_list=['--type', '-t'],
                   arg_type=get_enum_type(MediaType), help='The media type.')
        c.argument('file', options_list=['--file', '-f'], help='The path to the media file.')
        c.argument('streaming_uri', options_list=['--streaming-uri'], help='The streaming URI.')
