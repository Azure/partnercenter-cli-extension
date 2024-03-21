# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long
# pylint: disable=(too-many-instance-attributes

from azext_partnercenter.vendored_sdks.v1.partnercenter.apis import (
    BranchesClient, ListingClient, ProductClient, SubmissionClient, PackageClient, VariantClient, ListingImageClient, PackageConfigurationClient)


class SdkClientProvider:
    """provider of sdk clients"""
    def __init__(self, api_client):
        self._api_client = api_client
        self._product_client = None
        self._variant_client = None
        self._branches_client = None
        self._submission_client = None
        self._package_client = None
        self._listing_client = None
        self._listing_image_client = None
        self._package_configuration_client = None

    @property
    def product_client(self):
        if self._product_client is None:
            self._product_client = ProductClient(self._api_client)
        return self._product_client

    @property
    def variant_client(self):
        if self._variant_client is None:
            self._variant_client = VariantClient(self._api_client)
        return self._variant_client

    @property
    def listing_client(self):
        if self._listing_client is None:
            self._listing_client = ListingClient(self._api_client)
        return self._listing_client

    @property
    def listing_image_client(self):
        if self._listing_image_client is None:
            self._listing_image_client = ListingImageClient(self._api_client)
        return self._listing_image_client

    @property
    def branches_client(self):
        if self._branches_client is None:
            self._branches_client = BranchesClient(self._api_client)
        return self._branches_client

    @property
    def submission_client(self):
        if self._submission_client is None:
            self._submission_client = SubmissionClient(self._api_client)
        return self._submission_client

    @property
    def package_client(self):
        if self._package_client is None:
            self._package_client = PackageClient(self._api_client)
        return self._package_client

    @property
    def package_configuration_client(self):
        if self._package_configuration_client is None:
            self._package_configuration_client = PackageConfigurationClient(self._api_client)
        return self._package_configuration_client
