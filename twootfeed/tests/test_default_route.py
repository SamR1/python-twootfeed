from flask import Flask


def test_default_route(app: Flask) -> None:
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    data = response.data.decode()
    assert data == (
        'The RSS feeds are available on these urls : \r\n'
        'for Twitter : http://localhost:5000/_keywords_ '
        'or http://localhost:5000/tweets/_keywords_ ,\r\n'
        'for Mastodon : http://localhost:5000/toots/_keywords_'
    )
