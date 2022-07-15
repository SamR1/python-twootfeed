import string
from random import choice
from typing import Dict

import pytest
from twootfeed.utils.config import check_token
from twootfeed.utils.exceptions import (
    InvalidTokenException,
    MissingTokenException,
)


class TestCheckConfig:
    @pytest.mark.parametrize(
        'input_feed_config', [{}, {'token': ''}, {'token': None}]
    )
    def test_it_raises_exception_when_token_is_missing(
        self, input_feed_config: Dict
    ) -> None:
        with pytest.raises(
            MissingTokenException,
            match="token is missing in configuration",
        ):
            check_token(feed_config=input_feed_config)

    def test_it_raises_exception_when_token_is_invalid(self) -> None:
        with pytest.raises(
            InvalidTokenException,
            match="token is too short",
        ):
            check_token(
                feed_config={
                    'token': ''.join(
                        choice(string.ascii_letters) for _ in range(24)
                    )
                }
            )

    def test_it_does_not_raise_exception_when_token_is_valid(self) -> None:
        check_token(
            feed_config={
                'token': ''.join(
                    choice(string.ascii_letters) for _ in range(25)
                )
            }
        )
