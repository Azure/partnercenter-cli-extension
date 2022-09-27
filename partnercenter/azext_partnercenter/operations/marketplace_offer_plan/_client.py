from partnercenter.azext_partnercenter.vendored_sdks.v1.partnercenter.apis import ProductClient
from partnercenter.azext_partnercenter._client_factory import get_api_client
import json

class PlanClient():

    def __init__(self, cli_ctx, *_):
        self._api_client = get_api_client(cli_ctx, *_)
        self._client = ProductClient(self._api_client)
    

    def list(self):
        results = self._client.products_get(self._api_client.configuration.access_token)
        return list(map(self._to_dict, results.value))


    def _to_dict(self, item):
        return item.to_dict()