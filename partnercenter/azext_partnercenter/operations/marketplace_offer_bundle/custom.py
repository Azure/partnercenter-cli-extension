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
    print("inside bundle_offer with a manifest_file of " + manifest_file)
    container_name = "cpacontainer"
    mount_path = get_mount_path(manifest_file)
    print('The mount_path was ' + mount_path)

    result = start_container(container_name, mount_path)
    print('the result of start_container was ') 
    print(result)

    container_lookup_name = "/" + container_name
    container_id = get_container_id(container_lookup_name)
    print('container_id - ')
    print(container_id)

    result = call_verify(container_id, './cpaMount')
    print('bundle executed with a result of ') 
    print(result)


def update_bundle(cmd, instance, arg):
    # TODO: Implement partnercenter marketplace offer update
    return instance

def delete_bundle(cmd):
    raise CLIError('TODO: Implement `partnercenter marketplace offer delete`')

def get_bundle(cmd):
    raise CLIError('TODO: Implement `partnercenter marketplace offer show`')


def list_bundle(cmd):
    raise CLIError('TODO: Implement `partnercenter marketplace offer show`')
    
def start_container(container_name, mount_path):
    container_image = "bobjac/cnab:7.0"
    command = "docker run --name " + container_name + " -d -v /var/run/docker.sock:/var/run/docker.sock -v " + mount_path + ":/cpaMount " + container_image + " sleep infinity"
    return subprocess.run([command],shell=True,capture_output=True)

def stop_container(container_name):
    command = "docker stop " + container_name
    return subprocess.run([command],shell=True,capture_output=True)

def remove_container(container_name):
    command = "docker rm " + container_name
    return subprocess.run([command],shell=True,capture_output=True)

def get_mount_path(manifest_file):
    return os.path.dirname(manifest_file)

def get_container_id(container_name):
    client = docker.APIClient(base_url='unix://var/run/docker.sock')
    ps = client.containers(False, True)
    for item in ps:
        if item['Names'][0] == container_name:
            return item['Id']
    return ""

def call_verify(container_id, directory):
    command = "docker exec " + container_id + " cpa verify --directory " + directory
    print('Inside call_verify with a command of: ' + command)
    return subprocess.run([command],shell=True,capture_output=True)

def call_buildbundle(container_id, directory):
    command = "docker exec " + container_id + " cpa buildbundle --directory " + directory
    print('Inside call_buildbundle with a command of: ' + command)
    return subprocess.run([command],shell=True,capture_output=True)

