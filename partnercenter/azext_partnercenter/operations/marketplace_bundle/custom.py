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
from ._cnab_util import call_verify, call_buildbundle, _print_result, _get_container_id, _list_directory, _make_local_directory, _copy_to_local_directory, _login_to_acr, _get_running_container_id, _get_mount_path, _remove_container, _start_container, _stop_container

# API Operations
# pylint: disable=too-many-locals
def verify_bundle(manifest_file):
    container_id = _get_container_id(manifest_file)
    result = call_verify(container_id, './cpaMount')
    _print_result(result)

def build_bundle(manifest_file):
    container_id = _get_container_id(manifest_file)
    result = _login_to_acr(container_id)
    result = call_buildbundle(container_id, './cpalocal/cpaMount')
    _print_result(result)
    
def update_bundle(cmd, instance, arg):
    # TODO: Implement partnercenter marketplace offer update
    return instance

def delete_bundle(cmd):
    raise CLIError('TODO: Implement `partnercenter marketplace offer delete`')

def get_bundle(cmd):
    raise CLIError('TODO: Implement `partnercenter marketplace offer show`')

def list_bundle(cmd):
    raise CLIError('TODO: Implement `partnercenter marketplace offer show`')





