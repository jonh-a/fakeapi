from typing import Union
from generate_data import *


def traverse_json(obj: Union[list, dict]) -> Union[list, dict]:
    """
    recursively search through json to find and replace objects
    that contain the key/value pair "fakeapi_item": true
    """
    if isinstance(obj, dict):
        for key, value in obj.items():
            if isinstance(value, dict) and "fakeapi_item" in value:
                replaced_value = _get_replacement(value)
                obj[key] = replaced_value
            else:
                traverse_json(value)
    elif isinstance(obj, list):
        for i in range(len(obj)):
            traverse_json(obj[i])
    return obj


def _get_replacement(params: dict) -> Union[str, int]:
    type = params.get("type", "none")

    replacements = {
        "boolean": get_boolean(),
        "city": get_city(),
        "color": get_color(params),
        "country": get_country(),
        "country_code": get_country_code(),
        "date": get_date(),
        "domain_name": get_domain_name(params),
        "email": get_email(),
        "full_address": get_full_address(),
        "image_url": get_image_url(params),
        "ipv4": get_ipv4(),
        "name": get_name(),
        "number": get_random_number(params),
        "password": get_password(params),
        "slug": get_slug(),
        "street_address": get_street_address(),
        "text": get_text(params),
        "time": get_time(),
        "username": get_username(),
        "none": "No type provided.",
        "": "Invalid type provided.",
    }
    return replacements.get(type, "Invalid type provided.")
