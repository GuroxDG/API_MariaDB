
from useful_functions import ReaderConfig
from useful_functions import GetData
from sqlalchemy import create_engine, Double, String, Table, MetaData, Date, Column
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

connection = engine.connect()
connection.execute(text('DROP TABLE IF EXISTS Time_Series_FX'))

meta = MetaData()

timeSeries = Table(
    'Time_Series_FX', meta, 
    Column('from_symbol',String(5), primary_key=True), 
    Column('to_symbol',  String(5), primary_key=True), 
    Column('date',  Date), 
    Column('1_open', Double), 
    Column('2_high', Double), 
    Column('3_low',  Double), 
    Column('4_close',Double), 
)

meta.create_all(engine)
connection.commit()

api = config.get_api()
data = GetData(api_=api)
data_json = data.get_json('EUR','USD')
tipos_data = list(data_json.keys())
print(len(data_json[tipos_data[1]]))