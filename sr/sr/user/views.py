from flask import Blueprint, request, render_template, redirect, url_for

from sr.user.forms import RegistrationForm
from sr.user.models import User


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
    return render_template('login.html')
