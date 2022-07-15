from unittest.mock import patch

from flask import Flask

from .utils import MastodonApi, Tweepy, TwitterApi


@patch('twootfeed.twitter.generate_tweets_feed.tweepy', Tweepy([]))
@patch('twootfeed.twitter.routes.twitter_api', TwitterApi())
@patch('twootfeed.mastodon.routes.mastodon_api', MastodonApi([]))
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
