# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


def cf_offers(cli_ctx, *_):
    from azext_partnercenter.clients import OfferClient

    return OfferClient(cli_ctx, *_)


def cf_plans(cli_ctx, *_):
    from azext_partnercenter.clients import PlanClient

    return PlanClient(cli_ctx, *_)


def cf_plan_listing(cli_ctx, *_):
    from azext_partnercenter.clients import PlanListingClient

    return PlanListingClient(cli_ctx, *_)


def cf_offer_listing(cli_ctx, *_):
    from azext_partnercenter.clients import OfferListingClient

    return OfferListingClient(cli_ctx, *_)


def cf_offer_submission(cli_ctx, *_):
    from azext_partnercenter.clients import OfferSubmissionClient

    return OfferSubmissionClient(cli_ctx, *_)


def cf_plan_technicalconfiguration(cli_ctx, *_):
    from azext_partnercenter.clients import PlanTechnicalConfigurationClient

    return PlanTechnicalConfigurationClient(cli_ctx, *_)


def cf_listing_media(cli_ctx, *_):
    from azext_partnercenter.clients import ListingMediaClient

    return ListingMediaClient(cli_ctx, *_)
