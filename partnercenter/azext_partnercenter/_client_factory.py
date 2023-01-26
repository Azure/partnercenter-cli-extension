# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


def cf_offers(cli_ctx, *_):
    from azext_partnercenter.clients import OfferClient
    client = OfferClient(cli_ctx, *_)
    return client


def cf_plans(cli_ctx, *_):
    from azext_partnercenter.clients import PlanClient
    client = PlanClient(cli_ctx, *_)
    return client


def cf_plan_listing(cli_ctx, *_):
    from azext_partnercenter.clients import PlanListingClient
    client = PlanListingClient(cli_ctx, *_)
    return client


def cf_offer_listing(cli_ctx, *_):
    from azext_partnercenter.clients import OfferListingClient
    client = OfferListingClient(cli_ctx, *_)
    return client


def cf_plan_technicalconfiguration(cli_ctx, *_):
    from azext_partnercenter.clients import PlanTechnicalConfigurationClient
    client = PlanTechnicalConfigurationClient(cli_ctx, *_)
    return client


def cf_listing_media(cli_ctx, *_):
    from azext_partnercenter.clients import ListingMediaClient
    client = ListingMediaClient(cli_ctx, *_)
    return client
