from flask import Flask
from config import config_options, DevConfig
from flask_bootstrap import Bootstrap


bootstrap = Bootstrap()




def create_app(config_name):
    app = Flask(__name__)
    
    #app configurations
    app.config.from_object(config_options[config_name])
    
    #Initializing flask extensions
    bootstrap.init_app(app)
    
    
    
    # Setting app configurations
    app.config.from_object(DevConfig)
    
    #registering the main app Bluprints
    from .main import main as main_bluprint
    app.register_blueprint(main_bluprint)
    
    
    
    return app