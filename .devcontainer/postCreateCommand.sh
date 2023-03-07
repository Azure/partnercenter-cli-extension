#!/bin/bash

source /workspaces/partnercenter-cli-extension/env/bin/activate

azdev setup -r . -e partnercenter

clientId=$(echo $AZURE_CREDENTIALS | jq -r .clientId)
clientSecret=$(echo $AZURE_CREDENTIALS | jq -r .clientSecret)
tenantId=$(echo $AZURE_CREDENTIALS | jq -r .tenantId)

az login \
    --service-principal \
    -u $clientId \
    -p $clientSecret \
    --tenant $tenantId \
    --allow-no-subscriptions
