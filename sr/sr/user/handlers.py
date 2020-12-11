from flask import redirect, url_for

from sr.user.exceptions import UnauthenticatedException, UnauthorizedException, APIUnauthenticatedException, APIUnauthorizedException


def _handle_unauthenticated(e):
    return redirect(url_for('user.login'))


def _handle_apiunauthenticated(e):
    return '', 401


def _handle_unauthorized(e):
    return 'Permission Denied', 403


def _handle_apiunauthorized(e):
    return '', 403


def register_handler(app):
    app.register_error_handler(UnauthenticatedException, _handle_unauthenticated)
    app.register_error_handler(APIUnauthenticatedException, _handle_apiunauthenticated)
    app.register_error_handler(UnauthorizedException, _handle_unauthorized)
    app.register_error_handler(APIUnauthorizedException, _handle_apiunauthorized)
