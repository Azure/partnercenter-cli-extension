# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=raise-missing-from
# pylint: disable=no-self-use

import os
import os.path
import json
import docker
import yaml
from knack.util import CLIError


def verify(manifest_file):
    container = _get_container(manifest_file)
    result = container.exec_run('cpa verify --directory ./cpaMount')
    vr = VerifyResult(result.output.decode("utf-8"))
    return vr.to_list()


def bundle(manifest_file):
    container = _get_container(manifest_file)
    acr_name = _get_acr_name(manifest_file)
    result = container.exec_run('az acr login -n ' + acr_name)
    result = container.exec_run('cpa buildbundle', workdir='/cpaMount')
    return result


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
    return container


def _run_container(container_name, mount_path):
    client = docker.from_env()
    home_directory = os.path.expanduser('~')
    absolute_path = f'{home_directory}/.azure'

    # img = 'bobjac/cnab:9.0'
    img = 'mcr.microsoft.com/container-package-app:latest'
    cmd = 'sleep infinity'
    volumes = ['/var/run/docker.sock:/var/run/docker.sock', f'{mount_path}:/cpaMount', f'{absolute_path}:/root/.azure']
    container = client.containers.run(img, cmd, detach=True, volumes=volumes, name=container_name)
    return container


def _get_mount_path(manifest_file):
    return os.path.abspath(os.path.dirname(manifest_file))


def _get_acr_name(manifest_file):
    acr_name = ""
    with open(manifest_file, 'r', encoding="utf-8") as file:
        manifest = yaml.safe_load(file)
        registry_server = manifest['registryServer']
        index = registry_server.index('.')
        if index > -1:
            acr_name = registry_server[:index]
    return acr_name


# pylint: disable=too-few-public-methods


class VerifyResult:
    def __init__(self, raw_string):
        self.raw_string = raw_string

    def to_list(self):
        parsed_response = []
        parsed_json_result = self._parse_json()
        print(parsed_json_result)

        if parsed_json_result['templates']:
            mapped_templates = list(map(json.loads, parsed_json_result['templates']))
            parsed_response = {}
            parsed_response['templates'] = mapped_templates
            return parsed_response
        lines = parsed_json_result['stripped'].splitlines()
        lines = list(filter(None, lines))
        for idx, x in enumerate(lines):
            if x.find('validated,') > -1:
                result = self._parse_valided_line(x)
                file = result['file']
                total_file_failures = result['failures']
                if self._is_known_validation(file):
                    self._update_known_validation_response(parsed_response, lines, idx, file, total_file_failures)
                else:
                    self._update_unknown_validation_response(parsed_response, lines, idx, file)
        return parsed_response

    def _update_unknown_validation_response(self, parsed_response, lines, idx, file):
        template_files = self._get_template_file_cnt(file)
        if template_files > 0:
            self._update_template_validation_response(parsed_response, lines, idx, template_files)

    def _update_template_validation_response(self, parsed_response, lines, idx, template_files):
        appended_templates = 0
        current_idx = idx + 1
        while appended_templates < template_files and current_idx < len(lines):
            file_info = self._get_template_file_info(lines[current_idx])
            parsed_artifact = self._init_parsed_artifact(file_info['file'], file_info['failures'])
            if file_info['failures'] > 0:
                template_failures = self._get_template_failures(current_idx + 1, file_info['failures'], lines)
                parsed_artifact['Failures'] = template_failures
                current_idx = current_idx + len(template_failures) + 1
            parsed_response.append(parsed_artifact)
            appended_templates = appended_templates + 1

    def _update_known_validation_response(self, parsed_response, lines, idx, file, total_file_failures):
        parsed_artifact = self._init_parsed_artifact(file, total_file_failures)
        if total_file_failures > 0:
            failure_list = self._get_failure_list(lines, idx, total_file_failures)
            parsed_artifact['Failures'] = failure_list
        parsed_response.append(parsed_artifact)

    def _init_parsed_artifact(self, file, failures):
        parsed_artifact = {}
        parsed_artifact['Artifact Name'] = file
        parsed_artifact['Total Failures'] = failures
        return parsed_artifact

    def _get_template_failures(self, start_idx, failure_cnt, lines):
        end_idx = start_idx + failure_cnt
        template_failures = list(map(lambda x: x.strip(), lines[start_idx:end_idx]))
        return template_failures

    def _get_template_file_cnt(self, file):
        template_files = 0
        try:
            template_files = int(file)
        except ValueError:
            template_files = -1
        return template_files

    def _get_template_file_info(self, line):
        x = line.split(',')
        file_part = x[0].split('-')
        file_name = file_part[1].strip()
        failures = x[1].split()[0]
        failures = failures.strip()
        result = {
            'file': file_name,
            'failures': int(failures)
        }
        return result

    def _is_known_validation(self, file):
        known_validations = ['manifest', 'helm']
        file = file.lower()
        return file in known_validations

    def _get_failure_list(self, lines, validated_line_idx, total_file_failures):
        first_failure_idx = validated_line_idx + 1
        last_failure_idx = (validated_line_idx + total_file_failures) + 1
        return lines[first_failure_idx:last_failure_idx]

    def _parse_valided_line(self, line):
        x = line.split(',')
        file_name = x[0].split()[0]
        failures = x[1].split()[0]
        failures = failures.strip()
        result = {
            'file': file_name,
            'failures': int(failures)
        }
        return result

    def _parse_json(self):
        import re
        output = self.raw_string
        pattern = re.compile(r'\{(?:[^{}]|(?R))*\}')
        returned_list = pattern.findall(output)
        for json_string in returned_list:
            output = output.replace(json_string, "")
        parsed_results = {
            'stripped': output,
            'templates': returned_list
        }
        return parsed_results
