from generate_data import *


def test_fake_password_custom_length():
    output = get_password({"length": 30})
    assert isinstance(output, str)
    assert len(output) == 30


def test_random_number():
    output = get_random_number({"min": 300, "max": 400})
    assert isinstance(output, int)
    assert output >= 300 and output <= 400


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


def test_slug() -> str:
    output = get_slug()
    assert isinstance(output, str)
