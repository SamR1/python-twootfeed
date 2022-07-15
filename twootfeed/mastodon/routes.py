from typing import Tuple

from flask import Blueprint
from twootfeed import mastodon_api, param as mastodon_param
from twootfeed.mastodon.generate_toots_feed import generate_xml
from twootfeed.utils.decorator import require_token

mastodon_bp = Blueprint('mastodon', __name__)


@mastodon_bp.route('/toots/<hashtag>', methods=['GET'])
@require_token
def tootfeed_hashtag(hashtag: str) -> Tuple[str, int]:
    """generate a rss feed from parsed mastodon search"""
    return generate_xml(mastodon_api, mastodon_param, {'hashtag': hashtag})


@mastodon_bp.route('/toots/search/<query_feed>', methods=['GET'])
@mastodon_bp.route('/toot_search/<query_feed>', methods=['GET'])
@require_token
def tootfeed(query_feed: str) -> Tuple[str, int]:
    """generate a rss feed from parsed mastodon search"""
    return generate_xml(mastodon_api, mastodon_param, {'query': query_feed})


@mastodon_bp.route('/toots/favorites', methods=['GET'])
@mastodon_bp.route('/toot_favorites', methods=['GET'])
@require_token
def toot_favorites_feed() -> Tuple[str, int]:
    """generate a rss feed authenticated user's favorites"""
    return generate_xml(mastodon_api, mastodon_param, target='favorites')


@mastodon_bp.route('/toots/bookmarks', methods=['GET'])
@mastodon_bp.route('/toot_bookmarks', methods=['GET'])
@require_token
def toot_bookmarks_feed() -> Tuple[str, int]:
    """generate a rss feed authenticated user's bookmarks"""
    return generate_xml(mastodon_api, mastodon_param, target='bookmarks')


@mastodon_bp.route('/home_timeline', methods=['GET'])
@require_token
def home_timeline() -> Tuple[str, int]:
    """generate a rss feed authenticated user's bookmarks"""
    return generate_xml(mastodon_api, mastodon_param, target='home_timeline')
