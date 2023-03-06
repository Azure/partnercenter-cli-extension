# Managing Marketplace Applications

## Creating a Marketplace Application Offer


Here is how to define a Azure Application using the CLI:

1. Create your offer as an AzureApplication type
2. update the offer setup to sell through Microsoft

> NOTE: offer type cannot be changed once the offer is created. If the offer type is not AzureApplication, create a new offer

```bash
offer_id=myOfferId
plan_id=myPlanId

az partnercenter marketplace offer create \
    --offer-id $offer_id \
    --type AzureApplication \
    --alias "My App Alias"
az partnercenter marketplace offer setup update \
    --offer-id $offer_id \
    --sell-through-microsoft true

# create a plan for the offer
az partnercenter marketplace offer plan create \
    --offer-id $offer_id \
    --plan-id $plan_id \
    --name 'Test Plan'
```
