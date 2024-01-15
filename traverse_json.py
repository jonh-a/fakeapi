from generate_data import ( 
    get_fake_password, 
    get_random_number,
    get_profle,
)


def traverse_json(obj):
    profile = get_profle()

    if isinstance(obj, dict):
        for key, value in obj.items():
            if isinstance(value, dict) and "fakeapi_item" in value:
                if "type" in value:
                    replaced_value = _get_replacement(value, profile)
                else:
                    return { "error": True, "reason": "Type not defined."}
                obj[key] = replaced_value
            else:
                traverse_json(value)
    elif isinstance(obj, list):
        for i in range(len(obj)):
            traverse_json(obj[i])
    return obj


def _get_replacement(params, profile):
    replacements = {
        "number": get_random_number(params),
        "name": profile["name"],
        "email": profile["mail"],
        "username": profile["username"],
        "password": get_fake_password(params)
    }
    return replacements.get(params["type"], "")