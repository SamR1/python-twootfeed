import datetime

import feedgenerator
import pytz
from bs4 import BeautifulSoup
from flask import Blueprint

from twootfeed import mastodon_api, param

mastodon_bp = Blueprint('mastodon', __name__)
text_length_limit = int(param['feed'].get('text_length_limit', 100))


@mastodon_bp.route('/toots/<query_feed>', methods=['GET'])
def tootfeed(query_feed):
    """ generate a rss feed from parsed mastodon search """

    if mastodon_api:
        buffered = []
        hashtagResult = mastodon_api.timeline_hashtag(query_feed)

        for toot in hashtagResult:

            toot['htmltext'] = '<blockquote><div><img src="' + toot['account'][
                'avatar_static'] + \
                '" alt="' + toot['account']['display_name'] + \
                '" />   <strong>' + toot['account']['username'] + \
                ': </strong>' + toot['content'] + '<br>' + \
                '♻ : ' + str(toot['reblogs_count']) + ', ' + \
                '✰ : ' + str(
                toot['favourites_count']) + '</div></blockquote>'

            if isinstance(toot['created_at'], str):
                toot['created_at'] = datetime.datetime.strptime(
                    toot['created_at'], '%Y-%m-%dT%H:%M:%S.%fZ')

            buffered.append(toot.copy())

        utc = pytz.utc
        f = feedgenerator.Rss201rev2Feed(
            title=param['mastodon']['title'] + '"' + query_feed + '"',
            link=param['mastodon']['url'] + '/web/timelines/tag/' + query_feed,
            description=param['mastodon']['description'],
            language=param['feed']['language'],
            author_name=param['feed']['author_name'],
            feed_url=param['feed']['feed_url'])

        for toot in buffered:

            text = BeautifulSoup(toot['content'], "html.parser").text
            pubdate = toot['created_at']
            if not pubdate.tzinfo:
                pubdate = utc.localize(pubdate).astimezone(
                    pytz.timezone(param['feed']['timezone']))

            if len(text) > text_length_limit:
                text = text[:text_length_limit] + '... '
            f.add_item(
                title=toot['account']['display_name'] + ' (' + toot['account'][
                    'username'] + '): ' + text,
                link=toot['url'],
                pubdate=pubdate,
                description=toot['htmltext'])

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
        for toot in favorite_toots:

            toot['htmltext'] = '<blockquote><div><img src="' + toot['account'][
                'avatar_static'] + \
                '" alt="' + toot['account']['display_name'] + \
                '" />   <strong>' + toot['account']['username'] + \
                ': </strong>' + toot['content'] + '<br>' + \
                '♻ : ' + str(toot['reblogs_count']) + ', ' + \
                '✰ : ' + str(
                toot['favourites_count']) + '</div></blockquote>'

            if isinstance(toot['created_at'], str):
                toot['created_at'] = datetime.datetime.strptime(
                    toot['created_at'], '%Y-%m-%dT%H:%M:%S.%fZ')

            buffered.append(toot.copy())

        utc = pytz.utc
        f = feedgenerator.Rss201rev2Feed(
            title=param['mastodon']['title'] + ' Favourites ',
            link=param['mastodon']['url'] + '/web/favourites',
            description=param['mastodon']['description'],
            language=param['feed']['language'],
            author_name=param['feed']['author_name'],
            feed_url=param['feed']['feed_url'])

        for toot in buffered:

            text = BeautifulSoup(toot['content'], "html.parser").text
            pubdate = toot['created_at']
            if not pubdate.tzinfo:
                pubdate = utc.localize(pubdate).astimezone(
                    pytz.timezone(param['feed']['timezone']))

            if len(text) > text_length_limit:
                text = text[:text_length_limit] + '... '
            f.add_item(
                title=toot['account']['display_name'] + ' (' + toot['account'][
                    'username'] + '): ' + text,
                link=toot['url'],
                pubdate=pubdate,
                description=toot['htmltext'])

        xml = f.writeString('UTF-8')
    else:
        xml = 'error - Mastodon parameters not defined'

    return xml
