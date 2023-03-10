#!/usr/bin/env python

# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os
import re
from codecs import open
from setuptools import setup, find_packages

try:
    from azure_bdist_wheel import cmdclass
except ImportError:
    from distutils import log as logger

    logger.warn("Wheel is not available, disabling bdist_wheel hook")

NAME = "partnercenter"

# Version extraction inspired from 'requests'
with open(os.path.join("azext_partnercenter", "version.py"), "r") as fd:
    VERSION = re.search(r'^VERSION\s*=\s*[\'"]([^\'"]*)[\'"]', fd.read(), re.MULTILINE)[1]

if not VERSION:
    raise RuntimeError("Cannot find version information")

# The full list of classifiers is available at
# https://pypi.python.org/pypi?%3Aaction=list_classifiers
CLASSIFIERS = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "Intended Audience :: System Administrators",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "License :: OSI Approved :: MIT License",
]

# TODO: Add any additional SDK dependencies here
DEPENDENCIES = ["docker", "azure-storage-blob", "requests", "pydantic"]

EXTRA_DEPENDENCIES = {"test": ["azure-cli-core", "azure-cli-testsdk", "pytest"]}

with open("README.rst", "r", encoding="utf-8") as f:
    README = f.read()
with open("HISTORY.rst", "r", encoding="utf-8") as f:
    HISTORY = f.read()

setup(
    name=NAME,
    version=VERSION,
    description="Microsoft Azure CLI Extension for Partner Center",
    author="Microsoft Corporation",
    author_email="azpycli@microsoft.com",
    url="https://github.com/Azure/partnercenter-cli-extension/tree/main/partnercenter",
    long_description=README + "\n\n" + HISTORY,
    license="MIT",
    classifiers=CLASSIFIERS,
    packages=find_packages(),
    install_requires=DEPENDENCIES,
    extra_requires=EXTRA_DEPENDENCIES,
    package_data={"azext_partnercenter": ["azext_metadata.json"]},
)
