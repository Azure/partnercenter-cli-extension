#!/bin/bash
# Create a Codespace secert in your fork to log in to Azure
# https://github.com/azure/login#configure-deployment-credentials

source /home/codespace/env/bin/activate

azdev setup --repo . --ext partnercenter --deps-from requirements.txt
