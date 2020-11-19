from urllib.parse import urlparse

from sr.user.models import User


def test_list_login_required(client):
    response = client.get('/entry/list', follow_redirects=False)
    assert response.status_code == 302
    assert urlparse(response.location).path == '/user/login'


def test_list(client, init_database):
    user = User.create('test', 'test1')

    with client.session_transaction() as sess:
        sess['user_id'] = user.id

    response = client.get('/entry/list', follow_redirects=False)
    assert response.status_code == 200
