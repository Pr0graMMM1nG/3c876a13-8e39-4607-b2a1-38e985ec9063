import toml
from peewee import SqliteDatabase


class IDataBase(type):
    _instances: dict = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class DataBase(metaclass=IDataBase):
    @property
    def sqlite(self):
        with open('config.toml', mode='r') as file:
            db_name = toml.load(file)['database']['name']
            return SqliteDatabase(db_name)
