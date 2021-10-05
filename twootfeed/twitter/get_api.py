import tweepy


def get_twitter_api(param, app_log):
    twitter_api = None

    try:
        consumer_key = param['twitter']['consumerKey']
        consumer_secret = param['twitter']['consumerSecret']

        if consumer_key != '' and consumer_secret != '':
            auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
            twitter_api = tweepy.API(auth, wait_on_rate_limit=True)

        else:
            app_log.warning(
                'Twitter API: no consumer key and or consumer '
                'secret in config file.'
            )
    except Exception as e:
        app_log.error(f'Twitter API: invalid config file ({e})')

    return twitter_api
