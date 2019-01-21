from .. import app_log
from ..mastodon.get_api import get_mastodon_api
from ..twitter.get_api import get_twitter_api
from .data import invalid_param, invalid_param_api


def test_mastodon_invalid_param(caplog):
    mastodon_api = get_mastodon_api(invalid_param, app_log)
    assert mastodon_api is None
    assert len(caplog.records) == 1
    assert caplog.records[0].levelname == 'WARNING'
    assert caplog.records[0].message == ('Mastodon API: no client_id_file or'
                                         ' access_token_file.')


def test_twitter_invalid_param(caplog):
    twitter_api = get_twitter_api(invalid_param, app_log)
    assert twitter_api is None
    assert len(caplog.records) == 1
    assert caplog.records[0].levelname == 'WARNING'
    assert caplog.records[0].message == ('Twitter API: no consumer key and or'
                                         ' consumer secret in config file.')


def test_mastodon_incomplete_param(caplog):
    mastodon_api = get_mastodon_api(invalid_param_api, app_log)
    assert mastodon_api is None
    assert len(caplog.records) == 1
    assert caplog.records[0].levelname == 'ERROR'
    assert caplog.records[0].message == ('Mastodon API: invalid config file '
                                         '(\'NoneType\' object is not '
                                         'subscriptable)')


def test_twitter_incomplete_param(caplog):
    twitter_api = get_twitter_api(invalid_param_api, app_log)
    assert twitter_api is None
    assert len(caplog.records) == 1
    assert caplog.records[0].levelname == 'ERROR'
    assert caplog.records[0].message == ('Twitter API: invalid config file '
                                         '(\'NoneType\' object is not '
                                         'subscriptable)')
