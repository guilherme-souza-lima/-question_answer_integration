from dotenv import load_dotenv
import os

load_dotenv()


class ConfigBase:
    PATH_FILE = os.getenv('PATH_FILE')
    IA_API_KEY = os.getenv('IA_API_KEY')
    IA_MODEL = os.getenv('IA_MODEL')
    NUMBER_QUESTIONS = os.getenv('NUMBER_QUESTIONS')
    NUMBER_QUESTIONS_RESPONSE = os.getenv('NUMBER_QUESTIONS_RESPONSE')


class ProdConfig(ConfigBase):
    ENV = 'PROD'


class LocalConfig(ConfigBase):
    ENV = 'LOCAL'


def get_configuration():
    env = os.getenv('ENV', 'LOCAL')

    if env == 'PROD':
        return ProdConfig()
    else:
        return LocalConfig()


config = get_configuration()