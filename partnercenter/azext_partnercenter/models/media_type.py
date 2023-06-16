# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class MediaType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The media type"""

    Image = "image"
    Video = "video"
    AzureLogoLarge = "azureLargeLarge"
    AzureLogoSmall = "azureLogoSmall"
    AzureLogoMedium = "azureLogoMedium"
    AzureLogoWide = "azureLogoWide"
