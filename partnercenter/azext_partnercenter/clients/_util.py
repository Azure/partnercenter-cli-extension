# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


GRAPH_API_BASE_URL = "https://graph.microsoft.com/rp/product-ingestion"


def get_api_client(cli_ctx, *_):
    """Gets an instance of an sdk client"""
    #subscription_id = cli_ctx.data['subscription_id']

    from azure.cli.core._profile import Profile
    profile = Profile(cli_ctx=cli_ctx)

    #subscription = profile.get_subscription(subscription_id)
    creds, _, _ = profile.get_raw_token(resource="https://api.partner.microsoft.com")

    from partnercenter.azext_partnercenter.vendored_sdks.v1.partnercenter.api_client import ApiClient
    api_client = ApiClient()
    api_client.configuration.access_token = creds[1]
    
    # set authorixation header to the raw token credentials fetched 
    api_client.set_default_header("Authorization", creds[0] + " " + creds[1])
    api_client.set_default_header("If-Match", "*")

    return api_client

def get_api_client_for_graph(cli_ctx, *_):
    """Gets an instance of an sdk client"""

    from azure.cli.core._profile import Profile
    profile = Profile(cli_ctx=cli_ctx)

    creds, _, _ = profile.get_raw_token(resource="https://graph.microsoft.com")

    from partnercenter.azext_partnercenter.vendored_sdks.v1.partnercenter.api_client import ApiClient

    api_client = ApiClient()
    api_client.configuration.host = GRAPH_API_BASE_URL
    api_client.configuration.server_index = 0
    
    # set authorixation header to the raw token credentials fetched 
    api_client.set_default_header("Authorization", creds[0] + " " + creds[1])
    api_client.set_default_header("If-Match", "*")

    return api_client


def object_to_dict(item):
    if (type(item) is dict or item is None):
        return item
    if hasattr(item, "to_dict") and callable(item.to_dict):
        return item.to_dict()
    return vars(item)

from urllib.parse import parse_qs, urlparse


def get_combined_paged_results(method_with_paged_response, collect_items_as_dict=False):
    """Get combined paginated results from the SDK client that's generated from the Parnter Center API"""
    items = []
    response = method_with_paged_response() if method_with_paged_response.__code__.co_argcount == 0 else method_with_paged_response('')

    if collect_items_as_dict:
        items.extend(map(object_to_dict, response.value))
    else:
        items.extend(response.value)

    if ("nextLink" in response):
        next_link = response['nextLink']

        while (next_link is not None): 
            token = _get_skip_token(next_link)
            response = method_with_paged_response(token)
            if ("value" in response):
                if collect_items_as_dict:
                    items.extend(map(object_to_dict, response.value))
                else:
                    items.extend(response.value)
            next_link = None if "nextLink" not in response else response['nextLink']

    return items

def _get_skip_token(nextLink):
    """Gets the skip token from a nextLink url found in the response of the partner center API"""
    url_parts  = urlparse(nextLink)
    params = parse_qs(url_parts.query)
    return params['$skipToken'][0]
