# How to Manage Kubernetes qpps

## Creating a Marketplace Offer as a Kubernetes app

Currently, there isn't a 1:1 offer type in the Partner Center for a [Kubernetes app](https://learn.microsoft.com/en-us/azure/marketplace/azure-container-technical-assets-kubernetes?tabs=windows) offer type. The offer must be an Azure Container with the option to sell through Microsoft in the offer's setup. 

Here is how to define a Kubernetes app using the CLI:

1. Create your offer as an AzureContainer type
2. update the offer setup to sell through Microsoft

> NOTE: offer type cannot be changed once the offer is created. If the offer type is not AzureContainer, create a new offer

```bash
offer_id=myOfferId

az partnercenter marketplace offer create --id $offer_id --type AzureContainer --alias "My Offer Alias"
az partnercenter marketplace offer setup update --id $offer_id --sell-through-microsoft true

```

## Packaging the Kubernetes app

To achieve a seemless experience for our partners, we've integrated the official [container packaging tool](https://learn.microsoft.com/en-us/azure/marketplace/azure-container-technical-assets-kubernetes?tabs=linux#manually-run-the-packaging-tool) right into the CLI extension.

The packaging tool can be used directly, but the CLI is able to perform additional validation against the offer that the package is associated to, such as making sure that the offer is properly setup as a Kubernetes app.

### Dependencies

*The Partner Center CLI handles all the docker image management for you*. Instead of having to manually pull down the Docker image for the packaging tool, start a container instance, configure and set up the environment, the CLI streamlines this process.


> IMPORTANT: Because the CLI is using the packaging tool, it still requires that Docker be installed. This is already documented for the tool, [here](https://learn.microsoft.com/en-us/azure/marketplace/azure-container-technical-assets-kubernetes?tabs=linux#manually-run-the-packaging-tool).


### Verify and build the package

```bash
# get help for the commands
az partnercenter marketplace offer package -h

offer_id=myOfferId
manifest_file_path=/your/local/path/to/manifest.yaml

# verify and build your CNAB specific offer package
az partnercenter marketplace offer package verify --offer-id $offer_id --manifest-file $manifest_file_path
az partnercenter marketplace offer package build --offer-id $offer_id --manifest-file $manifest_file_path
```

#### Build command

The `...offer package build` command is equivalent to the `cpa buildbundle` command for the packaging tool, but easier. The CLI will handle the following:

1. The package commands on the CLI required an offer ID. This is because it performs additional checks on the offer.
2. All the docker container instance setup, including setting the ACR instance and calling `az acr login`. We will use the ACR information in the `manifest.yaml`

## Adding the package to the offer

> CLUSTER EXTENSION TYPE: The `--cluster-extension-type` is the billing identifier of your offer in AKS. More information can be found
> [here](https://learn.microsoft.com/en-us/azure/aks/cluster-extensions#usage-of-cluster-extensions) about the cluster extension


```bash

# get the current signed in account (either user or service principal)
acr_tenant_id=$(az account show --query tenantId --output tsv)
acr_subscription_id=$(az account show --query id --output tsv)
acr_resource_group_name=<the resource group that your acr instance is in>
acr_name=acr-instance-name

# cnab information
image_repository=com.contoso.cnab.bundle
image_tag=0.0.1
image_name="${image_repository}:${image_tag}"
image_digest=$(az acr repository show --name $acr_name --image $image_name --query digest --output tsv)

# offer & plan
offer_id=myOfferId
plan_id=myPlanId
cluster_extension_type=your.clusterExtension

# add the package to the technical configuration of the offer.
azm offer plan technical-configuration package add \
    --offer-id $offer_id \
    --plan-id $plan_id \
    --cluster-extension-type $cluster_extension_type \
    --subscription-id $acr_subscription_id \
    --tenant-id $acr_tenant_id \
    --registry $acr_name \
    --resource-group $acr_resource_group_name \
    --digest $image_digest \
    --repository $image_repository \
    --tag $image_tag
```