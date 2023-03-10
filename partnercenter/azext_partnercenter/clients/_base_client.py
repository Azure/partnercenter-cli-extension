# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=too-few-public-methods

from ._client_factory import get_api_client, get_api_client_for_graph
from ._sdk_client_provider import SdkClientProvider


class BaseClient:
    """Base client implementation"""

    def __init__(self, cli_ctx, *_):
        self._api_client = get_api_client(cli_ctx, *_)
        self._graph_api_client = get_api_client_for_graph(cli_ctx, *_)
        self._sdk = SdkClientProvider(self._api_client)

    def _get_access_token(self, host=None):
        if host is None or host == "api.partner.microsoft.com":
            return self._api_client.configuration.access_token
        if host == "graph.microsoft.com":
            return self._graph_api_client.configuration.access_token
        return None
