from typing import Tuple

from flask import Blueprint, request
from twootfeed import mastodon_api, param as mastodon_param
from twootfeed.mastodon.generate_toots_feed import generate_xml
from twootfeed.utils.decorator import require_token

mastodon_bp = Blueprint('mastodon', __name__)


@mastodon_bp.route('/toots/tags/<tag>', methods=['GET'])
@require_token
def toots_feed_hashtag(tag: str) -> Tuple[str, int]:
    """generate a rss feed from parsed mastodon search"""
    return generate_xml(mastodon_api, mastodon_param, {'hashtag': tag})


@mastodon_bp.route('/toots/search', methods=['GET'])
@require_token
def toots_feed_search() -> Tuple[str, int]:
    """generate a rss feed from parsed mastodon search"""
    q = request.args.get('q')
    if not q:
        return 'missing query', 400
    return generate_xml(mastodon_api, mastodon_param, {'query': q})


@mastodon_bp.route('/toots/favorites', methods=['GET'])
@require_token
def toots_favorites_feed() -> Tuple[str, int]:
    """generate a rss feed authenticated user's favorites"""
    return generate_xml(mastodon_api, mastodon_param, target='favorites')


@mastodon_bp.route('/toots/bookmarks', methods=['GET'])
@require_token
def toots_bookmarks_feed() -> Tuple[str, int]:
    """generate a rss feed authenticated user's bookmarks"""
    return generate_xml(mastodon_api, mastodon_param, target='bookmarks')


@mastodon_bp.route('/toots/home_timeline', methods=['GET'])
@require_token
def toots_home_timeline() -> Tuple[str, int]:
    """generate a rss feed authenticated user's home timeline"""
    return generate_xml(mastodon_api, mastodon_param, target='home_timeline')
