#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from flask import Flask
import feedgenerator
import pytz
import re
import tweepy
import yaml


app = Flask(__name__)
app.debug = True


with open('config.yml', 'r') as stream:
    try:
        param = yaml.load(stream)
    except yaml.YAMLError as e:
        print(e)


@app.route('/<query_feed>')
def rssfeed(query_feed):
    """ generate a rss feed from parsed twitter search """

    consumerKey = param['twitter']['consumerKey']
    consumerSecret = param['twitter']['consumerSecret']

    auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
    api = tweepy.API(auth)

    tweet = {}
    buffered = []

    for i in tweepy.Cursor(api.search, q=query_feed).items():
        try:
            a = i.text
            print(i)
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
                tweet['profile_image_url'] = i.user.profile_image_url
                tweet['user_name'] = i.user.name
                tweet['user_url'] = i.user.url
                tweet['id_str'] = i.id_str
                tweet['created_at'] = i.created_at
                tweet['retweets'] = i.retweet_count
                tweet['favorites'] = i.favorite_count
                tweet['tweet_url'] = 'https://twitter.com/' + tweet['user_name'] + '/status/' + tweet['id_str']

                tweet['htmltext'] = '<blockquote><div><img src="' + tweet['profile_image_url'] + \
                                    '" alt="' + tweet['screen_name'] + \
                                    '" />  <strong>' + tweet['user_name'] + \
                                    ': </strong>' + tweet['text']

                user_mentionslist = i.entities.get('user_mentions')
                for j in user_mentionslist:
                    if j != '':
                        tweet['htmltext'] = re.sub(('@' + j.get('screen_name')),
                                                   ('<a href="https://twitter.com/' + j.get(
                                                       'screen_name') + '" target="_blank">@' + j.get(
                                                       'screen_name') + '</a>'),
                                                   tweet['htmltext'])

                hashtaglist = i.entities.get('hashtags')
                for j in hashtaglist:
                    if j != '':
                        tweet['htmltext'] = re.sub(('#' + j.get('text')),
                                                   ('<a href="https://twitter.com/hashtag/' + j.get(
                                                       'text') + '?src=hash" target="_blank">#' + j.get(
                                                       'text') + '</a>'),
                                                   tweet['htmltext'])

                urllist = i.entities.get('urls')
                for j in urllist:
                    if j != '':
                        tweet['htmltext'] = re.sub((j.get('url')),
                                                   ('<a href="' + j.get('expanded_url') + '" target="_blank">' + j.get(
                                                       'display_url') + '</a>'),
                                                   tweet['htmltext'])

                medialist = i.entities.get('media')
                if medialist != None:
                    for j in medialist:
                        if j != '':
                            if (j.get('type') == 'photo'):
                                tweet['htmltext'] = re.sub(j.get('url'), '', tweet['htmltext'])
                                tweet['htmltext'] = tweet['htmltext'] + '<br><img src="' + j.get('media_url') + '"> '

                tweet['htmltext'] = tweet['htmltext'] + '<br> ♻️ : ' + str(tweet['retweets']) + ', ' + '✰ : ' + str(
                    tweet['favorites']) + '</blockquote>'

                buffered.append(tweet.copy())

    utc = pytz.utc
    f = feedgenerator.Rss201rev2Feed(title="Flux RSS - Recherche Twitter",
                                     link="http://www.twitter.com/",
                                     description="Résultat d'une recherche Twitter, retournée dans un flux RSS via Tweepy",
                                     language="fr",
                                     author_name="Moi",
                                     feed_url="http://localhost:8000/feed/rssfeed/")

    for tweet in buffered:
        f.add_item(title=tweet['screen_name'] + ' (' + tweet['user_name'] + '): ' + tweet['text'],
                   link=tweet['tweet_url'],
                   pubdate=utc.localize(tweet['created_at']).astimezone(pytz.timezone('Europe/Paris')),
                   description=tweet['htmltext'])

    xml = f.writeString('UTF-8')

    return xml


if __name__ == "__main__":
    app.run()
