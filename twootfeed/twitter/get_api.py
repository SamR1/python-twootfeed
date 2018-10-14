import tweepy


def get_twitter_api(param, app_log):
    twitter_api = None

    consumer_key = param['twitter']['consumerKey']
    consumer_secret = param['twitter']['consumerSecret']

    if consumer_key != '' and consumer_secret != '':
        try:
            auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
            twitter_api = tweepy.API(auth, wait_on_rate_limit=True)
        except Exception as e:
            app_log.error('Twitter API: ' + str(e))
    else:
        app_log.warning('Twitter API: no consumer key and or consumer secret '
                        'in config file.')
    return twitter_api
