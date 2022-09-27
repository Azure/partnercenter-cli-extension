import os
import os.path
import re
import subprocess
import time
import docker
import yaml

def verify(manifest_file):
    container = _get_container(manifest_file)
    result = container.exec_run('cpa verify --directory ./cpaMount')
    return result

def bundle(manifest_file):
    container = _get_container(manifest_file)
    acr_name = _get_acr_name(manifest_file)
    result = container.exec_run('az acr login -n ' + acr_name)
    result = container.exec_run('cpa buildbundle', workdir='/cpaMount')
    return result

def _print_container_result(result):
    output = result.output.decode("utf-8")
    print(output)

def _print_result(result):
    error = result.stderr.decode("utf-8")
    if len(error) > 0:
        print(error)

    output = result.stdout.decode("utf-8")
    print(output)

def _get_container(manifest_file):
    client = docker.from_env()
    container_name = "cpacontainer"
    try:
        container = client.containers.get(container_name)
        return container
    except:
        mount_path = _get_mount_path(manifest_file)
        container = _run_container(container_name, mount_path)
        return container

def _run_container(container_name, mount_path):
    client = docker.from_env()
    home_directory = os.path.expanduser('~')
    absolute_path = f'{home_directory}/.azure'
    volumes = ['/var/run/docker.sock:/var/run/docker.sock', mount_path+':/cpaMount', absolute_path+':/root/.azure']
    container = client.containers.run('bobjac/cnab:8.0', 'sleep infinity', detach=True, volumes=volumes, name=container_name)
    return container

def _get_mount_path(manifest_file):
    return os.path.dirname(manifest_file)

def _get_acr_name(manifest_file):
    acr_name = ""
    with open(manifest_file, 'r') as file:
        manifest = yaml.safe_load(file)
        registry_server = manifest['registryServer']
        index = registry_server.index('.')
        if index > -1:
            acr_name = registry_server[:index]

    return acr_name