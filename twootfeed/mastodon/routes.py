import datetime

import feedgenerator
import pytz
from bs4 import BeautifulSoup
from flask import Blueprint

from twootfeed import mastodon_api, param

mastodon_bp = Blueprint('mastodon', __name__)
text_length_limit = int(param['feed'].get('text_length_limit', 100))


def format_toot(toot):
    toot['htmltext'] = '<blockquote><div><img src="' + toot['account'][
        'avatar_static'] + \
        '" alt="' + toot['account']['display_name'] + \
        '" width= 100px"/>   <strong>' + toot['account']['username'] + \
        ': </strong>' + toot['content']

    source = toot.get('application')
    if source:
        toot['htmltext'] += '<i>Source: ' + source.get('name') + '</i>'

    medialist = toot.get('media_attachments')
    if len(medialist) > 0:
        toot['htmltext'] += '<br>'
    for media in medialist:
        if media.type == 'image':
            toot['htmltext'] += '<a href="' + \
                                media.get('url') + \
                                '" target="_blank"><img src="' + \
                                media.get('preview_url') + \
                                '"></a>'

    toot['htmltext'] += '<br>' + \
        '♻ : ' + str(toot['reblogs_count']) + ', ' + \
        '✰ : ' + str(toot['favourites_count']) + '</div></blockquote>'

    if isinstance(toot['created_at'], str):
        toot['created_at'] = datetime.datetime.strptime(
            toot['created_at'], '%Y-%m-%dT%H:%M:%S.%fZ')

    toot['text'] = BeautifulSoup(toot['content'], "html.parser").text

    utc = pytz.utc
    pubdate = toot['created_at']
    if not pubdate.tzinfo:
        toot['pubdate'] = utc.localize(pubdate).astimezone(
            pytz.timezone(param['feed']['timezone']))
    else:
        toot['pubdate'] = pubdate

    if len(toot['text']) > text_length_limit:
        toot['text'] = toot['text'][:text_length_limit] + '... '

    return toot


@mastodon_bp.route('/toots/<query_feed>', methods=['GET'])
def tootfeed(query_feed):
    """ generate a rss feed from parsed mastodon search """

    if mastodon_api:
        hashtag_result = mastodon_api.timeline_hashtag(query_feed)

        f = feedgenerator.Rss201rev2Feed(
            title=param['mastodon']['title'] + '"' + query_feed + '"',
            link=param['mastodon']['url'] + '/web/timelines/tag/' + query_feed,
            description=param['mastodon']['description'],
            language=param['feed']['language'],
            author_name=param['feed']['author_name'],
            feed_url=param['feed']['feed_url'])

        for toot in hashtag_result:
            formatted_toot = format_toot(toot)
            f.add_item(
                title=(formatted_toot['account']['display_name'] + ' (' +
                       formatted_toot['account']['username'] + '): ' +
                       formatted_toot['text']),
                link=formatted_toot['url'],
                pubdate=formatted_toot['pubdate'],
                description=formatted_toot['htmltext'])

        xml = f.writeString('UTF-8')
    else:
        xml = 'error - Mastodon parameters not defined'

    return xml


@mastodon_bp.route('/toot_favorites', methods=['GET'])
def toot_favorites_feed():
    """ generate an rss feed authenticated user's favorites """

    if mastodon_api:
        buffered = []
        favorite_toots = mastodon_api.favourites()

        f = feedgenerator.Rss201rev2Feed(
            title=param['mastodon']['title'] + ' Favourites ',
            link=param['mastodon']['url'] + '/web/favourites',
            description=param['mastodon']['description'],
            language=param['feed']['language'],
            author_name=param['feed']['author_name'],
            feed_url=param['feed']['feed_url'])

        for toot in favorite_toots:
            formatted_toot = format_toot(toot)
            f.add_item(
                title=(formatted_toot['account']['display_name'] + ' (' +
                       formatted_toot['account']['username'] + '): ' +
                       formatted_toot['text']),
                link=formatted_toot['url'],
                pubdate=formatted_toot['pubdate'],
                description=formatted_toot['htmltext'])

        xml = f.writeString('UTF-8')
    else:
        xml = 'error - Mastodon parameters not defined'

    return xml