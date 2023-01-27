# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long


def load_arguments(commands_loader, _):
    with commands_loader.argument_context('partnercenter marketplace offer submission') as c:
        c.argument('offer_id', options_list=['--offer-id'], help='The offer ID.')
        c.argument('submission_id', options_list=['--submission-id'], help='The offer submission ID.')