from faker import Faker
import random
import string 


fake = Faker()


def get_fake_name(params):
    return fake.name()


def get_fake_password(params):
    length = params.get("length", 12)
    return ''.join(random.choices(string.ascii_letters, k=length))


def get_random_number(params):
    min = params.get("min", 0)
    max = params.get("max", 100)
    return random.randint(min, max)