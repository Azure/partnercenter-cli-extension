# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from ._util import get_api_client


class BaseClient:
    """Base client implementation"""
    def __init__(self, cli_ctx, *_):
        self._api_client = get_api_client(cli_ctx, *_)


    def _get_access_token(self):
        return self._api_client.configuration.access_token