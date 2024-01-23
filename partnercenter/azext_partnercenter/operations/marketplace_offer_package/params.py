# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long

from enum import Enum
from azure.cli.core.commands.parameters import get_enum_type
from azext_partnercenter.models import AzureApplicationPackageType


class ArgGroup(str, Enum):
    """Command groups for package"""

    azure_app = "Azure application"
    app_installer = "App Installer"
    kubernetes_app = "Kubernetes application"


argument_help = {
    "manifest_file": """The path to the package manifest YAML file that describes the package, the CNAB bundle, and dependent artifacts.""",
    "package_type": """The Azure application package type. Defaults to Direct. If the value is AppInstaller, the package is bundled to use the App Installer. The direct packaging places templates directly into the app.zip""",
    "src_dir": """The directory path to the source application templates. Defaults to the current directory if not set. This is required if packaging an Azure managed application.""",
    "out_dir": """The directory path the package output will be placed.""",
    "app_installer_version": """The version of the marketplace AppInstaller to use. Defaults to the latest version. See https://github.com/microsoft/commercial-marketplace-offer-deploy for more information.""",
}


def load_arguments(commands_loader, _):
    with commands_loader.argument_context(
        "partnercenter marketplace offer package"
    ) as c:
        c.argument("offer_id", options_list=["--offer-id", "--id"], help="The Offer ID.")
        c.argument("manifest_file", options_list=["--manifest-file"], arg_group="Kubernetes application", help=argument_help["manifest_file"])
        c.argument("src_dir", options_list=["--src-dir", "--src"], arg_group=ArgGroup.azure_app.value, help=argument_help["src_dir"])
        c.argument("out_dir", options_list=["--out-dir", "--out"], arg_group=ArgGroup.azure_app.value, help=argument_help["out_dir"])
        c.argument("package_type", options_list=["--package-type", "-t"], arg_type=get_enum_type(AzureApplicationPackageType),
                   arg_group=ArgGroup.azure_app.value, help=argument_help["package_type"])
        c.argument("app_installer_version", options_list=["--app-installer-version", "-v"], arg_type=get_enum_type(AzureApplicationPackageType),
                   arg_group=ArgGroup.azure_app.value, help=argument_help["app_installer_version"])
