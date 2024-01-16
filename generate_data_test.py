from generate_data import *


def test_fake_password_custom_length():
    output = get_fake_password({"length": 30})
    assert isinstance(output, str)
    assert len(output) == 30


def test_random_number():
    output = get_random_number({"min": 300, "max": 400})
    assert isinstance(output, int)
    assert output >= 300 and output <= 400


def test_profile():
    output = get_profile()
    assert isinstance(output, dict)
    assert isinstance(output["name"], str)
    assert isinstance(output["email"], str)
    assert isinstance(output["username"], str)


def test_full_address():
    output = get_full_address()
    assert isinstance(output, str)


def test_street_address():
    output = get_street_address()
    assert isinstance(output, str)


def test_country():
    output = get_country()
    assert isinstance(output, str)


def test_city():
    output = get_city()
    assert isinstance(output, str)


def test_country_code():
    output = get_country_code()
    assert isinstance(output, str)


def test_color_name():
    output = get_color(params={format: "name"})
    assert isinstance(output, str)
    assert str.isalpha(output) is True


def test_color_hex():
    output = get_color(params={"format": "hex"})
    assert output.startswith("#")


def test_color_rgb_css():
    output = get_color(params={"format": "rgb_css"})
    assert output.startswith("rgb(")


def test_slug():
    output = get_slug()
    assert isinstance(output, str)
