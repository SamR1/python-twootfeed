from flask import Blueprint
from twootfeed import param, twitter_api
from twootfeed.twitter.generate_tweets_feed import generate_xml

twitter_bp = Blueprint('twitter', __name__)


@twitter_bp.route('/<query_feed>', methods=['GET'])
@twitter_bp.route('/tweets/<query_feed>', methods=['GET'])
def tweetfeed(query_feed):
    """generate a rss feed from parsed twitter search"""
    return generate_xml(twitter_api, query_feed, param)
