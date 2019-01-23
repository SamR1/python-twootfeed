import os
from os.path import abspath, dirname
from shutil import copyfile

import yaml

DEFAULT_CONFIG = '~/.config/twootfeed_config.yml'


def get_config():
    config_file = os.getenv('APP_CONFIG')
    if not config_file:
        config_file = os.path.expanduser(DEFAULT_CONFIG)
    if not os.path.isfile(config_file):
        config_example = os.path.join(dirname(abspath(__file__))[:-5],
                                      'config.example.yml')
        copyfile(config_example, config_file)
    with open(config_file, 'r', encoding='utf-8') as stream:
        return yaml.safe_load(stream)
