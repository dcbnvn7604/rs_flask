import pytest

from sr.models import User, UnauthorizedException


def test_user(init_database):
    user = User.create('test', 'test1')

    # with pytest.raises(UnauthorizedException):
    #     User.authenticate('test', 'test')
    
    User.authenticate('test', 'test1')
