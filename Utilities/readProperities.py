import configparser
import os
from pathlib import Path

# path = Path(__file__)
# ROOT_DIR = path.parent.absolute()
# config_path = os.path.join(ROOT_DIR, "Configuration/config.ini")

config = configparser.RawConfigParser()
config.read(".\\Configuration\\config.ini")


class ReadConfig:

    @staticmethod
    def getApplicationURL():
        return config.get('Login', 'baseURL')

    @staticmethod
    def getUsername():
        return config.get('Login', 'username')

    @staticmethod
    def getPassword():
        return config.get('Login', 'password')
