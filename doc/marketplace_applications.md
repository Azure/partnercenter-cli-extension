# Managing Marketplace Applications

## Creating a Marketplace Application Offer


Here is how to define a Azure Application using the CLI:

1. Create your offer as an AzureApplication type
2. update the offer setup to sell through Microsoft

> NOTE: offer type cannot be changed once the offer is created. If the offer type is not AzureApplication, create a new offer

```bash
offer_id=myOfferId
offer_summary="A sample offer summary"
offer_short_description="A sample offer description"
offer_description="<p> An HTML Formatted Offer Description</p>"

az partnercenter marketplace offer create \
    --offer-id $offer_id \
    --type AzureApplication \
    --alias "My App Alias"
az partnercenter marketplace offer setup update \
    --offer-id $offer_id \
    --sell-through-microsoft true
az partnercenter marketplace offer listing update \
    --offer-id $offer_id \
    --summary '{summary}' \
    --short-description '{short_description}' \
    --description '{description}'

# create a plan for the offer
plan_id=myPlanId
plan_summary="A sample plan description"
plan_description="<p> An HTML Formatted Application Plan Description</p>"

az partnercenter marketplace offer plan create \
    --offer-id $offer_id \
    --plan-id $plan_id \
    --name 'Test Plan'
az partnercenter marketplace offer plan listing update \
    --offer-id $offer_id \
    --plan-id $plan_id \
    --description '$plan_description' \
    --summary '$plan_summary'
```

> NOTE: you many also use an HTML file for the offer or plan description `--description @Description.html`
