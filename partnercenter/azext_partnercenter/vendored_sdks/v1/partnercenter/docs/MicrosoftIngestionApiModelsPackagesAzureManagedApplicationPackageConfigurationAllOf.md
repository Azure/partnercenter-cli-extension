# MicrosoftIngestionApiModelsPackagesAzureManagedApplicationPackageConfigurationAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_type** | **str** |  | [optional]  if omitted the server will use the default value of "AzureManagedApplicationPackageConfiguration"
**version** | **str** |  | [optional] 
**allow_jit_access** | **bool, none_type** |  | [optional] 
**can_enable_customer_actions** | **bool, none_type** |  | [optional] 
**allowed_customer_actions** | **[str]** |  | [optional] 
**public_azure_tenant_id** | **str** |  | [optional] 
**public_azure_authorizations** | [**[MicrosoftIngestionApiModelsPackagesRoleAuthorization]**](MicrosoftIngestionApiModelsPackagesRoleAuthorization.md) |  | [optional] 
**azure_government_tenant_id** | **str** |  | [optional] 
**azure_government_authorizations** | [**[MicrosoftIngestionApiModelsPackagesRoleAuthorization]**](MicrosoftIngestionApiModelsPackagesRoleAuthorization.md) |  | [optional] 
**policies** | [**[MicrosoftIngestionApiModelsPackagesAzurePolicy]**](MicrosoftIngestionApiModelsPackagesAzurePolicy.md) |  | [optional] 
**package_references** | [**[MicrosoftIngestionApiModelsCommonTypeValuePair]**](MicrosoftIngestionApiModelsCommonTypeValuePair.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


