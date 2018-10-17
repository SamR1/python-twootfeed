import re

import pytz
import tweepy
from flask import Blueprint

from twootfeed import param, twitter_api
from twootfeed.utils.feed_generation import generate_feed


twitter_bp = Blueprint('twitter', __name__)


def format_tweet(i):
    tweet = {'text': i.full_text, 'screen_name': i.user.screen_name,
             'profile_image_url': i.user.profile_image_url_https,
             'user_name': i.user.name, 'user_url': i.user.url,
             'id_str': i.id_str, 'created_at': i.created_at, 'source': i.source,
             'retweets': i.retweet_count, 'favorites': i.favorite_count}
    tweet['tweet_url'] = 'https://twitter.com/' + tweet[
        'user_name'] + '/status/' + tweet['id_str']

    tweet['htmltext'] = '<blockquote><div><img src="' + tweet[
        'profile_image_url'] + \
        '" alt="' + tweet['screen_name'] + \
        '" />   <strong>' + tweet['user_name'] + \
        ': </strong>' + tweet['text'] + \
        '<br><i>Source: ' + tweet[
            'source'] + '</i>'

    user_mentionslist = i.entities.get('user_mentions')
    for user in user_mentionslist:
        if user != '':
            tweet['htmltext'] = re.sub(
                ('@' + user.get('screen_name')),
                ('<a href="https://twitter.com/'
                 + user.get('screen_name')
                 + '" target="_blank">@'
                 + user.get('screen_name') + '</a>'),
                tweet['htmltext'])

    hashtaglist = i.entities.get('hashtags')
    for hashtag in hashtaglist:
        if hashtag != '':
            tweet['htmltext'] = re.sub(
                ('#' + hashtag.get('text')),
                ('<a href="https://twitter.com/hashtag/'
                 + hashtag.get('text')
                 + '?src=hash" target="_blank">#'
                 + hashtag.get('text') + '</a>'),
                tweet['htmltext']
            )

    urllist = i.entities.get('urls')
    for url in urllist:
        if url != '':
            tweet['htmltext'] = re.sub(
                (url.get('url')),
                ('<a href="'
                 + url.get('expanded_url')
                 + '" target="_blank">'
                 + url.get('display_url')
                 + '</a>'),
                tweet['htmltext'])
    try:
        medialist = i.extended_entities.get('media')
    except AttributeError:
        pass
    else:
        if medialist is not None:
            tweet['htmltext'] = tweet['htmltext'] + '<br> '
            for media in medialist:
                if media != '':
                    if media.get('type') == 'photo':
                        tweet['htmltext'] = re.sub(
                            media.get('url'), '',
                            tweet['htmltext']
                        )
                        tweet['htmltext'] = tweet['htmltext'] \
                                            + '<a href="' \
                                            + media.get('media_url_https') \
                                            + '" target="_blank"> ' \
                                              '<img src="' \
                                            + media.get('media_url_https') \
                                            + ':thumb' + '"> ' \
                                            + '</a>'

    location = i.place
    if location is not None:
        tweet['htmltext'] = tweet['htmltext'] \
                            + '<br><i>Location: ' \
                            + location.full_name + '</i>'

    tweet['htmltext'] = tweet['htmltext'] + '<br> ♻ : ' + str(
        tweet['retweets']) + ', ' + '♥ : ' + str(
        tweet['favorites']) + '</div></blockquote>'

    return tweet


@twitter_bp.route('/<query_feed>', methods=['GET'])
@twitter_bp.route('/tweets/<query_feed>', methods=['GET'])
def tweetfeed(query_feed):
    """ generate a rss feed from parsed twitter search """

    if twitter_api:
        feed_title = param['twitter']['title'] + '"' + query_feed + '"'
        feed_link = param['twitter']['link'] + query_feed
        f = generate_feed(feed_title, feed_link, param)

        for i in tweepy.Cursor(twitter_api.search,
                               q=query_feed,
                               tweet_mode='extended').items():
            try:
                i.full_text
            except Exception:
                break
            else:
                try:
                    retweeted_status = i.retweeted_status

                except Exception:
                    retweeted_status = False

                if not retweeted_status:  # only the original tweets
                    tweet = format_tweet(i)
                    f.add_item(
                        title=tweet['screen_name']
                        + ' ('
                        + tweet['user_name'] + '): '
                        + tweet['text'],
                        link=tweet['tweet_url'],
                        pubdate=pytz.utc.localize(
                            tweet['created_at']).astimezone(
                            pytz.timezone(param['feed']['timezone'])),
                        description=tweet['htmltext'])

        xml = f.writeString('UTF-8')
    else:
        xml = 'error - Twitter parameters not defined'

    return xml
