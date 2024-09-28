import pytest
from redis import Redis

from .main import app, normalize_url


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


def test_normalize_url():
    data = 'hello.com'
    exp = 'hello.com'
    assert normalize_url(data) == exp

    data = 'https://yandex.ru'
    exp = 'yandex.ru'
    assert normalize_url(data) == exp

    data = 'hello.com?from=2&to=3'
    exp = 'hello.com'
    assert normalize_url(data) == exp

