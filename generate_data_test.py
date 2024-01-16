from generate_data import (
    get_fake_password,
    get_random_number,
    get_profile,
    get_full_address,
    get_country,
    get_city,
    get_country_code,
    get_street_address,
)


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
