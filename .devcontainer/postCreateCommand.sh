#!/bin/bash

python -m pip install --user ./partnercenter[test]

clientId=$(echo $AZURE_CREDENTIALS | jq -r .clientId)
clientSecret=$(echo $AZURE_CREDENTIALS | jq -r .clientSecret)
tenantId=$(echo $AZURE_CREDENTIALS | jq -r .tenantId)

az login \
    --service-principal \
    -u $clientId \
    -p $clientSecret \
    --tenant $tenantId \
    --allow-no-subscriptions

python -m pip install setuptools wheel

cd partnercenter
python setup.py sdist bdist_wheel
az extension add --upgrade --source dist/partnercenter-*-py3-none-any.whl --yes
