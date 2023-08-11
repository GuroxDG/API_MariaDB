import re
import sys
from config.plugMariaDB import conn
from models.timeSeries import timeSeries
from utils.useful_functions import ReaderConfig
from utils.useful_functions import GetData
from sqlalchemy import text

def insertData(data = dict):
    print(data)

    from_symbol = data.from_symbol
    to_symbol   = data.to_symbol

    checkQuery = f"SELECT * FROM Time_Series_FX WHERE from_symbol = '{from_symbol}' AND to_symbol = '{to_symbol}' limit 1"

    output = conn.execute(text(checkQuery))
    resultado = output.fetchall()

    if len(resultado) > 0:
        return f'ya exite información respecto a from_symbol = {from_symbol} y to_symbol = {to_symbol}'

    config = ReaderConfig(sys.path[0]+'/config/credenciales.ini')
    api = config.get_api()

    data = GetData(api_=api)
    data_json = data.get_json(from_symbol,to_symbol)
    tipos_data = list(data_json.keys())
    print(tipos_data)
    data_insert = data_json[tipos_data[1]]
    data_insert = [data_insert[i]|{'date':i, 'from_symbol': from_symbol, 'to_symbol':to_symbol} for i in data_insert]

    data_insert_format = []
    for i in data_insert:
        new_dict = {re.sub(r'^\d+\.\s', '', k): v for k, v in i.items()}
        data_insert_format.append(new_dict)

    conn.execute(
        timeSeries.insert(), data_insert_format                   
    )

    respuesta = {
        'Consulta': checkQuery,
        'Registros': len(data_insert_format),
        'parametros' : data
    }
    return respuesta