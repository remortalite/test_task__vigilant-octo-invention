import pytest
from redis import Redis

from .main import app, r


@pytest.fixture
def client():
    app.config['TESTING'] = True
    return app.test_client()


def test_visited_links(client):
    with client:
        response = client.post('/visited_links', json={'links': ['test_hello.com', 'test_yandex.ru']})
        assert response.status_code == 200

        response = client.get('/visited_links')
        assert 'test_hello.com' in response.json['domains']
        assert 'test_yandex.ru' in response.json['domains']
        assert response.json['status'] == 'ok'
