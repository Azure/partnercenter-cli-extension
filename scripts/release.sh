#!/bin/bash

# required tools:
#   - git CLI
#   - github CLI (brew install gh)
#
#   to login using the GH CLI:
#       gh auth login -h github.com -p ssh --web
#       , then follow prompts
#
#   example call:
#   ./scripts/release.sh 0.2.2 v0.2.2-alpha

version_number=$1
version_tag=$2

function confirm_prompt() {
    text=$1
    read -p "$text (Y/n)" -n 1 -r
    echo    # (optional) move to a new line
    if [[ ! $REPLY =~ ^[Yy]$ ]]
    then
        echo "aborting."
        exit 1
    fi
}

function print_info() {
    echo ""
    echo "Release Information:"
    echo "-------------------------------"
    echo "Number: $version_number"
    echo "Tag:    $version_tag"
    echo ""

    confirm_prompt "Proceed with release?"
}

function install_github_cli() {
    gh_version=$(gh version)
    if [[ -z "$gh_version" ]]; then
        echo "GitHub CLI not installed. Installing..."
        brew install gh
    fi

    gh_version=$(gh version)
    echo "GitHub CLI installed [$gh_version]"
    echo ""
}

function git_tag_version() {
    confirm_prompt "Proceed with Git tag?"

    echo "tagging: $version_tag"
    # git tag -a $version_tag -m "$version_tag"

    # echo "pushing tag: $version_tag"
    # git push origin $version_tag
}

function release_extension() {
    echo "building extension."
    azdev extension build partnercenter


    whl_file=partnercenter-$version_number-py3-none-any.whl
    title="Partner Center Azure CLI Extension $version_tag"

    echo "creating GitHub release."
    gh release create $version_tag ./dist/$whl_file --generate-notes --draft --prerelease

    echo "updating Azure CLI index"
    whl_uri=https://github.com/Azure/partnercenter-cli-extension/releases/download/$version_tag/$whl_file

    azdev extension update-index $whl_uri
}

print_info
install_github_cli
git_tag_version

# install_github_cli
# tag_version
# release_extension