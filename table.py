from fake_data import Data, Sex
from models import Address, City, Street, User, db


class Table:
    def __init__(self) -> None:
        self._fake = Data()

    def create_table(self) -> None:
        db.connect()
        db.create_tables([User, City, Street, Address])

    def fill_database(self, count_row: int) -> None:
        city = self._fake.city(name="Chisinau")
        city.save()
        street = self._fake.street(name="Alba Iulia")
        street.save()
        for count in range(0, count_row, 1):
            address = self._fake.address(home_number=1,  city=city, street=street)
            address.save()
            user = self._fake.user(sex = Sex.MALE, address=address)
            user.save()
