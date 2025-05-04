from table import Table
from models import City, Street


def main():
    table = Table()
    city = City.create(name="Chisinau")
    street = Street.create(name=" Codrilor 8/5")
    for number in range(1, 120):
        table.create_apartment(apartament_number=number, city=city, street=street)


if __name__ == "__main__":
    main()
