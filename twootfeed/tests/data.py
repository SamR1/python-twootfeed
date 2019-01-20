invalid_param = {
    'twitter':
        {
            'consumerKey': '',
            'consumerSecret': '',
            'title': 'Recherche Twitter : ',
            'link': 'https://twitter.com/search?q=',
            'description': 'Résultat d\'une recherche Twitter retournée dans un flux RSS via Tweepy.'  # noqa
        },
    'mastodon':
        {
            'url': 'https://mastodon.social',
            'client_id_file': 'tootrss_clientcred_invalid.txt',
            'access_token_file': 'tootrss_clientcred_invalid.txt',
            'app_name': 'tootrss',
            'title': 'Recherche Mastodon : ',
            'description': 'Résultat d\'une recherche Mastodon retournée dans un flux RSS.'  # noqa
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
