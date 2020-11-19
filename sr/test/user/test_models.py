import pytest

from sr.user.models import User
from sr.user.exceptions import UnauthenticatedException


def test_user(init_database):
    user = User.create('test', 'test1')

    with pytest.raises(UnauthenticatedException):
        User.authenticate('test', 'test')
    
    User.authenticate('test', 'test1')
