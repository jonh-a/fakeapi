from typing import Union
from generate_data import *


def traverse_json(obj: Union[list, dict]) -> Union[list, dict]:
    if isinstance(obj, dict):
        for key, value in obj.items():
            if isinstance(value, dict) and "fakeapi_item" in value:
                if "type" in value:
                    replaced_value = _get_replacement(value)
                else:
                    return {"error": True, "reason": "Type not defined."}
                obj[key] = replaced_value
            else:
                traverse_json(value)
    elif isinstance(obj, list):
        for i in range(len(obj)):
            traverse_json(obj[i])
    return obj


def _get_replacement(params: dict) -> Union[str, int]:
    replacements = {
        "number": get_random_number(params),
        "name": get_name(),
        "email": get_email(),
        "username": get_username(),
        "password": get_password(params),
        "street_address": get_street_address(),
        "city": get_city(),
        "country": get_country(),
        "country_code": get_country_code(),
        "full_address": get_full_address(),
        "color": get_color(params),
        "slug": get_slug(),
        "ipv4": get_ipv4(),
        "image_url": get_image_url(params),
        "domain_name": get_domain_name(params),
        "boolean": get_boolean(),
        "date": get_date(),
        "time": get_time(),
    }
    return replacements.get(params["type"], "")
