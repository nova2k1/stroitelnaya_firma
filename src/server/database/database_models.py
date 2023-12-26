from peewee import *
import peewee
import settings

db = peewee.SqliteDatabase(database=f'{settings.DATABASE_PATH}/{settings.DATABASE_NAME}')

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    position = CharField(default='')
    login = CharField(default='')
    password = CharField(default='')
    power_level = IntegerField(default=0)

class Projects(BaseModel):
    name = CharField(default='')
    description = TextField(default='')
    start_date = TextField(default='')
    end_date = TextField(default='')


class Clients(BaseModel):
    name = CharField(default='')
    contact = CharField(default='')

class Employees(BaseModel):
    name = CharField(default='')
    position = CharField(default='')
    contact = CharField(default='')

class Materials(BaseModel):
    name = CharField(default='')
    quantity = IntegerField(default=0)

class Tasks(BaseModel):
    project_id = ForeignKeyField(Projects, default=0)
    employee_id = ForeignKeyField(Employees, default=0)
    description = TextField(default='')
    status = CharField(default='')


db.create_tables([User, Projects, Clients, Employees, Materials, Tasks])
