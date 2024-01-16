from traverse_json import traverse_json


def test_flat_json():
    input = {
        "name": {"fakeapi_item": True, "type": "name"},
        "number": {"fakeapi_item": True, "type": "number", "min": 30, "max": 300},
    }
    output = traverse_json(input)
    assert isinstance(output["name"], str)
    assert isinstance(output["number"], int)


def test_nested_json():
    input = {
        "data": {
            "name": {"fakeapi_item": True, "type": "name"},
            "username": {"fakeapi_item": True, "type": "username"},
            "password": {"fakeapi_item": True, "type": "password"},
            "nested": {
                "status": "OK",
                "metadata": {
                    "test": True,
                    "mutable": {
                        "number": {
                            "fakeapi_item": True,
                            "type": "number",
                            "min": 10,
                            "max": 60,
                        },
                        "email": {"fakeapi_item": True, "type": "email"},
                    },
                },
            },
        }
    }
    output = traverse_json(input)
    assert isinstance(output["data"], dict)
    assert isinstance(output["data"]["name"], str)
    assert isinstance(output["data"]["username"], str)
    assert isinstance(output["data"]["password"], str)
    assert isinstance(output["data"]["nested"]["metadata"]["mutable"]["number"], int)
    assert isinstance(output["data"]["nested"]["metadata"]["mutable"]["email"], str)


def test_array_json():
    input = [
        {
            "name": {"fakeapi_item": True, "type": "name"},
            "number": {"fakeapi_item": True, "type": "number", "min": 30, "max": 300},
        },
        {
            "name": {"fakeapi_item": True, "type": "name"},
            "number": {"fakeapi_item": True, "type": "number", "min": 30, "max": 300},
        },
    ]
    output = traverse_json(input)
    assert isinstance(output[0]["name"], str)
    assert isinstance(output[0]["number"], int)
    assert isinstance(output[1]["name"], str)
    assert isinstance(output[1]["number"], int)
