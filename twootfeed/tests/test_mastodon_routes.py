from uuid import uuid4

import pytest
from flask import Flask

from .data import TEST_TOKEN
from .test_twitter_routes import TestTwitterRoutes

MASTODON_ENDPOINTS = [
    '/toots/favorites',
    '/toots/bookmarks',
    '/toots/home_timeline',
]


class TestMastodonTagsRoute:
    endpoint = '/toots/tags/{tag}'

    def test_it_returns_401_when_token_is_missing(
        self, app_missing_token: Flask
    ) -> None:
        client = app_missing_token.test_client()

        response = client.get(self.endpoint.format(tag=uuid4().hex))

        assert response.status_code == 401
        data = response.data.decode()
        assert data == 'missing token'

    def test_it_returns_403_when_token_is_invalid(
        self, app_invalid_token: Flask
    ) -> None:
        client = app_invalid_token.test_client()

        response = client.get(
            f'{self.endpoint.format(tag=uuid4().hex)}?token=invalid'
        )

        assert response.status_code == 403
        data = response.data.decode()
        assert data == 'invalid token'

    def test_it_returns_200_when_tag_is_provided(self, app: Flask) -> None:
        client = app.test_client()

        response = client.get(
            f'{self.endpoint.format(tag=uuid4().hex)}?&token={TEST_TOKEN}'
        )

        assert response.status_code == 200
        data = response.data.decode()
        assert '<rss version="2.0">' in data


class TestMastodonSearchRoute(TestTwitterRoutes):
    endpoint = '/toots/search'


class TestMastodonRoutes:
    @pytest.mark.parametrize('input_endpoint', MASTODON_ENDPOINTS)
    def test_it_returns_401_when_token_is_missing(
        self, app_missing_token: Flask, input_endpoint: str
    ) -> None:
        client = app_missing_token.test_client()

        response = client.get(input_endpoint)

        assert response.status_code == 401
        data = response.data.decode()
        assert data == 'missing token'

    @pytest.mark.parametrize('input_endpoint', MASTODON_ENDPOINTS)
    def test_it_returns_403_when_token_is_invalid(
        self, app_invalid_token: Flask, input_endpoint: str
    ) -> None:
        client = app_invalid_token.test_client()

        response = client.get(f'{input_endpoint}?token=invalid')

        assert response.status_code == 403
        data = response.data.decode()
        assert data == 'invalid token'

    @pytest.mark.parametrize('input_endpoint', MASTODON_ENDPOINTS)
    def test_it_returns_200(self, app: Flask, input_endpoint: str) -> None:
        client = app.test_client()

        response = client.get(f'{input_endpoint}?token={TEST_TOKEN}')

        assert response.status_code == 200
        data = response.data.decode()
        assert '<rss version="2.0">' in data
