import re

import pytz
import tweepy
from twootfeed.utils.feed_generation import generate_feed


def format_tweet(tweet):
    rss_tweet = {
        'text': tweet.full_text,
        'user_name': tweet.user.name,
        'screen_name': tweet.user.screen_name,
        'created_at': tweet.created_at,
        'tweet_url': 'https://twitter.com/{}/status/{}'.format(
            tweet.user.screen_name, tweet.id_str
        ),
        'htmltext': (
            '<blockquote><div><img src="{}" alt="{}'.format(
                tweet.user.profile_image_url_https, tweet.user.screen_name
            )
            + ' profile image"/> <strong>{}: </strong>{}<br><i>'.format(
                tweet.user.name, tweet.full_text
            )
            + 'Source: {}</i>'.format(tweet.source)
        ),
    }

    user_mentionslist = tweet.entities.get('user_mentions')
    for user in user_mentionslist:
        if user != '':
            screen_name = user.get('screen_name')
            rss_tweet['htmltext'] = re.sub(
                '@' + user.get('screen_name'),
                (
                    f'<a href="https://twitter.com/{screen_name}" '
                    f'target="_blank">@{screen_name}</a>'
                ),
                rss_tweet['htmltext'],
            )

    hashtaglist = tweet.entities.get('hashtags')
    for hashtag in hashtaglist:
        if hashtag != '':
            tag = hashtag.get('text')
            rss_tweet['htmltext'] = re.sub(
                '#' + hashtag.get('text'),
                (
                    '<a href="https://twitter.com/hashtag/{}'.format(tag)
                    + '?src=hash" target="_blank">#{}</a>'.format(tag)
                ),
                rss_tweet['htmltext'],
            )

    urllist = tweet.entities.get('urls')
    for url in urllist:
        if url != '':
            rss_tweet['htmltext'] = re.sub(
                url.get('url'),
                '<a href="{}" target="_blank">{}</a>'.format(
                    url.get('expanded_url'), url.get('display_url')
                ),
                rss_tweet['htmltext'],
            )
    try:
        medialist = tweet.extended_entities.get('media')
    except AttributeError:
        pass
    else:
        if medialist is not None:
            rss_tweet['htmltext'] = rss_tweet['htmltext'] + '<br> '
            for media in medialist:
                if media != '':
                    if media.get('type') == 'photo':
                        media_url = media.get('media_url_https')
                        rss_tweet['htmltext'] = re.sub(
                            media.get('url'), '', rss_tweet['htmltext']
                        )
                        rss_tweet['htmltext'] += (
                            '<a href="{}" '.format(media_url)
                            + 'target="_blank"><img src="{}'.format(media_url)
                            + ':thumb"></a>'
                        )

    location = tweet.place
    if location is not None:
        rss_tweet['htmltext'] += '<br><i>Location: {}</i>'.format(
            location.full_name
        )

    rss_tweet['htmltext'] += '<br> ♻ : {}, ♥ : {}</div></blockquote>'.format(
        tweet.retweet_count, tweet.favorite_count
    )

    return rss_tweet


def generate_twitter_feed(api, query_feed, twitter_param):
    feed_title = twitter_param['twitter']['title'] + '"' + query_feed + '"'
    feed_link = twitter_param['twitter']['link'] + query_feed
    f = generate_feed(feed_title, feed_link, twitter_param)

    # https://developer.twitter.com/en/docs/tweets/search/api-reference/get-search-tweets.html  # noqa
    result = tweepy.Cursor(
        api,
        q=query_feed,
        tweet_mode='extended',  # to get tweet.full_text
        result_type='recent',
    )  # default is 'mixed'

    max_tweets = twitter_param['feed']['max_items']
    tweet_index = 0
    end_search = False

    for page in result.pages():
        if end_search:
            break

        for tweet in page:
            retweeted_status = getattr(tweet, 'retweeted_status', False)
            if not retweeted_status:  # only the original tweets
                tweet_index += 1
                if tweet_index > max_tweets:
                    end_search = True
                    break

                formatted_tweet = format_tweet(tweet)
                f.add_item(
                    title=formatted_tweet['user_name']
                    + ' ('
                    + formatted_tweet['screen_name']
                    + '): '
                    + formatted_tweet['text'],
                    link=formatted_tweet['tweet_url'],
                    pubdate=formatted_tweet['created_at'].astimezone(
                        pytz.timezone(twitter_param['feed']['timezone'])
                    ),
                    description=formatted_tweet['htmltext'],
                )

    return f.writeString('UTF-8')


def generate_xml(api, query_feed, param):
    if api:
        xml = generate_twitter_feed(api.search_tweets, query_feed, param)
        code = 200
    else:
        xml = 'error - Twitter parameters not defined'
        code = 401
    return xml, code
