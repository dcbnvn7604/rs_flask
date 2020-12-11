from sr.entry.models import Entry


def test_list_authentication(client):
    response = client.get('/api/entry')

    assert response.status_code == 401


def test_list(client, token):
    response = client.get('/api/entry', headers={'Authorization': 'Bearer %s' % (token,)})

    assert response.status_code == 200


def test_create_authentication(client):
    response = client.post('/api/entry', data={'title': 'title 1', 'content': 'content 1'})

    assert response.status_code == 401


def test_create_has_permission(client, token):
    response = client.post('/api/entry', data={'title': 'title 1', 'content': 'content 1'}, headers={'Authorization': 'Bearer %s' % (token,)})

    assert response.status_code == 403


def test_create(client, token_with_permisssions):
    response = client.post('/api/entry', data={'title': 'title 1', 'content': 'content 1'}, headers={'Authorization': 'Bearer %s' % (token_with_permisssions[0],)})
    assert response.status_code == 201


def test_update_authentication(client):
    response = client.put('/api/entry/1', data={'title': 'title 1', 'content': 'content 1'})

    assert response.status_code == 401


def test_update_has_permission(client, token):
    response = client.put('/api/entry/1', data={'title': 'title 1', 'content': 'content 1'}, headers={'Authorization': 'Bearer %s' % (token,)})

    assert response.status_code == 403


def test_update(client, token_with_permisssions):
    Entry.create('title', 'content', token_with_permisssions[1])
    response = client.put('/api/entry/1', data={'title': 'title 1', 'content': 'content 1'}, headers={'Authorization': 'Bearer %s' % (token_with_permisssions[0],)})

    assert response.status_code == 200
