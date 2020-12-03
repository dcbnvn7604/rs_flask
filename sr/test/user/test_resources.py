def test_login_fail(client, init_database):
    response = client.post('/api/user/login', data={'username': 'test', 'password': 'test1'})
    assert response.status_code == 401


def test_login(client, user):
    response = client.post('/api/user/login', data={'username': 'test', 'password': 'test1'})
    assert response.status_code == 200
    assert 'token' in response.json
