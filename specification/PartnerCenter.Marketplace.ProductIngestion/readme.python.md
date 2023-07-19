## Python

These settings apply only when `--python` is specified on the command line.
Please also specify `--python-sdks-folder=<path to the root directory of your azure-sdk-for-python clone>`.

``` yaml $(python)
openapi-type: data-plane
license-header: MICROSOFT_MIT_NO_VERSION
package-name: partnercenter-marketplace-productingestion
namespace: partnercenter.marketplace.productingestion
package-version: "1.0.0"
clear-output-folder: true
```

``` yaml $(python)
no-namespace-folders: true
```