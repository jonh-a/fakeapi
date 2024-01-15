from faker import Faker
fake = Faker()

def get_fake_name(params):
    return fake.name()