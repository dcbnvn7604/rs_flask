from flask import Flask
import os
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

from sr.db import db
from sr.user.views import blueprint as user_blueprint
from sr.user.resources import blueprint as user_api_blueprint
from sr.entry.views import blueprint as entry_blueprint
from sr.user.handlers import register_handler


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_TEST_DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['LOGIN_REDIRECT_URL'] = '/entry/list'

    JWTManager(app)

    app.register_blueprint(user_blueprint)
    app.register_blueprint(user_api_blueprint)
    app.register_blueprint(entry_blueprint)
    db.init_app(app)
    register_handler(app)

    migrate = Migrate(app, db)

    return app