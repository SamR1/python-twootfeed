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
        'The RSS feeds for search are available on these endpoints: '
        '"tweets?q=QUERY&token=TOKEN" for Twitter or '
        '"toots/search?q=QUERY&token=TOKEN" for Mastodon.'
    )
