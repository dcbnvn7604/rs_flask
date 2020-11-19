from flask import session

from sr.user.exceptions import UnauthenticatedException


def authenticate_success(user):
    session['user_id'] = user.id


def login_required(func):
    def _func(*args, **kwargs):
        if 'user_id' not in session:
            raise UnauthenticatedException
        return func(*args, **kwargs)

    return _func
