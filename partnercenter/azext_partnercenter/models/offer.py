# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
from enum import Enum
from azure.core import CaseInsensitiveEnumMeta
from msrest.serialization import Model


class Offer(Model):
    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, **kwargs):
        super(Offer, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)
        self.name = kwargs.get('name', None)
        self._resource = kwargs.get('resource', None)


class OfferType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The offer types"""

    SOFTWAREASASERVICE = "SoftwareAsAService"
    AZUREAPPLICATION = "AzureApplication"
    AZURETHIRDPARTYVIRTUALMACHINE = "AzureThirdPartyVirtualMachine"
    AZURECONTAINER = "AzureContainer"
    AZURECONSULTINGSERVICE = "AzureConsultingService"
    AZUREDYNAMICS365FORCUSTOMERENGAGEMENT = "AzureDynamics365ForCustomerEngagement"
    AZUREDYNAMICS365FOROPERATIONS = "AzureDynamics365ForOperations"
    AZUREDYNAMICS365BUSINESSCENTRAL = "AzureDynamics365BusinessCentral"
    AZUREIOTEDGEMODULE = "AzureIoTEdgeModule"
    AZUREMANAGEDSERVICE = "AzureManagedService"
    AZUREPOWERBIAPP = "AzurePowerBIApp"
    AZUREPOWERBIVISUAL = "AzurePowerBIVisual"