from flask import Flask
import os
from flask_migrate import Migrate

from .models import db


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_TEST_DATABASE_URI')
    db.init_app(app)
    migrate = Migrate(app, db)

    return app