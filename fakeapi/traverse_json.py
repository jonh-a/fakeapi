from typing import Union
import fakeapi.generate_data as gd


def traverse_json(obj: Union[list, dict]) -> Union[list, dict]:
    """
    recursively search through json to find and replace objects
    that contain the key/value pair "fakeapi_item": true
    """
    if isinstance(obj, dict):
        for key, value in obj.items():
            if isinstance(value, dict) and "fakeapi_item" in value:
                if "count" in value and isinstance(value["count"], int):
                    obj[key] = [_get_replacement(value) for _ in range(value["count"])]
                else:
                    obj[key] = _get_replacement(value)
            else:
                traverse_json(value)
    elif isinstance(obj, list):
        for i in range(len(obj)):
            traverse_json(obj[i])
    return obj


def _get_replacement(params: dict) -> Union[str, int]:
    type = params.get("type", "none")

    replacements = {
        "boolean": gd.get_boolean(),
        "city": gd.get_city(),
        "color": gd.get_color(params),
        "coordinates": gd.get_coordinates(params),
        "country": gd.get_country(),
        "country_code": gd.get_country_code(),
        "date": gd.get_date(),
        "domain_name": gd.get_domain_name(params),
        "email": gd.get_email(),
        "full_address": gd.get_full_address(),
        "image_url": gd.get_image_url(params),
        "ipv4": gd.get_ipv4(),
        "isbn": gd.get_isbn(params),
        "name": gd.get_name(),
        "number": gd.get_random_number(params),
        "password": gd.get_password(params),
        "slug": gd.get_slug(),
        "street_address": gd.get_street_address(),
        "text": gd.get_text(params),
        "time": gd.get_time(),
        "username": gd.get_username(),
        "none": "No type provided.",
        "": "Invalid type provided.",
    }
    return replacements.get(type, "Invalid type provided.")
