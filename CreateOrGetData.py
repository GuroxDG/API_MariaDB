import sys
from useful_functions import ReaderConfig
from useful_functions import GetData
from sqlalchemy import create_engine, Double, String, Table, MetaData, Date, Column, Select
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

meta = MetaData()

timeSeries = Table(
    'Time_Series_FX', meta, 
    Column('from_symbol',String(5), primary_key=True), 
    Column('to_symbol',  String(5), primary_key=True), 
    Column('date',  Date, primary_key=True), 
    Column('1. open', Double), 
    Column('2. high', Double), 
    Column('3. low',  Double), 
    Column('4. close',Double), 
)

meta.create_all(engine)
connection.commit()

from_symbol = sys.argv[1]
to_symbol = sys.argv[2]

validateQuery = f"SELECT * FROM Time_Series_FX WHERE from_symbol = '{from_symbol}' AND to_symbol = '{to_symbol}' limit 1"
output = connection.execute(text(validateQuery))
resultado = output.fetchall()

if len(resultado) > 0:
    print(f'ya exite información respecto a from_symbol = {from_symbol} y to_symbol = {to_symbol}')
    sys.exit(1)

api = config.get_api()
data = GetData(api_=api)

data_json = data.get_json(from_symbol,to_symbol)
tipos_data = list(data_json.keys())

data_insert = data_json[tipos_data[1]]
data_insert = [data_insert[i]|{'date':i, 'from_symbol': from_symbol, 'to_symbol':to_symbol} for i in data_insert]

connection.execute(timeSeries.insert(),
    data_insert                   
)
connection.commit()