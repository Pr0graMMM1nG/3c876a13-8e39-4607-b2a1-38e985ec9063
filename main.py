from table import Table
from models import City, Street


def main():
    table = Table()
    city = City.create(name="Chisinau")
    street = Street.create(name="Alba Iulia")
    for number in range(1, 10):
        table.create_apartment(apartament_number=number, city=city, street=street)


if __name__ == "__main__":
    main()
