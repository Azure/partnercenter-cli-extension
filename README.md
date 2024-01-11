# Partner Center Azure CLI Extension (Preview)

The Partner Center CLI Extension adds Partner Center commands to the Azure CLI 2.0.

## Quickstart

1. Install the Azure CLI. You must have at least v2.0.69, which you can verify with az --version command.
2. Add the Partner Center Azure CLI Extension
3. Run the az login command

If the CLI can open your default browser, it will do so and load a sign-in page. Otherwise, you need to open a browser page and follow the instructions on the command line to enter an authorization code after navigating to https://aka.ms/devicelogin in your browser. For more information, see the Azure CLI login page.

> See the [How to associate an Azure AD application with your Partner Center account](https://learn.microsoft.com/en-us/azure/marketplace/azure-app-apis#how-to-associate-an-azure-ad-application-with-your-partner-center-account)

### 2. Adding the Partner Center CLI extension

The extension is the officially listed Azure CLI extension for Partner Center.

```bash
az extension add --name partnercenter
```

> IMPORTANT: Due to being still preview, the latest version of the extension that's been published to the official Azure CLI extensions index may be different than
the latest version we've released. To add the latest, unpublished version that's been released:

1. Go to the [releases](https://github.com/Azure/partnercenter-cli-extension/releases)
2. Choose the version you'd like to add to your Azure CLI instance
3. Right-click on the *.whl file and copy the URL
4. Finally, install the extension using the wheel URL

```bash
az extension add --source https://github.com/Azure/partnercenter-cli-extension/releases/download/v0.2.2-alpha/partnercenter-0.2.2-py3-none-any.whl
```

## Usage

```bash
$ az partnercenter [subgroup(s)] [command] {parameters}
```

Adding the Extension, exposes the `marketplace` group. Within the marketplace group, here are some of the primary subgroups available:

- `offer` - includes subgroups `package`, `setup`, `listing`, `listing media`, `plan`
- `offer plan` - includes subgroups `technical-configuration`
- `offer plan technical-configuration` - includes subgroup `package`

For usage and help content for any command, pass in the -h parameter, for example:

```
az partnercenter marketplace offer -h

Group
    az partnercenter marketplace offer
Subgroups:
    listing
    package
    plan
    setup

Commands:
    create
    delete
    list
    show
```

- You can view the various commands and its usage here - [docs.microsoft.com - Azure CLI Extension for Partner Center Reference](https://learn.microsoft.com/en-us/cli/azure/service-page/partner%20center%20(azure%20marketplace)?view=azure-cli-latest)

## Contributing

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.opensource.microsoft.com.

When you submit a pull request, a CLA bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.


## Developer Setup

```
python -m venv env
source env/bin/activate
pip install -r requirements.txt
pip install azdev

azdev setup
```
## Trademarks

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft
trademarks or logos is subject to and must follow
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship.
Any use of third-party trademarks or logos are subject to those third-party's policies.


## Getting Started

https://github.com/Azure/azure-cli/blob/master/doc/extensions/authoring.md
