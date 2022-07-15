import os
from os.path import abspath, dirname
from shutil import copyfile
from typing import Any, Dict

import yaml

from .exceptions import InvalidTokenException, MissingTokenException

DEFAULT_DIRECTORY = os.path.expanduser('~/.config/twootfeed/')
TWOOTFEED_CONFIG_DIR = os.getenv('TWOOTFEED_CONFIG_DIR', '')
default_directory: str = (
    TWOOTFEED_CONFIG_DIR if TWOOTFEED_CONFIG_DIR else DEFAULT_DIRECTORY
)
DEFAULT_CONFIG = default_directory + 'config.yml'


def get_config_file(config_file_path: str) -> str:
    if not config_file_path:
        config_file_path = os.path.expanduser(DEFAULT_CONFIG)
    if not os.path.isfile(config_file_path):
        config_example = os.path.join(
            dirname(abspath(__file__))[:-5], 'config.example.yml'
        )
        os.makedirs(os.path.dirname(DEFAULT_DIRECTORY), exist_ok=True)
        copyfile(config_example, config_file_path)
    return config_file_path


def get_config() -> Any:
    config_file = get_config_file(os.getenv('TWOOTFEED_CONFIG_FILE', ''))
    with open(config_file, 'r', encoding='utf-8') as stream:
        return yaml.safe_load(stream)


def init_config() -> bool:
    return get_config() is not None


def check_token(feed_config: Dict) -> None:
    token = feed_config.get('token')
    if not token:
        raise MissingTokenException("token is missing in configuration")

    if len(token) < 25:
        raise InvalidTokenException("token is too short")
