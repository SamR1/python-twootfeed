import logging
import os
import sys

from flask import Flask
from twootfeed.mastodon.get_api import get_mastodon_api
from twootfeed.twitter.get_api import get_twitter_api
from twootfeed.utils.config import get_config

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


def create_app():
    app = Flask(__name__)
    app_log.setLevel(logging.DEBUG if app.debug else logging.INFO)

    from .mastodon.routes import mastodon_bp
    from .twitter.routes import twitter_bp

    app.register_blueprint(mastodon_bp)
    app.register_blueprint(twitter_bp)

    @app.route('/')
    def index_page():
        message = (
            'The RSS feeds are available on these urls : \r\n'
            'for Twitter : http://localhost:5000/_keywords_ or '
            'http://localhost:5000/tweets/_keywords_ ,\r\n'
            'for Mastodon : http://localhost:5000/toots/_keywords_'
        )

        return message

    return app
