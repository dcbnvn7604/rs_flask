from flask import Blueprint, render_template

from sr.entry.models import Entry
from sr.user.utils import login_required


blueprint = Blueprint('entry', __name__, url_prefix='/entry', template_folder='templates')


@blueprint.route('/list', methods=['GET'])
@login_required
def list():
    entries = Entry.list()
    return render_template('list.html')
