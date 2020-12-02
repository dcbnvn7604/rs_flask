from urllib.parse import urlparse

from sr.entry.models import Entry


def test_list_login_required(client):
    response = client.get('/entry/list', follow_redirects=False)
    assert response.status_code == 302
    assert urlparse(response.location).path == '/user/login'


def test_list(client, logined_user):
    response = client.get('/entry/list', follow_redirects=False)
    assert response.status_code == 200


def test_create_login_required(client):
    response = client.get('/entry/create', follow_redirects=False)
    assert response.status_code == 302
    assert urlparse(response.location).path == '/user/login'


def test_create_has_permissions(client, logined_user):
    response = client.get('/entry/create', follow_redirects=False)
    assert response.status_code == 403


def test_create(client, logined_user_with_permissions):
    response = client.post('/entry/create', data={'title': 'title 1', 'content': 'content 1'}, follow_redirects=False)
    assert response.status_code == 302
    assert urlparse(response.location).path == '/entry/list'


def test_update_login_required(client):
    response = client.get('/entry/1/update', follow_redirects=False)
    assert response.status_code == 302
    assert urlparse(response.location).path == '/user/login'


def test_update_has_permissions(client, logined_user):
    response = client.get('/entry/1/update', follow_redirects=False)
    assert response.status_code == 403


def test_update_not_found(client, logined_user_with_permissions):
    response = client.post('/entry/1/update', data={'title': 'title 1', 'content': 'content 1'}, follow_redirects=False)
    assert response.status_code == 404


def test_update(client, logined_user_with_permissions):
    Entry.create('title', 'content', logined_user_with_permissions)

    response = client.post('/entry/1/update', data={'title': 'title 1', 'content': 'content 1'}, follow_redirects=False)
    assert response.status_code == 302
    assert urlparse(response.location).path == '/entry/list'


def test_delete_login_required(client):
    response = client.post('/entry/1/delete', follow_redirects=False)
    assert response.status_code == 302
    assert urlparse(response.location).path == '/user/login'


def test_delete_has_permissions(client, logined_user):
    response = client.post('/entry/1/delete', follow_redirects=False)
    assert response.status_code == 403


def test_delete_not_found(client, logined_user_with_permissions):
    response = client.post('/entry/1/delete', follow_redirects=False)
    assert response.status_code == 404


def test_delete(client, logined_user_with_permissions):
    Entry.create('title', 'content', logined_user_with_permissions)

    response = client.post('/entry/1/delete', follow_redirects=False)
    assert response.status_code == 302
    assert urlparse(response.location).path == '/entry/list'
