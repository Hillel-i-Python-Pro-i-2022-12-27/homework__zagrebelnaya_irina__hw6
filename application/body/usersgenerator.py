from typing import NamedTuple
from random import randint
from faker import Faker

fake = Faker()


class User(NamedTuple):
    name: str
    email: str


def generate_entity() -> User:
    user_name = fake.first_name()
    return User(name=user_name, email=f"{user_name.lower()}{randint(100, 200)}@mail.com")


def generate_users(number):
    for i in range(number):
        yield generate_entity()


def print_result_of_generation_users(number=100) -> dict:
    list_users = {}
    for user in generate_users(number):
        list_users[user.name] = user.email
    return list_users
