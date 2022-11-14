# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azext_partnercenter.operations.marketplace_offer import MarketplaceOfferOperations
from azext_partnercenter.operations.marketplace_offer_package import MarketplaceOfferPackageOperations
from azext_partnercenter.operations.marketplace_offer_submission import MarketplaceOfferSubmissionOperations
from azext_partnercenter.operations.marketplace_offer_plan import MarketplaceOfferPlanOperations
from azext_partnercenter.operations.marketplace_offer_plan_setup import MarketplaceOfferPlanSetupOperations
from azext_partnercenter.operations.marketplace_offer_plan_technicalconfiguration import MarketplaceOfferPlanTechnicalConfigurationOperations
from azext_partnercenter.operations.marketplace_offer_plan_listing import MarketplaceOfferPlanListingOperations
from azext_partnercenter.operations.marketplace_offer_listing_contact import MarketplaceOfferListingContactOperations
from azext_partnercenter.operations.marketplace_offer_listing_uri import MarketplaceOfferListingUriOperations
from azext_partnercenter.operations.marketplace_offer_listing import MarketplaceOfferListingOperations
from azext_partnercenter.operations.marketplace_offer_setup import MarketplaceOfferSetupOperations
from azext_partnercenter.operations.marketplace_offer_listing_media import MarketplaceOfferListingImageOperations
from azext_partnercenter.operations.marketplace_bundle import MarketplaceBundleOperations


class PartnerCenterSubGroupCommandsLoader():
    def __init__(self, commands_loader):
        self.commands_loader = commands_loader
        self.subgroup_command_loaders = [
            MarketplaceOfferOperations(self),
            # TODO: review package as part of CLI
            # MarketplaceOfferPackageOperations(self),
            MarketplaceOfferSubmissionOperations(self),
            MarketplaceOfferPlanOperations(self),
            MarketplaceOfferPlanSetupOperations(self),
            MarketplaceOfferPlanTechnicalConfigurationOperations(self),
            MarketplaceOfferListingOperations(self),
            MarketplaceOfferSetupOperations(self),
            MarketplaceBundleOperations(self),
            MarketplaceOfferPlanListingOperations(self),
            MarketplaceOfferListingContactOperations(self),
            MarketplaceOfferListingUriOperations(self),
            MarketplaceOfferListingImageOperations(self)
        ]

    def load_arguments(self, _):
        for command_loader in self.subgroup_command_loaders:
            command_loader.load_arguments(_)

    def load_command_table(self, _):
        for command_loader in self.subgroup_command_loaders:
            command_loader.load_command_table(_)
