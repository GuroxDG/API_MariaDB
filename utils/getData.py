import sys
import re

from sqlalchemy import text


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

data_insert_f = []
for i in data_insert:
    new_dict = {re.sub(r'^\d+\.\s', '', k): v for k, v in i.items()}
    data_insert.append(new_dict)

connection.execute(timeSeries.insert(),
    data_insert                   
)
connection.commit()