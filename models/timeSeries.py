from sqlalchemy import Column, Table
from sqlalchemy import Double, String, Table, Date, Column
from config.plugMariaDB import meta, engine

timeSeries = Table(
    'Time_Series_FX', meta, 
    Column('from_symbol',String(5), primary_key=True), 
    Column('to_symbol',  String(5), primary_key=True), 
    Column('date',  Date, primary_key=True), 
    Column('open', Double), 
    Column('high', Double), 
    Column('low',  Double), 
    Column('close',Double), 
)

meta.create_all(engine)