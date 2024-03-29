import secrets
from copy import deepcopy
from datetime import datetime
from typing import Dict

import pytz

TEST_TOKEN = secrets.token_urlsafe()
max_items = 20

init_param: Dict = {
    'twitter': {
        'consumerKey': '',
        'consumerSecret': '',
        'title': 'Twitter Search Feed:',
        'link': 'https://twitter.com/search?q=',
        'description': 'Twitter search results.',
    },
    'mastodon': {
        'url': 'https://mastodon.social',
        'client_id_file': 'tootrss_clientcred.txt',
        'access_token_file': 'tootrss_usercred.txt',
        'app_name': 'tootrss',
        'title': 'Mastodon Feed:',
        'description': 'Mastodon generated feed from search.',
    },
    'feed': {
        'language': 'fr',
        'author_name': '',
        'feed_url': 'http://localhost:8080',
        'timezone': 'Europe/Paris',
        'text_length_limit': 100,
        'max_items': max_items,
        'token': TEST_TOKEN,
    },
    'app': {'host': 'localhost', 'port': '8080', 'nb_workers': 2},
}

invalid_param: Dict = deepcopy(init_param)
invalid_param['mastodon']['client_id_file'] = 'tootrss_clientcred_invalid.txt'
invalid_param['mastodon']['access_token_file'] = 'tootrss_usercred_invalid.txt'

invalid_param_api: Dict = deepcopy(invalid_param)
invalid_param_api['twitter'] = None
invalid_param_api['mastodon'] = None

# minimal structure
tweet_1 = {
    'created_at': datetime(2017, 4, 6, 15, 24, 15, tzinfo=pytz.UTC),
    'id': 850006245121695744,
    'id_str': '850006245121695744',
    'full_text': 'We are sharing our vision for the future of the Twitter API',
    'user': {
        'id': 2244994945,
        'name': 'Twitter Dev',
        'screen_name': 'TwitterDev',
        'location': 'Internet',
        'url': 'https://dev.twitter.com',
        'profile_image_url_https': '',
    },
    'place': {},
    'source': '',
    'entities': {'hashtags': [], 'urls': [], 'user_mentions': []},
    'retweet_count': 0,
    'favorite_count': 0,
}

retweet = tweet_1.copy()
retweet['retweeted_status'] = True

tweet_no_full_text = tweet_1.copy()
tweet_no_full_text['text'] = tweet_no_full_text['full_text']
tweet_no_full_text.pop('full_text', None)


formatted_tweet_1 = {
    'text': 'We are sharing our vision for the future of the Twitter API',
    'user_name': 'Twitter Dev',
    'screen_name': 'TwitterDev',
    'created_at': datetime(2017, 4, 6, 15, 24, 15, tzinfo=pytz.UTC),
    'tweet_url': 'https://twitter.com/TwitterDev/status/850006245121695744',
    'htmltext': '<blockquote><div><img src="" '
    'alt="TwitterDev profile image" style="border-radius: 50%;"/> '
    '<strong>Twitter Dev </strong>We are sharing our vision for '
    'the future of the Twitter API<br>'
    '<i>Source: </i><br><i>Location: None</i><br>'
    ' ♻ : 0, ♥ : 0</div></blockquote>',
}
tweet_1_feed = (
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<rss version="2.0">'
    '<channel>'
    '<title>Twitter Search Feed: "test"</title>'
    '<link>https://twitter.com/search?q=test</link>'
    '<description>Twitter search results.</description>'
    '<language>fr</language>'
    '<lastBuildDate></lastBuildDate>'
    '<item>'
    '<title>Twitter Dev (TwitterDev): We are sharing our vision for the '
    'future of the Twitter API</title>'
    '<link>https://twitter.com/TwitterDev/status/850006245121695744</link>'
    '<description>&lt;blockquote&gt;&lt;div&gt;&lt;img src="" '
    'alt="TwitterDev profile image" style="border-radius: 50%;"/&gt; '
    '&lt;strong&gt;Twitter Dev '
    '&lt;/strong&gt;We are sharing our vision for the future of the Twitter '
    'API&lt;br&gt;&lt;i&gt;Source: &lt;/i&gt;&lt;br&gt;&lt;i&gt;Location: '
    'None&lt;/i&gt;&lt;br&gt; ♻ : 0, ♥ : 0&lt;/div&gt;&lt;/blockquote&gt;'
    '</description>'
    '<pubDate>Thu, 06 Apr 2017 17:24:15 +0200</pubDate>'
    '</item>'
    '</channel>'
    '</rss>'
)

tweet_20_feed = (
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<rss version="2.0">'
    '<channel>'
    '<title>Twitter Search Feed: "test"</title>'
    '<link>https://twitter.com/search?q=test</link>'
    '<description>Twitter search results.</description>'
    '<language>fr</language>'
    '<lastBuildDate></lastBuildDate>'
    + (
        '<item>'
        '<title>Twitter Dev (TwitterDev): We are sharing our vision for the '
        'future of the Twitter API</title>'
        '<link>https://twitter.com/TwitterDev/status/850006245121695744</link>'
        '<description>&lt;blockquote&gt;&lt;div&gt;&lt;img src="" '
        'alt="TwitterDev profile image" style="border-radius: 50%;"/&gt; '
        '&lt;strong&gt;Twitter Dev '
        '&lt;/strong&gt;We are sharing our vision for the future of the '
        'Twitter '
        'API&lt;br&gt;&lt;i&gt;Source: &lt;/i&gt;&lt;br&gt;&lt;i&gt;Location: '
        'None&lt;/i&gt;&lt;br&gt; ♻ : 0, ♥ : 0&lt;/div&gt;&lt;/blockquote&gt;'
        '</description>'
        '<pubDate>Thu, 06 Apr 2017 17:24:15 +0200</pubDate>'
        '</item>'
    )
    * max_items
    + '</channel>'
    '</rss>'
)

# full tweet
tweet_2 = {
    'created_at': datetime(2019, 1, 18, 8, 0, 25, tzinfo=pytz.UTC),
    'id': 1111111111111111111,
    'id_str': '1111111111111111111',
    'full_text': 'tweet #test cc @userB @userC #opensource \n\n'
    'https://t.co/AAAAAAAAAA https://t.co/BBBBBBBBBB',
    'truncated': False,
    'display_text_range': [0, 93],
    'entities': {
        'hashtags': [
            {'text': 'test', 'indices': [6, 11]},
            {'text': 'opensource', 'indices': [29, 40]},
        ],
        'symbols': [],
        'user_mentions': [
            {
                'screen_name': 'userB',
                'name': 'User B',
                'id': 2222222222222,
                'id_str': '2222222222222',
                'indices': [15, 21],
            },
            {
                'screen_name': 'userC',
                'name': 'User C',
                'id': 3333333333333,
                'id_str': '3333333333333',
                'indices': [22, 28],
            },
        ],
        'urls': [
            {
                'url': 'https://t.co/AAAAAAAAAA',
                'expanded_url': 'https://www.example.com/test/'
                'this-is-an-example',
                'display_url': 'example.com/test/this-is-…',
                'indices': [45, 68],
            }
        ],
        'media': [
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
                    'medium': {'w': 1200, 'h': 848, 'resize': 'fit'},
                },
            },
            {
                "id": 8888888888888888888,
                "id_str": "8888888888888888888",
                "indices": [237, 260],
                "media_url": "http://pbs.twimg.com/ext_tw_video_thumb/"
                "1212121212121212121/pu/img/DxDxDxDxDxDxDxD.jpg",
                "media_url_https": "https://pbs.twimg.com/ext_tw_video_thumb/"
                "1212121212121212121/pu/img/"
                "DxDxDxDxDxDxDxD.jpg",
                "url": "https://t.co/AAAAAAAAAA",
                "display_url": "pic.twitter.com/AAAAAAAAAA",
                "expanded_url": "https://twitter.com/CROSHDF/status/"
                "1212121212121212121/video/1",
                "type": "video",
                "sizes": {
                    "thumb": {"w": 150, "h": 150, "resize": "crop"},
                    "small": {"w": 383, "h": 680, "resize": "fit"},
                    "medium": {"w": 675, "h": 1200, "resize": "fit"},
                    "large": {"w": 1080, "h": 1920, "resize": "fit"},
                },
            },
            {
                "id": 7777777777777777777,
                "id_str": "7777777777777777777",
                "indices": [67, 90],
                "media_url": "http://pbs.twimg.com/tweet_video_thumb/"
                "DDDDDDDDDDDDDDD.jpg",
                "media_url_https": "https://pbs.twimg.com/tweet_video_thumb/"
                "DDDDDDDDDDDDDDD.jpg",
                "url": "https://t.co/CCCCCCCCCC",
                "display_url": "pic.twitter.com/ETn6mEs0vP",
                "expanded_url": "https://twitter.com/UserA/status/"
                "7777777777777777777/photo/1",
                "type": "animated_gif",
                "sizes": {
                    "small": {"w": 498, "h": 448, "resize": "fit"},
                    "thumb": {"w": 150, "h": 150, "resize": "crop"},
                    "large": {"w": 498, "h": 448, "resize": "fit"},
                    "medium": {"w": 498, "h": 448, "resize": "fit"},
                },
            },
        ],
    },
    'extended_entities': {
        'media': [
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
                    'medium': {'w': 1200, 'h': 848, 'resize': 'fit'},
                },
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
                    'small': {'w': 680, 'h': 481, 'resize': 'fit'},
                },
            },
            {
                "id": 8888888888888888888,
                "id_str": "8888888888888888888",
                "indices": [237, 260],
                "media_url": "http://pbs.twimg.com/ext_tw_video_thumb/"
                "1212121212121212121/pu/img/DxDxDxDxDxDxDxD.jpg",
                "media_url_https": "https://pbs.twimg.com/ext_tw_video_thumb/"
                "1212121212121212121/pu/img/"
                "DxDxDxDxDxDxDxD.jpg",
                "url": "https://t.co/AAAAAAAAAA",
                "display_url": "pic.twitter.com/AAAAAAAAAA",
                "expanded_url": "https://twitter.com/CROSHDF/status/"
                "1212121212121212121/video/1",
                "type": "video",
                "sizes": {
                    "thumb": {"w": 150, "h": 150, "resize": "crop"},
                    "small": {"w": 383, "h": 680, "resize": "fit"},
                    "medium": {"w": 675, "h": 1200, "resize": "fit"},
                    "large": {"w": 1080, "h": 1920, "resize": "fit"},
                },
                "video_info": {
                    "aspect_ratio": [9, 16],
                    "duration_millis": 56704,
                    "variants": [
                        {
                            "content_type": "application/x-mpegURL",
                            "url": "https://video.twimg.com/ext_tw_video/"
                            "1212121212121212121/pu/pl/ttEz4_ebdrQaB5EW"
                            ".m3u8?tag=12&container=fmp4",
                        },
                        {
                            "bitrate": 950000,
                            "content_type": "video/mp4",
                            "url": "https://video.twimg.com/ext_tw_video/"
                            "1212121212121212121/pu/vid/480x852/"
                            "eVydKjMo5pY7qWYj.mp4?tag=12",
                        },
                        {
                            "bitrate": 632000,
                            "content_type": "video/mp4",
                            "url": "https://video.twimg.com/ext_tw_video/"
                            "1212121212121212121/pu/vid/320x568/"
                            "S5c9t3ytXZ5UJ9Ag.mp4?tag=12",
                        },
                        {
                            "bitrate": 2176000,
                            "content_type": "video/mp4",
                            "url": "https://video.twimg.com/ext_tw_video/"
                            "1212121212121212121/pu/vid/720x1280/"
                            "NuzHqlk2lXf2AFFI.mp4?tag=12",
                        },
                    ],
                },
                "additional_media_info": {"monetizable": False},
            },
            {
                "id": 7777777777777777777,
                "id_str": "7777777777777777777",
                "indices": [67, 90],
                "media_url": "http://pbs.twimg.com/tweet_video_thumb/"
                "DDDDDDDDDDDDDDD.jpg",
                "media_url_https": "https://pbs.twimg.com/tweet_video_thumb/"
                "DDDDDDDDDDDDDDD.jpg",
                "url": "https://t.co/CCCCCCCCCC",
                "display_url": "pic.twitter.com/ETn6mEs0vP",
                "expanded_url": "https://twitter.com/UserA/status/"
                "7777777777777777777/photo/1",
                "type": "animated_gif",
                "sizes": {
                    "small": {"w": 498, "h": 448, "resize": "fit"},
                    "thumb": {"w": 150, "h": 150, "resize": "crop"},
                    "large": {"w": 498, "h": 448, "resize": "fit"},
                    "medium": {"w": 498, "h": 448, "resize": "fit"},
                },
                "video_info": {
                    "aspect_ratio": [249, 224],
                    "variants": [
                        {
                            "bitrate": 0,
                            "content_type": "video/mp4",
                            "url": "https://video.twimg.com/tweet_video/"
                            "DDDDDDDDDDDDDDD.mp4",
                        }
                    ],
                },
            },
        ]
    },
    'metadata': {'iso_language_code': 'fr', 'result_type': 'recent'},
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
                'urls': [
                    {
                        'url': 'https://t.co/xxxxxxxxxx',
                        'expanded_url': 'https://github.com/UserA',
                        'display_url': 'github.com/UserA',
                        'indices': [0, 23],
                    }
                ]
            },
            'description': {'urls': []},
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
        'translator_type': 'none',
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
    'lang': 'fr',
}
formatted_tweet_2 = {
    'text': 'tweet #test cc @userB @userC #opensource \n\nhttps://t.co/AAAAAAAAAA https://t.co/BBBBBBBBBB',  # noqa
    'user_name': 'User A',
    'screen_name': 'UserA',
    'created_at': datetime(2019, 1, 18, 8, 0, 25, tzinfo=pytz.UTC),
    'tweet_url': 'https://twitter.com/UserA/status/1111111111111111111',
    'htmltext': '<blockquote>'
    '<div>'
    '<img src="https://pbs.twimg.com/profile_images/xxxxxxxxxxxxxxxxxxxxxxxxxxxx_normal.jpg" alt="UserA profile image" style="border-radius: 50%;"/> '  # noqa
    '<strong>User A </strong>'
    'tweet <a href="https://twitter.com/hashtag/test?src=hash" target="_blank">#test</a> '  # noqa
    'cc '
    '<a href="https://twitter.com/userB" target="_blank">@userB</a> '  # noqa
    '<a href="https://twitter.com/userC" target="_blank">@userC</a> '  # noqa
    '<a href="https://twitter.com/hashtag/opensource?src=hash" target="_blank">#opensource</a> \n\n'  # noqa
    '<a href="https://www.example.com/test/this-is-an-example" target="_blank">example.com/test/this-is-…</a> <br>'  # noqa
    '<i>Source: <a href="https://example.com/" rel="nofollow">Twitter for Android</a></i><br> '  # noqa
    '<a href="https://pbs.twimg.com/media/DxDxDxDxDxDxDxD.jpg" target="_blank"><img src="https://pbs.twimg.com/media/DxDxDxDxDxDxDxD.jpg:thumb"></a>'  # noqa
    '<a href="https://pbs.twimg.com/media/xDxDxDxDxDxDxDx.jpg" target="_blank"><img src="https://pbs.twimg.com/media/xDxDxDxDxDxDxDx.jpg:thumb"></a>'  # noqa
    '<video controls><source src="https://video.twimg.com/ext_tw_video/1212121212121212121/pu/vid/320x568/S5c9t3ytXZ5UJ9Ag.mp4?tag=12" '  # noqa
    'poster="https://pbs.twimg.com/ext_tw_video_thumb/1212121212121212121/pu/img/DxDxDxDxDxDxDxD.jpg">'  # noqa
    'Your browser does not support the video tag.</video> '
    '<video autoplay loop muted inline><source src="https://video.twimg.com/tweet_video/DDDDDDDDDDDDDDD.mp4" '  # noqa
    'poster="https://pbs.twimg.com/tweet_video_thumb/DDDDDDDDDDDDDDD.jpg">'
    'Your browser does not support the video tag.</video> <br>'
    ' ♻ : 4, ♥ : 8'
    '</div>'
    '</blockquote>',
}

empty_feed = (
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<rss version="2.0">'
    '<channel>'
    '<title>Twitter Search Feed: "test"</title>'
    '<link>https://twitter.com/search?q=test</link>'
    '<description>Twitter search results.</description>'
    '<language>fr</language>'
    '<lastBuildDate></lastBuildDate></channel></rss>'
)

empty_feed_with_no_index = (
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<rss version="2.0">'
    '<channel>'
    '<xhtml:meta xmlns:xhtml="http://www.w3.org/1999/xhtml" '
    'name="robots" content="noindex" />'
    '<title>Twitter Search Feed: "test"</title>'
    '<link>https://twitter.com/search?q=test</link>'
    '<description>Twitter search results.</description>'
    '<language>fr</language>'
    '<lastBuildDate></lastBuildDate></channel></rss>'
)

toot1 = {
    'id': 111111111111111111,
    'created_at': datetime(2018, 10, 25, 14, 16, 42, 11000),
    'in_reply_to_id': None,
    'in_reply_to_account_id': None,
    'sensitive': False,
    'spoiler_text': '',
    'visibility': 'public',
    'language': 'en',
    'uri': 'https://mastodon.social/users/UserD/statuses/111111111111111111',
    'content': '<p>What\'s New in <a href="https://linuxjobs.social/tags/'
    'python" class="mention hashtag" rel="nofollow noopener" '
    'target="_blank">#<span>python</span></a> today?</p>',
    'url': 'https://mastodon.social/@UserD/111111111111111111',
    'replies_count': 0,
    'reblogs_count': 0,
    'favourites_count': 0,
    'favourited': False,
    'reblogged': False,
    'muted': False,
    'pinned': False,
    'reblog': None,
    'application': {},
    'account': {
        'id': 00000,
        'username': 'UserD',
        'acct': 'UserD',
        'display_name': 'User',
        'locked': False,
        'bot': False,
        'created_at': datetime(2017, 4, 4, 9, 20, 43, 157000),
        'note': '',
        'url': 'https://mastodon.social/@UserD',
        'avatar': 'https://files.mastodon.social/accounts/avatars/000/000/000/original/DxDxDxDxDxDxDxDx.jpg',  # noqa
        'avatar_static': 'https://files.mastodon.social/accounts/avatars/000/000/000/original/DxDxDxDxDxDxDxDx.jpg',  # noqa
        'header': 'https://files.mastodon.social/accounts/headers/000/000/000/original/xDxDxDxDxDxDxDxD.jpg',  # noqa
        'header_static': 'https://files.mastodon.social/accounts/headers/000/000/000/original/xDxDxDxDxDxDxDxD.jpg',  # noqa
        'followers_count': 10,
        'following_count': 20,
        'statuses_count': 300,
        'emojis': [],
        'fields': [],
    },
    'media_attachments': [],
    'mentions': [],
    'tags': [],
    'emojis': [],
    'card': None,
}

formatted_toot1 = {
    'boosted': '',
    'display_name': 'User',
    'screen_name': 'UserD',
    'created_at': datetime(2018, 10, 25, 14, 16, 42, 11000),
    'url': 'https://mastodon.social/@UserD/111111111111111111',
    'htmltext': '<blockquote>'
    '<div>'
    '<img src="https://files.mastodon.social/accounts/avatars/000/000/000/original/DxDxDxDxDxDxDxDx.jpg" alt="User" width= 100px" style="border-radius: 50%;"/> '  # noqa
    '<strong>User </strong>'
    '<p>What\'s New in <a href="https://linuxjobs.social/tags/python" class="mention hashtag" rel="nofollow noopener" target="_blank">#<span>python</span></a> today?</p>'  # noqa
    '<br>♻ : 0, ✰ : 0, 🌐</div></blockquote>',
    'text': 'What\'s New in #python today?',
}
toot_1_feed = (
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<rss version="2.0">'
    '<channel>'
    '<title>Mastodon Feed: search "test"</title>'
    '<link>https://mastodon.social/web/timelines/tag/test</link><'
    'description>Mastodon generated feed from search.</description>'
    '<language>fr</language>'
    '<lastBuildDate></lastBuildDate>'
    '<item>'
    '<title>User (UserD): What\'s New in #python today?</title>'
    '<link>https://mastodon.social/@UserD/111111111111111111</link>'
    '<description>&lt;blockquote&gt;&lt;div&gt;&lt;img src="https://files.'
    'mastodon.social/accounts/avatars/000/000/000/original/DxDxDxDxDxDxDxDx'
    '.jpg" alt="User" width= 100px" style="border-radius: 50%;"/&gt; '
    '&lt;strong&gt;User &lt;/strong&gt'
    ';&lt;p&gt;What\'s New in &lt;a href="https://linuxjobs.social/tags/'
    'python" class="mention hashtag" rel="nofollow noopener" target="_blank'
    '"&gt;#&lt;span&gt;python&lt;/span&gt;&lt;/a&gt; today?&lt;/p&gt;&lt;br'
    '&gt;♻ : 0, ✰ : 0, 🌐&lt;/div&gt;&lt;/blockquote&gt;</description>'
    '<pubDate>Thu, 25 Oct 2018 16:16:42 +0200</pubDate>'
    '</item>'
    '</channel>'
    '</rss>'
)
toot_20_feed = (
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<rss version="2.0">'
    '<channel>'
    '<title>Mastodon Feed: search "test"</title>'
    '<link>https://mastodon.social/web/timelines/tag/test</link><'
    'description>Mastodon generated feed from search.</description>'
    '<language>fr</language>'
    '<lastBuildDate></lastBuildDate>'
    + (
        '<item>'
        '<title>User (UserD): What\'s New in #python today?</title>'
        '<link>https://mastodon.social/@UserD/111111111111111111</link>'
        '<description>&lt;blockquote&gt;&lt;div&gt;&lt;img src="https://files'
        '.mastodon.social/accounts/avatars/000/000/000/original/'
        'DxDxDxDxDxDxDxDx.jpg" alt="User" width= 100px" style="border-radius: '
        '50%;"/&gt; &lt;strong&gt;'
        'User &lt;/strong&gt;&lt;p&gt;What\'s New in &lt;a href="https://'
        'linuxjobs.social/tags/python" class="mention hashtag" rel="nofollow'
        ' noopener" target="_blank"&gt;#&lt;span&gt;python&lt;/span&gt;&lt;/a'
        '&gt; today?&lt;/p&gt;&lt;br&gt;♻ : 0, ✰ : 0, 🌐&lt;/div&gt;&lt;/'
        'blockquote&gt;</description>'
        '<pubDate>Thu, 25 Oct 2018 16:16:42 +0200</pubDate>'
        '</item>'
    )
    * max_items
    + '</channel>'
    '</rss>'
)
toot_1_bookmarks_feed = (
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<rss version="2.0">'
    '<channel>'
    '<xhtml:meta xmlns:xhtml="http://www.w3.org/1999/xhtml" '
    'name="robots" content="noindex" />'
    '<title>Mastodon Feed: Bookmarks</title>'
    '<link>https://mastodon.social/web/bookmarks</link><'
    'description> bookmarks toots.</description>'
    '<language>fr</language>'
    '<lastBuildDate></lastBuildDate>'
    '<item>'
    '<title>User (UserD): What\'s New in #python today?</title>'
    '<link>https://mastodon.social/@UserD/111111111111111111</link>'
    '<description>&lt;blockquote&gt;&lt;div&gt;&lt;img src="https://files.'
    'mastodon.social/accounts/avatars/000/000/000/original/DxDxDxDxDxDxDxDx'
    '.jpg" alt="User" width= 100px" style="border-radius: 50%;"/&gt; '
    '&lt;strong&gt;User &lt;/strong&gt'
    ';&lt;p&gt;What\'s New in &lt;a href="https://linuxjobs.social/tags/'
    'python" class="mention hashtag" rel="nofollow noopener" target="_blank'
    '"&gt;#&lt;span&gt;python&lt;/span&gt;&lt;/a&gt; today?&lt;/p&gt;&lt;br'
    '&gt;♻ : 0, ✰ : 0, 🌐&lt;/div&gt;&lt;/blockquote&gt;</description>'
    '<pubDate>Thu, 25 Oct 2018 16:16:42 +0200</pubDate>'
    '</item>'
    '</channel>'
    '</rss>'
)
toot_20_bookmarks_feed = (
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<rss version="2.0">'
    '<channel>'
    '<xhtml:meta xmlns:xhtml="http://www.w3.org/1999/xhtml" '
    'name="robots" content="noindex" />'
    '<title>Mastodon Feed: Bookmarks</title>'
    '<link>https://mastodon.social/web/bookmarks</link><'
    'description> bookmarks toots.</description>'
    '<language>fr</language>'
    '<lastBuildDate></lastBuildDate>'
    + (
        '<item>'
        '<title>User (UserD): What\'s New in #python today?</title>'
        '<link>https://mastodon.social/@UserD/111111111111111111</link>'
        '<description>&lt;blockquote&gt;&lt;div&gt;&lt;img src="https://files.'
        'mastodon.social/accounts/avatars/000/000/000/original/'
        'DxDxDxDxDxDxDxDx.jpg" alt="User" width= 100px" style="border-radius: '
        '50%;"/&gt; &lt;strong&gt;'
        'User &lt;/strong&gt;&lt;p&gt;What\'s New in &lt;a href="https://'
        'linuxjobs.social/tags/python" class="mention hashtag" rel="nofollow '
        'noopener" target="_blank"&gt;#&lt;span&gt;python&lt;/span&gt;&lt;/a&'
        'gt; today?&lt;/p&gt;&lt;br&gt;♻ : 0, ✰ : 0, 🌐&lt;/div&gt;&lt;/'
        'blockquote&gt;</description>'
        '<pubDate>Thu, 25 Oct 2018 16:16:42 +0200</pubDate>'
        '</item>'
    )
    * max_items
    + '</channel>'
    '</rss>'
)
toot_1_favorites_feed = (
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<rss version="2.0">'
    '<channel>'
    '<xhtml:meta xmlns:xhtml="http://www.w3.org/1999/xhtml" '
    'name="robots" content="noindex" />'
    '<title>Mastodon Feed: Favourites</title>'
    '<link>https://mastodon.social/web/favourites</link><'
    'description> favourites toots.</description>'
    '<language>fr</language>'
    '<lastBuildDate></lastBuildDate>'
    '<item>'
    '<title>User (UserD): What\'s New in #python today?</title>'
    '<link>https://mastodon.social/@UserD/111111111111111111</link>'
    '<description>&lt;blockquote&gt;&lt;div&gt;&lt;img src="https://files.'
    'mastodon.social/accounts/avatars/000/000/000/original/DxDxDxDxDxDxDxDx'
    '.jpg" alt="User" width= 100px" style="border-radius: 50%;"/&gt; '
    '&lt;strong&gt;User &lt;/strong&gt'
    ';&lt;p&gt;What\'s New in &lt;a href="https://linuxjobs.social/tags/'
    'python" class="mention hashtag" rel="nofollow noopener" target="_blank'
    '"&gt;#&lt;span&gt;python&lt;/span&gt;&lt;/a&gt; today?&lt;/p&gt;&lt;br'
    '&gt;♻ : 0, ✰ : 0, 🌐&lt;/div&gt;&lt;/blockquote&gt;</description>'
    '<pubDate>Thu, 25 Oct 2018 16:16:42 +0200</pubDate>'
    '</item>'
    '</channel>'
    '</rss>'
)
toot_20_favorites_feed = (
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<rss version="2.0">'
    '<channel>'
    '<xhtml:meta xmlns:xhtml="http://www.w3.org/1999/xhtml" '
    'name="robots" content="noindex" />'
    '<title>Mastodon Feed: Favourites</title>'
    '<link>https://mastodon.social/web/favourites</link><'
    'description> favourites toots.</description>'
    '<language>fr</language>'
    '<lastBuildDate></lastBuildDate>'
    + (
        '<item>'
        '<title>User (UserD): What\'s New in #python today?</title>'
        '<link>https://mastodon.social/@UserD/111111111111111111</link>'
        '<description>&lt;blockquote&gt;&lt;div&gt;&lt;img src="https://files.'
        'mastodon.social/accounts/avatars/000/000/000/original/'
        'DxDxDxDxDxDxDxDx.jpg" alt="User" width= 100px" style="border-radius: '
        '50%;"/&gt; &lt;strong&gt;'
        'User &lt;/strong&gt;&lt;p&gt;What\'s New in &lt;a href="https://'
        'linuxjobs.social/tags/python" class="mention hashtag" rel="nofollow '
        'noopener" target="_blank"&gt;#&lt;span&gt;python&lt;/span&gt;&lt;/a&'
        'gt; today?&lt;/p&gt;&lt;br&gt;♻ : 0, ✰ : 0, 🌐&lt;/div&gt;&lt;/'
        'blockquote&gt;</description>'
        '<pubDate>Thu, 25 Oct 2018 16:16:42 +0200</pubDate>'
        '</item>'
    )
    * max_items
    + '</channel>'
    '</rss>'
)

toot2 = {
    'id': 111111111111111111,
    'created_at': datetime(2018, 10, 25, 14, 16, 42, 11000),
    'in_reply_to_id': None,
    'in_reply_to_account_id': None,
    'sensitive': False,
    'spoiler_text': '',
    'visibility': 'public',
    'language': 'en',
    'uri': 'https://mastodon.social/users/UserD/statuses/111111111111111111',
    'content': '<p>This is a <a href="https://mastodon.social/tags/testtag" class="mention hashtag" rel="tag">#<span>TestTag</span></a></p>',  # noqa
    'url': 'https://mastodon.social/@UserD/111111111111111111',
    'replies_count': 0,
    'reblogs_count': 0,
    'favourites_count': 0,
    'favourited': False,
    'reblogged': False,
    'muted': False,
    'pinned': False,
    'reblog': None,
    'application': {
        'name': 'Twidere for Android',
        'website': 'https://github.com/TwidereProject/',
    },
    'account': {
        'id': 00000,
        'username': 'UserD',
        'acct': 'UserD',
        'display_name': 'User',
        'locked': False,
        'bot': False,
        'created_at': datetime(2017, 4, 4, 9, 20, 43, 157000),
        'note': '',
        'url': 'https://mastodon.social/@UserD',
        'avatar': 'https://files.mastodon.social/accounts/avatars/000/000/000/original/DxDxDxDxDxDxDxDx.jpg',  # noqa
        'avatar_static': 'https://files.mastodon.social/accounts/avatars/000/000/000/original/DxDxDxDxDxDxDxDx.jpg',  # noqa
        'header': 'https://files.mastodon.social/accounts/headers/000/000/000/original/xDxDxDxDxDxDxDxD.jpg',  # noqa
        'header_static': 'https://files.mastodon.social/accounts/headers/000/000/000/original/xDxDxDxDxDxDxDxD.jpg',  # noqa
        'followers_count': 10,
        'following_count': 20,
        'statuses_count': 300,
        'emojis': [],
        'fields': [
            {
                'name': 'GitHub',
                'value': '<a href="https://github.com/UserD" rel="nofollow noopener" target="_blank"><span class="invisible">https://</span><span class="">github.com/UserD</span><span class="invisible"></span></a>',  # noqa
                'verified_at': None,
            }
        ],
    },
    'media_attachments': [
        {
            'id': 7398805,
            'type': 'image',
            'url': 'https://files.mastodon.social/media_attachments/files/999/999/999/original/a2a2a2a2a2a2a2a2.jpg',  # noqa
            'preview_url': 'https://files.mastodon.social/media_attachments/files/999/999/999/small/a2a2a2a2a2a2a2a2.jpg',  # noqa
            'remote_url': None,
            'text_url': 'https://mastodon.social/media/2a2a2a2a2a2a2_a2a2a',  # noqa
            'meta': {
                'original': {
                    'width': 1109,
                    'height': 1478,
                    'size': '1109x1478',
                    'aspect': 0.7503382949932341,
                },
                'small': {
                    'width': 346,
                    'height': 461,
                    'size': '346x461',
                    'aspect': 0.7505422993492408,
                },
            },
            'description': None,
        },
        {
            "id": 10872710422,
            "type": "video",
            "url": "https://files.mastodon.social/cache/media_attachments/files/888/888/888/888/888/888/original/b1b1b1b1b1b1b1b1.mp4",  # noqa
            "preview_url": "https://files.mastodon.social/cache/media_attachments/files/108/778/808/662/710/422/small/b1b1b1b1b1b1b1b1.png",  # noqa
            "remote_url": None,
            "preview_remote_url": None,
            "text_url": None,
            "meta": {
                "original": {
                    "width": 360,
                    "height": 450,
                    "frame_rate": "10400/347",
                    "duration": 19.109,
                    "bitrate": 572691,
                },
                "small": {
                    "width": 320,
                    "height": 400,
                    "size": "320x400",
                    "aspect": 0.8,
                },
            },
            "description": None,
            "blurhash": "UcvWGoxGxZRv~qxuxuj[DioLt7oftRRjWVvB",
        },
        {
            "id": 108806907390,
            "type": "gifv",
            "url": "https://files.mastodon.social/cache/media_attachments/files/777/777/777/777/777/777/original/d4d4d4d4d4d4d4d4.mp4",  # noqa
            "preview_url": "https://files.mastodon.social/cache/media_attachments/files/777/777/777/777/777/777/small/d4d4d4d4d4d4d4d4.png",  # noqa
            "remote_url": None,
            "preview_remote_url": None,
            "text_url": None,
            "meta": {
                "original": {
                    "width": 1156,
                    "height": 720,
                    "frame_rate": "60/1",
                    "duration": 18.517,
                    "bitrate": 1660750,
                },
                "small": {
                    "width": 400,
                    "height": 249,
                    "size": "400x249",
                    "aspect": 1.606425702811245,
                },
            },
            "description": None,
            "blurhash": "UvEfv#tQk8%2~Wogozxavtt7s;%2Iot7smvz",
        },
    ],
    'mentions': [],
    'tags': [
        {'name': 'testtag', 'url': 'https://mastodon.social/tags/testtag'}
    ],
    'emojis': [],
    'card': None,
}

formatted_toot2 = {
    'boosted': '',
    'display_name': 'User',
    'screen_name': 'UserD',
    'created_at': datetime(2018, 10, 25, 14, 16, 42, 11000),
    'url': 'https://mastodon.social/@UserD/111111111111111111',
    'htmltext': '<blockquote>'
    '<div>'
    '<img src="https://files.mastodon.social/accounts/avatars/000/000/000/original/DxDxDxDxDxDxDxDx.jpg" alt="User" width= 100px" style="border-radius: 50%;"/> '  # noqa
    '<strong>User </strong>'
    '<p>This is a <a href="https://mastodon.social/tags/testtag" class="mention hashtag" rel="tag">#<span>TestTag</span></a></p>'  # noqa
    '<i>Source: Twidere for Android</i><br>'
    '<a href="https://files.mastodon.social/media_attachments/files/999/999/999/original/a2a2a2a2a2a2a2a2.jpg" target="_blank"><img src="https://files.mastodon.social/media_attachments/files/999/999/999/small/a2a2a2a2a2a2a2a2.jpg"></a>'  # noqa
    '<video width="320" height="400" controls>'
    ' <source src="https://files.mastodon.social/cache/media_attachments/files/888/888/888/888/888/888/original/b1b1b1b1b1b1b1b1.mp4" '  # noqa
    'poster="https://files.mastodon.social/cache/media_attachments/files/108/778/808/662/710/422/small/b1b1b1b1b1b1b1b1.png" '  # noqa
    'type="video/mp4">Your browser does not support the video tag.</video> '
    '<video width="400" height="249" autoplay loop muted inline>'
    ' <source src="https://files.mastodon.social/cache/media_attachments/files/777/777/777/777/777/777/original/d4d4d4d4d4d4d4d4.mp4" '  # noqa
    'poster="https://files.mastodon.social/cache/media_attachments/files/777/777/777/777/777/777/small/d4d4d4d4d4d4d4d4.png" '  # noqa
    'type="video/mp4">Your browser does not support the video tag.</video> '
    '<br>♻ : 0, ✰ : 0, 🌐</div></blockquote>',
    'text': 'This is a ... ',
}

empty_toot_feed = (
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<rss version="2.0">'
    '<channel>'
    '<xhtml:meta xmlns:xhtml="http://www.w3.org/1999/xhtml" '
    'name="robots" content="noindex" />'
    '<title>Mastodon Feed: search "test"</title>'
    '<link>https://mastodon.social/web/timelines/tag/test</link><'
    'description>Mastodon generated feed from search.</description>'
    '<language>fr</language>'
    '<lastBuildDate></lastBuildDate>'
    '</channel>'
    '</rss>'
)

empty_toot_search_feed = (
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<rss version="2.0">'
    '<channel>'
    '<xhtml:meta xmlns:xhtml="http://www.w3.org/1999/xhtml" '
    'name="robots" content="noindex" />'
    '<title>Mastodon Feed: search "test"</title>'
    '<link>https://mastodon.social/web/search/</link><'
    'description>Mastodon generated feed from search.</description>'
    '<language>fr</language>'
    '<lastBuildDate></lastBuildDate>'
    '</channel>'
    '</rss>'
)
toot_1_search_feed = (
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<rss version="2.0">'
    '<channel>'
    '<xhtml:meta xmlns:xhtml="http://www.w3.org/1999/xhtml" '
    'name="robots" content="noindex" />'
    '<title>Mastodon Feed: search "test"</title>'
    '<link>https://mastodon.social/web/search/</link><'
    'description>Mastodon generated feed from search.</description>'
    '<language>fr</language>'
    '<lastBuildDate></lastBuildDate>'
    '<item>'
    '<title>User (UserD): What\'s New in #python today?</title>'
    '<link>https://mastodon.social/@UserD/111111111111111111</link>'
    '<description>&lt;blockquote&gt;&lt;div&gt;&lt;img src="https://files.'
    'mastodon.social/accounts/avatars/000/000/000/original/DxDxDxDxDxDxDxDx'
    '.jpg" alt="User" width= 100px" style="border-radius: 50%;"/&gt; '
    '&lt;strong&gt;User &lt;/strong&gt'
    ';&lt;p&gt;What\'s New in &lt;a href="https://linuxjobs.social/tags/'
    'python" class="mention hashtag" rel="nofollow noopener" target="_blank'
    '"&gt;#&lt;span&gt;python&lt;/span&gt;&lt;/a&gt; today?&lt;/p&gt;&lt;br'
    '&gt;♻ : 0, ✰ : 0, 🌐&lt;/div&gt;&lt;/blockquote&gt;</description>'
    '<pubDate>Thu, 25 Oct 2018 16:16:42 +0200</pubDate>'
    '</item>'
    '</channel>'
    '</rss>'
)

reblog = {
    'id': 222222222222222222,
    'created_at': datetime(2018, 10, 25, 14, 17, 22, 00000),
    'in_reply_to_id': None,
    'in_reply_to_account_id': None,
    'sensitive': False,
    'spoiler_text': '',
    'visibility': 'public',
    'language': 'en',
    'uri': "https://mastodon.social/users/userA/statuses/222222222222222222/activity",  # noqa
    'content': '',
    'url': "https://mastodon.social/users/userA/statuses/222222222222222222/activity",  # noqa
    'replies_count': 0,
    'reblogs_count': 0,
    'favourites_count': 0,
    'favourited': False,
    'reblogged': False,
    'muted': False,
    'pinned': False,
    'reblog': {
        'id': 111111111111111111,
        'created_at': datetime(2018, 10, 25, 14, 16, 42, 11000),
        'in_reply_to_id': None,
        'in_reply_to_account_id': None,
        'sensitive': False,
        'spoiler_text': '',
        'visibility': 'public',
        'language': 'en',
        'uri': 'https://mastodon.social/users/UserD/statuses/111111111111111111',  # noqa
        'content': '<p>What\'s New in <a href="https://linuxjobs.social/tags/'
        'python" class="mention hashtag" rel="nofollow noopener" '
        'target="_blank">#<span>python</span></a> today?</p>',
        'url': 'https://mastodon.social/@UserD/111111111111111111',
        'replies_count': 0,
        'reblogs_count': 0,
        'favourites_count': 0,
        'favourited': False,
        'reblogged': False,
        'muted': False,
        'pinned': False,
        'reblog': None,
        'application': {},
        'account': {
            'id': 00000,
            'username': 'UserD',
            'acct': 'UserD',
            'display_name': 'User',
            'locked': False,
            'bot': False,
            'created_at': datetime(2017, 4, 4, 9, 20, 43, 157000),
            'note': '',
            'url': 'https://mastodon.social/@UserD',
            'avatar': 'https://files.mastodon.social/accounts/avatars/000/000/000/original/DxDxDxDxDxDxDxDx.jpg',  # noqa
            'avatar_static': 'https://files.mastodon.social/accounts/avatars/000/000/000/original/DxDxDxDxDxDxDxDx.jpg',  # noqa
            'header': 'https://files.mastodon.social/accounts/headers/000/000/000/original/xDxDxDxDxDxDxDxD.jpg',  # noqa
            'header_static': 'https://files.mastodon.social/accounts/headers/000/000/000/original/xDxDxDxDxDxDxDxD.jpg',  # noqa
            'followers_count': 10,
            'following_count': 20,
            'statuses_count': 300,
            'emojis': [],
            'fields': [],
        },
        'media_attachments': [],
        'mentions': [],
        'tags': [],
        'emojis': [],
        'card': None,
    },
    'application': {},
    'account': {
        'id': 11111,
        'username': 'UserA',
        'acct': 'UserA',
        'display_name': 'User A',
        'locked': False,
        'bot': False,
        'created_at': datetime(2019, 4, 1, 11, 21, 41, 77000),
        'note': '',
        'url': 'https://mastodon.social/@UserA',
        'avatar': 'https://files.mastodon.social/accounts/avatars/000/000/000/original/DxDxDxDxDxDxDxDx.jpg',  # noqa
        'avatar_static': 'https://files.mastodon.social/accounts/avatars/000/000/000/original/DxDxDxDxDxDxDxDx.jpg',  # noqa
        'header': 'https://files.mastodon.social/accounts/headers/000/000/000/original/xDxDxDxDxDxDxDxD.jpg',  # noqa
        'header_static': 'https://files.mastodon.social/accounts/headers/000/000/000/original/xDxDxDxDxDxDxDxD.jpg',  # noqa
        'followers_count': 1,
        'following_count': 2,
        'statuses_count': 3,
        'emojis': [],
        'fields': [],
    },
    'media_attachments': [],
    'mentions': [],
    'tags': [],
    'emojis': [],
    'card': None,
}

formatted_reblog = {
    'boosted': 'Boosted by User A: ',
    'display_name': 'User',
    'screen_name': 'UserD',
    'created_at': datetime(2018, 10, 25, 14, 17, 22),
    'url': 'https://mastodon.social/@UserD/111111111111111111',
    'htmltext': '<blockquote>'
    '<div>Boosted by User A: </div>'
    '<div>'
    '<img src="https://files.mastodon.social/accounts/avatars/000/000/000/original/DxDxDxDxDxDxDxDx.jpg" alt="User" width= 100px" style="border-radius: 50%;"/> '  # noqa
    '<strong>User </strong>'
    '<p>What\'s New in <a href="https://linuxjobs.social/tags/python" class="mention hashtag" rel="nofollow noopener" target="_blank">#<span>python</span></a> today?</p>'  # noqa
    '<br>♻ : 0, ✰ : 0, 🌐</div></blockquote>',
    'text': 'What\'s New in #python today?',
}

toot_1_home_timeline_feed = (
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<rss version="2.0">'
    '<channel>'
    '<xhtml:meta xmlns:xhtml="http://www.w3.org/1999/xhtml" '
    'name="robots" content="noindex" />'
    '<title>Mastodon Feed: Home Timeline</title>'
    '<link>https://mastodon.social</link><'
    'description> home timeline.</description>'
    '<language>fr</language>'
    '<lastBuildDate></lastBuildDate>'
    '<item>'
    '<title>User (UserD): What\'s New in #python today?</title>'
    '<link>https://mastodon.social/@UserD/111111111111111111</link>'
    '<description>&lt;blockquote&gt;&lt;div&gt;&lt;img src="https://files.'
    'mastodon.social/accounts/avatars/000/000/000/original/DxDxDxDxDxDxDxDx'
    '.jpg" alt="User" width= 100px" style="border-radius: 50%;"/&gt; '
    '&lt;strong&gt;User &lt;/strong&gt'
    ';&lt;p&gt;What\'s New in &lt;a href="https://linuxjobs.social/tags/'
    'python" class="mention hashtag" rel="nofollow noopener" target="_blank'
    '"&gt;#&lt;span&gt;python&lt;/span&gt;&lt;/a&gt; today?&lt;/p&gt;&lt;br'
    '&gt;♻ : 0, ✰ : 0, 🌐&lt;/div&gt;&lt;/blockquote&gt;</description>'
    '<pubDate>Thu, 25 Oct 2018 16:16:42 +0200</pubDate>'
    '</item>'
    '</channel>'
    '</rss>'
)

toot_20_home_timeline_feed = (
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<rss version="2.0">'
    '<channel>'
    '<xhtml:meta xmlns:xhtml="http://www.w3.org/1999/xhtml" '
    'name="robots" content="noindex" />'
    '<title>Mastodon Feed: Home Timeline</title>'
    '<link>https://mastodon.social</link><'
    'description> home timeline.</description>'
    '<language>fr</language>'
    '<lastBuildDate></lastBuildDate>'
    + (
        '<item>'
        '<title>User (UserD): What\'s New in #python today?</title>'
        '<link>https://mastodon.social/@UserD/111111111111111111</link>'
        '<description>&lt;blockquote&gt;&lt;div&gt;&lt;img src="https://files.'
        'mastodon.social/accounts/avatars/000/000/000/original/'
        'DxDxDxDxDxDxDxDx.jpg" alt="User" width= 100px" style="border-radius: '
        '50%;"/&gt; &lt;strong&gt;'
        'User &lt;/strong&gt;&lt;p&gt;What\'s New in &lt;a href="https://'
        'linuxjobs.social/tags/python" class="mention hashtag" rel="nofollow '
        'noopener" target="_blank"&gt;#&lt;span&gt;python&lt;/span&gt;&lt;/a&'
        'gt; today?&lt;/p&gt;&lt;br&gt;♻ : 0, ✰ : 0, 🌐&lt;/div&gt;&lt;/'
        'blockquote&gt;</description>'
        '<pubDate>Thu, 25 Oct 2018 16:16:42 +0200</pubDate>'
        '</item>'
    )
    * max_items
    + '</channel>'
    '</rss>'
)
