# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class MediaType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The media type"""

    Image = "Image"
    Video = "Video"
    LogoLarge = "AzureLogoLarge"
    LogoSmall = "AzureLogoSmall"
    LogoMedium = "AzureLogoMedium"
    LogoWide = "AzureLogoWide"
