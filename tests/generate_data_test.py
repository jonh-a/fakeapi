import sys

print("PYTHONPATH:", sys.path)

from fakeapi.generate_data import *

print(get_password({"length": 30}))

def test_password_custom_length():
    output = get_password({"length": 30})
    assert isinstance(output, str)
    assert len(output) == 30


def test_password_invalid_length():
    output = get_password({"length": "invalid"})
    assert isinstance(output, str)
    assert len(output) == 12


def test_random_number():
    output = get_random_number({"min": 300, "max": 400})
    assert isinstance(output, int)
    assert output >= 300 and output <= 400


def test_random_number_invalid_params():
    output = get_random_number({"min": "invalid", "max": "invalid"})
    assert isinstance(output, int)
    assert output >= 0 and output <= 100


def test_username():
    assert isinstance(get_username(), str)


def test_email():
    assert isinstance(get_email(), str)


def test_name():
    assert isinstance(get_name(), str)


def test_full_address():
    assert isinstance(get_full_address(), str)


def test_street_address():
    assert isinstance(get_street_address(), str)


def test_country():
    assert isinstance(get_country(), str)


def test_city():
    assert isinstance(get_city(), str)


def test_country_code():
    assert isinstance(get_country_code(), str)


def test_color_name():
    output = get_color(params={format: "name"})
    assert isinstance(output, str)
    assert str.isalpha(output) is True


def test_color_hex():
    assert get_color(params={"format": "hex"}).startswith("#")


def test_color_rgb_css():
    assert get_color(params={"format": "rgb_css"}).startswith("rgb(")


def test_color_invalid():
    assert isinstance(get_color(params={"format": "invalid"}), str)


def test_slug():
    output = get_slug()
    assert isinstance(output, str)


def test_text():
    assert isinstance(get_text({"sentences": 1}), str)


def test_text_invalid_sentence_count():
    assert isinstance(get_text({"sentences": "invalid"}), str)
