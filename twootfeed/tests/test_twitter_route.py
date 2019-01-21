from ..twitter.routes import format_tweet
from .data import formatted_tweet_1, formatted_tweet_2, tweet_1, tweet_2
from .utils import ToDotNotation


def test_format_toot():
    assert format_tweet(ToDotNotation(tweet_1)) == formatted_tweet_1
    assert format_tweet(ToDotNotation(tweet_2)) == formatted_tweet_2
