# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


def cf_partnercenter(cli_ctx, *_):

    from azure.cli.core.commands.client_factory import get_mgmt_service_client
    # TODO: Replace CONTOSO with the appropriate label and uncomment
    # from azure.mgmt.CONTOSO import CONTOSOManagementClient
    # return get_mgmt_service_client(cli_ctx, CONTOSOManagementClient)
    # Enter a context with an instance of the API client
    # api_client = ApiClient()

    # api_instance = ProductClient(api_client)
    # authorization = "Authorization_example" # str | User authorization
    # filter = "$filter_example" # str | Filter for paged collection. Filter by ResourceType or ExternalIDs with operation eq is allowed. (optional)
    # skip_token = "$skipToken_example" # str | Skip token for paged collection (optional)
    # client_request_id = "Client-Request-ID_example" # str | ID of request provIDed by user (optional)
    
    return None


def cf_plans(cli_ctx, *_):
    from partnercenter.azext_partnercenter.operations.marketplace_offer_plan._client import PlanClient
    client = PlanClient(cli_ctx, *_)
    return client

def cf_list(cli_ctx, *_):
    from partnercenter.azext_partnercenter.operations.marketplace_offer._client import ListClient
    client = ListClient(cli_ctx, *_)
    return client

def get_api_client(cli_ctx, *_):
    """Gets an instance of an sdk client"""
    subscription_id = cli_ctx.data['subscription_id']

    from azure.cli.core._profile import Profile
    profile = Profile(cli_ctx=cli_ctx)

    subscription = profile.get_subscription(subscription_id)
    creds, _, _ = profile.get_raw_token(resource="https://api.partner.microsoft.com")

    from partnercenter.azext_partnercenter.vendored_sdks.v1.partnercenter.api_client import ApiClient
    api_client = ApiClient()
    api_client.configuration.access_token = creds[1]
    
    # set authorixation header to the raw token credentials fetched 
    api_client.set_default_header("Authorization", creds[0] + " " + creds[1])

    return api_client
