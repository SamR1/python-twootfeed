import pytz
from bs4 import BeautifulSoup
from flask import Blueprint
from twootfeed import mastodon_api, param as mastodon_param
from twootfeed.utils.feed_generation import generate_feed

mastodon_bp = Blueprint('mastodon', __name__)


def format_toot(toot, text_length_limit):
    rss_toot = {
        'display_name': toot['account']['display_name'],
        'screen_name': toot['account']['username'],
        'created_at': toot['created_at'],
        'url': toot['url'],
        'htmltext': ("<blockquote><div><img src=\""
                     f"{toot['account']['avatar_static']}\" "
                     f"alt=\"{toot['account']['display_name']}\""
                     f" width= 100px\"/> "
                     f"<strong>{toot['account']['display_name']}: </strong>"
                     f"{toot['content']}")
    }

    source = toot.get('application')
    if source:
        rss_toot['htmltext'] += '<i>Source: {}</i>'.format(source.get('name'))

    medialist = toot.get('media_attachments')
    if len(medialist) > 0:
        rss_toot['htmltext'] += '<br>'
    for media in medialist:
        if media['type'] == 'image':
            rss_toot['htmltext'] += (f"<a href=\"{media.get('url')}\" target="
                                     f"\"_blank\"><img src=\""
                                     f"{media.get('preview_url')}\"></a>")

    rss_toot['htmltext'] += (f"<br>♻ : {toot['reblogs_count']}, "
                             f"✰ : {toot['favourites_count']}"
                             f"</div></blockquote>")

    rss_toot['text'] = BeautifulSoup(toot['content'], "html.parser").text

    if len(rss_toot['text']) > text_length_limit:
        rss_toot['text'] = rss_toot['text'][:text_length_limit] + '... '

    return rss_toot


def generate_mastodon_feed(
        result, param, feed_title, feed_link, feed_desc=None):
    text_length_limit = int(param['feed'].get('text_length_limit', 100))
    f = generate_feed(feed_title, feed_link, param, feed_desc)

    for toot in result:
        formatted_toot = format_toot(toot, text_length_limit)
        pubdate = formatted_toot['created_at']
        if not pubdate.tzinfo:
            pubdate = pytz.utc.localize(pubdate).astimezone(
                pytz.timezone(param['feed']['timezone']))
        f.add_item(
            title=(formatted_toot['display_name'] + ' (' +
                   formatted_toot['screen_name'] + '): ' +
                   formatted_toot['text']),
            link=formatted_toot['url'],
            pubdate=pubdate,
            description=formatted_toot['htmltext'])

    xml = f.writeString('UTF-8')

    return xml


def generate_xml(api, param, query_feed=None):
    if api:
        if query_feed:
            result = api.timeline_hashtag(query_feed)
            feed_title = param['mastodon']['title'] + '"' + query_feed + '"'
            feed_link = (param['mastodon']['url'] + '/web/timelines/tag/' +
                         query_feed)
            feed_desc = param['mastodon']['description']
        else:
            result = api.favourites()
            feed_title = param['mastodon']['title'] + ' Favourites'
            feed_link = param['mastodon']['url'] + '/web/favourites'
            feed_desc = param['feed']['author_name'] + ' favourites toots.'
        xml = generate_mastodon_feed(
            result, param, feed_title, feed_link, feed_desc)
    else:
        xml = 'error - Mastodon parameters not defined'
    return xml


@mastodon_bp.route('/toots/<query_feed>', methods=['GET'])
def tootfeed(query_feed):
    """ generate a rss feed from parsed mastodon search """
    return generate_xml(mastodon_api, mastodon_param, query_feed)


@mastodon_bp.route('/toot_favorites', methods=['GET'])
def toot_favorites_feed():
    """ generate an rss feed authenticated user's favorites """
    return generate_xml(mastodon_api, mastodon_param)
