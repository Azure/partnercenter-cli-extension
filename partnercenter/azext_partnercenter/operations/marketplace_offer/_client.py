from unicodedata import name
from partnercenter.azext_partnercenter.vendored_sdks.v1.partnercenter.apis import ListingClient
from partnercenter.azext_partnercenter._client_factory import get_api_client
import json

class ListClient():

    def __init__(self, cli_ctx, *_):
        self._api_client = get_api_client(cli_ctx, *_)
        self._client = ListingClient(self._api_client)
    

    def list(self, product_id, instance_id):
        results = self._client.products_product_id_listings_get_by_instance_id_instance_i_dinstance_id_get(product_id, instance_id, self._api_client.configuration.access_token)
        return list(map(self._to_dict, results.value))

    def create(self, offer_id, offer_alias, resource_type):
        from partnercenter.azext_partnercenter.vendored_sdks.v1.partnercenter.apis import ProductClient
        from partnercenter.azext_partnercenter.vendored_sdks.v1.partnercenter.models import MicrosoftIngestionApiModelsProductsAzureProduct
        from partnercenter.azext_partnercenter.vendored_sdks.v1.partnercenter.models import MicrosoftIngestionApiModelsCommonTypeValuePair
        
        key_val = MicrosoftIngestionApiModelsCommonTypeValuePair(type='AzureOfferID', value=offer_alias)
        external_ids = [key_val]
        prod = MicrosoftIngestionApiModelsProductsAzureProduct(resource_type=resource_type, name=offer_id, id=offer_id, external_ids=external_ids,IsModularPublishing=True)
        
        product_client = ProductClient(self._api_client)
        result = product_client.products_post(self._api_client.configuration.access_token, microsoft_ingestion_api_models_products_azure_product=prod, _content_type="application/json")
        return result


    def _to_dict(self, item):
        return item.to_dict()