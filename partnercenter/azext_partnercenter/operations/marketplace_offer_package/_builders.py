import os
from pathlib import Path
from knack.cli import CLIError
from azext_partnercenter.models.offer_package_type import AzureApplicationPackageType
from azext_partnercenter._client_factory import cf_offer_listing
from modm.marketplace.application_packaging_options import ApplicationPackageOptions
from modm.marketplace.application_package_info import ApplicationPackageInfo
from modm.marketplace.application_package import ApplicationPackage

# pylint: disable=too-few-public-methods


class DirectAzureAppPackageBuilder:
    def __init__(self, template_file):
        self.template_file = template_file

    def build(self):
        raise NotImplementedError(
            "The direct package type cannot be built. It is not yet supported."
        )


class AppInstallerAzureAppPackageBuilder:
    create_ui_definition_file_name = "createUiDefinition.json"

    def __init__(self, offer_listing, version, src_dir, out_dir):
        self.cwd = Path(os.getcwd())
        self.src_dir = self._resolve_path(src_dir)
        self.out_dir = self._resolve_path(out_dir)

        self.offer_listing = offer_listing
        self.version = version

        self.solution_template = self._get_template_file()
        self.create_ui_definition = self.src_dir.joinpath(
            self.create_ui_definition_file_name
        ).resolve()

    def build(self):
        """Builds an application package and produces an app.zip"""
        package = ApplicationPackage(
            ApplicationPackageInfo(
                self.solution_template,
                self.create_ui_definition,
                self.offer_listing.name,
                self.offer_listing.description,
            )
        )
        result = package.create(
            ApplicationPackageOptions(
                version=self.version, use_vmi_reference=False, out_dir=self.out_dir
            )
        )

        return result.serialize()

    def _resolve_path(self, path):
        if path is None:
            return self.cwd
        return self.cwd.joinpath(path).resolve()

    def _get_template_file(self):
        file_name_that_starts_with_main = self.src_dir.glob("main*")
        if file_name_that_starts_with_main is None:
            raise CLIError(
                "No main template file was found in the src directory. file must be named 'main.*' or 'mainTemplate.*'"
            )
        template_file = next(file_name_that_starts_with_main)
        return self.src_dir.joinpath(template_file).resolve()


def _create_package_builder(cmd, package_type, **kwargs):
    """Creates a package builder based on the package type"""
    offer_id = kwargs["offer_id"]
    src_dir = Path(kwargs["src_dir"] if kwargs["src_dir"] is not None else os.getcwd())
    out_dir = Path(kwargs["out_dir"] if kwargs["out_dir"] is not None else os.getcwd())
    version = kwargs["version"]

    if package_type == AzureApplicationPackageType.AppInstaller:
        offer_listing = cf_offer_listing(cmd.cli_ctx, kwargs).get(offer_id)
        return AppInstallerAzureAppPackageBuilder(
            offer_listing,
            version=version,
            src_dir=src_dir,
            out_dir=out_dir,
        )

    if package_type == AzureApplicationPackageType.Direct:
        return DirectAzureAppPackageBuilder(template_file=kwargs["template_file"])

    raise ValueError(f"Package type {package_type} is not supported by the CLI.")
