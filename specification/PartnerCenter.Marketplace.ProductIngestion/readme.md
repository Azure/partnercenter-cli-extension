# Partner Center Marketplace Ingestion API

> see https://aka.ms/autorest

This is the AutoRest configuration file for Partner Center Marketplace (Ingestion API).

**stable v1**
Current documentation on the Partner Center Ingestion API is located at: https://learn.microsoft.com/en-us/partner-center/marketplace/azure-app-apis

[Arsen Vladimirskiy](https://arsenvlad.medium.com/) also has a blog post on API usage, here](https://arsenvlad.medium.com/using-partner-center-ingestion-api-for-managing-azure-application-offers-in-azure-marketplace-b47b290dd947)


**preview (latest)**
The unified Product Ingestion API, delivered via MS Graph API, is the latest API version.

Documentation: https://learn.microsoft.com/en-us/partner-center/marketplace/product-ingestion-api


## Getting Started

To build the SDKs for My API, simply install AutoRest via `npm` (`npm install -g autorest`) and then run:

> `autorest readme.md`

To see additional help and options, run:

> `autorest --help`

For other options on installation see [Installing AutoRest](https://aka.ms/autorest/install) on the AutoRest github page.

---

## Configuration

### Basic Information

These are the global settings for the Marketplace.

``` yaml
title: ProductIngestionClient
tag: package-preview-2022-03-01
```

### Tag: 2020-09-10

This version of the v1 API uses the earliest known date we know of that the specification was published. This version of the specification
is made available here for diff purposes, and we don't generate from it. Use stable tag `2022-10-27` instead.


### Tag: 2022-10-27

This version of the v1 API was captured from modifications [here](https://github.com/microsoft/az-partner-center-cli/blob/main/Partner_Ingestion_SwaggerDocument.json) (credit to @alexandrakoller and @dciborow)

These settings apply only when `--tag=package-2022-10-27` is specified on the command line.

```yaml $(tag) == 'package-2022-10-27'
input-file:
  - PartnerCenter.Marketplace.ProductIngestion/stable/2022-10-27/productingestion.json
```

### Tag: package-preview-2022-03-01

These settings apply only when `--tag=package-preview-2022-03-01` is specified on the command line.

``` yaml $(tag) == 'package-preview-2022-03-01'
output-folder: $(python-sdks-folder)/product_ingestion/2022-03-01-preview
input-file:
  - preview/2022-03-01-preview/product.json
```

---

# Code Generation

## Swagger to SDK

This section describes what SDK should be generated by the automatic system.
This is not used by Autorest itself.

``` yaml $(swagger-to-sdk)
swagger-to-sdk:
  - repo: azure-sdk-for-python-track2
  - repo: azure-sdk-for-go
  - repo: azure-sdk-for-js
  - repo: azure-sdk-for-java
  - repo: azure-powershell
```

## Python

See configuration in [readme.python.md](./readme.python.md)

## Suppression

``` yaml

```