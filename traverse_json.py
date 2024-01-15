from generate_data import (
    get_fake_name, 
    get_fake_password, 
    get_random_number,
)


def traverse_json(obj):
    if isinstance(obj, dict):
        for key, value in obj.items():
            if isinstance(value, dict) and "fakeapi_item" in value:
                if "type" in value:
                    replaced_value = _get_replacement(value)
                else:
                    return { "error": True, "reason": "Type not defined."}
                obj[key] = replaced_value
            else:
                traverse_json(value)
    elif isinstance(obj, list):
        for i in range(len(obj)):
            traverse_json(obj[i])
    return obj


def _get_replacement(params):
    replacements = {
        "number": get_random_number(params),
        "name": get_fake_name(params),
        "username": "jonsmith1",
        "password": get_fake_password(params)
    }
    return replacements.get(params["type"], "")