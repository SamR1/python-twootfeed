import os

from mastodon import Mastodon


def get_mastodon_api(param, app_log):
    mastodon_api = None

    client_file = 'twootfeed/' + param['mastodon']['client_id_file']
    access_token_file = ('twootfeed/' +
                         param['mastodon']['access_token_file'])

    if os.path.exists(client_file) and os.path.exists(access_token_file):
        try:
            mastodon_url = param['mastodon'].get('url',
                                                 'https://mastodon.social')
            mastodon_api = Mastodon(
                client_id=client_file,
                access_token=access_token_file,
                api_base_url=mastodon_url
            )
        except Exception as e:
            app_log.error('Mastodon API: ' + str(e))
    else:
        app_log.warning('Mastodon API: no client_id_file or '
                        'access_token_file. ')
    return mastodon_api
