import logging
import os
import sys

from flask import Flask
from twootfeed.mastodon.get_api import get_mastodon_api
from twootfeed.twitter.get_api import get_twitter_api
from twootfeed.utils.config import check_token, get_config

log_file = os.getenv('TWOOTFEED_LOG')
logging.basicConfig(
    filename=log_file,
    format=('%(asctime)s - %(name)s - %(levelname)s - ' '%(message)s'),
    datefmt='%Y/%m/%d %H:%M:%S',
)
app_log = logging.getLogger('twootfeed')
app_log.debug('starting Python Twootfeed')

try:
    param = get_config()
except Exception as e:
    app_log.error(e)
    sys.exit(1)

twitter_api = get_twitter_api(param, app_log)
mastodon_api = get_mastodon_api(param, app_log)


def create_app() -> Flask:
    app = Flask(__name__)
    app_config = os.getenv('TWOOTFEED_SETTINGS', 'ProductionConfig')
    app.config.from_object(f'twootfeed.config.{app_config}')
    app_log.setLevel(logging.DEBUG if app.debug else logging.INFO)

    check_token(app.config['FEED_CONFIG'])

    from .mastodon.routes import mastodon_bp
    from .twitter.routes import twitter_bp

    app.register_blueprint(mastodon_bp)
    app.register_blueprint(twitter_bp)

    @app.route('/')
    def index_page() -> str:
        message = (
            'The RSS feeds for search are available on these endpoints: '
            '"tweets?q=QUERY&token=TOKEN" for Twitter or '
            '"toots/search?q=QUERY&token=TOKEN" for Mastodon.'
        )

        return message

    return app
