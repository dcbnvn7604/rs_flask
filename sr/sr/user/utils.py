from flask import session
from functools import wraps

from sr.user.exceptions import UnauthenticatedException


def authenticate_success(user):
    session['user_id'] = user.id


def login_required(func):
    @wraps(func)
    def _func(*args, **kwargs):
        if 'user_id' not in session:
            raise UnauthenticatedException
        return func(*args, **kwargs)

    return _func
