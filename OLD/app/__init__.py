from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from .routes import routes  # Importe o Blueprint 'routes'

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)

    app.register_blueprint(routes)  # Registre o Blueprint

    return app
