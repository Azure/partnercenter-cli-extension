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


def cf_offers(cli_ctx, *_):
    from partnercenter.azext_partnercenter.clients import OfferClient
    client = OfferClient(cli_ctx, *_)
    return client


def cf_plans(cli_ctx, *_):
    from partnercenter.azext_partnercenter.clients import PlanClient
    client = PlanClient(cli_ctx, *_)
    return client


def cf_plan_listing(cli_ctx, *_):
    from partnercenter.azext_partnercenter.clients import PlanListingClient
    client = PlanListingClient(cli_ctx, *_)
    return client


def cf_plan_setup(cli_ctx, *_):
    from partnercenter.azext_partnercenter.clients import PlanSetupClient
    client = PlanSetupClient(cli_ctx, *_)
    return client

def cf_plan_listing_media(cli_ctx, *_):
    from partnercenter.azext_partnercenter.clients import PlanListingMediaClient
    client = PlanListingMediaClient(cli_ctx, *_)
    return client
