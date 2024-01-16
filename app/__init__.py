from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'  # Use the path to your database
    db.init_app(app)

    # Import and register the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .api.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    with app.app_context():
        from . import models
        db.create_all()

    return app