from twootfeed.utils.feed_generation import add_noindex

from .data import empty_feed, empty_feed_with_no_index


class TestAddNoIndexMeta:
    def test_it_returns_feed_with_no_index_meta(self) -> None:
        assert add_noindex(empty_feed) == empty_feed_with_no_index
