# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long

def load_arguments(commands_loader, _):
    with commands_loader.argument_context('partnercenter marketplace bundle') as c:
        c.argument('manifest_file', help='The location of the manifest file.')
