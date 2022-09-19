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
def create_offer(cmd, arg):
    raise CLIError('TODO: Implement `partnercenter marketplace offer create`')


def update_offer(cmd, instance, arg):
    # TODO: Implement partnercenter marketplace offer update
    return instance

def delete_offer(cmd):
    raise CLIError('TODO: Implement `partnercenter marketplace offer delete`')

def get_offer(cmd):
    raise CLIError('TODO: Implement `partnercenter marketplace offer show`')


def list_offer(cmd):
    raise CLIError('TODO: Implement `partnercenter marketplace offer show`')

def bundle_offer(manifest_file):
    print("inside bundle_offer with a manifest_file of " + manifest_file)
    container_name = "cpacontainer"
    mount_path = get_mount_path(manifest_file)

    result = start_container(container_name, mount_path)

    container_lookup_name = "/" + container_name
    container_id = get_container_id(container_lookup_name)



    raise CLIError('TODO: Implement `partnercenter marketplace offer bundle`')

def start_container(container_name, mount_path):
    command = "docker run --name " + container_name + " -d -v /var/run/docker.sock:/var/run/docker.sock -v " + mount_path + ":/cpa mcr.microsoft.com/container-package-app:latest sleep infinity"
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

def call_buildbundle(container_id, directory):
    command = "docker exec " + container_id + " cpa buildbundle --directory " + directory
