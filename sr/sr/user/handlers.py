from flask import redirect, url_for

from sr.user.exceptions import UnauthenticatedException


def _handle_unauthenticated(e):
    return redirect(url_for('user.login'))


def register_handler(app):
    app.register_error_handler(UnauthenticatedException, _handle_unauthenticated)
