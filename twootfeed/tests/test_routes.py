from uuid import uuid4

import pytest
from flask import Flask

MASTODON_ENDPOINTS = [
    '/toots/favorites',
    '/toot_favorites',
    '/toots/bookmarks',
    '/toot_bookmarks',
    '/home_timeline',
]


class TestTwitterRoutesToken:
    endpoint = '/{keyword}'

    def test_it_returns_401_when_token_is_missing(
        self, app_missing_token: Flask
    ) -> None:
        client = app_missing_token.test_client()

        response = client.get(self.endpoint.format(keyword=uuid4().hex))

        assert response.status_code == 401
        data = response.data.decode()
        assert data == 'missing token in parameters'

    def test_it_returns_403_when_token_is_invalid(
        self, app_invalid_token: Flask
    ) -> None:
        client = app_invalid_token.test_client()

        response = client.get(
            f'{self.endpoint.format(keyword=uuid4().hex)}?token=invalid'
        )

        assert response.status_code == 403
        data = response.data.decode()
        assert data == 'invalid token'


class TestTwitterTweetsRouteToken(TestTwitterRoutesToken):
    endpoint = '/tweets/{keyword}'


class TestMastodonHashtagRouteToken:
    endpoint = '/toots/{hashtag}'

    def test_it_returns_401_when_token_is_missing(
        self, app_missing_token: Flask
    ) -> None:
        client = app_missing_token.test_client()

        response = client.get(self.endpoint.format(hashtag=uuid4().hex))

        assert response.status_code == 401
        data = response.data.decode()
        assert data == 'missing token in parameters'

    def test_it_returns_403_when_token_is_invalid(
        self, app_invalid_token: Flask
    ) -> None:
        client = app_invalid_token.test_client()

        response = client.get(
            f'{self.endpoint.format(hashtag=uuid4().hex)}?token=invalid'
        )

        assert response.status_code == 403
        data = response.data.decode()
        assert data == 'invalid token'


class TestMastodonSearchRouteToken:
    endpoint = '/toots/search/{query_feed}'

    def test_it_returns_401_when_token_is_missing(
        self, app_missing_token: Flask
    ) -> None:
        client = app_missing_token.test_client()

        response = client.get(self.endpoint.format(query_feed=uuid4().hex))

        assert response.status_code == 401
        data = response.data.decode()
        assert data == 'missing token in parameters'

    def test_it_returns_403_when_token_is_invalid(
        self, app_invalid_token: Flask
    ) -> None:
        client = app_invalid_token.test_client()

        response = client.get(
            f'{self.endpoint.format(query_feed=uuid4().hex)}?token=invalid'
        )

        assert response.status_code == 403
        data = response.data.decode()
        assert data == 'invalid token'


class TestMastodonSearchAlternativeRouteToken(TestMastodonSearchRouteToken):
    endpoint = '/toot_search/{query_feed}'


class TestMastodonRoutesToken:
    @pytest.mark.parametrize('input_endpoint', MASTODON_ENDPOINTS)
    def test_it_returns_401_when_token_is_missing(
        self, app_missing_token: Flask, input_endpoint: str
    ) -> None:
        client = app_missing_token.test_client()

        response = client.get(input_endpoint)

        assert response.status_code == 401
        data = response.data.decode()
        assert data == 'missing token in parameters'

    @pytest.mark.parametrize('input_endpoint', MASTODON_ENDPOINTS)
    def test_it_returns_403_when_token_is_invalid(
        self, app_invalid_token: Flask, input_endpoint: str
    ) -> None:
        client = app_invalid_token.test_client()

        response = client.get(f'{input_endpoint}?token=invalid')

        assert response.status_code == 403
        data = response.data.decode()
        assert data == 'invalid token'
