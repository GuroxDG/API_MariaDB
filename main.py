import configparser

from sqlalchemy import create_engine
from sqlalchemy import text

config = configparser.ConfigParser()
config.read('credenciales.ini')

user = config['LOAD']['user']
password = config['LOAD']['password']
host = config['LOAD']['host']
port = int(config['LOAD']['port'])
database = config['LOAD']['database']

connectQuery = f'mariadb+mariadbconnector://{user}:{password}@{host}:{port}/{database}'
print(f'string de conección -> {connectQuery}')

engine = create_engine(
    connectQuery, echo=True
)

with engine.connect() as connection:
    connection.execute(text('DROP TABLE IF EXISTS example'))
    connection.execute(text('CREATE TABLE example (id INTEGER, name VARCHAR(20))'))
    connection.commit()