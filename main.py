
from useful_functions import ReaderConfig
from sqlalchemy import create_engine
from sqlalchemy import text


config = ReaderConfig('credenciales.ini')
map_parameters = config.get_credentials()

user     = map_parameters['user']
password = map_parameters['password']
host     = map_parameters['host']
port     = map_parameters['port']
database = map_parameters['database']

connectQuery = f'mariadb+mariadbconnector://{user}:{password}@{host}:{port}/{database}'
print(f'string de conección -> {connectQuery}')

engine = create_engine(
    connectQuery, echo=True
)

with engine.connect() as connection:
    connection.execute(text('DROP TABLE IF EXISTS example'))
    connection.execute(text('CREATE TABLE example (id INTEGER, name VARCHAR(20))'))
    connection.commit()