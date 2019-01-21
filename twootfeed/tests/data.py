invalid_param = {
    'twitter':
        {
            'consumerKey': '',
            'consumerSecret': '',
            'title': 'Recherche Twitter : ',
            'link': 'https://twitter.com/search?q=',
            'description': 'Résultat d\'une recherche Twitter retournée dans'
                           ' un flux RSS via Tweepy.'
        },
    'mastodon':
        {
            'url': 'https://mastodon.social',
            'client_id_file': 'tootrss_clientcred_invalid.txt',
            'access_token_file': 'tootrss_clientcred_invalid.txt',
            'app_name': 'tootrss',
            'title': 'Recherche Mastodon : ',
            'description': 'Résultat d\'une recherche Mastodon retournée dans'
                           ' un flux RSS.'
        },
    'feed':
        {
            'language': 'fr',
            'author_name': '',
            'feed_url': 'http://localhost:5000/',
            'timezone': 'Europe/Paris',
            'text_length_limit': 100
        }
}

# minimal structure
tweet_1 = {
    'created_at': 'Thu Apr 06 15:24:15 +0000 2017',
    'id_str': '850006245121695744',
    'full_text': 'We are sharing our vision for the future of the Twitter API',
    'user': {
        'id': 2244994945,
        'name': 'Twitter Dev',
        'screen_name': 'TwitterDev',
        'location': 'Internet',
        'url': 'https://dev.twitter.com',
        'description': 'Your official source for Twitter Platform news'
    },
    'place': {},
    'entities': {
        'hashtags': [],
        'urls': [],
        'user_mentions': []
    }
}
formatted_tweet_1 = {
    'text': 'We are sharing our vision for the future of the Twitter API',
    'user_name': 'Twitter Dev',
    'screen_name': 'TwitterDev',
    'created_at': 'Thu Apr 06 15:24:15 +0000 2017',
    'tweet_url': 'https://twitter.com/TwitterDev/status/850006245121695744',
    'htmltext': '<blockquote><div><img src="None" '
                'alt="TwitterDevprofile image"/> '
                '<strong>Twitter Dev: </strong>We are sharing our vision for '
                'the future of the Twitter API<br>'
                '<i>Source: None</i><br><i>Location: None</i><br>'
                ' ♻ : None, ♥ : None</div></blockquote>'
}

# full tweet
tweet_2 = {
    'created_at': 'Fri Jan 18 08:00:25 +0000 2019',
    'id': 1111111111111111111,
    'id_str': '1111111111111111111',
    'full_text': 'tweet #test cc @userB @userC #opensource \n\n'
                 'https://t.co/AAAAAAAAAA https://t.co/BBBBBBBBBB',
    'truncated': False,
    'display_text_range': [0, 93],
    'entities': {
        'hashtags':
            [
                {'text': 'test', 'indices': [6, 11]},
                {'text': 'opensource', 'indices': [29, 40]},
            ],
        'symbols': [],
        'user_mentions':
            [
                {
                    'screen_name': 'userB',
                    'name': 'User B',
                    'id': 2222222222222,
                    'id_str': '2222222222222',
                    'indices': [15, 21]
                },
                {
                    'screen_name': 'userC',
                    'name': 'User C',
                    'id': 3333333333333,
                    'id_str': '3333333333333',
                    'indices': [22, 28]
                }
            ],
        'urls':
            [
                {
                    'url': 'https://t.co/AAAAAAAAAA',
                    'expanded_url': 'https://www.example.com/test/'
                                    'this-is-an-example',
                    'display_url': 'example.com/test/this-is-…',
                    'indices': [45, 68]
                }
            ],
        'media':
            [
                {
                    'id': 9999999999999999999,
                    'id_str': '9999999999999999999',
                    'indices': [69, 92],
                    'media_url': 'http://pbs.twimg.com/media/'
                                 'DxDxDxDxDxDxDxD.jpg',
                    'media_url_https': 'https://pbs.twimg.com/media/'
                                       'DxDxDxDxDxDxDxD.jpg',
                    'url': 'https://t.co/BBBBBBBBBB',
                    'display_url': 'pic.twitter.com/pictwitter',
                    'expanded_url': 'https://twitter.com/UserA/status/'
                                    '1111111111111111111/photo/1',
                    'type': 'photo',
                    'sizes': {
                        'large': {'w': 2048, 'h': 1448, 'resize': 'fit'},
                        'thumb': {'w': 150, 'h': 150, 'resize': 'crop'},
                        'small': {'w': 680, 'h': 481, 'resize': 'fit'},
                        'medium': {'w': 1200, 'h': 848, 'resize': 'fit'}
                    }
                }
            ]
    },
    'extended_entities':
        {
            'media':
                [
                    {
                        'id': 9999999999999999999,
                        'id_str': '9999999999999999999',
                        'indices': [69, 92],
                        'media_url': 'http://pbs.twimg.com/media/'
                                     'DxDxDxDxDxDxDxD.jpg',
                        'media_url_https': 'https://pbs.twimg.com/media/'
                                           'DxDxDxDxDxDxDxD.jpg',
                        'url': 'https://t.co/BBBBBBBBBB',
                        'display_url': 'pic.twitter.com/pictwitter',
                        'expanded_url': 'https://twitter.com/UserA/status/'
                                        '1111111111111111111/photo/1',
                        'type': 'photo',
                        'sizes': {
                            'large': {'w': 2048, 'h': 1448, 'resize': 'fit'},
                            'thumb': {'w': 150, 'h': 150, 'resize': 'crop'},
                            'small': {'w': 680, 'h': 481, 'resize': 'fit'},
                            'medium': {'w': 1200, 'h': 848, 'resize': 'fit'}
                        }
                    },
                    {
                        'id': 8888888888888888888,
                        'id_str': '8888888888888888888',
                        'indices': [69, 92],
                        'media_url': 'http://pbs.twimg.com/media/'
                                     'xDxDxDxDxDxDxDx.jpg',
                        'media_url_https': 'https://pbs.twimg.com/media/'
                                           'xDxDxDxDxDxDxDx.jpg',
                        'url': 'https://t.co/BBBBBBBBBB',
                        'display_url': 'pic.twitter.com/pictwitter',
                        'expanded_url': 'https://twitter.com/UserA/status/'
                                        '1111111111111111111/photo/1',
                        'type': 'photo',
                        'sizes': {
                            'thumb': {'w': 150, 'h': 150, 'resize': 'crop'},
                            'medium': {'w': 1200, 'h': 848, 'resize': 'fit'},
                            'large': {'w': 2048, 'h': 1447, 'resize': 'fit'},
                            'small': {'w': 680, 'h': 481, 'resize': 'fit'}
                        }
                    }
                ]
        },
    'metadata': {
        'iso_language_code': 'fr',
        'result_type': 'recent'
    },
    'source': '<a href="https://example.com/" rel="nofollow">'
              'Twitter for Android</a>',
    'in_reply_to_status_id': None,
    'in_reply_to_status_id_str': None,
    'in_reply_to_user_id': None,
    'in_reply_to_user_id_str': None,
    'in_reply_to_screen_name': None,
    'user': {
        'id': 20901996,
        'id_str': '20901996',
        'name': 'User A',
        'screen_name': 'UserA',
        'location': '',
        'description': 'just a user!',
        'url': 'https://t.co/xxxxxxxxxx',
        'entities': {
            'url': {
                'urls':
                    [
                        {'url': 'https://t.co/xxxxxxxxxx',
                         'expanded_url': 'https://github.com/UserA',
                         'display_url': 'github.com/UserA',
                         'indices': [0, 23]
                         }
                    ]
            },
            'description': {
                'urls': []
            }
        },
        'protected': False,
        'followers_count': 10000,
        'friends_count': 100,
        'listed_count': 10,
        'created_at': 'Sun Feb 15 10:31:50 +0000 2009',
        'favourites_count': 5555,
        'utc_offset': None,
        'time_zone': None,
        'geo_enabled': True,
        'verified': False,
        'statuses_count': 9999,
        'lang': 'fr',
        'contributors_enabled': False,
        'is_translator': False,
        'is_translation_enabled': False,
        'profile_background_color': '000000',
        'profile_background_image_url': 'http://abs.twimg.com/images/themes/'
                                        'theme14/bg.gif',
        'profile_background_image_url_https': 'https://abs.twimg.com/images/'
                                              'themes/theme14/bg.gif',
        'profile_background_tile': False,
        'profile_image_url': 'http://pbs.twimg.com/profile_images/'
                             'xxxxxxxxxxxxxxxxxxxxxxxxxxxx_normal.jpg',
        'profile_image_url_https': 'https://pbs.twimg.com/profile_images/'
                                   'xxxxxxxxxxxxxxxxxxxxxxxxxxxx_normal.jpg',
        'profile_banner_url': 'https://pbs.twimg.com/profile_banners/'
                              'xxxxxxxx/xxxxxxxxxx',
        'profile_link_color': '575757',
        'profile_sidebar_border_color': 'FFFFFF',
        'profile_sidebar_fill_color': 'EFEFEF',
        'profile_text_color': '333333',
        'profile_use_background_image': True,
        'has_extended_profile': False,
        'default_profile': False,
        'default_profile_image': False,
        'following': None,
        'follow_request_sent': None,
        'notifications': None,
        'translator_type': 'none'
    },
    'geo': None,
    'coordinates': None,
    'place': None,
    'contributors': None,
    'is_quote_status': False,
    'retweet_count': 4,
    'favorite_count': 8,
    'favorited': False,
    'retweeted': False,
    'possibly_sensitive': False,
    'lang': 'fr'
}
formatted_tweet_2 = {
    'text': 'tweet #test cc @userB @userC #opensource \n\nhttps://t.co/AAAAAAAAAA https://t.co/BBBBBBBBBB',  # noqa
    'user_name': 'User A',
    'screen_name': 'UserA',
    'created_at': 'Fri Jan 18 08:00:25 +0000 2019',
    'tweet_url': 'https://twitter.com/UserA/status/1111111111111111111',
    'htmltext': '<blockquote>'
                '<div>'
                '<img src="https://pbs.twimg.com/profile_images/xxxxxxxxxxxxxxxxxxxxxxxxxxxx_normal.jpg" alt="UserAprofile image"/> '  # noqa
                '<strong>User A: </strong>'
                'tweet <a href="https://twitter.com/hashtag/test?src=hash" target="_blank">#test</a> '  # noqa
                'cc '
                '<a href="https://twitter.com/userB" target="_blank">@userB</a> '  # noqa
                '<a href="https://twitter.com/userC" target="_blank">@userC</a> '  # noqa
                '<a href="https://twitter.com/hashtag/opensource?src=hash" target="_blank">#opensource</a> \n\n'  # noqa
                '<a href="https://www.example.com/test/this-is-an-example" target="_blank">example.com/test/this-is-…</a> <br>'  # noqa
                '<i>Source: <a href="https://example.com/" rel="nofollow">Twitter for Android</a></i><br> '  # noqa
                '<a href="https://pbs.twimg.com/media/DxDxDxDxDxDxDxD.jpg" target="_blank"><img src="https://pbs.twimg.com/media/DxDxDxDxDxDxDxD.jpg:thumb"></a>'  # noqa
                '<a href="https://pbs.twimg.com/media/xDxDxDxDxDxDxDx.jpg" target="_blank"><img src="https://pbs.twimg.com/media/xDxDxDxDxDxDxDx.jpg:thumb"></a><br>'  # noqa
                ' ♻ : 4, ♥ : 8'
                '</div>'
                '</blockquote>'
}
