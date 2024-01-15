from generate_data import ( 
    get_fake_password, 
    get_random_number,
    get_profle,
    get_full_address,
    get_country,
    get_city,
    get_country_code,
    get_street_address,
)

def traverse_json(obj):
    profile = get_profle()
    data = recurse(obj, profile)
    return data


def recurse(obj, profile):
    if isinstance(obj, dict):
        for key, value in obj.items():
            if isinstance(value, dict) and "fakeapi_item" in value:
                if "type" in value:
                    replaced_value = _get_replacement(value, profile)
                else:
                    return { "error": True, "reason": "Type not defined."}
                obj[key] = replaced_value
            else:
                recurse(value, profile)
    elif isinstance(obj, list):
        for i in range(len(obj)):
            recurse(obj[i], profile)
    return obj


def _get_replacement(params, profile):
    replacements = {
        "number": get_random_number(params),
        "name": profile["name"],
        "email": profile["email"],
        "username": profile["username"],
        "password": get_fake_password(params),
        "street_address": get_street_address(),
        "city": get_city(),
        "country": get_country(),
        "country_code": get_country_code(),
        "full_address": get_full_address(),
        
    }
    return replacements.get(params["type"], "")