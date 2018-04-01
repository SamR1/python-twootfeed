#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import datetime
import os
import re

import feedgenerator
import pytz
import tweepy
from bs4 import BeautifulSoup
from flask import Flask
from mastodon import Mastodon

from config import get_config

app = Flask(__name__)
app.debug = True

param = get_config()

text_length_limit = int(param['feed'].get('text_length_limit', 100))

# Twitter
try:
    consumerKey = param['twitter']['consumerKey']
    consumerSecret = param['twitter']['consumerSecret']

    auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
    api = tweepy.API(auth)
except Exception as e:
    print('Error Twitter connection: ' + str(e))
    twitterOK = False
else:
    twitterOK = True

# Mastodon
try:
    client_file = 'python-twootfeed/' + param['mastodon']['client_id_file']
    if not os.path.exists(client_file):
        raise Exception('File not found: ' + client_file)
    access_token_file = 'python-twootfeed/' \
                        + param['mastodon']['access_token_file']
    if not os.path.exists(access_token_file):
        raise Exception('File not found: ' + client_file)

    mastodon_url = param['mastodon'].get('url', 'https://mastodon.social')

    mastodon = Mastodon(
        client_id=client_file,
        access_token=access_token_file,
        api_base_url=mastodon_url
    )
except Exception as e:
    print('Error Mastodon instance creation: ' + str(e))
    mastodonOK = False
else:
    mastodonOK = True


@app.route('/')
def index():
    message = 'The RSS feeds are available on these urls : \r\n' \
              'for Twitter : http://localhost:5000/_keywords_ or ' \
              'http://localhost:5000/tweets/_keywords_ ,\r\n' \
              'for Mastodon : http://localhost:5000/toots/_keywords_'

    return message


@app.route('/<query_feed>')
@app.route('/tweets/<query_feed>')
def tweetfeed(query_feed):
    """ generate a rss feed from parsed twitter search """

    if twitterOK:
        tweet = {}
        buffered = []

        for i in tweepy.Cursor(api.search, q=query_feed).items():
            try:
                i.text
            except Exception:
                break
            else:
                try:
                    retweeted_status = i.retweeted_status

                except Exception:
                    retweeted_status = False

                if not retweeted_status:  # only the original tweets

                    tweet['text'] = i.text
                    tweet['screen_name'] = i.user.screen_name
                    tweet['profile_image_url'] = i.user.profile_image_url_https
                    tweet['user_name'] = i.user.name
                    tweet['user_url'] = i.user.url
                    tweet['id_str'] = i.id_str
                    tweet['created_at'] = i.created_at
                    tweet['source'] = i.source
                    tweet['retweets'] = i.retweet_count
                    tweet['favorites'] = i.favorite_count
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
                    for j in user_mentionslist:
                        if j != '':
                            tweet['htmltext'] = re.sub(
                                ('@' + j.get('screen_name')),
                                ('<a href="https://twitter.com/'
                                 + j.get('screen_name')
                                 + '" target="_blank">@'
                                 + j.get('screen_name') + '</a>'),
                                tweet['htmltext'])

                    hashtaglist = i.entities.get('hashtags')
                    for j in hashtaglist:
                        if j != '':
                            tweet['htmltext'] = re.sub(
                                ('#' + j.get('text')),
                                ('<a href="https://twitter.com/hashtag/'
                                 + j.get('text')
                                 + '?src=hash" target="_blank">#'
                                 + j.get('text') + '</a>'),
                                tweet['htmltext']
                            )

                    urllist = i.entities.get('urls')
                    for j in urllist:
                        if j != '':
                            tweet['htmltext'] = re.sub(
                                (j.get('url')),
                                ('<a href="'
                                 + j.get('expanded_url')
                                 + '" target="_blank">'
                                 + j.get('display_url')
                                 + '</a>'),
                                tweet['htmltext'])
                    try:
                        medialist = i.extended_entities.get('media')
                    except AttributeError:
                        pass
                    else:
                        if medialist is not None:
                            tweet['htmltext'] = tweet['htmltext'] + '<br> '
                            for j in medialist:
                                if j != '':
                                    if j.get('type') == 'photo':
                                        tweet['htmltext'] = re.sub(
                                            j.get('url'), '',
                                            tweet['htmltext']
                                        )
                                        tweet['htmltext'] = tweet['htmltext'] \
                                            + '<a href="' \
                                            + j.get('media_url_https')\
                                            + '" target="_blank"> ' \
                                              '<img src="' \
                                            + j.get('media_url_https') \
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

                    buffered.append(tweet.copy())

        utc = pytz.utc
        f = feedgenerator.Rss201rev2Feed(
            title=param['twitter']['title'] + '"' + query_feed + '"',
            link=param['twitter']['link'] + query_feed,
            description=param['twitter']['description'],
            language=param['feed']['language'],
            author_name=param['feed']['author_name'],
            feed_url=param['feed']['feed_url'])

        for tweet in buffered:
            f.add_item(
                title=tweet['screen_name']
                + ' ('
                + tweet['user_name'] + '): '
                + tweet['text'],
                link=tweet['tweet_url'],
                pubdate=utc.localize(tweet['created_at']).astimezone(
                    pytz.timezone(param['feed']['timezone'])),
                description=tweet['htmltext'])

        xml = f.writeString('UTF-8')
    else:
        xml = 'error - Twitter parameters not defined'

    return xml


@app.route('/toots/<query_feed>')
def tootfeed(query_feed):
    """ generate a rss feed from parsed mastodon search """

    if mastodonOK:
        buffered = []
        hashtagResult = mastodon.timeline_hashtag(query_feed)

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


@app.route('/toot_favorites')
def toot_favorites_feed():
    """ generate an rss feed authenticated user's favorites """

    if mastodonOK:
        buffered = []
        favorite_toots = mastodon.favourites()
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


if __name__ == "__main__":
    app.run(use_reloader=True)
