from tornado.autoreload import add_reload_hook

from fake_data import Data, Sex
from models import Address, City, Street, User, db
from service import Apartment, Builder
from random import Random
from typing import Tuple, List


class Table:
    def __init__(self) -> None:
        self._fake = Data()
        self._create_table()

    def _create_table(self) -> None:
        db.connect()
        db.create_tables([User, City, Street, Address])

    def _create_adult(self, address: Address)-> Tuple[User, User]:
        father = self._fake.user(sex= Sex.MALE, min_age=25, max_age=30, address = address)
        mother = self._fake.user(sex=Sex.FEMALE, min_age=23, max_age=28, address = address)
        return father, mother

    def _create_child(self,address: Address)->List[User]:
        child_list = []
        random_child_count: int = Random().randint(a=0, b=5)
        sex = [Sex.MALE, Sex.FEMALE]
        random_child_sex: Sex = Random().choice(sex)
        if random_child_count == 0:
            return []
        for _ in range(random_child_count):
            child = self._fake.user(sex=random_child_sex, min_age=1, max_age=12, address = address)
            child_list.append(child)
        return child_list


    def create_apartment(self, apartament_number: int, city: City, street: Street)-> None:
        builder = Builder()
        builder.set_city(city=city)
        builder.set_street(street=street)
        builder.set_address(home_number=apartament_number)
        adult = self._create_adult(address=builder.address)
        builder.set_adult(father=adult[0], mother=adult[1])
        children = self._create_child(address=builder.address)
        builder.set_child(children)



