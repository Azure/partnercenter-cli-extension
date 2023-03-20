# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class PlanTechnicalConfigurationType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The plan's technical configuration type"""

    Container = "Container"
    ContainerCnab = "ContainerCnab"
