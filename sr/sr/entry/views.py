from flask import Blueprint, render_template, request, session, redirect, url_for

from sr.entry.models import Entry
from sr.entry.forms import EntryForm
from sr.user.utils import login_required
from sr.user.models import User


blueprint = Blueprint('entry', __name__, url_prefix='/entry', template_folder='templates')


@blueprint.route('/list', methods=['GET'])
@login_required
def list():
    entries = Entry.list()
    return render_template('list.html')


@blueprint.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    form = EntryForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.by_id(session['user_id'])
            entry = Entry.create(form.data['title'], form.data['content'], user)
            return redirect(url_for('entry.list'))

    return render_template('form.html')
