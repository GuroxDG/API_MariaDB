import sqlalchemy
import configparser
from sqlalchemy.ext.declarative import declarative_base

config = configparser.ConfigParser()
config.read('credenciales.ini')

user=config['LOAD']['user']
password=config['LOAD']['password']
host=config['LOAD']['host']
port=int(config['LOAD']['port'])
database=config['LOAD']['database']

connectQuery = f'mariadb+mariadbconnector://{user}:{password}@{host}:{port}/{database}'
print(connectQuery)

engine = sqlalchemy.create_engine(
    connectQuery
)