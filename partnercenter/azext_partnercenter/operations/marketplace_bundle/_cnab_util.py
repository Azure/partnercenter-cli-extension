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

    vr = VerifyResult(result.output.decode("utf-8"))
    dict = vr.to_list()

    return dict
    #return result.output

def bundle(manifest_file):
    container = _get_container(manifest_file)
    acr_name = _get_acr_name(manifest_file)
    result = container.exec_run('az acr login -n ' + acr_name)
    result = container.exec_run('cpa buildbundle', workdir='/cpaMount')
    return result

# def _parse_verify_response(response):
#     parsed_response = {}

#     parsed_template_result = _parse_template_results(response)

#     if parsed_template_result['templates']:
#         mapped_templates = list(map(lambda x: json.loads(x), parsed_template_result['templates']))
#         parsed_response['templates'] = mapped_templates

#     lines = parsed_template_result['stripped'].splitlines()
#     for idx, x in enumerate(lines):
#         if x.find('validated,') > -1:
#             result = _parse_valided_line(x)

#     return parsed_response

# def _parse_valided_line(line):
#     x = line.split(',')

#     file_name = x[0].split()[0]
#     failures = x[1].split()[0]
#     failures = failures.strip()

#     result = {
#         'file': file_name,
#         'failures': int(failures)
#     }

#     return result

# def _parse_template_results(response):
#     import regex
#     output = response.output.decode("utf-8")
#     pattern = regex.compile(r'\{(?:[^{}]|(?R))*\}')
#     returned_list = pattern.findall(output)

#     for json_string in returned_list:
#         output = output.replace(json_string, "")

#     parsed_results = {
#         'stripped': output,
#         'templates': returned_list
#     }
#     return parsed_results

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
    img = 'bobjac/cnab:9.0'
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


class VerifyResult:

    def __init__(self, raw_string):
        self.raw_string = raw_string
        self.known_validations = ['manifest', 'helm']

    def to_list(self):
        parsed_response = []

        parsed_json_result = self._parse_json()

        if parsed_json_result['templates']:
            mapped_templates = list(map(lambda x: json.loads(x), parsed_json_result['templates']))
            parsed_response['templates'] = mapped_templates
            return parsed_response
        
        lines = parsed_json_result['stripped'].splitlines()
        print(f'len(lines) before filtering - {len(lines)}')
        lines = list(filter(None, lines))
        print(f'len(lines) after filtering - {len(lines)}')
        for idx, x in enumerate(lines):
            if x.find('validated,') > -1:
                result = self._parse_valided_line(x)
                file = result['file']
                total_file_failures = result['failures']

                if file.lower() in self.known_validations:
                    parsed_artifact = {}
                    parsed_artifact['Artifact Name'] = file
                    parsed_artifact['Total Failures'] = total_file_failures
                                
                    if total_file_failures > 0:
                        failure_list = self._get_failure_list(lines, idx, file, total_file_failures)
                        parsed_artifact['Failures'] = failure_list
                    
                    parsed_response.append(parsed_artifact)
                else:
                    template_files = 0
                    try:
                        template_files = int(file)
                    except ValueError:
                        template_files = -1
                    
                    if template_files > 0:
                        appended_templates = 0
                        current_idx = idx + 1
                        current_file = ''
                        while appended_templates < template_files:
                            current_line = lines[current_idx:current_idx+1]
                            print(f'len(lines) - {len(lines)}')
                            print(f'current_idx - {current_idx}')
                            print(f'Current Line - {current_line}')
                            file_info = self._get_template_file_info(lines[current_idx]) 
                            parsed_artifact = {}
                            parsed_artifact['Artifact Name'] = file_info['file']
                            parsed_artifact['Total Failures'] = file_info['failures']
                    
                            if file_info['failures'] > 0:
                                failure_start_idx = current_idx + 1
                                failure_end_idx = failure_start_idx + file_info['failures']
                                template_failures = lines[failure_start_idx:failure_end_idx]
                                parsed_artifact['Failures'] = template_failures
                            
                            parsed_response.append(parsed_artifact)
                            appended_templates = appended_templates + 1
                            
        return parsed_response


    def _get_template_file_info(self, line):
        print('inside _get_template_file_info')
        x = line.split(',')

        file_part = x[0].split('-')
        file_name = file_part[1].strip()
        print(f'file_name - {file_name}')

        failures = x[1].split()[0]
        failures = failures.strip()
        print(f'failures - {failures}')
        
        result = {
            'file': file_name,
            'failures': int(failures)
        }

        return result


    def _get_failure_list(self, lines, validated_line_idx, file, total_file_failures):
        first_failure_idx = validated_line_idx + 1
        last_failure_idx = (validated_line_idx + total_file_failures) + 1
        return lines[first_failure_idx:last_failure_idx]        

    def _get_template_failure_list(self, lines, validated_line_idx, file, total_file_failures):
        failures = []
        return failures

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
        import regex
        output = self.raw_string
        pattern = regex.compile(r'\{(?:[^{}]|(?R))*\}')
        returned_list = pattern.findall(output)

        for json_string in returned_list:
            output = output.replace(json_string, "")

        parsed_results = {
            'stripped': output,
            'templates': returned_list
        }
        return parsed_results