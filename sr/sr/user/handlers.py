from flask import redirect, url_for

from sr.user.exceptions import UnauthenticatedException, UnauthorizedException


def _handle_unauthenticated(e):
    return redirect(url_for('user.login'))


def _handle_unauthorized(e):
    return 'Permission Denied', 403


def register_handler(app):
    app.register_error_handler(UnauthenticatedException, _handle_unauthenticated)
    app.register_error_handler(UnauthorizedException, _handle_unauthorized)
