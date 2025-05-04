from models import Address, City, User, Street

class Apartment:
    def __init__(self) -> None:
        self.city: City = City()
        self.street: Street = Street()
        self.address: Address = Address()
        self.adult: list[User] = []
        self.child: list[User] = []


class Builder:
    def __init__(self) -> None:
        self.apartament = Apartment()

    def set_city(self, city: City):
        self.apartament.city = city

    def set_street(self, street: Street):
        self.apartament.street = street

    def set_address(self, home_number: int):
        self.apartament.address = Address.create(home_number=home_number, city=self.apartament.city, street= self.apartament.street)

    def set_adult(self, father: User, mother: User):
        self.apartament.adult = [father, mother]

    def set_child(self, child: list[User]):
        self.apartament.child.extend(child)

    @property
    def apartment(self)-> Apartment:
        return self.apartament

    @property
    def address(self)-> Address:
        return self.apartament.address
