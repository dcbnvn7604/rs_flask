from flask import Blueprint, request, render_template, redirect, url_for, current_app

from sr.user.forms import RegistrationForm, LoginForm
from sr.user.models import User
from sr.user.exceptions import UnauthenticatedException
from sr.user.utils import authenticate_success, deauthenticate


blueprint = Blueprint('user', __name__, url_prefix='/user', template_folder='templates')


@blueprint.route('/register', methods=('GET', 'POST'))
def register():
    form = RegistrationForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            User.create(form.data['username'], form.data['password'])
            return redirect(url_for('user.login'))

    return render_template('register.html', form=form)


@blueprint.route('/login', methods=('GET', 'POST'))
def login():
    form = LoginForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            try:
                user = User.authenticate(form.data['username'], form.data['password'])
                authenticate_success(user)
                return redirect(current_app.config['LOGIN_REDIRECT_URL'])
            except UnauthenticatedException:
                pass

    return render_template('login.html')


@blueprint.route('/logout', methods=('GET', 'POST'))
def logout():
    deauthenticate()
    return redirect(url_for('user.login'))
