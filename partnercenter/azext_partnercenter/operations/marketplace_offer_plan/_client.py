from partnercenter.azext_partnercenter.vendored_sdks.v1.partnercenter.apis import (ProductClient, BranchesClient)
from partnercenter.azext_partnercenter._client_factory import get_api_client
from partnercenter.azext_partnercenter._util import get_combined_paged_results
from partnercenter.azext_partnercenter.vendored_sdks.v1.partnercenter.apis import (
    BranchesClient, ProductClient)


class PlanClient():

    def __init__(self, cli_ctx, *_):
        self._api_client = get_api_client(cli_ctx, *_)
        self._product_client = ProductClient(self._api_client)
        self._branch_client = BranchesClient(self._api_client)

    def list(self):
        results = self._product_client.products_get(self._api_client.configuration.access_token)
        return list(map(self._to_dict, results.value))


    def _to_dict(self, item):
        return item.to_dict()