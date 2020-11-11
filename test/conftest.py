import pytest
import flask_migrate
import concurrent.futures as cf
import os

from sr import create_app, db


migrations_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'sr', 'migrations')


@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_TEST_DATABASE_URI')
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
    return app.test_client()
