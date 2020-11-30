import pytest
from werkzeug.datastructures import MultiDict

from test.utils import generate_data
from sr.entry.forms import EntryForm


entry_data = {
    'title': 'a' * 30,
    'content': 'b' * 100
}


@pytest.mark.parametrize(
    "field,data,error",
    [
        ('title', generate_data(entry_data, exclude=['title']), 'This field is required.'),
        ('title', generate_data(entry_data, update={'title': ''}), 'This field is required.'),
        ('title', generate_data(entry_data, update={'title': 'a' * 31}), 'Field cannot be longer than 30 characters.'),
        ('content', generate_data(entry_data, exclude=['content']), 'This field is required.'),
        ('content', generate_data(entry_data, update={'content': ''}), 'This field is required.'),
        ('content', generate_data(entry_data, update={'content': 'a' * 101}), 'Field cannot be longer than 100 characters.'),
    ]
)
def test_entry_form_invalid(field, data, error, app):
    with app.test_request_context('/'):
        form = EntryForm(MultiDict(data))
        assert form.validate() == False, "Field {} Error {}" % (field, error)
        assert error in form.errors[field]


@pytest.mark.parametrize(
    "data",
    [
        entry_data,
        generate_data(entry_data, update={'title': 'a' * 29}),
        generate_data(entry_data, update={'content': 'b' * 99}),
    ]
)
def test_entry_form(data, app):
    with app.test_request_context('/'):
        form = EntryForm(MultiDict(data))
        assert form.validate() == True
