from faker import Faker
import random
import string


fake = Faker()


def get_text(params) -> str:
    sentences: int = params.get("sentences", 1)
    if isinstance(sentences, int) and sentences >= 1:
        return fake.paragraph(nb_sentences=sentences, variable_nb_sentences=False)
    return fake.paragraph(nb_sentences=1, variable_nb_sentences=False)


def get_random_number(params: dict) -> int:
    min: int = params.get("min", 0)
    max: int = params.get("max", 100)
    if not isinstance(min, int) or not isinstance(max, int):
        return random.randint(0, 100)
    return random.randint(min, max)


def get_password(params: dict) -> str:
    length: int = params.get("length", 12)
    if not isinstance(length, int):
        length = 12
    return "".join(random.choices(string.ascii_letters, k=length))


def get_boolean() -> bool:
    return random.choice([True, False])


def get_name():
    return fake.name()


def get_username() -> str:
    return fake.user_name()


def get_email() -> str:
    return fake.email()


def get_color(params: dict) -> str:
    format = params.get("format", "name")
    if format == "hex":
        return fake.safe_hex_color()
    elif format == "rgb":
        return fake.rgb_color()
    elif format == "rgb_css":
        return fake.rgb_css_color()
    else:
        return fake.safe_color_name()


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


def get_slug() -> str:
    return fake.slug()


def get_ipv4() -> str:
    return fake.ipv4_public()


def get_image_url(params: dict) -> str:
    w = params.get("width", 640)
    h = params.get("height", 480)
    if not isinstance(w, int) or not isinstance(h, int) or w <= 0 or h <= 0:
        w = 640
        h = 480
    return fake.image_url(width=w, height=h)


def get_domain_name(params: dict) -> str:
    subdomains: int = params.get("subdomains", 0)
    if isinstance(subdomains, int) is False or subdomains == 0:
        return fake.domain_name()
    return fake.domain_name(subdomains)


def get_date() -> str:
    return fake.date()


def get_time() -> str:
    return fake.time()
