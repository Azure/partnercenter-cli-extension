import os
import os.path
import re
import subprocess
import time
import docker
import yaml

def call_verify(container_id, directory):
    command = "docker exec " + container_id + " cpa verify --directory " + directory
    return subprocess.run([command],shell=True,capture_output=True)

def call_buildbundle(container_id, directory):
    command = "docker exec -w /cpaMount " + container_id + " cpa buildbundle"
    return subprocess.run([command],shell=True,capture_output=True)

def _print_result(result):
    error = result.stderr.decode("utf-8")
    if len(error) > 0:
        print(error)

    output = result.stdout.decode("utf-8")
    print(output)

def _get_running_container_id(container_name):
    client = docker.APIClient(base_url='unix://var/run/docker.sock')
    ps = client.containers(False, True)
    for item in ps:
        if item['Names'][0] == container_name:
            return item['Id']
    return ""

def _get_container_id(manifest_file):
    container_name = "cpacontainer"
    container_lookup_name = "/" + container_name
    container_id  = _get_running_container_id(container_lookup_name)

    if container_id == "":
        mount_path = _get_mount_path(manifest_file)
        result = _start_container(container_name, mount_path)
        container_id = _get_running_container_id(container_lookup_name)
    
    return container_id

def _start_container(container_name, mount_path):
    container_image = "bobjac/cnab:8.0"
    command = "docker run --name " + container_name + " -d -v /var/run/docker.sock:/var/run/docker.sock -v " + mount_path + ":/cpaMount" + " -v $HOME/.azure:/root/.azure "+ container_image + " sleep infinity"
    print(command)
    return subprocess.run([command],shell=True,capture_output=True)

def _stop_container(container_name):
    command = "docker stop " + container_name
    return subprocess.run([command],shell=True,capture_output=True)

def _remove_container(container_name):
    command = "docker rm " + container_name
    return subprocess.run([command],shell=True,capture_output=True)

def _get_mount_path(manifest_file):
    return os.path.dirname(manifest_file)

def _make_local_directory(container_id, directory):
    command = "docker exec " + container_id + " mkdir " + directory
    return subprocess.run([command],shell=True,capture_output=True)

def _list_directory(container_id, directory):
    command = "docker exec " + container_id + " ls -la " + directory
    return subprocess.run([command],shell=True,capture_output=True)

def _copy_to_local_directory(container_id, directory):
    command = "docker exec " + container_id + " cp -R /cpaMount " + directory
    return subprocess.run([command],shell=True,capture_output=True)

def _login_to_acr(container_id, acr_name):
    command = "docker exec " + container_id + " az acr login -n " + acr_name
    return subprocess.run([command],shell=True,capture_output=True)

def _get_acr_name(manifest_file):
    acr_name = ""
    with open(manifest_file, 'r') as file:
        manifest = yaml.safe_load(file)
        registry_server = manifest['registryServer']
        index = registry_server.index('.')
        if index > -1:
            acr_name = registry_server[:index]

    return acr_name