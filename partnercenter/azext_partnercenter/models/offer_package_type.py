# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class AzureApplicationPackageType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """
    The Azure Application package type.

    Describes the type of the application package. Direct means that the templates are
    installed directly into the app package. AppInstaller means that the templates are bundled
    up with the App Installer (that supports bicep and terraform templates)
    """

    Direct = "Direct"
    """The default packaging type. The templates are installed directly into the app package."""

    AppInstaller = "AppInstaller"
    """The templates are bundled up with the App Installer (that supports bicep and terraform templates)"""
