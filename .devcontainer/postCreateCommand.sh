#!/bin/bash

python -m venv env
source env/bin/activate
pip install azdev

azdev setup -r .
azdev extension repo add ../partnercenter-cli-extension/
azdev extension add partnercenter
