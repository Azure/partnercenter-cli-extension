# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


from azext_partnercenter.version import VERSION


USER_AGENT_HEADER = {'User-Agent': f"AzureCLI-PCExt/{VERSION}"}


def add_user_agent_header(set_headers_func):
    """Adds the user agent header to the headers dictionary."""
    if set_headers_func is None or not callable(set_headers_func):
        raise ValueError("set_headers_func must be a callable function.")
    key_name = list(USER_AGENT_HEADER.keys())[0]
    set_headers_func(key_name, USER_AGENT_HEADER[key_name])