#!/bin/bash

# required tools:
#   - git CLI
#   - github CLI (brew install gh)
#
#   to login using the GH CLI:
#       gh auth login -h github.com -p ssh --web
#       , then follow prompts

version_number=$1
version_tag=$2

function install_github_cli() {
    gh_version=$(gh version)
    if [[ -z "$gh_version" ]]; then
        echo "GitHub CLI not installed. Installing..."
        #brew install gh
    fi

    gh_version=$(gh version)
    echo "GitHub CLI version: $gh_version"


}

function tag_version() {
    echo "tagging: $version_tag"
    git tag -a $version_tag -m "$version_tag"

    echo "pushing tag: $version_tag"
    git push origin $version_tag
}

function release_extension() {
    azdev extension build partnercenter

    whl_file=partnercenter-$version_number-py3-none-any.whl
    title="Partner Center Azure CLI Extension $version_tag"

    gh release create $version_tag ./dist/$whl_file --generate-notes --draft --prerelease

    echo "updating Azure CLI index"
    whl_uri=https://github.com/Azure/partnercenter-cli-extension/releases/download/$version_tag/$whl_file

    azdev extension update-index $whl_uri
}

