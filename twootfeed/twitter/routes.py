from typing import Tuple

from flask import Blueprint, request
from twootfeed import param, twitter_api
from twootfeed.twitter.generate_tweets_feed import generate_xml
from twootfeed.utils.decorator import require_token

twitter_bp = Blueprint('twitter', __name__)


@twitter_bp.route('/tweets', methods=['GET'])
@require_token
def tweetfeed() -> Tuple[str, int]:
    """generate a rss feed from parsed twitter search"""
    q = request.args.get('q')
    if not q:
        return 'missing query', 400
    return generate_xml(twitter_api, q, param)
