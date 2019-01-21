import re
from unittest.mock import patch

from ..twitter.routes import format_tweet, generate_twitter_feed, generate_xml
from .data import (
    empty_feed,
    formatted_tweet_1,
    formatted_tweet_2,
    invalid_param as param,
    tweet_1,
    tweet_1_feed,
    tweet_2,
)
from .utils import Api as TwitterApi, ToDotNotation


def test_format_toot():
    assert format_tweet(ToDotNotation(tweet_1)) == formatted_tweet_1
    assert format_tweet(ToDotNotation(tweet_2)) == formatted_tweet_2


@patch('tweepy.Cursor')
def test_tweetfeed_empty(fake_tweepy_no_tweets):
    val = generate_twitter_feed(None, 'test', param)
    # remove date
    val = re.sub(
        r'(<lastBuildDate>)(.*)(</lastBuildDate>)',
        '<lastBuildDate></lastBuildDate>',
        val
    )
    assert val == empty_feed


@patch('tweepy.Cursor')
def test_tweetfeed_retweet(get_mock, fake_tweepy_retweet):
    get_mock.return_value = fake_tweepy_retweet.return_value
    val = generate_twitter_feed(None, 'test', param)
    # remove date
    val = re.sub(
        r'(<lastBuildDate>)(.*)(</lastBuildDate>)',
        '<lastBuildDate></lastBuildDate>',
        val
    )
    assert val == empty_feed


@patch('tweepy.Cursor')
def test_tweetfeed_no_full_text(get_mock, fake_tweepy_no_full_text):
    get_mock.return_value = fake_tweepy_no_full_text.return_value
    val = generate_twitter_feed(None, 'test', param)
    # remove date
    val = re.sub(
        r'(<lastBuildDate>)(.*)(</lastBuildDate>)',
        '<lastBuildDate></lastBuildDate>',
        val
    )
    assert val == empty_feed


@patch('tweepy.Cursor')
def test_tweetfeed_ok(get_mock, fake_tweepy_ok):
    get_mock.return_value = fake_tweepy_ok.return_value
    val = generate_twitter_feed(None, 'test', param)
    # remove date
    val = re.sub(
        r'(<lastBuildDate>)(.*)(</lastBuildDate>)',
        '<lastBuildDate></lastBuildDate>',
        val
    )
    assert val == tweet_1_feed


@patch('tweepy.Cursor')
def test_generate_xml_ok(get_mock, fake_tweepy_ok):
    get_mock.return_value = fake_tweepy_ok.return_value
    val = generate_xml(TwitterApi(), 'test', param)
    # remove date
    val = re.sub(
        r'(<lastBuildDate>)(.*)(</lastBuildDate>)',
        '<lastBuildDate></lastBuildDate>',
        val
    )
    assert val == tweet_1_feed


def test_generate_xml_no_api():
    val = generate_xml(None, 'test', param)
    assert val == 'error - Twitter parameters not defined'
