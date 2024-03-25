# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class PackageConfiguration(Model):
    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'allowed_customer_actions': {'key': 'allowedCustomerActions', 'type': '[str]'},
        'azure_government_authorizations': {'key': 'azureGovernmentAuthorizations', 'type': '[PackageAuthorization]'},
        'can_enable_customer_actions': {'key': 'canEnableCustomerActions', 'type': 'bool'},
        'customerAccessEnableState': {'key': 'customerAccessEnableState', 'type': 'str'},
        'deploymentMode': {'key': 'deploymentMode', 'type': 'str'},
        'odata_etag': {'key': '@odata.etag', 'type': 'str'},
        'package_references': {'key': 'packageReferences', 'type': '[PackageReference]'},
        'public_azure_authorizations': {'key': 'publicAzureAuthorizations', 'type': '[PackageAuthorization]'},
        'public_azure_tenant_id': {'key': 'publicAzureTenantID', 'type': 'str'},
        'publisherManagementMode': {'key': 'publisherManagementMode', 'type': 'str'},
        'resource_type': {'key': 'resourceType', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'}
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.id = kwargs.get('id', None)
        self.allowed_customer_actions = kwargs.get('allowed_customer_actions', [])
        self.azure_government_authorizations = kwargs.get('azure_government_authorizations', [])
        self.can_enable_customer_actions = kwargs.get('can_enable_customer_actions', False)
        self.customerAccessEnableState = kwargs.get('customerAccessEnableState', None)
        self.deploymentMode = kwargs.get('deploymentMode', None)
        self.odata_etag = kwargs.get('odata_etag', None)
        self.package_references = kwargs.get('package_references', [])
        self.public_azure_authorizations = kwargs.get('public_azure_authorizations', [])
        self.public_azure_tenant_id = kwargs.get('public_azure_tenant_id', None)
        self.publisherManagementMode = kwargs.get('publisherManagementMode', None)
        self.resource_type = kwargs.get('resource_type', None)
        self.version = kwargs.get('version', None)
        self._resource = kwargs.get('resource', None)
