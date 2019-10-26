import os
class Config:
    
    '''
    Describes the general configurations
    
    '''
    QUOTES_API_BASE_URL = os.environ.get(' QUOTES_API_BASE_URL')
    SECRET__KEY = os.environ.get('SECRET__KEY ')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://brian:brayo13@localhost/blog'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    
    
    
    @staticmethod
    def init_app(app):
        pass
    
    
    
class ProdConfig(Config):
    
    '''
    Production configuration child class
    
    Args:
        Config: The parent configuration class with general configuration settings
    '''
    
class DevConfig(Config):
    
    '''
    Development configuration child class
    
    Args:
        Config: The parent configuration class with general configuration settings
        
    '''
    DEBUG = True
    

config_options = {
    'development':DevConfig,
    'production': ProdConfig
}
    
    