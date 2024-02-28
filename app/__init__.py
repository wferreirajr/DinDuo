from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .main import main as main_blueprint
from .users import users as users_blueprint
from .api.auth import auth as auth_blueprint

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///DinDuo.sqlite'  # Use the path to your database
    db.init_app(app)

    # Import and register the blueprint
    app.register_blueprint(main_blueprint)
    app.register_blueprint(users_blueprint, url_prefix='/users')

    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    with app.app_context():
        from . import models
        db.create_all()

    return app