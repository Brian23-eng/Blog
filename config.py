import os

class Config:
    
    
    QUOTES_BASE_URL =os.environ.get('QUOTES_BASE_URL')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    
class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}