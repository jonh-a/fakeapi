from generate_data import get_fake_name

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


def _get_replacement(replacement_object):
    replacements = {
        "number": 4,
        "name": get_fake_name(replacement_object),
        "username": "jonsmith1",
        "password": "asdf1234"
    }
    return replacements.get(replacement_object["type"], "")