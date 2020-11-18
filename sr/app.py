from flask import Flask
import os
from flask_migrate import Migrate

from sr.db import db
from sr.user.views import blueprint


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_TEST_DATABASE_URI')
    app.config['LOGIN_REDIRECT_URL'] = '/'
    app.register_blueprint(blueprint)
    db.init_app(app)
    migrate = Migrate(app, db)

    return app