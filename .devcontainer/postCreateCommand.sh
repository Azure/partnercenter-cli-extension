#!/bin/bash

# python -m venv env
source env/bin/activate
# pip install azdev

azdev setup -r .
azdev extension repo add ../partnercenter-cli-extension/
azdev extension add partnercenter

clientId=$(echo $AZURE_CREDENTIALS | jq -r .clientId)
clientSecret=$(echo $AZURE_CREDENTIALS | jq -r .clientSecret)
tenantId=$(echo $AZURE_CREDENTIALS | jq -r .tenantId)

az login \
    --service-principal \
    -u $clientId \
    -p $clientSecret \
    --tenant $tenantId \
    --allow-no-subscriptions
