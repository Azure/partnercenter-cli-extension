# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# Product Ingestion API

from __future__ import annotations
from enum import Enum
from typing import List, Optional, Union
from pydantic import BaseModel, Extra, Field, constr

# Implementation is through pedantic via json schema to pydantic model generation
# This is in until we can figure out how jsonschema can be used with autorest as well as autorest support for anyof unions, etc.

class DurableId(BaseModel):
    __root__: constr(regex=r'^[a-z](-?[a-z0-9]+)*/[a-z0-9-]+(\/?[a-z0-9-])*$') = Field(
        ..., description='A durable-id to an existing resource.', title='DurableId'
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
    external_id: constr(
        regex=r'^[a-z0-9][a-z0-9-_]{2,49}$', min_length=3, max_length=50
    ) = Field(
        ...,
        alias='externalId',
        description='ExternalId for product and plan references. Property reference must be named product or plan.',
    )


class ResourceName(BaseModel):
    resource_name: constr(
        regex=r'^[a-zA-Z0-9-_]+$', min_length=1, max_length=50
    ) = Field(
        ...,
        alias='resourceName',
        description='Resource Name that can be referenced using this value by another resource.',
    )


class ResourceReference(BaseModel):
    __root__: Union[DurableId, ExternalId, ResourceName] = Field(
        ..., title='ResourceReference'
    )


class SchemaUri(BaseModel):
    __root__: constr(
        regex=r'^https://(schema\.mp\.microsoft\.com)|(product-ingestion\.azureedge\.net)/schema/[a-z][a-z0-9]+(?:-[a-z0-9]+)*/\d{4}(?:-\d\d){2}(?:-dev|-preview\d+)?$'
    ) = Field(..., title='SchemaUri')


class CnabReference(BaseModel):
    class Config:
        extra = Extra.forbid

    tenant_id: constr(
        regex=r'^[({]?[a-fA-F0-9]{8}[-]?([a-fA-F0-9]{4}[-]?){3}[a-fA-F0-9]{12}[})]?$',
        min_length=1,
        max_length=36,
    ) = Field(..., alias='tenantId')
    subscription_id: constr(
        regex=r'^[({]?[a-fA-F0-9]{8}[-]?([a-fA-F0-9]{4}[-]?){3}[a-fA-F0-9]{12}[})]?$',
        min_length=1,
        max_length=36,
    ) = Field(..., alias='subscriptionId')
    resource_group_name: constr(min_length=1, max_length=100) = Field(
        ..., alias='resourceGroupName'
    )
    registry_name: constr(min_length=1, max_length=100) = Field(
        ..., alias='registryName'
    )
    repository_name: constr(min_length=1, max_length=100) = Field(
        ..., alias='repositoryName'
    )
    tag: constr(min_length=1)
    digest: constr(
        regex=r'^[a-z0-9]+([+._\-][a-z0-9]+)*:[a-zA-Z0-9=_\-]+$',
        min_length=1,
        max_length=100,
    )


class ContainerCnabPlanTechnicalConfigurationProperties(BaseModel):
    payload_type: str = Field(..., alias='payloadType')
    cluster_extension_type: constr(
        regex=r'^[a-zA-Z\.-]{1,50}$', min_length=1, max_length=50
    ) = Field(..., alias='clusterExtensionType')
    cnab_references: List[CnabReference] = Field(..., alias='cnabReferences')


class ImageTag(BaseModel):
    __root__: constr(min_length=1, max_length=100)


class MaskedSecret(BaseModel):
    __root__: str = Field(..., title='MaskedSecret')


class InnerError(BaseModel):
    resource_id: Optional[ResourceReference] = Field(None, alias='resourceId')
    code: Code
    message: Optional[str] = None
    details: Optional[List[InnerError]] = None


class ImageRepositoryDetails(BaseModel):
    class Config:
        extra = Extra.forbid

    subscription_id: constr(
        regex=r'^[({]?[a-fA-F0-9]{8}[-]?([a-fA-F0-9]{4}[-]?){3}[a-fA-F0-9]{12}[})]?$',
        min_length=1,
        max_length=36,
    ) = Field(..., alias='subscriptionId')
    resource_group_name: constr(min_length=1, max_length=100) = Field(
        ..., alias='resourceGroupName'
    )
    registry_name: constr(min_length=1, max_length=100) = Field(
        ..., alias='registryName'
    )
    user_name: constr(min_length=1, max_length=100) = Field(..., alias='userName')
    password: Union[constr(min_length=1, max_length=100), MaskedSecret]
    repository_name: Optional[constr(min_length=1, max_length=100)] = Field(
        None, alias='repositoryName'
    )


class ContainerImagePlanTechnicalConfigurationProperties(BaseModel):
    payload_type: str = Field(..., alias='payloadType')
    image_repository_details: ImageRepositoryDetails = Field(
        ..., alias='imageRepositoryDetails'
    )
    image_tags: List[ImageTag] = Field(
        ..., alias='imageTags', max_items=16, min_items=1
    )


class Validation(InnerError):
    _schema: Optional[SchemaUri] = Field(None, alias='$schema')
    level: Level


class Resource(BaseModel):
    class Config:
        extra = Extra.allow

    resource_name: Optional[constr(min_length=1, max_length=50)] = Field(
        None, alias='resourceName'
    )
    id: Optional[DurableId] = None
    validations: Optional[List[Validation]] = None


class ContainerPlanTechnicalConfiguration(Resource):
    product: ResourceReference
    plan: ResourceReference


InnerError.update_forward_refs()
