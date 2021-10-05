from unittest.mock import Mock

import pytest

from .. import create_app
from .data import retweet, tweet_1, tweet_no_full_text
from .utils import Tweepy


def mock_api(tweets):
    mock_response = Mock()
    mock_response.return_value = Tweepy(tweets)
    return mock_response


@pytest.fixture
def app(monkeypatch, tmpdir):
    test_dir = str(tmpdir)
    monkeypatch.setenv('TWOOTFEED_CONFIG', test_dir)
    monkeypatch.setenv('TWOOTFEED_CONFIG_FILE', test_dir + '/config.yml')
    app = create_app()
    return app


@pytest.fixture()
def fake_tweepy_ok():
    return mock_api(tweets=[tweet_1])


@pytest.fixture()
def fake_tweepy_retweet():
    return mock_api(tweets=[retweet])


@pytest.fixture()
def fake_tweepy_no_full_text():
    return mock_api(tweets=[tweet_no_full_text])


@pytest.fixture()
def fake_tweepy_no_tweets():
    return mock_api(tweets=[])


@pytest.fixture()
def fake_tweepy_200_ok():
    return mock_api(tweets=[tweet_1] * 200)


@pytest.fixture()
def fake_tweepy_220_ok():
    return mock_api(
        tweets=[tweet_1] * 200 + [tweet_no_full_text] * 10 + [retweet] * 10
    )
