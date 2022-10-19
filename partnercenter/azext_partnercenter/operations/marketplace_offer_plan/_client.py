from partnercenter.azext_partnercenter._client_factory import get_api_client
from partnercenter.azext_partnercenter._util import get_combined_paged_results
from partnercenter.azext_partnercenter.vendored_sdks.v1.partnercenter.apis import (
    BranchesClient, ProductClient, VariantClient)
from partnercenter.azext_partnercenter.vendored_sdks.v1.partnercenter.models import ProductsProductIDVariantsGetRequest, MicrosoftIngestionApiModelsVariantsAzureSkuVariant, MicrosoftIngestionApiModelsVariantsAzureSkuVariantAllOf


class PlanClient():

    def __init__(self, cli_ctx, *_):
        self._api_client = get_api_client(cli_ctx, *_)
        self._product_client = ProductClient(self._api_client)
        self._branch_client = BranchesClient(self._api_client)
        self._variant_client = VariantClient(self._api_client)

    def list(self):
        items = get_combined_paged_results(self._product_client.products_get, self._api_client.configuration.access_token)
        return items

    def create(self, product_id, external_id, friendly_name):
        resource_type = "AzureSkuVariant"
        prod_var_req = ProductsProductIDVariantsGetRequest(resource_type=resource_type, friendly_name=friendly_name, external_id=external_id)
        result = self._variant_client.products_product_id_variants_post(product_id=product_id, authorization=self._api_client.configuration.access_token, products_product_id_variants_get_request=prod_var_req)
        return result.to_dict()

    def _to_dict(self, item):  
        return item.to_dict()