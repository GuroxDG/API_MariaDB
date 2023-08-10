import configparser

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