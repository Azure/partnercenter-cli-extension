# ProductsProductIDPackageconfigurationsPackageConfigurationIDGet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_type** | **str** |  | [optional]  if omitted the server will use the default value of "AzureResourceManagerTestDrivePackageConfiguration"
**id** | **str** |  | [optional] 
**odata_etag** | **str** |  | [optional] 
**package_type** | **str** |  | [optional] 
**application_installation_uri** | **str** |  | [optional] 
**package_references** | [**[MicrosoftIngestionApiModelsCommonTypeValuePair]**](MicrosoftIngestionApiModelsCommonTypeValuePair.md) |  | [optional] 
**base_license_model** | **str** |  | [optional] 
**require_s2_s_outbound_and_crm_secure_store_access** | **bool, none_type** |  | [optional] 
**application_configuration_uri** | **str** |  | [optional] 
**package_location_uri** | **str** |  | [optional] 
**package_region_availabilities** | [**[MicrosoftIngestionApiModelsPackagesPackageRegionAvailability]**](MicrosoftIngestionApiModelsPackagesPackageRegionAvailability.md) |  | [optional] 
**multiple_packages_in_package_file** | **bool, none_type** |  | [optional] 
**release_version** | **str** |  | [optional] 
**solution_identifier** | **str** |  | [optional] 
**azure_active_directory_application_id** | **str** |  | [optional] 
**azure_active_directory_application_key** | **str** |  | [optional] 
**azure_active_directory_tenant_id** | **str** |  | [optional] 
**test_drive_duration** | **int, none_type** |  | [optional] 
**azure_active_directory_tenant_name** | **str** |  | [optional] 
**max_concurrent_test_drives** | **int, none_type** |  | [optional] 
**instance_uri** | **str** |  | [optional] 
**role_name** | **str** |  | [optional] 
**instance_web_api_uri** | **str** |  | [optional] 
**trial_legal_entity** | **str** |  | [optional] 
**version** | **str** |  | [optional] 
**allow_jit_access** | **bool, none_type** |  | [optional] 
**can_enable_customer_actions** | **bool, none_type** |  | [optional] 
**allowed_customer_actions** | **[str]** |  | [optional] 
**public_azure_tenant_id** | **str** |  | [optional] 
**public_azure_authorizations** | [**[MicrosoftIngestionApiModelsPackagesRoleAuthorization]**](MicrosoftIngestionApiModelsPackagesRoleAuthorization.md) |  | [optional] 
**azure_government_tenant_id** | **str** |  | [optional] 
**azure_government_authorizations** | [**[MicrosoftIngestionApiModelsPackagesRoleAuthorization]**](MicrosoftIngestionApiModelsPackagesRoleAuthorization.md) |  | [optional] 
**policies** | [**[MicrosoftIngestionApiModelsPackagesAzurePolicy]**](MicrosoftIngestionApiModelsPackagesAzurePolicy.md) |  | [optional] 
**regions** | **[str]** |  | [optional] 
**hot_instances** | **int, none_type** |  | [optional] 
**warm_instances** | **int, none_type** |  | [optional] 
**cold_instances** | **int, none_type** |  | [optional] 
**azure_subscription_id** | **str** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


