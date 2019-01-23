import os
from os.path import abspath, dirname
from shutil import copyfile

import yaml

DEFAULT_DIRECTORY = os.path.expanduser('~/.config/twootfeed/')
DEFAULT_CONFIG = DEFAULT_DIRECTORY + 'config.yml'

default_directory = (os.getenv('APP_CONFIG_DIR')
                     if os.getenv('APP_CONFIG_DIR')
                     else DEFAULT_DIRECTORY)


def get_config():
    config_file = os.getenv('APP_CONFIG')
    if not config_file:
        config_file = os.path.expanduser(DEFAULT_CONFIG)
    if not os.path.isfile(config_file):
        config_example = os.path.join(dirname(abspath(__file__))[:-5],
                                      'config.example.yml')
        os.makedirs(os.path.dirname(DEFAULT_DIRECTORY), exist_ok=True)
        copyfile(config_example, config_file)
    with open(config_file, 'r', encoding='utf-8') as stream:
        return yaml.safe_load(stream)
