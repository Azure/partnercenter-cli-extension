# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# Product Ingestion API
# Implementation is through pedantic via json schema to pydantic model generation
# This is in until we can figure out how jsonschema can be used with autorest as well as autorest support for anyof unions, etc.

from __future__ import annotations
from ast import pattern
from datetime import datetime
from enum import Enum
from typing import List, Optional, Union
from pydantic import ConfigDict, BaseModel, Field, RootModel


class DurableId(RootModel):
    root: str = Field(
        ...,
        description='A durable-id to an existing resource.',
        title='DurableId',
        pattern=r'^[a-z](-?[a-z0-9]+)*/[a-z0-9-]+(/?[a-z0-9-])*$'
    )


class Level(Enum):
    informational = 'informational'
    warning = 'warning'


class Code(Enum):
    business_validation_error = 'businessValidationError'
    collection_limit_exceeded = 'collectionLimitExceeded'
    invalid_id = 'invalidId'
    invalid_entity_status = 'invalidEntityStatus'
    invalid_request = 'invalidRequest'
    invalid_resource = 'invalidResource'
    invalid_state = 'invalidState'
    not_deployed = 'notDeployed'
    not_supported = 'notSupported'
    operation_canceled = 'operationCanceled'
    product_locked = 'productLocked'
    resource_not_found = 'resourceNotFound'
    schema_validation_error = 'schemaValidationError'


class ExternalId(BaseModel):
    external_id: str = Field(
        ...,
        alias='externalId',
        description='ExternalId for product and plan references. Property reference must be named product or plan.',
        pattern=r'^[a-z0-9][a-z0-9-_]{2,49}$',
        min_length=3,
        max_length=50,
    )


class ResourceName(BaseModel):
    resource_name: str = Field(
        ...,
        alias='resourceName',
        description='Resource Name that can be referenced using this value by another resource.',
        pattern=r'^[a-zA-Z0-9-_]+$',
        min_length=1,
        max_length=50,
    )


class ResourceReference(RootModel):
    root: Union[DurableId, ExternalId, ResourceName] = Field(
        ..., title='ResourceReference'
    )


class SchemaUri(RootModel):
    root: str = Field(..., title='SchemaUri', pattern=r'^https://(schema\.mp\.microsoft\.com)|(product-ingestion\.azureedge\.net)/schema/[a-z][a-z0-9]+(?:-[a-z0-9]+)*/\d{4}(?:-\d\d){2}(?:-dev|-preview\d+)?$')


class CnabReference(BaseModel):
    model_config = ConfigDict(extra="forbid")

    tenant_id: str = Field(
        ...,
        alias='tenantId',
        pattern=r'^[({]?[a-fA-F0-9]{8}[-]?([a-fA-F0-9]{4}[-]?){3}[a-fA-F0-9]{12}[})]?$',
        min_length=1,
        max_length=36)
    subscription_id: str = Field(
        ...,
        alias='subscriptionId',
        pattern=r'^[({]?[a-fA-F0-9]{8}[-]?([a-fA-F0-9]{4}[-]?){3}[a-fA-F0-9]{12}[})]?$',
        min_length=1,
        max_length=36)
    resource_group_name: str = Field(
        ..., alias='resourceGroupName', min_length=1, max_length=100
    )
    registry_name: str = Field(
        ..., alias='registryName', min_length=1, max_length=100
    )
    repository_name: str = Field(
        ..., alias='repositoryName', min_length=1, max_length=100
    )
    tag: str
    digest: str
    # tag: constr(min_length=1)
    # digest: constr(
    #     regex=r'^[a-z0-9]+([+._\-][a-z0-9]+)*:[a-zA-Z0-9=_\-]+$',
    #     min_length=1,
    #     max_length=100,
    # )


class ContainerCnabPlanTechnicalConfigurationProperties(BaseModel):
    payload_type: str = Field(..., alias='payloadType')
    cluster_extension_type: str = Field(..., alias='clusterExtensionType', pattern=r'^[a-zA-Z\.-]{1,50}$', min_length=1, max_length=50)
    cnab_references: List[CnabReference] = Field(..., alias='cnabReferences')


class ImageTag(RootModel):
    root: str
    # root: constr(min_length=1, max_length=100)


class MaskedSecret(RootModel):
    root: str = Field(..., title='MaskedSecret')


class ValidationInnerError(BaseModel):
    resource_id: Optional[ResourceReference] = Field(None, alias='resourceId')
    code: Code
    message: Optional[str] = None
    details: Optional[List[ValidationInnerError]] = None


class ImageRepositoryDetails(BaseModel):
    model_config = ConfigDict(extra="forbid")

    subscription_id: str = Field(
        ...,
        alias='subscriptionId',
        pattern=r'^[({]?[a-fA-F0-9]{8}[-]?([a-fA-F0-9]{4}[-]?){3}[a-fA-F0-9]{12}[})]?$',
        min_length=1,
        max_length=36)
    resource_group_name: str = Field(
        ..., alias='resourceGroupName', min_length=1, max_length=100
    )
    registry_name: str = Field(
        ..., alias='registryName', min_length=1, max_length=100
    )
    user_name: str = Field(..., alias='userName', min_length=1, max_length=100)
    password: Union[str, MaskedSecret]
    repository_name: Optional[str] = Field(
        None, alias='repositoryName', min_length=1, max_length=100
    )


class ContainerImagePlanTechnicalConfigurationProperties(BaseModel):
    payload_type: str = Field(..., alias='payloadType')
    image_repository_details: ImageRepositoryDetails = Field(
        ..., alias='imageRepositoryDetails'
    )
    image_tags: List[ImageTag] = Field(
        ..., alias='imageTags', max_length=16, min_length=1
    )


class Validation(ValidationInnerError):
    schema_uri: Optional[SchemaUri] = Field(None, alias='$schema')
    level: Level


class Resource(BaseModel):
    model_config = ConfigDict(extra="allow")

    resource_name: Optional[str] = Field(
        None, alias='resourceName', min_length=1, max_length=50
    )
    id: Optional[DurableId] = None
    validations: Optional[List[Validation]] = None


class ContainerPlanTechnicalConfiguration(Resource):
    product: ResourceReference
    plan: ResourceReference


class ConfigureResources(BaseModel):
    model_config = ConfigDict(extra="forbid")

    schema_uri: Optional[SchemaUri] = Field(None, alias='$schema')
    resources: List[Resource] = Field(..., min_length=1)


class JobStatus(Enum):
    not_started = 'notStarted'
    running = 'running'
    completed = 'completed'


class JobResult(Enum):
    pending = 'pending'
    succeeded = 'succeeded'
    failed = 'failed'


class SchemaUri(RootModel):
    root: str = Field(..., title='SchemaUri', pattern=r'^https://(schema\.mp\.microsoft\.com)|(product-ingestion\.azureedge\.net)/schema/[a-z][a-z0-9]+(?:-[a-z0-9]+)*/\d{4}(?:-\d\d){2}(?:-dev|-preview\d+)?$')


class Code(Enum):
    bad_request = 'badRequest'
    unauthorized = 'unauthorized'
    forbidden = 'forbidden'
    not_found = 'notFound'
    method_not_allowed = 'methodNotAllowed'
    request_timeout = 'requestTimeout'
    conflict = 'conflict'
    locked = 'locked'
    internal_server_error = 'internalServerError'
    not_implemented = 'notImplemented'
    service_unavailable = 'serviceUnavailable'


class ExternalId(BaseModel):
    external_id: str = Field(
        ...,
        alias='externalId',
        description='ExternalId for product and plan references. Property reference must be named product or plan.',
        pattern=r'^[a-z0-9][a-z0-9-_]{2,49}$',
        min_length=3,
        max_length=50
    )


class ResourceName(BaseModel):
    resource_name: str = Field(
        ...,
        alias='resourceName',
        description='Resource Name that can be referenced using this value by another resource.',
        pattern=r'^[a-zA-Z0-9-_]+$',
        min_length=1,
        max_length=50
    )


class DurableId(RootModel):
    root: str = Field(
        ...,
        description='A durable-id to an existing resource.',
        title='DurableId',
        pattern=r'^[a-z](-?[a-z0-9]+)*/[a-z0-9-]+(/?[a-z0-9-])*$'
    )


class ErrorCode(Enum):
    business_validation_error = 'businessValidationError'
    collection_limit_exceeded = 'collectionLimitExceeded'
    invalid_id = 'invalidId'
    invalid_entity_status = 'invalidEntityStatus'
    invalid_request = 'invalidRequest'
    invalid_resource = 'invalidResource'
    invalid_state = 'invalidState'
    not_deployed = 'notDeployed'
    not_supported = 'notSupported'
    operation_canceled = 'operationCanceled'
    product_locked = 'productLocked'
    resource_not_found = 'resourceNotFound'
    schema_validation_error = 'schemaValidationError'


class ResourceReference(RootModel):
    root: Union[DurableId, ExternalId, ResourceName] = Field(
        ..., title='ResourceReference'
    )


class InnerError(BaseModel):
    resource_id: Optional[ResourceReference] = Field(None, alias='resourceId')
    code: ErrorCode
    message: Optional[str] = None
    details: Optional[List[InnerError]] = None


class Error(BaseModel):
    resource_id: Optional[ResourceReference] = Field(None, alias='resourceId')
    code: Code
    message: Optional[str] = None
    details: Optional[List[InnerError]] = None


class ConfigureResourcesStatus(BaseModel):
    model_config = ConfigDict(extra="forbid")

    schema_uri: Optional[SchemaUri] = Field(None, alias='$schema')
    job_id: str = Field(..., alias='jobId')
    job_status: JobStatus = Field(..., alias='jobStatus')
    job_result: JobResult = Field(..., alias='jobResult')
    job_start: Optional[datetime] = Field(None, alias='jobStart')
    job_end: Optional[datetime] = Field(None, alias='jobEnd')
    resource_uri: Optional[str] = Field(None, alias='resourceUri')
    errors: Optional[List[Error]] = None

# Submission support


class TargetType(Enum):
    flight = 'flight'
    sandbox = 'sandbox'
    draft = 'draft'
    preview = 'preview'
    live = 'live'
    certification = 'certification'
    retail = 'retail'


class LifecycleState(Enum):
    not_available = 'notAvailable'
    never_used = 'neverUsed'
    test = 'test'
    preview = 'preview'
    generally_available = 'generallyAvailable'
    deprecated = 'deprecated'
    decommissioned = 'decommissioned'
    deleted = 'deleted'


class DeprecationScheduleReason(Enum):
    critical_security_issue = 'criticalSecurityIssue'
    end_of_support = 'endOfSupport'
    other = 'other'


class AlternativeProduct(BaseModel):
    model_config = ConfigDict(extra="forbid")

    product: ResourceReference


class AlternativePlan(BaseModel):
    model_config = ConfigDict(extra="forbid")

    plan: ResourceReference


class DeprecationSchedule(BaseModel):
    model_config = ConfigDict(extra="forbid")

    schema_uri: Optional[SchemaUri] = Field(None, alias='$schema')
    date: Optional[date] = None
    date_offset: Optional[str] = Field(None, alias='dateOffset')
    reason: Optional[DeprecationScheduleReason] = None
    alternative: Optional[Union[AlternativeProduct, AlternativePlan]] = None


class ResourceTarget(BaseModel):
    target_type: TargetType = Field(..., alias='targetType')


class Submission(Resource):
    schema_uri: Optional[SchemaUri] = Field(None, alias='$schema')
    product: ResourceReference
    target: ResourceTarget
    status: Optional[JobStatus] = None
    lifecycle_state: Optional[LifecycleState] = Field(
        'generallyAvailable', alias='lifecycleState'
    )
    deprecation_schedule: Optional[DeprecationSchedule] = Field(
        None, alias='deprecationSchedule'
    )
    result: Optional[JobResult] = None
    created: Optional[datetime] = None


ValidationInnerError.update_forward_refs()
InnerError.update_forward_refs()
