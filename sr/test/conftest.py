import pytest
import flask_migrate
import concurrent.futures as cf
import os
from flask_jwt_extended import create_access_token

from app import create_app
from sr.db import db
from sr.user.models import User, Permission


@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_TEST_DATABASE_URI')
    app.config['WTF_CSRF_SECRET_KEY'] = 'WTF_CSRF_SECRET_KEY'
    app.config['SECRET_KEY'] = 'SECRET_KEY'
    app.config['WTF_CSRF_ENABLED'] = False
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = False
    return app


@pytest.fixture
def init_database(app):
    with app.app_context():
        flask_migrate.upgrade(revision='head')
        yield
        db.session.remove()
        flask_migrate.downgrade(revision='base')


@pytest.fixture
def client(app):
    with app.test_client() as c:
        yield c


@pytest.fixture
def user(init_database):
    user = User.create('test', 'test1')
    return user


@pytest.fixture
def logined_user(client, user):
    with client.session_transaction() as sess:
        sess['user_id'] = user.id

    return user


@pytest.fixture
def logined_user_with_permissions(logined_user):
    logined_user.permissions = Permission.query.all()
    db.session.commit()
    return logined_user


@pytest.fixture
def token(user):
    return create_access_token(user.username)


@pytest.fixture
def token_with_permisssions(user):
    user.permissions = Permission.query.all()
    db.session.commit()
    return create_access_token(user.username)
