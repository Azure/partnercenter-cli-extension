# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.util import CLIError
from knack.log import get_logger
from ._cnab_util import (bundle, verify)


logger = get_logger(__name__)


def verify_bundle(manifest_file):
    result = verify(manifest_file)
    return result


def build_bundle(manifest_file):
    result = bundle(manifest_file)
    return result.output


def update_bundle(instance):
    # TODO: Implement partnercenter marketplace offer update
    return instance


def delete_bundle(cmd):
    raise CLIError('TODO: Implement `partnercenter marketplace offer delete`')


def get_bundle(cmd):
    raise CLIError('TODO: Implement `partnercenter marketplace offer show`')


def list_bundle(cmd):
    raise CLIError('TODO: Implement `partnercenter marketplace offer show`')
