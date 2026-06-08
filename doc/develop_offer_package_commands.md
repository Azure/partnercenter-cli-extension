# Developing offer package commands locally

This guide covers local setup for the `az partnercenter marketplace offer package`
commands, especially `verify` and `build`.

The package commands wrap the Microsoft commercial marketplace container
packaging tool. The extension starts the packaging container for you, mounts the
directory containing the package manifest as `/data`, mounts your Azure CLI
profile from `~/.azure`, and runs the packaging tool inside that container.

## Prerequisites

- Python 3.10 or newer
- Azure CLI
- Docker with the local Docker daemon running
- Access to a Partner Center account and Azure Container Registry for end-to-end
  package verification and build testing

## Set up the extension for local development

From the repository root:

```bash
python -m venv env
source env/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip install azdev azure-cli azure-cli-testsdk

azdev setup --repo . --ext partnercenter --deps-from requirements.txt
az extension list --query "[?name=='partnercenter']"
```

The development container runs the same `azdev setup --repo . --ext
partnercenter --deps-from requirements.txt` command from
`.devcontainer/postCreateCommand.sh`.

## Authenticate

The package commands reuse the Azure CLI profile that is mounted into the
packaging container, so sign in before running `verify` or `build`:

```bash
az login
az account show
```

For service-principal workflows, authenticate with the Azure CLI command that
matches your environment before running the package command.

## Prepare an offer for package testing

`verify` and `build` only support Azure container offers configured to sell
through Microsoft. The local command path checks this before invoking the
packaging tool.

```bash
offer_id=myOfferId

az partnercenter marketplace offer create \
  --id $offer_id \
  --type AzureContainer \
  --alias "My Offer Alias"

az partnercenter marketplace offer setup update \
  --id $offer_id \
  --sell-through-microsoft true
```

## Run verify and build locally

The manifest file path must point to the package manifest YAML file. The
extension mounts the manifest's parent directory into the packaging container, so
keep any files referenced by the manifest under that directory.

```bash
offer_id=myOfferId
manifest_file_path=/absolute/path/to/manifest.yaml

az partnercenter marketplace offer package verify \
  --offer-id $offer_id \
  --manifest-file $manifest_file_path

az partnercenter marketplace offer package build \
  --offer-id $offer_id \
  --manifest-file $manifest_file_path
```

During `build`, the extension reads `registryServer` from the manifest and uses
the value before the first `.` as the Azure Container Registry name for
`az acr login`.

## Troubleshooting local runs

- If Docker is unavailable, start Docker and retry. The command uses Docker to
  run `mcr.microsoft.com/container-package-app:latest`.
- If authentication fails inside the packaging container, refresh your Azure CLI
  login with `az login` and verify that `~/.azure` exists on the host.
- If the manifest cannot find referenced files, move those files under the
  manifest directory or update the manifest paths. Only the manifest directory is
  mounted into the packaging container as `/data`.
- If `build` cannot log in to ACR, confirm that the manifest's `registryServer`
  value starts with the target registry name and that the signed-in Azure
  account has access to that registry.
- If the command reports that the offer is not set up for CNAB bundles, verify
  that the offer is an `AzureContainer` offer and that `sell-through-microsoft`
  is enabled on the offer setup.

## Useful source files

- `partnercenter/azext_partnercenter/operations/marketplace_offer_package/commands.py`
- `partnercenter/azext_partnercenter/operations/marketplace_offer_package/params.py`
- `partnercenter/azext_partnercenter/operations/marketplace_offer_package/custom.py`
- `partnercenter/azext_partnercenter/operations/marketplace_offer_package/_cnab_util.py`
