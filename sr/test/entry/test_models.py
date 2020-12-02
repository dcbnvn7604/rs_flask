from sr.user.models import User
from sr.entry.models import Entry


def test_entry_search(init_database):
    user = User.create('test', 'test1')
    Entry.create('title 1', 'content 1', user)
    Entry.create('title 2', 'content 2', user)

    entries = Entry.search()
    assert len(entries) == 2
    assert entries[0].user.id == 1
    assert entries[0].id == 1

    entries = Entry.search(q='2')
    assert len(entries) == 1
    assert entries[0].user.id == 1
    assert entries[0].id == 2
