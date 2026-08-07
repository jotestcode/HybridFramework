from faker import Faker

fake = Faker()

def random_email():
    return fake.unique.email()