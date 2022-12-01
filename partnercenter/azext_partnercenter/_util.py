from urllib.parse import parse_qs, urlparse


def get_combined_paged_results(method_with_paged_response, collect_items_as_dict=False):
    """Get combined paginated results from the SDK client that's generated from the Parnter Center API"""
    items = []
    response = method_with_paged_response() if method_with_paged_response.__code__.co_argcount == 0 else method_with_paged_response('')

    if collect_items_as_dict:
        items.extend(map(object_to_dict, response.value))
    else:
        items.extend(response.value)

    if ("nextLink" in response):
        next_link = response['nextLink']

        while (next_link is not None):
            token = _get_skip_token(next_link)
            response = method_with_paged_response(token)
            if ("value" in response):
                if collect_items_as_dict:
                    items.extend(map(object_to_dict, response.value))
                else:
                    items.extend(response.value)
            next_link = None if "nextLink" not in response else response['nextLink']

    return items


def _get_skip_token(nextLink):
    """Gets the skip token from a nextLink url found in the response of the partner center API"""
    url_parts  = urlparse(nextLink)
    params = parse_qs(url_parts.query)
    return params['$skipToken'][0]


def object_to_dict(item):
    if (type(item) is dict or item is None):
        return item
    if hasattr(item, "to_dict") and callable(item.to_dict):
        return item.to_dict()
    return vars(item)
