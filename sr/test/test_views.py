import pytest
from urllib.parse import urlparse


def test_register_get(client):
    response = client.get('/user/register')
    assert response.status_code == 200


def test_register_post(client, init_database):
    response = client.post('/user/register', data={'username': 'username1', 'password': 'password1', 'repassword': 'password1'}, follow_redirects=False)
    assert response.status_code == 302
    assert urlparse(response.location).path == '/user/login'

    response = client.post('/user/login', data={'username': 'username1', 'password': 'password1'})
    assert response.status_code == 302
    assert urlparse(response.location).path == '/'
