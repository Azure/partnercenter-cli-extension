# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


def get_api_client(cli_ctx, *_):
    """Gets an instance of an sdk client"""
    print(f'cli_ctx - {cli_ctx}')
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

    return api_client