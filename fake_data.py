from enum import Enum

from faker import Faker

from models import Address, City, Street, User

fake =  Faker(locale="ro_RO")
# Faker.seed(0) uncomment if you want the data be the same every time

class Sex(Enum):
    MALE = 1
    FEMALE = 2
    UNKNOWN = 3

class Data:

    def city(self, name: str)-> City:
        return City.create(name=name)

    def street(self, name: str)-> Street:
        return Street.create(name=name)

    def address(self, home_number: int, street: Street, city: City)-> Address:
        return Address.create(
            home_number=home_number,
            street = street,
            city = city)

    def user(self, second_name:str, sex: Sex, min_age: int, max_age: int, address: Address)-> User:
        second_name = second_name
        match sex:
            case Sex.MALE:
                usr = User.create(
                    firstname=fake.first_name_male(),
                    secondname=second_name,
                    sex = Sex.MALE.name,
                    birthday = fake.date_of_birth(minimum_age=min_age, maximum_age=max_age),
                    address= address)
                return usr
            case Sex.FEMALE:
                usr = User.create(
                    firstname=fake.first_name_female(),
                    secondname=second_name,
                    sex = Sex.FEMALE.name,
                    birthday = fake.date_of_birth(minimum_age=min_age, maximum_age=max_age),
                address = address)
                return usr
            case _:
                usr = User.create(
                    firstname=fake.first_name_unisex(),
                    secondname=second_name,
                    sex = Sex.UNKNOWN.name,
                    birthday = fake.date_of_birth(minimum_age=min_age, maximum_age=max_age),
                    address = address)
                return usr

    def second_name(self)-> str:
        return fake.last_name()
