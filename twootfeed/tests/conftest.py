import os
from typing import Any, Dict, List
from unittest.mock import Mock

import pytest
from flask import Flask

from .. import create_app
from .data import retweet, tweet_1, tweet_no_full_text
from .utils import Tweepy

os.environ['FLASK_ENV'] = 'testing'
os.environ['TWOOTFEED_SETTINGS'] = 'TestingConfig'


def mock_api(tweets: List[Dict]) -> Mock:
    mock_response = Mock()
    mock_response.return_value = Tweepy(tweets)
    return mock_response


def get_app(monkeypatch: pytest.MonkeyPatch, tmpdir: Any) -> Flask:
    test_dir = str(tmpdir)
    monkeypatch.setenv('TWOOTFEED_CONFIG', test_dir)
    monkeypatch.setenv('TWOOTFEED_CONFIG_FILE', test_dir + '/config.yml')
    app = create_app()
    return app


@pytest.fixture
def app(monkeypatch: pytest.MonkeyPatch, tmpdir: Any) -> Flask:
    return get_app(monkeypatch, tmpdir)


@pytest.fixture
def app_missing_token(monkeypatch: pytest.MonkeyPatch, tmpdir: Any) -> Flask:
    app = get_app(monkeypatch, tmpdir)
    app.config['TOKEN'] = ''
    return app


@pytest.fixture
def app_invalid_token(monkeypatch: pytest.MonkeyPatch, tmpdir: Any) -> Flask:
    app = get_app(monkeypatch, tmpdir)
    app.config['TOKEN'] = 'invalid_token'
    return app


@pytest.fixture()
def fake_tweepy_ok() -> Mock:
    return mock_api(tweets=[tweet_1])


@pytest.fixture()
def fake_tweepy_retweet() -> Mock:
    return mock_api(tweets=[retweet])


@pytest.fixture()
def fake_tweepy_no_full_text() -> Mock:
    return mock_api(tweets=[tweet_no_full_text])


@pytest.fixture()
def fake_tweepy_no_tweets() -> Mock:
    return mock_api(tweets=[])


@pytest.fixture()
def fake_tweepy_200_ok() -> Mock:
    return mock_api(tweets=[tweet_1] * 200)


@pytest.fixture()
def fake_tweepy_220_ok() -> Mock:
    return mock_api(
        tweets=[tweet_1] * 200 + [tweet_no_full_text] * 10 + [retweet] * 10
    )
