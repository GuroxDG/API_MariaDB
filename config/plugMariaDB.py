import sys
from utils.useful_functions import ReaderConfig
from utils.useful_functions import GetData
from sqlalchemy import create_engine, MetaData

config = ReaderConfig(sys.path[0]+'/config/credenciales.ini')
map_parameters = config.get_credentials()

user     = map_parameters['user']
password = map_parameters['password']
host     = map_parameters['host']
port     = map_parameters['port']
database = map_parameters['database']

connectQuery = f'mariadb+mariadbconnector://{user}:{password}@{host}:{port}/{database}'
print(f'conexión -> {connectQuery}')
engine = create_engine(
    connectQuery, echo=True
)

meta = MetaData()
conn = engine.connect()


