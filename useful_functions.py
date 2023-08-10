import configparser
import requests
import json

class ReaderConfig():
    def  __init__(self,path=str) -> None:
        self.config = configparser.ConfigParser()
        self.config.read(path)

    def get_credentials(self) -> dict:
        parameters = {}
        parameters['user']      = self.config['CREATE']['user']
        parameters['password']  = self.config['CREATE']['password']
        parameters['host']      = self.config['CREATE']['host']
        parameters['port']      = int(self.config['CREATE']['port'])
        parameters['database']  = self.config['CREATE']['database']
        return parameters
    
    def get_api(self) -> str:
        api = self.config['GET']['API_KEY']
        return api
    
class GetData():
    def __init__(self, api_=str) -> None:
        self.apikey = api_

    def get_json(self, from_symbol = str, to_symbol = str) -> dict:
        url =  f'https://www.alphavantage.co/query?function=FX_DAILY'
        url += f'&from_symbol={from_symbol}&to_symbol={to_symbol}'
        url += f'&outputsize=full'
        url += f'&apikey={self.apikey}'

        print(f'url request -> {url}')

        response = requests.get(url=url)

        return response.json()
    