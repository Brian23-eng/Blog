from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config_options, DevConfig
from flask_bootstrap import Bootstrap


bootstrap = Bootstrap()
db = SQLAlchemy()




def create_app(config_name):
    app = Flask(__name__)
    
    #app configurations
    app.config.from_object(config_options[config_name])
    
    #Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    
    
    
    # Setting app configurations
    app.config.from_object(DevConfig)
    
    #registering the main app Bluprints
    from .main import main as main_bluprint
    app.register_blueprint(main_bluprint)
    
    # registering the auth blueprint
    from .auth import auth as main_bluprint
    app.register_blueprint(main_bluprint, url_prefix = '/auth')
    
    
    
    return app