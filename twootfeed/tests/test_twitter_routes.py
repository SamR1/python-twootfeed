from uuid import uuid4

from flask import Flask

from .data import TEST_TOKEN


class TestTwitterRoutes:
    endpoint = '/tweets'

    def test_it_returns_401_when_token_is_missing(
        self, app_missing_token: Flask
    ) -> None:
        client = app_missing_token.test_client()

        response = client.get(self.endpoint)

        assert response.status_code == 401
        data = response.data.decode()
        assert data == 'missing token'

    def test_it_returns_403_when_token_is_invalid(
        self, app_invalid_token: Flask
    ) -> None:
        client = app_invalid_token.test_client()

        response = client.get(f'{self.endpoint}?token=invalid')

        assert response.status_code == 403
        data = response.data.decode()
        assert data == 'invalid token'

    def test_it_returns_400_when_query_is_missing(self, app: Flask) -> None:
        client = app.test_client()

        response = client.get(f'{self.endpoint}?token={TEST_TOKEN}')

        assert response.status_code == 400
        data = response.data.decode()
        assert data == 'missing query'

    def test_it_returns_200_when_query_valid(self, app: Flask) -> None:
        client = app.test_client()

        response = client.get(
            f'{self.endpoint}?q={uuid4().hex}&token={TEST_TOKEN}'
        )

        assert response.status_code == 200
        data = response.data.decode()
        assert '<rss version="2.0">' in data
