import pytest

from sr.db import db
from sr.user.models import User, Permission
from sr.user.exceptions import UnauthenticatedException


def test_authenticate(init_database):
    user = User.create('test', 'test1')

    with pytest.raises(UnauthenticatedException):
        User.authenticate('test', 'test')
    
    User.authenticate('test', 'test1')


def test_has_permissions(init_database):
    user = User.create('test', 'test1')
    user_id = user.id
    permissions = Permission.query.filter(Permission.name.in_(['entry.create', 'entry.update'])).all()
    user.permissions = permissions
    db.session.commit()

    user = User.by_id(user_id)
    assert user.has_permissions(['entry.create'])
    assert not user.has_permissions(['entry.create', 'entry.delete'])
