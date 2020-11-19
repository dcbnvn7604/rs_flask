import pytest
import flask_migrate
import concurrent.futures as cf
import os

from app import create_app
from sr.db import db


migrations_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'sr', 'migrations')


@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_TEST_DATABASE_URI')
    app.config['WTF_CSRF_SECRET_KEY'] = 'WTF_CSRF_SECRET_KEY'
    app.config['SECRET_KEY'] = 'SECRET_KEY'
    app.config['WTF_CSRF_ENABLED'] = False
    return app


@pytest.fixture
def init_database(app):
    with app.app_context():
        db.create_all()
        yield
        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app):
    with app.test_client() as c:
        yield c
