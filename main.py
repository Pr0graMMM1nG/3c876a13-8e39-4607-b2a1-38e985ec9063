from table import Table


def main():
    table = Table()
    table.create_table()
    table.fill_database(100)

if __name__ == "__main__":
    main()
