# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os
import os.path
import re
import subprocess
import time
import docker
from azure.cli.core.util import sdk_no_wait
from knack.util import CLIError
from ._cnab_util import bundle, verify, _print_container_result

# API Operations
# pylint: disable=too-many-locals
def verify_bundle(manifest_file):
    result = verify(manifest_file)
    _print_container_result(result)

def build_bundle(manifest_file):
    result = bundle(manifest_file)
    _print_container_result(result)
    
def update_bundle(cmd, instance, arg):
    # TODO: Implement partnercenter marketplace offer update
    return instance

def delete_bundle(cmd):
    raise CLIError('TODO: Implement `partnercenter marketplace offer delete`')

def get_bundle(cmd):
    raise CLIError('TODO: Implement `partnercenter marketplace offer show`')

def list_bundle(cmd):
    raise CLIError('TODO: Implement `partnercenter marketplace offer show`')








