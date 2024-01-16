from faker import Faker
import random
import string


fake = Faker()


def _get_email_domain() -> str:
    return random.choice(["@gmail.com", "@yahoo.com", "@hotmail.com"])


def _get_username(name: str) -> str:
    name_split = name.split(" ")
    first = name_split[0]
    last = name_split[1]
    return random.choice(
        [
            f"{first}{last}".lower(),
            f"{first[0]}{last}".lower(),
            f"{first}{last[0]}".lower(),
        ]
    )


def _get_fake_name():
    return fake.name()


def get_profile() -> dict:
    name = _get_fake_name()
    username = _get_username(name)
    email = f"{username}{_get_email_domain()}"
    return {
        "name": name,
        "email": email,
        "username": username,
    }


def get_fake_password(params: dict) -> str:
    length = params.get("length", 12)
    return "".join(random.choices(string.ascii_letters, k=length))


def get_random_number(params: dict) -> int:
    min = params.get("min", 0)
    max = params.get("max", 100)
    return random.randint(min, max)


def get_city() -> str:
    return fake.city()


def get_country() -> str:
    return fake.country()


def get_country_code() -> str:
    return fake.country_code()


def get_street_address() -> str:
    return fake.street_address()


def get_full_address() -> str:
    return fake.address()
