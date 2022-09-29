import os
import os.path
import sys
import docker
import yaml
import json
from knack.util import CLIError

def verify(manifest_file):
    container = _get_container(manifest_file)
    result = container.exec_run('cpa verify --directory ./cpaMount')
    response = _parse_verify_response(result)
    templates = response['templates']
    return response

def bundle(manifest_file):
    container = _get_container(manifest_file)
    acr_name = _get_acr_name(manifest_file)
    result = container.exec_run('az acr login -n ' + acr_name)
    result = container.exec_run('cpa buildbundle', workdir='/cpaMount')
    return result

def _parse_verify_response(response):
    parsed_template_result = _parse_template_results(response)
    mapped_templates = list(map(lambda x: json.loads(x), parsed_template_result['templates']))

    parsed_response = {
        'templates': mapped_templates
    }

    return parsed_response

def _parse_template_results(response):
    import regex
    output = response.output.decode("utf-8")
    pattern = regex.compile(r'\{(?:[^{}]|(?R))*\}')
    returned_list = pattern.findall(output)

    for json_string in returned_list:
        output = output.replace(json_string, "")

    print(output)
    parsed_results = {
        'stripped': output,
        'templates': returned_list
    }
    return parsed_results

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

    except docker.errors.NotFound:
        mount_path = _get_mount_path(manifest_file)
        container = _run_container(container_name, mount_path)
    except:
        raise CLIError('There was an unknow error when trying to find the cpacontainer')
    finally:
        return container

def _run_container(container_name, mount_path):
    client = docker.from_env()
    home_directory = os.path.expanduser('~')
    absolute_path = f'{home_directory}/.azure'
    img = 'bobjac/cnab:8.0'
    cmd = 'sleep infinity'
    volumes = ['/var/run/docker.sock:/var/run/docker.sock', f'{mount_path}:/cpaMount', f'{absolute_path}:/root/.azure']
    container = client.containers.run(img, cmd, detach=True, volumes=volumes, name=container_name)
    return container

def _get_mount_path(manifest_file):
    return os.path.dirname(manifest_file)

def _get_acr_name(manifest_file):
    acr_name = ""
    with open(manifest_file, 'r', encoding="utf-8") as file:
        manifest = yaml.safe_load(file)
        registry_server = manifest['registryServer']
        index = registry_server.index('.')
        if index > -1:
            acr_name = registry_server[:index]

    return acr_name
