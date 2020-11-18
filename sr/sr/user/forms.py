from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length, EqualTo, ValidationError

from sr.user.models import User


class RegistrationForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(max=User.USERNAME_LENGTH)])
    password = PasswordField('password', validators=[InputRequired(), Length(max=User.PASSWORD_LENGTH), EqualTo('repassword')])
    repassword = PasswordField('repassword')

    def validate_username(self, field):
        if User.exists(field.data):
            raise ValidationError('username exists')


class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(max=User.USERNAME_LENGTH)])
    password = PasswordField('password', validators=[InputRequired(), Length(max=User.PASSWORD_LENGTH)])
