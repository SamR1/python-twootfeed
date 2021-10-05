import os

from mastodon import Mastodon
from twootfeed.utils.config import default_directory


def get_mastodon_api(param, app_log):
    mastodon_api = None

    try:
        mastodon_param = param['mastodon']
        client_file = default_directory + mastodon_param['client_id_file']
        access_token_file = (
            default_directory + mastodon_param['access_token_file']
        )

        if os.path.isfile(client_file) and os.path.isfile(access_token_file):

            mastodon_url = param['mastodon'].get(
                'url', 'https://mastodon.social'
            )
            mastodon_api = Mastodon(
                client_id=client_file,
                access_token=access_token_file,
                api_base_url=mastodon_url,
            )
        else:
            app_log.warning(
                'Mastodon API: no client_id_file or ' 'access_token_file.'
            )
    except Exception as e:
        app_log.error(f'Mastodon API: invalid config file ({e})')

    return mastodon_api
