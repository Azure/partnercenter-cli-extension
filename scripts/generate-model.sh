#! /bin/bash

# Call this while in the ./api directory
cd ./specification
python_sdks_folder=../partnercenter/azext_partnercenter/vendored_sdks
autorest PartnerCenter.Marketplace.ProductIngestion/readme.md --python --python-sdks-folder=$python_sdks_folder --tag=package-preview-2022-03-01
