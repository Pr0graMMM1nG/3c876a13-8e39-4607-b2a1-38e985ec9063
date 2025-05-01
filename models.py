from peewee import CharField, DateField, ForeignKeyField, IntegerField, Model

from database import DataBase

db = DataBase().sqlite

class BaseModel(Model):
    class Meta:
        database = db

class City(BaseModel):
    name = CharField()

class Street(BaseModel):
    name = CharField()

class Address(BaseModel):
    home_number = IntegerField()
    city = ForeignKeyField(City, backref="cities")
    street = ForeignKeyField(Street, backref="streets")

class User(BaseModel):
    firstname = CharField()
    secondname = CharField()
    sex = CharField()
    birthday = DateField()
    address = ForeignKeyField(Address, backref="users")
