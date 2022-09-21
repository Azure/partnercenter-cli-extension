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

# API Operations
# pylint: disable=too-many-locals
def verify_bundle(manifest_file):
    container_id = _get_container_id(manifest_file)
    result = call_verify(container_id, './cpaMount')
    _print_result(result)

def build_bundle(manifest_file):
    container_id = _get_container_id(manifest_file)
    result = call_buildbundle(container_id, './cpaMount')
    _print_result(result)
    
def call_verify(container_id, directory):
    command = "docker exec " + container_id + " cpa verify --directory " + directory
    return subprocess.run([command],shell=True,capture_output=True)

def call_buildbundle(container_id, directory):
    command = "docker exec " + container_id + " cpa buildbundle --directory " + directory
    return subprocess.run([command],shell=True,capture_output=True)

def update_bundle(cmd, instance, arg):
    # TODO: Implement partnercenter marketplace offer update
    return instance

def delete_bundle(cmd):
    raise CLIError('TODO: Implement `partnercenter marketplace offer delete`')

def get_bundle(cmd):
    raise CLIError('TODO: Implement `partnercenter marketplace offer show`')

def list_bundle(cmd):
    raise CLIError('TODO: Implement `partnercenter marketplace offer show`')

def _print_result(result):
    output = result.stdout.decode("utf-8")
    error = result.stderr.decode("utf-8")
    print(output)

def _get_container_id(manifest_file):
    container_name = "cpacontainer"
    container_lookup_name = "/" + container_name
    container_id  = _get_running_container_id(container_lookup_name)

    if container_id == "":
        mount_path = _get_mount_path(manifest_file)
        result = _start_container(container_name, mount_path)
        container_id = _get_running_container_id(container_lookup_name)
    
    return container_id

def _get_running_container_id(container_name):
    client = docker.APIClient(base_url='unix://var/run/docker.sock')
    ps = client.containers(False, True)
    for item in ps:
        if item['Names'][0] == container_name:
            return item['Id']
    return ""

def _start_container(container_name, mount_path):
    container_image = "bobjac/cnab:8.0"
    command = "docker run --name " + container_name + " -d -v /var/run/docker.sock:/var/run/docker.sock -v " + mount_path + ":/cpaMount " + container_image + " sleep infinity"
    return subprocess.run([command],shell=True,capture_output=True)

def _stop_container(container_name):
    command = "docker stop " + container_name
    return subprocess.run([command],shell=True,capture_output=True)

def _remove_container(container_name):
    command = "docker rm " + container_name
    return subprocess.run([command],shell=True,capture_output=True)

def _get_mount_path(manifest_file):
    return os.path.dirname(manifest_file)




