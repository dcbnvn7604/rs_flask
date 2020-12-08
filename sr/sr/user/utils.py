from flask import session
from functools import wraps

from sr.user.exceptions import UnauthenticatedException, UnauthorizedException
from sr.user.models import User


def authenticate_success(user):
    session['user_id'] = user.id

def deauthenticate():
    session.clear()


def login_required(func):
    @wraps(func)
    def _func(*args, **kwargs):
        if 'user_id' not in session:
            raise UnauthenticatedException
        return func(*args, **kwargs)

    return _func


def has_permissions(permissions):
    def wrapper(func):
        @wraps(func)
        @login_required
        def _func(*args, **kwargs):
            user = User.by_id(session['user_id'])
            if not user.has_permissions(permissions):
                raise UnauthorizedException
            return func(*args, **kwargs)
        return _func
    return wrapper
