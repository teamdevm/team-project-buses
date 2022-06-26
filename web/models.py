import peewee
from os import environ


db_filename = environ.get("BUSES_DB_FILE", "./data/buses.db")
db = peewee.SqliteDatabase(db_filename)


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
        

class Bus(BaseModel):
    bus_id = peewee.TextField(column_name="bus_id", primary_key=True)
    number = peewee.IntegerField(column_name="number")
    
    class Meta:
        table_name = "bus"
        
        
class Stop(BaseModel):
    stop_id = peewee.IntegerField(column_name="stop_id", primary_key=True)
    name = peewee.TextField(column_name="name")
    
    class Meta:
        table_name = "stop"
        
        
class BusStop(BaseModel):
    bus_stop_id = peewee.IntegerField(column_name="bus_stop_id", primary_key=True)
    bus_id = peewee.ForeignKeyField(Bus, backref="stops")
    stop_id = peewee.ForeignKeyField(Stop, backref="buses")
    
    class Meta:
        table_name = "bus_stop"
        
     
class ArrivingTime(BaseModel):
    bus_stop_id = peewee.ForeignKeyField(BusStop)
    is_weekday = peewee.BooleanField(column_name="is_weekday")
    arriving_time = peewee.IntegerField(column_name="arriving_time")
    
    class Meta:
        primary_key = peewee.CompositeKey("bus_stop_id", "is_weekday", "arriving_time")
        table_name = "arriving_time"
        
        
class Route(BaseModel):
    route_id = peewee.IntegerField(column_name="route_id", primary_key=True)
    departure_stop_id = peewee.ForeignKeyField(Stop)
    arrival_stop_id = peewee.ForeignKeyField(Stop)
    
    class Meta:
        table_name = "route"
        
        
class UserRoute(BaseModel):
    user_id = peewee.ForeignKeyField(User)
    route_id = peewee.ForeignKeyField(Route)
    name = peewee.TextField(column_name="name")
    
    class Meta:
        primary_key = peewee.CompositeKey("user_id", "route_id")
        table_name = "user_route" 
