from html import unescape
from typing import Dict, List, Optional, Tuple

import pytz
from bs4 import BeautifulSoup
from mastodon import Mastodon
from twootfeed.utils.feed_generation import add_noindex, generate_feed

TOOT_VISIBILITY = {
    'public': '🌐',  # Visible to everyone, shown in public timelines.
    'unlisted': '🔓',  # Visible to public, but not included in public timelines.  # noqa
    'private': '🔒',  # Visible to followers only, and to any mentioned users.
    'direct': '<strong>@</strong>',  # Visible only to mentioned users.
}


def get_visibility_icon(toot: Dict) -> str:
    return f"{TOOT_VISIBILITY[toot['visibility']]}"


def format_toot(toot: Dict, text_length_limit: int) -> Dict:
    created_at = toot['created_at']
    boosted = ""
    html_boosted = ""

    reblog = toot.get('reblog')
    if reblog:
        boosted = f"Boosted by {toot['account']['display_name']}: "
        html_boosted = f"<div>{boosted}</div>"
        toot = reblog
        toot['created_at'] = created_at

    rss_toot = {
        'display_name': toot['account']['display_name'],
        'screen_name': toot['account']['username'],
        'created_at': toot['created_at'],
        'url': toot['url'],
        'htmltext': (
            f"<blockquote>{html_boosted}<div><img src=\""
            f"{toot['account']['avatar_static']}\" "
            f"alt=\"{toot['account']['display_name']}\""
            f" width= 100px\" style=\"border-radius: 50%;\"/> "
            f"<strong>{toot['account']['display_name']} </strong>"
            f"{toot['content']}"
        ),
        'boosted': boosted,
    }

    source = toot.get('application')
    if source:
        rss_toot['htmltext'] += '<i>Source: {}</i>'.format(source.get('name'))

    medialist = toot.get('media_attachments', [])
    if len(medialist) > 0:
        rss_toot['htmltext'] += '<br>'
    for media in medialist:
        url = media.get('url')
        if media['type'] == 'image':
            rss_toot['htmltext'] += (
                f"<a href=\"{url}\" target="
                f"\"_blank\"><img src=\""
                f"{media.get('preview_url')}\"></a>"
            )
        if media['type'] in ['video', 'gifv']:
            attrs = (
                'controls'
                if media['type'] == 'video'
                else 'autoplay loop muted inline'
            )
            small = media.get('meta', {}).get('small', {})
            width = small.get('width', 400)
            height = small.get('height', 225)
            preview_url = media.get('preview_url')
            rss_toot['htmltext'] += (
                f"<video width=\"{width}\" height=\"{height}\" {attrs}>"
                f" <source src=\"{url}\" poster=\"{preview_url}\" "
                f"type=\"video/mp4\">"
                "Your browser does not support the video tag."
                "</video> "
            )

        description = media.get('description')
        if description:
            rss_toot[
                'htmltext'
            ] += f"<pre style=\"white-space: normal;\">{description}</pre>"

    visibility_icon = get_visibility_icon(toot)
    rss_toot['htmltext'] += (
        f"<br>♻ : {toot['reblogs_count']}, "
        f"✰ : {toot['favourites_count']}, "
        f"{visibility_icon}</div></blockquote>"
    )

    rss_toot['text'] = BeautifulSoup(
        unescape(toot['content']), "html.parser"
    ).text

    if len(rss_toot['text']) > text_length_limit:
        rss_toot['text'] = rss_toot['text'][:text_length_limit] + '... '

    return rss_toot


def generate_mastodon_feed(
    result: List[Dict],
    param: Dict,
    feed_title: str,
    feed_link: str,
    feed_desc: Optional[str] = None,
) -> str:
    text_length_limit = int(param['feed'].get('text_length_limit', 100))
    f = generate_feed(feed_title, feed_link, param, feed_desc)

    max_toots = param['feed']['max_items'] - 1
    for toot_index, toot in enumerate(result):
        if toot_index > max_toots:
            break
        formatted_toot = format_toot(toot, text_length_limit)
        pubdate = formatted_toot['created_at']
        if not pubdate.tzinfo:
            pubdate = pytz.utc.localize(pubdate).astimezone(
                pytz.timezone(param['feed']['timezone'])
            )
        f.add_item(
            title=(
                formatted_toot['boosted']
                + formatted_toot['display_name']
                + ' ('
                + formatted_toot['screen_name']
                + '): '
                + formatted_toot['text']
            ),
            link=formatted_toot['url'],
            pubdate=pubdate,
            description=formatted_toot['htmltext'],
        )

    xml = f.writeString('UTF-8')

    return xml


def get_next_toots(
    api: Mastodon, first_toots: List[Dict], max_items: int
) -> List[Dict]:
    if len(first_toots) == 0:
        return first_toots
    result = first_toots
    nb_items = len(result)
    next_toots = api.fetch_next(first_toots)
    while next_toots:
        nb_next_toots = len(next_toots)
        if nb_items + nb_next_toots < max_items:
            result += next_toots
            nb_items = len(result)
            next_toots = api.fetch_next(next_toots)
        else:
            result += next_toots[: (max_items - nb_items)]
            next_toots = None
    return result


def generate_xml(
    api: Mastodon,
    param: Dict,
    query_feed: Optional[Dict] = None,
    target: Optional[str] = None,
) -> Tuple[str, int]:
    if api:
        max_items = param['feed']['max_items']
        if query_feed:
            hashtag = query_feed.get('hashtag')
            query = query_feed.get('query')
            if hashtag:
                result = api.timeline_hashtag(hashtag)
                result = get_next_toots(api, result, max_items)
                feed_title = (
                    param['mastodon']['title'] + ' search "' + hashtag + '"'
                )
                feed_link = (
                    param['mastodon']['url'] + '/web/timelines/tag/' + hashtag
                )
            else:
                search_result = api.search(query, resolve=True)
                result = search_result['statuses'][: max_items - 1]
                feed_title = (
                    param['mastodon']['title'] + ' search "' + query + '"'
                )
                feed_link = param['mastodon']['url'] + '/web/search/'
            feed_desc = param['mastodon']['description']
        elif target == 'favorites':
            result = api.favourites()
            result = get_next_toots(api, result, max_items)
            feed_title = param['mastodon']['title'] + ' Favourites'
            feed_link = param['mastodon']['url'] + '/web/favourites'
            feed_desc = param['feed']['author_name'] + ' favourites toots.'
        elif target == 'bookmarks':
            result = api.bookmarks()
            result = get_next_toots(api, result, max_items)
            feed_title = param['mastodon']['title'] + ' Bookmarks'
            feed_link = param['mastodon']['url'] + '/web/bookmarks'
            feed_desc = param['feed']['author_name'] + ' bookmarks toots.'
        elif target == 'home_timeline':
            result = api.timeline_home()
            result = get_next_toots(api, result, max_items)
            feed_title = param['mastodon']['title'] + ' Home Timeline'
            feed_link = param['mastodon']['url']
            feed_desc = param['feed']['author_name'] + ' home timeline.'
        else:
            raise Exception('Invalid target')
        xml = add_noindex(
            generate_mastodon_feed(
                result, param, feed_title, feed_link, feed_desc
            )
        )
        code = 200
    else:
        xml = 'error - Mastodon parameters not defined'
        code = 401
    return xml, code
