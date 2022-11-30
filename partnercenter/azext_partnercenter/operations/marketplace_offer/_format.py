


from collections import OrderedDict
import re


def list_output_format(result):
    return _output_format(result, (lambda item: OrderedDict([
        ('ID', _get_value_as_str(item, 'id')),
        ('NAME', _get_value_as_str(item, 'name')),
        ('TYPE', _get_offer_type_display_name(item))
    ])))

def _output_format(result, format_group):
    if 'value' in result and isinstance(result['value'], list):
        result = result['value']
    obj_list = result if isinstance(result, list) else [result]
    return [format_group(item) for item in obj_list]


def _get_value_as_str(item, *args):
    """Get a nested value from a dict.
    :param dict item: The dict object
    """
    try:
        for arg in args:
            item = item[arg]
        return str(item) if item else ' '
    except (KeyError, TypeError, IndexError):
        return ' '


def _get_offer_type_display_name(item):
    try:
       value = item = item['type']
       regex = re.compile('(?!^)(?=[A-Z])', re.MULTILINE)
       return re.sub(regex, " ", value)
    except (KeyError, TypeError, IndexError):
        return ' '