import re
from unittest.mock import Mock, patch

from twootfeed.utils.feed_generation import add_noindex

from ..twitter.generate_tweets_feed import (
    format_tweet,
    generate_twitter_feed,
    generate_xml,
)
from .data import (
    empty_feed,
    formatted_tweet_1,
    formatted_tweet_2,
    invalid_param as param,
    tweet_1,
    tweet_1_feed,
    tweet_2,
    tweet_20_feed,
)
from .utils import Tweet, TwitterApi


def test_format_tweet() -> None:
    assert format_tweet(Tweet(tweet_1)) == formatted_tweet_1
    assert format_tweet(Tweet(tweet_2)) == formatted_tweet_2


@patch('tweepy.Cursor')
def test_tweetfeed_empty(fake_tweepy_no_tweets: Mock) -> None:
    val = generate_twitter_feed(None, 'test', param)
    # remove date
    val = re.sub(
        r'(<lastBuildDate>)(.*)(</lastBuildDate>)',
        '<lastBuildDate></lastBuildDate>',
        val,
    )
    assert val == empty_feed


@patch('tweepy.Cursor')
def test_tweetfeed_retweet(get_mock: Mock, fake_tweepy_retweet: Mock) -> None:
    get_mock.return_value = fake_tweepy_retweet.return_value
    val = generate_twitter_feed(None, 'test', param)
    # remove date
    val = re.sub(
        r'(<lastBuildDate>)(.*)(</lastBuildDate>)',
        '<lastBuildDate></lastBuildDate>',
        val,
    )
    assert val == empty_feed


@patch('tweepy.Cursor')
def test_tweetfeed_ok(get_mock: Mock, fake_tweepy_ok: Mock) -> None:
    get_mock.return_value = fake_tweepy_ok.return_value
    val = generate_twitter_feed(None, 'test', param)
    # remove date
    val = re.sub(
        r'(<lastBuildDate>)(.*)(</lastBuildDate>)',
        '<lastBuildDate></lastBuildDate>',
        val,
    )
    assert val == tweet_1_feed


@patch('tweepy.Cursor')
def test_tweetfeed_limit_ok(get_mock: Mock, fake_tweepy_200_ok: Mock) -> None:
    get_mock.return_value = fake_tweepy_200_ok.return_value
    val = generate_twitter_feed(None, 'test', param)
    # remove date
    val = re.sub(
        r'(<lastBuildDate>)(.*)(</lastBuildDate>)',
        '<lastBuildDate></lastBuildDate>',
        val,
    )
    assert val == tweet_20_feed


@patch('tweepy.Cursor')
def test_tweetfeed_limit_with_retweet_ok(
    get_mock: Mock, fake_tweepy_220_ok: Mock
) -> None:
    get_mock.return_value = fake_tweepy_220_ok.return_value
    val = generate_twitter_feed(None, 'test', param)
    # remove date
    val = re.sub(
        r'(<lastBuildDate>)(.*)(</lastBuildDate>)',
        '<lastBuildDate></lastBuildDate>',
        val,
    )
    assert val == tweet_20_feed


@patch('tweepy.Cursor')
def test_generate_xml_ok(get_mock: Mock, fake_tweepy_ok: Mock) -> None:
    get_mock.return_value = fake_tweepy_ok.return_value
    val, code = generate_xml(TwitterApi(), 'test', param)
    # remove date
    val = re.sub(
        r'(<lastBuildDate>)(.*)(</lastBuildDate>)',
        '<lastBuildDate></lastBuildDate>',
        val,
    )
    assert val == add_noindex(tweet_1_feed)
    assert code == 200


def test_generate_xml_no_api() -> None:
    val, code = generate_xml(None, 'test', param)
    assert val == 'error - Twitter parameters not defined'
    assert code == 401
