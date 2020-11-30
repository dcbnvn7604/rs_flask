from urllib.parse import urlparse


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


def test_create(client, logined_user):
    response = client.post('/entry/create', data={'title': 'title 1', 'content': 'content 1'}, follow_redirects=False)
    assert response.status_code == 302
    assert urlparse(response.location).path == '/entry/list'
