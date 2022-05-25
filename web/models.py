import peewee


db = peewee.SqliteDatabase("data/buses.db")


class BaseModel(peewee.Model):
    class Meta:
        database = db


class User(BaseModel):
    id = peewee.IntegerField(column_name="id", primary_key=True)
    login = peewee.TextField(column_name="login")
    password = peewee.TextField(column_name="password")
    registration_date = peewee.IntegerField(column_name="registration_date")

    class Meta:
        table_name = "user"
