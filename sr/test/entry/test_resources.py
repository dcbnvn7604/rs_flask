def test_list_authentication(client):
    response = client.get('/api/entry')

    assert response.status_code == 401


def test_list(client, token):
    response = client.get('/api/entry', headers={'Authorization': 'Bearer %s' % (token,)})
    assert response.status_code == 200
