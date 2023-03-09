#!/bin/bash
# Create a Codespace secert in your fork to log in to Azure
# https://github.com/azure/login#configure-deployment-credentials

if [ -z "$AZURE_CREDENTIALS" ]; then
    echo "Skipping login. Credentials not found."
else

    clientId=$(echo $AZURE_CREDENTIALS | jq -r .clientId)
    clientSecret=$(echo $AZURE_CREDENTIALS | jq -r .clientSecret)
    tenantId=$(echo $AZURE_CREDENTIALS | jq -r .tenantId)

    az login \
        --service-principal \
        -u $clientId \
        -p $clientSecret \
        --tenant $tenantId \
        --allow-no-subscriptions
fi
