from sr.user.models import User
from sr.entry.models import Entry


def test_entry_list(init_database):
    user = User.create('test', 'test1')
    entry = Entry.create('title 1', 'content 1', user)

    entries = Entry.list()
    assert len(entries) == 1
    assert entries[0].user.id == 1
    assert user.entries[0].id == 1
