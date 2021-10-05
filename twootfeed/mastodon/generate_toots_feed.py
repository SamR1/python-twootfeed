from html import unescape

import pytz
from bs4 import BeautifulSoup
from twootfeed.utils.feed_generation import generate_feed


def format_toot(toot, text_length_limit):
    rss_toot = {
        'display_name': toot['account']['display_name'],
        'screen_name': toot['account']['username'],
        'created_at': toot['created_at'],
        'url': toot['url'],
        'htmltext': (
            "<blockquote><div><img src=\""
            f"{toot['account']['avatar_static']}\" "
            f"alt=\"{toot['account']['display_name']}\""
            f" width= 100px\"/> "
            f"<strong>{toot['account']['display_name']}: </strong>"
            f"{toot['content']}"
        ),
    }

    source = toot.get('application')
    if source:
        rss_toot['htmltext'] += '<i>Source: {}</i>'.format(source.get('name'))

    medialist = toot.get('media_attachments')
    if len(medialist) > 0:
        rss_toot['htmltext'] += '<br>'
    for media in medialist:
        if media['type'] == 'image':
            rss_toot['htmltext'] += (
                f"<a href=\"{media.get('url')}\" target="
                f"\"_blank\"><img src=\""
                f"{media.get('preview_url')}\"></a>"
            )

    rss_toot['htmltext'] += (
        f"<br>♻ : {toot['reblogs_count']}, "
        f"✰ : {toot['favourites_count']}"
        f"</div></blockquote>"
    )

    rss_toot['text'] = BeautifulSoup(
        unescape(toot['content']), "html.parser"
    ).text

    if len(rss_toot['text']) > text_length_limit:
        rss_toot['text'] = rss_toot['text'][:text_length_limit] + '... '

    return rss_toot


def generate_mastodon_feed(
    result, param, feed_title, feed_link, feed_desc=None
):
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
                formatted_toot['display_name']
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


def get_next_toots(api, first_toots, max_items):
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


def generate_xml(api, param, query_feed=None, favorites=False):
    if api:
        max_items = param['feed']['max_items']
        if query_feed:
            hashtag = query_feed.get('hashtag')
            query = query_feed.get('query')
            if hashtag:
                result = api.timeline_hashtag(hashtag)
                result = get_next_toots(api, result, max_items)
                feed_title = param['mastodon']['title'] + '"' + hashtag + '"'
                feed_link = (
                    param['mastodon']['url'] + '/web/timelines/tag/' + hashtag
                )
            else:
                search_result = api.search(query, resolve=True)
                result = search_result['statuses'][: max_items - 1]
                feed_title = param['mastodon']['title'] + '"' + query + '"'
                feed_link = param['mastodon']['url'] + '/web/search/'
            feed_desc = param['mastodon']['description']
        elif favorites:
            result = api.favourites()
            result = get_next_toots(api, result, max_items)
            feed_title = param['mastodon']['title'] + ' Favourites'
            feed_link = param['mastodon']['url'] + '/web/favourites'
            feed_desc = param['feed']['author_name'] + ' favourites toots.'
        else:
            result = api.bookmarks()
            result = get_next_toots(api, result, max_items)
            feed_title = param['mastodon']['title'] + ' Bookmarks'
            feed_link = param['mastodon']['url'] + '/web/bookmarks'
            feed_desc = param['feed']['author_name'] + ' bookmarks toots.'
        xml = generate_mastodon_feed(
            result, param, feed_title, feed_link, feed_desc
        )
        code = 200
    else:
        xml = 'error - Mastodon parameters not defined'
        code = 401
    return xml, code
