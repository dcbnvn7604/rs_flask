from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import InputRequired, Length

from sr.entry.models import Entry


class EntryForm(FlaskForm):
    title = StringField('title', validators=[InputRequired(), Length(max=Entry.TITLE_LENGTH)])
    content = TextAreaField('content', validators=[InputRequired(), Length(max=Entry.CONTENT_LENGTH)])
