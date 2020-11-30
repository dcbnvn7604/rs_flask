import pytest
from werkzeug.datastructures import MultiDict

from sr.user.forms import RegistrationForm, LoginForm
from sr.user.models import User
from test.utils import generate_data


registraition_data = {
    'username': 'username1',
    'password': 'password1',
    'repassword': 'password1'
}


@pytest.mark.parametrize(
    "field,data,error",
    [
        ('username', generate_data(registraition_data, exclude=['username']), 'This field is required.'),
        ('username', generate_data(registraition_data, update={'username': ''}), 'This field is required.'),
        ('username', generate_data(registraition_data, update={'username': 'a' * 129}), 'Field cannot be longer than 128 characters.'),
        ('password', generate_data(registraition_data, exclude=['password']), 'This field is required.'),
        ('password', generate_data(registraition_data, update={'password': ''}), 'This field is required.'),
        ('password', generate_data(registraition_data, update={'password': 'a' * 90}), 'Field cannot be longer than 89 characters.'),
        ('password', generate_data(registraition_data, update={'repassword': 'password2'}), 'Field must be equal to repassword.'),
    ]
)
def test_registration_form_invalid(field, data, error, app, init_database):
    with app.test_request_context('/'):
        form = RegistrationForm(MultiDict(data))
        assert form.validate() == False, "Field {} Error {}" % (field, error)
        assert error in form.errors[field]


def test_registration_form_username_exists(init_database, app):
    user = User.create('username1', 'username1')
    with app.test_request_context('/'):
        form = RegistrationForm(MultiDict(registraition_data))
        assert form.validate() == False
        assert 'username exists' in form.errors['username']


@pytest.mark.parametrize(
    "data",
    [
        registraition_data,
        generate_data(registraition_data, update={'username': 'a' * 128, 'password': 'b' * 89, 'repassword': 'b' * 89})
    ]
)
def test_registration_form(data, app, init_database):
    with app.test_request_context('/'):
        form = RegistrationForm(MultiDict(data))
        assert form.validate() == True


login_data = {
    'username': 'username1',
    'password': 'password1'
}


@pytest.mark.parametrize(
    "field,data,error",
    [
        ('username', generate_data(login_data, exclude=['username']), 'This field is required.'),
        ('username', generate_data(login_data, update={'username': ''}), 'This field is required.'),
        ('username', generate_data(login_data, update={'username': 'a' * 129}), 'Field cannot be longer than 128 characters.'),
        ('password', generate_data(login_data, exclude=['password']), 'This field is required.'),
        ('password', generate_data(login_data, update={'password': ''}), 'This field is required.'),
        ('password', generate_data(login_data, update={'password': 'a' * 90}), 'Field cannot be longer than 89 characters.'),
    ]
)
def test_login_form_invalid(field, data, error, app):
    with app.test_request_context('/'):
        form = LoginForm(MultiDict(data))
        assert form.validate() == False, "Field {} Error {}" % (field, error)
        assert error in form.errors[field]
