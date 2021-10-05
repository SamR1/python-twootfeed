import os
from os.path import abspath, dirname
from shutil import copyfile

import yaml

DEFAULT_DIRECTORY = os.path.expanduser('~/.config/twootfeed/')
default_directory = (
    os.getenv('TWOOTFEED_CONFIG_DIR')
    if os.getenv('TWOOTFEED_CONFIG_DIR')
    else DEFAULT_DIRECTORY
)
DEFAULT_CONFIG = default_directory + 'config.yml'


def get_config_file(config_file):
    if not config_file:
        config_file = os.path.expanduser(DEFAULT_CONFIG)
    if not os.path.isfile(config_file):
        config_example = os.path.join(
            dirname(abspath(__file__))[:-5], 'config.example.yml'
        )
        os.makedirs(os.path.dirname(DEFAULT_DIRECTORY), exist_ok=True)
        copyfile(config_example, config_file)
    return config_file


def get_config():
    config_file = get_config_file(os.getenv('TWOOTFEED_CONFIG_FILE'))
    with open(config_file, 'r', encoding='utf-8') as stream:
        return yaml.safe_load(stream)


def init_config():
    return get_config() is not None
