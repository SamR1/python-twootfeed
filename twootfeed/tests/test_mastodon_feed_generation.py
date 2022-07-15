import re

import pytest

from ..mastodon.generate_toots_feed import (
    format_toot,
    generate_mastodon_feed,
    generate_xml,
)
from .data import (
    empty_toot_feed,
    empty_toot_search_feed,
    formatted_reblog,
    formatted_toot1,
    formatted_toot2,
    invalid_param as param,
    reblog,
    toot1,
    toot2,
    toot_1_bookmarks_feed,
    toot_1_favorites_feed,
    toot_1_feed,
    toot_1_search_feed,
    toot_100_bookmarks_feed,
    toot_100_favorites_feed,
    toot_100_feed,
)
from .utils import MastodonApi


def test_format_toot() -> None:
    assert format_toot(toot1, 100) == formatted_toot1
    assert format_toot(toot2, 10) == formatted_toot2
    assert format_toot(reblog, 100) == formatted_reblog


def test_generate_feed() -> None:
    val = generate_mastodon_feed(
        [toot1],
        param,
        'Recherche Mastodon : "test"',
        'https://mastodon.social/web/timelines/tag/test',
        'Résultat d\'une recherche Mastodon retournée dans un flux RSS.',
    )
    # remove date
    val = re.sub(
        r'(<lastBuildDate>)(.*)(</lastBuildDate>)',
        '<lastBuildDate></lastBuildDate>',
        val,
    )
    assert val == toot_1_feed


def test_generate_feed_200_toots() -> None:
    val = generate_mastodon_feed(
        [toot1] * 200,
        param,
        'Recherche Mastodon : "test"',
        'https://mastodon.social/web/timelines/tag/test',
        'Résultat d\'une recherche Mastodon retournée dans un flux RSS.',
    )
    # remove date
    val = re.sub(
        r'(<lastBuildDate>)(.*)(</lastBuildDate>)',
        '<lastBuildDate></lastBuildDate>',
        val,
    )
    assert val == toot_100_feed


def test_generate_xml_no_api() -> None:
    val, code = generate_xml(None, param, {'hashtag': 'test'})
    assert val == 'error - Mastodon parameters not defined'
    assert code == 401


def test_generate_xml_no_toots() -> None:
    api = MastodonApi([])
    val, code = generate_xml(api, param, {'hashtag': 'test'})
    val = re.sub(
        r'(<lastBuildDate>)(.*)(</lastBuildDate>)',
        '<lastBuildDate></lastBuildDate>',
        val,
    )
    assert val == empty_toot_feed
    assert code == 200


def test_generate_xml_query_ok() -> None:
    api = MastodonApi([toot1])
    val, code = generate_xml(api, param, {'hashtag': 'test'})
    val = re.sub(
        r'(<lastBuildDate>)(.*)(</lastBuildDate>)',
        '<lastBuildDate></lastBuildDate>',
        val,
    )
    assert val == toot_1_feed
    assert code == 200


def test_generate_xml_query_limit_ok() -> None:
    api = MastodonApi([toot1] * 200)
    val, code = generate_xml(api, param, {'hashtag': 'test'})
    val = re.sub(
        r'(<lastBuildDate>)(.*)(</lastBuildDate>)',
        '<lastBuildDate></lastBuildDate>',
        val,
    )
    assert val == toot_100_feed
    assert code == 200


def test_generate_xml_search_no_toots() -> None:
    api = MastodonApi([])
    val, code = generate_xml(api, param, {'query': 'test'})
    val = re.sub(
        r'(<lastBuildDate>)(.*)(</lastBuildDate>)',
        '<lastBuildDate></lastBuildDate>',
        val,
    )
    assert val == empty_toot_search_feed
    assert code == 200


def test_generate_xml_search_ok() -> None:
    api = MastodonApi([toot1])
    val, code = generate_xml(api, param, {'query': 'test'})
    val = re.sub(
        r'(<lastBuildDate>)(.*)(</lastBuildDate>)',
        '<lastBuildDate></lastBuildDate>',
        val,
    )
    assert val == toot_1_search_feed
    assert code == 200


def test_generate_xml_favorites_ok() -> None:
    api = MastodonApi([toot1])
    val, code = generate_xml(api, param, target='favorites')
    val = re.sub(
        r'(<lastBuildDate>)(.*)(</lastBuildDate>)',
        '<lastBuildDate></lastBuildDate>',
        val,
    )
    assert val == toot_1_favorites_feed
    assert code == 200


def test_generate_xml_favorites_limit_ok() -> None:
    api = MastodonApi([toot1] * 150)
    val, code = generate_xml(api, param, target='favorites')
    val = re.sub(
        r'(<lastBuildDate>)(.*)(</lastBuildDate>)',
        '<lastBuildDate></lastBuildDate>',
        val,
    )
    assert val == toot_100_favorites_feed
    assert code == 200


def test_generate_xml_bookmarks_ok() -> None:
    api = MastodonApi([toot1])
    val, code = generate_xml(api, param, target='bookmarks')
    val = re.sub(
        r'(<lastBuildDate>)(.*)(</lastBuildDate>)',
        '<lastBuildDate></lastBuildDate>',
        val,
    )
    assert val == toot_1_bookmarks_feed
    assert code == 200


def test_generate_xml_bookmarks_limit_ok() -> None:
    api = MastodonApi([toot1] * 150)
    val, code = generate_xml(api, param, target='bookmarks')
    val = re.sub(
        r'(<lastBuildDate>)(.*)(</lastBuildDate>)',
        '<lastBuildDate></lastBuildDate>',
        val,
    )
    assert val == toot_100_bookmarks_feed
    assert code == 200


def test_it_raises_exception_when_target_is_invalid() -> None:
    api = MastodonApi([])
    with pytest.raises(Exception, match='Invalid target'):
        generate_xml(api, param, target='invalid')
